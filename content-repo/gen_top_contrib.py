#!/usr/bin/env python3

import argparse
import os
import re

import requests
from typing import List, Dict
from datetime import datetime

PR_NUMBER_REGEX = re.compile(r'(?<=pull/)([0-9]+)')
USER_NAME_REGEX = re.compile(r'(?<=@)[a-zA-Z-0-9]+')
TOKEN = os.getenv('GITHUB_TOKEN', '')
URL = 'https://api.github.com'
HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
}
if TOKEN:
    HEADERS['Authorization'] = 'Bearer ' + TOKEN
VERIFY = os.getenv('SKIP_SSL_VERIFY') is None


# override print so we have a timestamp with each print
def timestamped_print(*args, **kwargs):
    __builtins__.print(datetime.now().strftime("%H:%M:%S.%f"), *args, **kwargs)


print = timestamped_print


def create_grid(dataset: list) -> str:
    """
    Create a table grid of the github users
    Args:
        dataset (list): The dataset to create the table from, in this case, the list of github users.

    Returns (str): table grid of github users

    """
    row_length = 7
    html_card = ''
    for i in range(0, len(dataset), row_length):
        html_card += '<tr>'
        for element in dataset[i:i+row_length]:
            html_card += f'\n<td>{element} </td>\n'
        html_card += '</tr>\n'

    return html_card


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


def github_pagination_prs(url: str, params: dict, res) -> list:
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
        for link in links:
            last_page = link[link.find("<")+1:link.find(">")][-1]
        while params['page'] <= int(last_page):
            params['page'] = params['page'] + 1
            response = requests.request('GET', url, params=params, headers=HEADERS, verify=VERIFY)
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
    res = requests.request('GET', url, headers=HEADERS, params=params, verify=VERIFY)
    res.raise_for_status()
    prs = res.json().get('items', [])

    next_pages_prs = github_pagination_prs(url, params, res)
    prs.extend(next_pages_prs)

    external_prs = get_external_prs(prs)

    return external_prs


def get_contrib_prs() -> List[Dict]:
    """
    Get the contributors prs.
    Returns: The list of PRs.
    """
    url = URL + '/search/issues'
    query = 'type:pr state:closed org:demisto repo:content is:merged base:master head:contrib/'
    params = {
        'q': query,
        'per_page': 100,
        'page': 1
    }
    res = requests.request('GET', url, headers=HEADERS, params=params, verify=VERIFY)
    res.raise_for_status()
    prs = res.json().get('items', [])

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

    return contrib_prs


def get_github_user(user_name: str) -> Dict:
    """
    Get the github user.
    Args:
        user_name (str): the github username.

    Returns: The user avatar and its profile.

    """
    url = f'{URL}/users/{user_name}'
    res = requests.request('GET', url, headers=HEADERS, verify=VERIFY)
    if res.status_code == 404:
        print(f'The user {user_name} was not found.')
    else:
        response = res.json()
        return response


def get_inner_pr_request() -> list:
    """
    Get the inner pr information (will be used to get the user).
    Returns (list): http response - prs_info.
    """
    users_info = []
    external_prs = get_contrib_prs()
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

    return users_info


def get_contributors_users(users_info) -> list:
    """
    Get the github users from the inner PRs.
    Args:
        users_info (list): the response of get_inner_pr_request()

    Returns (list): Github users

    """
    users = []
    for item in users_info:
        user = item.get('login')
        github_profile = item.get('html_url')
        pr_body = item.get('body')

        if not user == 'xsoar-bot':
            users.append({
                'Contributor': f"<img src='{item.get('avatar_url')}'/><br></br> "
                               f"<a href='{github_profile}' target='_blank'>{user}</a>"
            })

        if user == 'xsoar-bot':
            if 'Contributor' in pr_body:
                contributor = USER_NAME_REGEX.search(pr_body)[0].replace('\n', '')
                user_info = get_github_user(contributor)
                github_avatar = user_info.get('avatar_url')
                github_profile = user_info.get('html_url')
                if not github_avatar and not github_profile:
                    print(f'The user "{contributor}" was not found.')
                    continue

                users.append({
                    'Contributor': f"<img src='{github_avatar}'/><br></br> "
                                   f"<a href='{github_profile}' target='_blank'>{contributor}</a>"
                })

    for user in users:
        prs = users.count(user)
        user.update({'Number of Contribution(s)': prs})

    list_users = []
    result = {i['Contributor']: i for i in reversed(users)}.values()
    new_res = sorted(result, key=lambda k: k['Number of Contribution(s)'], reverse=True)

    for user in new_res:
        user['Contributor'] += f'<br></br>{user["Number of Contribution(s)"]} Contributions'
        list_users.append(user['Contributor'])

    return list_users


def main():
    parser = argparse.ArgumentParser(description='Generate Top contributors page.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--target", help="Target dir to generate docs at.", required=True)
    args = parser.parse_args()
    contrib_target = args.target + '/top-contributors.md'
    response = get_inner_pr_request()
    users_list = get_contributors_users(response)
    with open(contrib_target, 'a', encoding='utf-8') as f:
        f.write(f'\n {create_grid(users_list)}')


if __name__ == '__main__':
    main()
