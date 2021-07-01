import argparse
import os
import re
import shutil
import sys

import requests
from collections import OrderedDict

# Disable insecure warnings
import urllib3
from mdx_utils import (fix_mdx, fix_relative_images, normalize_id,
                       start_mdx_server, stop_mdx_server, verify_mdx_server)

urllib3.disable_warnings()


PR_NUMBER_REGEX = re.compile(r'([0-9]+)')
URL = 'https://api.github.com'
HEADERS = {
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': "Bearer " + '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'
}


def make_markdown_table(array):

    """ Input: Python list with rows of table as lists
               First element as header.
        Output: String to put into a .md file
    """
    markdown = '# Top XSOAR Contributors'
    markdown += "\n" + str("| ") + " "

    markdown += "User | Prs |  <!-- --> " + "\n"

    markdown += '|'
    for i in range(len(array[0])):
        markdown += str("-------------- | ")
    markdown += "\n"

    for entry in array[0:]:
        markdown += str("| ")
        user = entry.get('User')
        prs = entry.get('PRs')
        image = entry.get('Image')
        to_add = str(user) + str(" | ") + str(prs) + str(" | ") + f'<img src="{image}" style=width:50px>'
        markdown += to_add
        markdown += "\n"

    return markdown + "\n"


def get_contrib_prs():
    inner_prs = []
    pr_bodies = []
    url = URL + '/search/issues'
    query = 'type:pr state:closed org:demisto repo:content is:merged base:master head:contrib/'
    params = {
        'q': query,
        'per_page': 100,
        'page': 5
    }
    res = requests.request('GET', url, headers=HEADERS, params=params, verify=False)
    prs = res.json().get('items', [])
    link = res.headers.get('Link')
    if link:
        links = link.split(',')
        for link in links:
            last_page = link[link.find("<")+1:link.find(">")][-1]
        while params['page'] <= int(last_page):
            params['page'] = params['page'] + 1
            response = requests.request('GET', url, params=params, headers=HEADERS, verify=False)
            next_page_prs = response.json().get('items', [])
            prs.extend(next_page_prs)
    for pr in prs:
        pr_body = pr.get('body', '')
        inner_pr = PR_NUMBER_REGEX.search(pr_body)
        if inner_pr is not None:
            pr_bodies.append(pr_body)
            inner_prs.append(inner_pr[0])

    return pr_bodies, inner_prs


def get_pr_user():
    users = []
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
            user = response.get('user').get('login')

            if not user == 'xsoar-bot':
                users.append({
                    'User': user,
                    'Image': response.get('user').get('avatar_url')
                })
    for user in users:
        prs = users.count(user)

        user.update({'PRs': prs})

    result = {i['User']: i for i in reversed(users)}.values()
    new_res = sorted(result, key=lambda k: k['PRs'], reverse=True)[:10]

    res = make_markdown_table(new_res)
    return fix_mdx(res)


def main():
    parser = argparse.ArgumentParser(description='Generate Top contributors page.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--target", help="Target dir to generate docs at.", required=True)
    args = parser.parse_args()
    start_mdx_server()
    contrib_base = f'{os.path.dirname(os.path.abspath(__file__))}/top-contribution.md'
    contrib_target = args.target + '/top-contribution.md'
    shutil.copy(contrib_base, contrib_target)
    with open(contrib_target, 'a', encoding='utf-8') as f:
        f.write(get_pr_user())

    print('Stopping mdx server ...')
    stop_mdx_server()


if __name__ == "__main__":
    main()
