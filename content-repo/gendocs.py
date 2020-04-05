#!/usr/bin/env python3

import argparse
import re
import os
import sys
import glob
import yaml
import inflection
import traceback
import shutil
import json
from bs4 import BeautifulSoup
from mdx_utils import fix_mdx, start_mdx_server, stop_mdx_server, verify_mdx_server
from CommonServerPython import tableToMarkdown  # type: ignore
from typing import List, Optional
from datetime import datetime
from multiprocessing import Pool
from functools import partial

# override print so we have a timestamp with each print
org_print = print


def timestamped_print(*args, **kwargs):
    org_print(datetime.now().strftime("%H:%M:%S.%f"), *args, **kwargs)


print = timestamped_print


INTEGRATION_DOCS_MATCH = [
    "Integrations/[^/]+?/README.md",
    "Integrations/.+_README.md",
    "Packs/[^/]+?/Integrations/[^/]+?/README.md",
    "Packs/[^/]+?/Integrations/.+_README.md",
    "Beta_Integrations/[^/]+?/README.md",
    "Beta_Integrations/.+_README.md",
]
SCRIPTS_DOCS_MATCH = [
    "Scripts/[^/]+?/README.md",
    "Scripts/.+_README.md",
    "Packs/[^/]+?/Scripts/[^/]+?/README.md",
    "Packs/[^/]+?/Scripts/.+_README.md",
]
PLAYBOOKS_DOCS_MATCH = [
    "Playbooks/.+_README.md",
    "Packs/[^/]+?/Playbooks/.+_README.md",
]
INTEGRATIONS_PREFIX = 'integrations'
SCRIPTS_PREFIX = 'scripts'
PLAYBOOKS_PREFIX = 'playbooks'
NO_HTML = '<!-- NOT_HTML_DOC -->'
YES_HTML = '<!-- HTML_DOC -->'
BRANCH = os.getenv('HEAD', 'master')
# env vars for faster development
MAX_FILES = int(os.getenv('MAX_FILES', -1))
FILE_REGEX = os.getenv('FILE_REGEX')


def normalize_id(id: str):
    id = inflection.dasherize(inflection.underscore(id)).replace(' ', '-')
    # replace all non word carachercters (dash is ok)
    return re.sub(r'[^\w-]', '', id)


class DocInfo:
    def __init__(self, id: str, name: str, description: str, readme: str, error_msg: Optional[str] = None):
        self.id = id
        self.name = name
        self.description = description
        self.readme = readme
        self.error_msg = error_msg


def findfiles(match_patterns: List[str], target_dir: str) -> List[str]:
    """Return the list of found files based upon the passed fnmatch patters. Will perform case insensative search regardless of OS.

    Arguments:
        match_patterns {List[str]} -- list of fnmatch patters
        target_dir {str} -- targer dir

    Returns:
        list of found dirs
    """
    rules = [re.compile(target_dir + "/" + r, re.IGNORECASE) for r in match_patterns]
    res = []
    for d in glob.glob(target_dir + "/**", recursive=True):
        for r in rules:
            if r.match(d):
                res.append(d)
                continue
    return res


def is_html_doc(txt: str) -> bool:
    if txt.startswith(NO_HTML):
        return False
    if txt.startswith(YES_HTML):
        return True
    # use some heuristics to try to figure out if this is html
    return txt.startswith('<p>') or ('<thead>' in txt and '<tbody>' in txt)


def gen_html_doc(txt: str) -> str:
    # create a javascript string
    soup = BeautifulSoup(txt, features="html.parser")
    txt = soup.prettify()
    txt = json.dumps(txt)
    return (f'export const txt = {txt};\n\n' +
            '<div dangerouslySetInnerHTML={{__html: txt}} />\n')


def process_readme_doc(target_dir: str, content_dir: str, readme_file: str, ) -> DocInfo:
    try:
        base_dir = os.path.dirname(readme_file)
        if readme_file.endswith('_README.md'):
            ymlfile = readme_file[0:readme_file.index('_README.md')] + '.yml'
        else:
            ymlfiles = glob.glob(base_dir + '/*.yml')
            if not ymlfiles:
                raise ValueError(f'no yml file found')
            if len(ymlfiles) > 1:
                raise ValueError(f'mulitple yml files found: {ymlfiles}')
            ymlfile = ymlfiles[0]
        with open(ymlfile, 'r', encoding='utf-8') as f:
            yml_data = yaml.safe_load(f)
        id = yml_data.get('commonfields', {}).get('id') or yml_data['id']
        id = normalize_id(id)
        name = yml_data.get('display') or yml_data['name']
        desc = yml_data.get('description') or yml_data.get('comment')
        doc_info = DocInfo(id, name, desc, readme_file)
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.strip():
            raise ValueError(f'empty file')
        if is_html_doc(content):
            print(f'{readme_file}: detect html file')
            content = gen_html_doc(content)
        else:
            content = fix_mdx(content)
        # check if we have a header
        lines = content.splitlines(True)
        has_header = len(lines) >= 2 and lines[0].startswith('---') and lines[1].startswith('id:')
        if not has_header:
            readme_repo_path = readme_file
            if readme_repo_path.startswith(content_dir):
                readme_repo_path = readme_repo_path[len(content_dir):]
            edit_url = f'https://github.com/demisto/content/blob/{BRANCH}/{readme_repo_path}'
            content = f'---\nid: {id}\ntitle: "{doc_info.name}"\ncustom_edit_url: {edit_url}\n---\n\n' + content
        verify_mdx_server(content)
        with open(f'{target_dir}/{id}.md', mode='w', encoding='utf-8') as f:  # type: ignore
            f.write(content)
        return doc_info
    except Exception as ex:
        print(f'fail: {readme_file}. Exception: {traceback.format_exc()}')
        return DocInfo('', '', '', readme_file, str(ex).splitlines()[0])
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def index_doc_infos(doc_infos: List[DocInfo], link_prefix: str):
    if not doc_infos:
        return ''
    table_items = []
    for d in doc_infos:
        table_items.append({
            'Name': f'[{d.name}]({link_prefix}/{d.id})',
            'Description': d.description
        })
    res = tableToMarkdown('', table_items, headers=['Name', 'Description'])
    return fix_mdx(res)


