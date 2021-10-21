#!/usr/bin/env python3

# Run this file with pipenv. For example pipenv run content-repo/post_github_comment.py

import argparse
import traceback
from typing import List, Tuple
import requests
import subprocess
import os
import re
import json
import yaml
from mdx_utils import normalize_id

ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')


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


def get_modified_files():
    files = subprocess.check_output(['git', 'diff', '--name-only', 'origin/master...HEAD', '--', 'docs', 'content-repo/extra-docs/'],
                                    text=True, cwd=ROOT_DIR)
    return [line for line in files.splitlines() if line.lower().endswith('.md')]


def get_front_matter_data(file: str):
    with open(file, "r") as f:
        head = f.read(4096)
    front_matter_match = re.match(r'---\n(.*?)\n---', head, re.DOTALL)
    if not front_matter_match:
        raise ValueError(f'No front matter. Doc file: {file}')
    yml_matter = front_matter_match[1]
    return yaml.safe_load(yml_matter)


def get_link_for_doc_file(base_url: str, file: str):
    yml_data = get_front_matter_data(file)
    name = yml_data.get('title') or file
    relative_path = os.path.relpath(file, ROOT_DIR)
    path = f'{base_url}/{os.path.dirname(relative_path)}/{yml_data["id"]}'
    return (name, path)


def get_link_for_ref_file(base_url: str, file: str):
    if 'releases' in file:
        name = os.path.splitext(os.path.basename(file))[0]
        return (f'Content Release {name}', f'{base_url}/docs/reference/releases/{name}')
    # articles/integrations
    yml_data = get_front_matter_data(file)
    name = yml_data.get('title') or file
    id = yml_data.get('id') or normalize_id(name)
    relative_path = os.path.relpath(file, ROOT_DIR).replace('content-repo/extra-docs', 'docs/reference')
    path = f'{base_url}/{os.path.dirname(relative_path)}/{id}'
    return (name, path)


def get_modified_links(base_url: str):
    links: List[Tuple[str, str]] = []
    for f in get_modified_files():
        try:
            if f.startswith('docs'):
                links.append(get_link_for_doc_file(base_url, f))
            else:
                links.append(get_link_for_ref_file(base_url, f))
        except Exception as ex:
            print(f'Failed getting modified link for file: {f}. Exception: {str(ex)}')
            traceback.print_exc()
    return links


def post_comment(deploy_info_file: str):
    post_url = get_post_url()
    if not post_url:
        print('Skipping post comment as could not resolve a PR post url!!')
        return
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise ValueError("Can't post comment. GITHUB_TOKEN env variable is not set")

    host = "Netlify"
    # handle Netlify deployment message
    if deploy_info_file.endswith(".json"):
        with open(deploy_info_file, 'r') as f:
            netlify_info = json.load(f)
        deploy_url = netlify_info['deploy_url']

    # handle Firebase deployment message
    else:
        host = "Firebase"
        with open(deploy_info_file, 'r') as f:
            if matched_url := re.search("https://xsoar-pan-dev--pull-request-.*web.app", f.read()):
                deploy_url = matched_url.group(0)

    # preview message
    message = f"# {host} Preview Site Available\n\n" \
        "Congratulations! The automatic build has completed succesfully.\n" \
        f"A preview site is available at: {deploy_url}\n\n---\n" \
        "**Important:** Make sure to inspect your changes at the preview site."
    if os.getenv('CIRCLE_BRANCH') == 'master':
        # TODO - revert url to "https://xsoar.pan.dev" after the migration
        url = "https://xsoar.pan.dev" if host == "Netlify" else "https://xsoar-pan-dev.web.app"

        message = f"#{host} Production Site Updated\n\n" \
            "Congratulations! The automatic build has completed successfully.\n" \
            f"The production site of our docs has been updated. You can view it at: {url}"
    else:
        # add detcted changes
        try:
            links = get_modified_links(deploy_url)
            if links:
                message += '\n\nDetected modified urls:\n'
                for link in links:
                    message += f'*  [{link[0]}]({link[1]})\n'
        except Exception as ex:
            print(f'Failed getting modified file links: {str(ex)}')
            traceback.print_exc()
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
    parser.add_argument("deploy_info_file",
                        help="The deploy file. For example: deploy-info.json / deploy-info-firebase.txt")
    args = parser.parse_args()
    if not os.getenv('GITHUB_TOKEN'):
        print("No github key set. Will not post a message!")
        return
    post_comment(args.deploy_info_file)


if __name__ == "__main__":
    main()
