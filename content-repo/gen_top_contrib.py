#!/usr/bin/env python3

import argparse
import os
import re

import requests
import urllib3

# Disable insecure warnings
urllib3.disable_warnings()


PR_NUMBER_REGEX = re.compile(r'(?<=pull/)([0-9]+)')
USER_NAME_REGEX = re.compile(r'(?<=@)[a-zA-z-0-9]+')
TOKEN = os.getenv('GITHUB_TOKEN')
URL = 'https://api.github.com'
HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'Bearer ' + TOKEN
}


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


def get_external_prs(prs: list):
    """
    Get the external prs from the internal.
    We are using this to get the contributor github user in get_pr_user command.
    Args:
        prs: list of internal prs.

    Returns:
        inner_prs: list of external prs.
        pr_bodies: list of external pr bodies.
    """
    inner_prs = []
    pr_bodies = []
    for pr in prs:
        pr_body = pr.get('body', '')
        if inner_pr := PR_NUMBER_REGEX.search(pr_body):
            pr_bodies.append(pr_body)
            inner_prs.append(inner_pr[0])

    return pr_bodies, inner_prs


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
            response = requests.request('GET', url, params=params, headers=HEADERS, verify=False)
            next_page_prs = response.json().get('items', [])
            prs.extend(next_page_prs)

    return prs


def get_contractors_prs() -> list:
    """
    Get all contractors pr numbers and users we want to ignore in the calculation.
    Returns: The inner pr numbers list of the contractors and the users we want to ignore.
    """
    url = URL + '/search/issues'
    query = 'type:pr state:closed org:demisto repo:content is:merged base:master ' \
            'head:contrib/crest head:contrib/qmasters head:contrib/mchasepan head:contrib/roybi72'
    params = {
        'q': query,
        'per_page': 100,
        'page': 1
    }
    res = requests.request('GET', url, headers=HEADERS, params=params, verify=False)
    res.raise_for_status()
    prs = res.json().get('items', [])

    next_pages_prs = github_pagination_prs(url, params, res)
    prs.extend(next_pages_prs)

    _, inner_prs = get_external_prs(prs)

    return inner_prs


def get_contrib_prs():
    """
    Get the contributors prs.
    Returns: The list of inner PRs and a list of the pr bodies.
    """
    url = URL + '/search/issues'
    query = 'type:pr state:closed org:demisto repo:content is:merged base:master head:contrib/'
    params = {
        'q': query,
        'per_page': 100,
        'page': 1
    }
    res = requests.request('GET', url, headers=HEADERS, params=params, verify=False)
    res.raise_for_status()
    prs = res.json().get('items', [])

    # Get all the PRs from all pages
    next_pages_prs = github_pagination_prs(url, params, res)
    prs.extend(next_pages_prs)

    pr_bodies, inner_prs = get_external_prs(prs)
    contractors_prs = get_contractors_prs()
    for pr in inner_prs:
        if pr in contractors_prs:
            inner_prs.remove(pr)

    return pr_bodies, inner_prs


def get_github_user(user_name: str):
    """
    Get the github user.
    Args:
        user_name (str): the github username.

    Returns: The user avatar and its profile.

    """
    url = f'{URL}/users/{user_name}'
    res = requests.request('GET', url, headers=HEADERS, verify=False)
    response = res.json()
    github_avatar = response.get('avatar_url')
    github_profile = response.get('html_url')

    return github_avatar, github_profile


def get_inner_pr_request() -> dict:
    """
    Get the inner pr information (will be used to get the user).
    Returns (dict): http response - prs_info.
    """
    prs_info = {}
    _, inner_prs = get_contrib_prs()
    for pr in inner_prs:
        url = URL + f'/repos/demisto/content/pulls/{pr}'
        res = requests.request('GET', url, headers=HEADERS, verify=False)
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
            prs_info.update(response)

    return prs_info


def get_contributors_users(response) -> list:
    """
    Get the github users from the inner PRs.
    Args:
        response (dict): the response of get_inner_pr_request()

    Returns (list): Github users

    """
    users = []
    user = response.get('user').get('login')
    github_profile = response.get('user').get('html_url')

    if not user == 'xsoar-bot':
        users.append({
            'Contributor': f"<img src='{response.get('user').get('avatar_url')}'/><br></br> "
                           f"<a href='{github_profile}' target='_blank'>{user}</a>"
        })

    if user == 'xsoar-bot':
        pr_body = response.get('body')
        if 'Contributor' in pr_body:
            contributor = USER_NAME_REGEX.search(pr_body)[0].replace('\n', '')
            github_avatar, github_profile = get_github_user(contributor)
            if not github_avatar and not github_profile:
                print(f'The user "{contributor}" was not found.')

            users.append({
                'Contributor': f"<img src='{github_avatar}'/><br></br> "
                               f"<a href='{github_profile}' target='_blank'>{contributor}</a>"
            })
    for user in users:
        prs = users.count(user)
        user.update({'Number of Contributions': prs})

    list_users = []
    result = {i['Contributor']: i for i in reversed(users)}.values()
    new_res = sorted(result, key=lambda k: k['Number of Contributions'], reverse=True)

    for user in new_res:
        user['Contributor'] += f'<br></br>{user["Number of Contributions"]} Contributions'
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