# POOL has to be declared after process_readme_doc so it can find it when doing map
# multiprocess pool
POOL_SIZE = 4
POOL = Pool(POOL_SIZE)


def create_docs(content_dir: str, target_dir: str, regex_list: List[str], prefix: str):
    print(f'Using BRANCH: {BRANCH}')
    # Search for readme files
    readme_files = findfiles(regex_list, content_dir)
    print(f'Processing: {len(readme_files)} {prefix} files ...')
    if MAX_FILES > 0:
        print(f'DEV MODE. Truncating file list to: {MAX_FILES}')
        readme_files = readme_files[:MAX_FILES]
    if FILE_REGEX:
        print(f'DEV MODE. Matching only files which match: {FILE_REGEX}')
        regex = re.compile(FILE_REGEX)
        readme_files = list(filter(regex.search, readme_files))
    target_sub_dir = f'{target_dir}/{prefix}'
    if not os.path.exists(target_sub_dir):
        os.makedirs(target_sub_dir)
    doc_infos: List[DocInfo] = []
    success = []
    fail = []
    # flush before starting multi process
    sys.stdout.flush()
    sys.stderr.flush()
    seen_docs = {}
    for doc_info in POOL.map(partial(process_readme_doc, target_sub_dir, content_dir), readme_files):
        if doc_info.error_msg:
            fail.append(f'{doc_info.readme} ({doc_info.error_msg})')
        elif doc_info.id in seen_docs:
            fail.append(f'{doc_info.readme} (duplicate with {seen_docs[doc_info.id].readme})')
        else:
            doc_infos.append(doc_info)
            success.append(doc_info.readme)
            seen_docs[doc_info.id] = doc_info
    org_print(f'\n===========================================\nSuccess {prefix} docs ({len(success)}):')
    for r in sorted(success):
        print(r)
    org_print(f'\n===========================================\nFailed {prefix} docs ({len(fail)}):')
    for r in sorted(fail):
        print(r)
    org_print("\n===========================================\n")
    return sorted(doc_infos, key=lambda d: d.name)  # sort by name


def main():
    parser = argparse.ArgumentParser(description='Generate Content Docs',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--target", help="Target dir to generate docs at.", required=True)
    parser.add_argument("-d", "--dir", help="Content repo dir.", required=True)
    args = parser.parse_args()
    print(f'Using multiprocess pool size: {POOL_SIZE}')
    print('Starting MDX server...')
    start_mdx_server()
    prefix = os.path.basename(args.target)
    integrations_full_prefix = f'{prefix}/{INTEGRATIONS_PREFIX}'
    scripts_full_prefix = f'{prefix}/{SCRIPTS_PREFIX}'
    playbooks_full_prefix = f'{prefix}/{PLAYBOOKS_PREFIX}'
    integration_doc_infos = create_docs(args.dir, args.target, INTEGRATION_DOCS_MATCH, INTEGRATIONS_PREFIX)
    playbooks_doc_infos = create_docs(args.dir, args.target, PLAYBOOKS_DOCS_MATCH, PLAYBOOKS_PREFIX)
    script_doc_infos = create_docs(args.dir, args.target, SCRIPTS_DOCS_MATCH, SCRIPTS_PREFIX)
    index_base = f'{os.path.dirname(os.path.abspath(__file__))}/reference-index.md'
    index_target = args.target + '/index.md'
    shutil.copy(index_base, index_target)
    with open(index_target, 'a', encoding='utf-8') as f:
        f.write("\n\n## Integrations\n\n")
        f.write(index_doc_infos(integration_doc_infos, INTEGRATIONS_PREFIX))
        f.write("\n\n## Playbooks\n\n")
        f.write(index_doc_infos(playbooks_doc_infos, PLAYBOOKS_PREFIX))
        f.write("\n\n## Scripts\n\n")
        f.write(index_doc_infos(script_doc_infos, SCRIPTS_PREFIX))
    integration_items = [f'{integrations_full_prefix}/{d.id}' for d in integration_doc_infos]
    playbook_items = [f'{playbooks_full_prefix}/{d.id}' for d in playbooks_doc_infos]
    script_items = [f'{scripts_full_prefix}/{d.id}' for d in script_doc_infos]
    sidebar = [
        {
            "type": "doc",
            "id": f'{prefix}/index'
        },
        {
            "type": "category",
            "label": "Integrations",
            "items": integration_items
        },
        {
            "type": "category",
            "label": "Playbooks",
            "items": playbook_items
        },
        {
            "type": "category",
            "label": "Scripts",
            "items": script_items
        }
    ]
    with open(f'{args.target}/sidebar.json', 'w') as f:
        json.dump(sidebar, f, indent=4)
    print('Stopping mdx server ...')
    stop_mdx_server()


if __name__ == "__main__":
    main()
