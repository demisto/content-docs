#!/usr/bin/env python3

import argparse
import json
import os
import re
import tempfile

import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from typing import List, Dict, Tuple
from datetime import datetime
from google.cloud import storage


# override print so we have a timestamp with each print
def timestamped_print(*args, **kwargs):
    __builtins__.print(datetime.now().strftime("%H:%M:%S.%f"), *args, **kwargs)


print = timestamped_print

PR_NUMBER_REGEX = re.compile(r'(?<=pull/)([0-9]+)')
USER_NAME_REGEX = re.compile(r'(?<=@)[a-zA-Z-0-9]+')
PAGE_NUMBER_REGEX = re.compile(r'(?<=&page=)([0-9]+)')
TOKEN = os.getenv('GITHUB_TOKEN', '')
SERVICE_ACCOUNT = os.getenv('GCP_SERVICE_ACCOUNT')
URL = 'https://api.github.com'
QUERY = 'type:pr state:closed org:demisto repo:content is:merged base:master head:contrib/ sort:updated-desc'
HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
}
if TOKEN:
    HEADERS['Authorization'] = 'Bearer ' + TOKEN
    print('Using token authentication')
VERIFY = os.getenv('SKIP_SSL_VERIFY') is None


# Retry class which uses 60 seconds backoff and only 2 retries
class SearchRetry(Retry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_backoff_time(self):
        print('Rate limit hit returning 60 seconds backoff time')
        return 60.0


search_session = requests.Session()
search_session.mount("https://", HTTPAdapter(max_retries=SearchRetry(
    total=2,
    status_forcelist=[429, 403, 500, 502, 503, 504],
)))


def create_grid(dataset: list) -> str:
    """
    Create a table grid of the GitHub users
    Args:
        dataset (list): The dataset to create the table from, in this case, the list of GitHub users.

    Returns (str): table grid of GitHub users

    """
    row_length = 7
    html_card = ''
    for i in range(0, len(dataset), row_length):
        html_card += '<tr>'
        for element in dataset[i:i + row_length]:
            html_card += f'\n<td>{element} </td>\n'
        html_card += '</tr>\n'

    return html_card


def create_service_account_file():
    """
    Create a service account json file from the circle variable.
    """
    service_account_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json')
    json.dump(json.loads(SERVICE_ACCOUNT), service_account_file)
    service_account_file.flush()

    return service_account_file


def get_contributors_file_from_bucket(service_account_file):
    storage_client = storage.Client.from_service_account_json(service_account_file)
    bucket = storage_client.bucket('xsoar-ci-artifacts')
    blob = bucket.blob('content-cache-docs/contributors.json')
    contributors = blob.download_as_string()

    return contributors


def update_contributors_file(service_account_file, list_users):
    storage_client = storage.Client.from_service_account_json(service_account_file)
    bucket = storage_client.bucket('xsoar-ci-artifacts')
    blob = bucket.blob('content-cache-docs/contributors.json')
    blob.upload_from_string(list_users)


def get_external_prs(prs: list) -> List[Dict]:
    """
    Get the external prs from the internal.
    We are using this to get the contributor github user in get_pr_user command.
    Args:
        prs: list of internal prs.

    Returns:
        external_prs (List[Dict]): list of the external prs (contains the pr number and its body)
    """
    external_prs = []
    for pr in prs:
        pr_body = pr.get('body', '')
        if inner_pr := PR_NUMBER_REGEX.search(pr_body):
            external_prs.append({
                'pr_number': inner_pr[0],
                'pr_body': pr_body
            })

    return external_prs


def github_pagination_prs(url: str, params: dict, res) -> list | None:
    """
    Paginate through all the pages in Github according to search query
    Args:
        url (str): the request url
        params (dict): params for the request
        res: the response from the http_request

    Returns: prs (dict)
    """
    prs = []
    if link := res.headers.get('Link'):
        links = link.split(',')
        last_page = links[-1]
        last_page_link = last_page[last_page.find("<") + 1:last_page.find(">")]
        try:
            print(f"Fetching last_page_link {last_page_link}")
            last_pr_number = PAGE_NUMBER_REGEX.search(last_page_link)[0]
        except IndexError:
            print(f"Error: Couldn't find the last page number. \n Last page link - {last_page_link}")
            return

        while params['page'] < int(last_pr_number):
            params['page'] = params['page'] + 1
            response = search_session.request('GET', url, params=params, headers=HEADERS, verify=VERIFY)
            response.raise_for_status()
            next_page_prs = response.json().get('items', [])
            prs.extend(next_page_prs)

    return prs


def get_contractors_prs() -> list:
    """
    Get all contractors pr numbers and users we want to ignore in the calculation.
    Returns: The external prs list of the contractors and the users we want to ignore.
    """
    url = URL + '/search/issues'
    query = 'type:pr state:closed org:demisto repo:content is:merged base:master ' \
            'head:contrib/crest head:contrib/qmasters head:contrib/mchasepan head:contrib/roybi72'
    params = {
        'q': query,
        'per_page': 100,
        'page': 1
    }
    res = search_session.request('GET', url, headers=HEADERS, params=params, verify=VERIFY)
    res.raise_for_status()
    prs = res.json().get('items', [])

    next_pages_prs = github_pagination_prs(url, params, res)
    prs.extend(next_pages_prs)

    external_prs = get_external_prs(prs)

    return external_prs


def get_contrib_prs(query: str) -> Tuple[List[Dict], str]:
    """
    Get the contributors' prs.
    Returns: The list of PRs.
    """
    url = URL + '/search/issues'
    params = {
        'q': query,
        'per_page': 100,
        'page': 1
    }
    res = search_session.request('GET', url, headers=HEADERS, params=params, verify=VERIFY)
    res.raise_for_status()
    prs = res.json().get('items', [])
    last_updated = ''
    if prs:
        last_updated_contribution = prs[0]
        last_updated = last_updated_contribution.get('updated_at')

    # Get all the PRs from all pages
    next_pages_prs = github_pagination_prs(url, params, res)
    prs.extend(next_pages_prs)

    contrib_prs = get_external_prs(prs)
    contractors_prs = get_contractors_prs()
    for item in contrib_prs:
        pr = item.get('pr_number')
        for external_pr in contractors_prs:
            pr_number = external_pr.get('pr_number')
            if pr_number == pr:
                contrib_prs = [i for i in contrib_prs if not (i['pr_number'] == pr_number)]

    return contrib_prs, last_updated


def get_github_user(user_name: str) -> Dict:
    """
    Get the GitHub user.
    Args:
        user_name (str): the GitHub username.

    Returns: The user avatar and its profile.

    """
    url = f'{URL}/users/{user_name}'
    res = requests.request('GET', url, headers=HEADERS, verify=VERIFY)
    if res.status_code == 404:
        print(f'The user {user_name} was not found.')
    else:
        response = res.json()
        return response


def get_inner_pr_request(query: str) -> Tuple[list, str]:
    """
    Get the inner pr information (will be used to get the user).
    Args:
        query (str): The query to use to get the contributions PRs.
    Returns:
        users_info (list): http response - prs_info.
        last_updated (str): The last updated PR timestamp.
    """
    users_info = []
    external_prs, last_updated = get_contrib_prs(query)
    for item in external_prs:
        pr_body = item.get('pr_body')
        pr = item.get('pr_number')
        if 'Contributor' in pr_body:
            contributor = USER_NAME_REGEX.search(pr_body)[0].replace('\n', '')
            user_profile = get_github_user(contributor)
            if user_profile:
                users_info.append(user_profile)
        else:
            url = URL + f'/repos/demisto/content/pulls/{pr}'
            res = requests.request('GET', url, headers=HEADERS, verify=VERIFY)
            if res.status_code == 404:
                print(f'The following PR was not found: {pr}')
                continue
            if res.status_code >= 400:
                try:
                    json_res = res.json()
                    if json_res.get('errors') is None:
                        print('Error in API call to the GitHub Integration [%d] - %s' % (res.status_code, res.reason))
                except ValueError:
                    print('Error in API call to GitHub Integration [%d] - %s' % (res.status_code, res.reason))
            if res.status_code == 200:
                response = res.json()
                user_response = response.get('user')
                inner_pr_body = response.get('body')
                user_response.update({'body': inner_pr_body})
                users_info.append(user_response)

    return users_info, last_updated


def get_contributors_users(users_info, last_update: str) -> dict:
    """
    Get the GitHub users from the inner PRs.
    Args:
        users_info (list): the response of get_inner_pr_request()
        last_update (str): the last updated PR timestamp

    Returns (dict): GitHub users

    """
    users = {}
    for item in users_info:
        user = item.get('login')
        pr_body = item.get('body')
        github_profile = item.get('html_url')
        github_avatar = item.get('avatar_url')

        # Contributions from UI
        if user == 'xsoar-bot':
            if 'Contributor' in pr_body:
                user = USER_NAME_REGEX.search(pr_body)[0].replace('\n', '')
                user_info = get_github_user(user)
                github_avatar = user_info.get('avatar_url')
                github_profile = user_info.get('html_url')
                if not github_avatar and not github_profile:
                    print(f'The user "{user}" was not found.')
                    continue

        if user not in users:
            users.update({
                user: {
                    'user': user,
                    'github_profile': github_profile,
                    'github_avatar': github_avatar,
                    'number_of_contributions': 1
                }
            })
        else:
            users[user]['number_of_contributions'] += 1

    if last_update:
        users.update({'last_update': last_update})

    return users


def create_users_list(users_dict: dict) -> List:
    users = []
    contributors = []
    users_dict.pop('last_update')
    sorted_users_list = sorted(users_dict.items(), key=lambda x: x[1]['number_of_contributions'], reverse=True)

    for key, value in sorted_users_list:
        users.append({
            'Contributor': f"<img src='{value.get('github_avatar')}'/><br></br> "
                           f"<a href='{value.get('github_profile')}' target='_blank'>{value.get('user')}</a>"
                           f"<br></br>{value.get('number_of_contributions')} Contributions"
        })

    for contributor in users:
        contributors.append(contributor['Contributor'])

    return contributors


def update_users_list(users_dict: dict, contributors_file_dict: dict):
    """
    Update the contributors list with the number of the current PRs
    Args:
        users_dict (dict): the users list
        contributors_file_dict (dict): The list from the contributors file to update

    Returns: The updated users dict - to update the contributors file

    """
    # In case of no new prs after last timestamp user_dict can be empty
    if users_dict:
        # Updating the last update timestamp
        last_update = users_dict.pop('last_update')
        contributors_file_dict['last_update'] = last_update
        for user in users_dict.items():
            new_prs = user[1]['number_of_contributions']
            # Case of new user
            if user[0] not in contributors_file_dict.keys():
                contributors_file_dict.update({user[0]: user[1]})
            else:
                contributors_file_dict[user[0]]['number_of_contributions'] += new_prs

    return contributors_file_dict


def main():
    global QUERY
    parser = argparse.ArgumentParser(description='Generate Top contributors page.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--target", help="Target dir to generate docs at.", required=True)
    args = parser.parse_args()
    contrib_target = args.target + '/top-contributors.md'
    try:
        service_account_file = create_service_account_file()
        contributors_data = get_contributors_file_from_bucket(service_account_file.name)

        # This part should always run unless it is the first time or in a case of a previous malfunction
        if contributors_data:
            # Update the query with the last_updated pr timestamp
            contributors_data = json.loads(contributors_data)
            last_updated_timestamp = contributors_data.get('last_update')
            QUERY += f' merged:>{last_updated_timestamp}'

        response, last_updated = get_inner_pr_request(QUERY)
        users_dict = get_contributors_users(response, last_updated)

        if contributors_data:
            # Update the file with recent contributions
            users_dict = update_users_list(users_dict, contributors_data)

        print('Updating contributors file...')
        update_contributors_file(service_account_file.name, json.dumps(users_dict, indent=4))
        users = create_users_list(users_dict)
        with open(contrib_target, 'a', encoding='utf-8') as f:
            f.write(f'\n {create_grid(users)}')
    except requests.exceptions.HTTPError as ex:
        print(f'Requests errors: {ex}')
        res = requests.request('GET', "https://api.github.com/rate_limit", headers=HEADERS, verify=VERIFY)
        print(f'Github Rate Limit response: {res.text}')
        raise


if __name__ == '__main__':
    main()
