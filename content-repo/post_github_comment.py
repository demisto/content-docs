#!/usr/bin/env python3

# Run this file with pipenv. For example pipenv run content-repo/post_github_comment.py

import argparse
import requests
import subprocess
import os
import re
import json


def get_post_url():
    if os.getenv('PR_NUM'):
        pr_num = os.getenv('PR_NUM')
        return f'https://api.github.com/repos/demisto/content-docs/issues/{pr_num}/comments'
    if os.getenv('CIRCLE_PULL_REQUEST'):
        # change: https://github.com/demisto/content-docs/pull/9
        # to: https://api.github.com/repos/demisto/content-docs/issues/9/comments
        post_url = os.environ['CIRCLE_PULL_REQUEST'].replace('github.com', 'api.github.com/repos').replace('pull', 'issues') + "/comments"
    else:
        # try to get from comment
        last_comment = subprocess.check_output(["git", "log", "-1", "--pretty=%B"], text=True)
        m = re.search(r"#(\d+)", last_comment, re.MULTILINE)
        if not m:
            print("No issue id found in last commit comment. Ignoring: \n------\n{}\n-------".format(last_comment))
            return
        issue_id = m.group(1)
        print("Issue id found from last commit comment: " + issue_id)
        post_url = "https://api.github.com/repos/demisto/content-docs/issues/{}/comments".format(issue_id)
    return post_url


def post_comment(netlify_deploy_file: str):
    post_url = get_post_url()
    if not post_url:
        print('Skipping post comment as could not resolve a PR post url!!')
        return
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("Can't post comment. GITHUB_TOKEN env variable is not set")
    with open(netlify_deploy_file, 'r') as f:
        netlify_info = json.load(f)
    deplpy_url = netlify_info['deploy_url']
    # preview message
    message = "# Preview Site Available\n\n" \
        "Congratulations! The automatic build has completed succesfully.\n" \
        f"A preview site is available at: {deplpy_url}\n\n---\n" \
        "**Important:** Make sure to inspect your changes at the preview site."
    if os.getenv('CIRCLE_BRANCH') == 'master':
        message = "# Production Site Updated\n\n" \
            "Congratulations! The automatic build has completed succesfully.\n" \
            "The production site of our docs has been updated. You can view it at: https://xsoar.pan.dev"
    print(f'Going to post comment:\n------------\n{message}\n------------\nto url: {post_url}')
    verify = os.getenv('SKIP_SSL_VERIFY') is None
    headers = {'Authorization': 'Bearer ' + token}
    res = requests.post(post_url, json={"body": message}, headers=headers, verify=verify)
    res.raise_for_status()


def main():
    desc = """Post a message to github about the deployed site. Relies on environment variables:
GITHUB_TOKEN: api key of user to use for posting
PR_NUM: if set will use this as the pull request number. Otherwise will move on to CIRCLE_PULL_REQUEST
CIRCLE_PULL_REQUEST: pull request url to use to get the pull id. Such as: https://github.com/demisto/content-docs/pull/9
if CIRCLE_PULL_REQUEST will try to get issue id from last commit comment (case of merge into master)
CIRCLE_BRANCH: if set to master treats as a production deployment
SKIP_SSL_VERIFY: if set will skip ssl verification (used for testing behind GP)
    """
    parser = argparse.ArgumentParser(description=desc,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("netlify_deploy_json", help="The netlify deploy json file. For example: deploy-info.json")
    args = parser.parse_args()
    if not os.getenv('GITHUB_TOKEN'):
        print("No github key set. Will not post a message!")
        return
    post_comment(args.netlify_deploy_json)


if __name__ == "__main__":
    main()
