#!/usr/bin/env python3

# Runs as part of the Forked PR Deploy flow (see: .github/workflows/forked-pr-deploy.yml)
# Expecets to recieve the Github pull_request event file

import json
import argparse
import requests
import os
import shutil

VERIFY_SSL = not (os.getenv('VERIFY_SSL') and os.getenv('VERIFY_SSL').lower() in ('false', '0', 'no'))

if not VERIFY_SSL:
    requests.packages.urllib3.disable_warnings()


def download_file(url: str, target_path: str):
    with requests.get(url, stream=True, verify=VERIFY_SSL) as r:
        r.raise_for_status()
        with open(target_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f, length=32*1024*1024)


def download_site_build(event_file: str, download_path: str = "build-site.tar.gz") -> int:
    """Will download the site bulid if this is a forked PR bulid.

    Args:
        event_file (str): event file from the workflow

    Returns:
        int: PR num of the build if relevant
    """
    with open(event_file, 'r') as f:
        github_event = json.load(f)
    target_url = github_event['target_url']
    print(f'target_url: {target_url}')
    # target_url is of the form:
    # https://circleci.com/gh/demisto/content-docs/142?utm_campaign=vcs-integration-link&utm_medium=referral&utm_source=github-build-li
    target_url = target_url.split('?')[0]
    build_num = target_url.split('/')[-1]
    print(f'circleci build: {build_num}')
    circle_url = f'https://circleci.com/api/v1.1/project/github/demisto/content-docs/{build_num}'
    print(f'Checking circleci url: {circle_url}')
    res = requests.get(circle_url, verify=VERIFY_SSL)
    res.raise_for_status()
    build_json = res.json()
    # check that this is a pull request
    if not build_json.get('pull_requests') or not build_json.get('pull_requests')[0].get('url'):
        print('Not a pull request. Skipping')
        return 0
    branch = build_json.get('branch')
    if not branch or not branch.startswith('pull/'):
        print(f'Skipping branch as it is not an external pull: {branch}')
        return 0
    pr_num = branch.split('/')[1]
    # get artifacts
    res = requests.get(f'{circle_url}/artifacts', verify=VERIFY_SSL)
    res.raise_for_status()
    artifacts = res.json()
    download_url = None
    for art in artifacts:
        if 'build-site.tar.gz' in art.get('path'):
            download_url = art.get('url')
            break
    if not download_url:
        raise ValueError(f"download url missing for artifacts: {artifacts}")
    print(f'Downloading build artifact from: {download_url} (pr num: {pr_num}) to: {download_path} ...')
    download_file(download_url, download_path)
    return int(pr_num)


def main():
    parser = argparse.ArgumentParser(description='Deploy Site Build from CircleCI Forked PR Build',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-e", "--event", help="Github event data file which triggered the workflow", required=True)
    args = parser.parse_args()
    pr = download_site_build(args.event)
    if pr:
        # priint so workflow picks up the pr
        # see: https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-commands-for-github-actions#setting-an-output-parameter
        print('set output for forked pr: {pr}')
        print(f'::set-output name=forked_pr::{pr}')
    else:
        print('not outputting forked pr as no pr num found')


if __name__ == "__main__":
    main()
