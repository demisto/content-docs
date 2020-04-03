#!/usr/bin/env python3

import argparse
import re
import os
import glob
import yaml
import inflection
import traceback
import shutil
import json
import tempfile
from bs4 import BeautifulSoup
from mdx_utils import fix_mdx, verify_mdx
from CommonServerPython import tableToMarkdown  # type: ignore
from typing import List

INTEGRATION_DOCS_MATCH = [
    "Integrations/[^/]+?/README.md",
    "Integrations/.+_README.md",
    "Packs/[^/]+?/Integrations/[^/]+?/README.md",
    "Packs/[^/]+?/Integrations/.+_README.md",
    "Beta_Integrations/[^/]+?/README.md",
    "Beta_Integrations/.+_README.md",
]
INTEGRATIONS_PREFIX = 'integrations'
NO_HTML = '<!-- NOT_HTML_DOC -->'
YES_HTML = '<!-- HTML_DOC -->'
BRANCH = os.getenv('HEAD', 'master')


class DocInfo:
    def __init__(self, id: str, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description


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


def process_integration_doc(readme_file: str, target_dir: str, content_dir: str) -> DocInfo:
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
    id = yml_data['commonfields']['id']
    id = inflection.dasherize(inflection.underscore(id)).replace(' ', '-').replace('?', '')
    doc_info = DocInfo(id, yml_data['display'], yml_data.get('description'))
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
        content = f'---\nid: {id}\ntitle: {doc_info.name}\ncustom_edit_url: {edit_url}\n---\n\n' + content
    with tempfile.NamedTemporaryFile('w', encoding='utf-8') as f:  # type: ignore
        f.write(content)
        f.flush()
        verify_mdx(f.name)
        shutil.copy(f.name, f'{target_dir}/{id}.md')
    return doc_info


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


def create_integration_docs(content_dir: str, target_dir: str):
    print(f'Using BRANCH: {BRANCH}')
    # Search for integration readme files
    readme_files = findfiles(INTEGRATION_DOCS_MATCH, content_dir)
    print(f'Processing: {len(readme_files)} integrations ...')
    prefix = os.path.basename(target_dir)
    prefix = f'{prefix}/{INTEGRATIONS_PREFIX}'
    integrations_dir = f'{target_dir}/{INTEGRATIONS_PREFIX}'
    if not os.path.exists(integrations_dir):
        os.makedirs(integrations_dir)
    doc_infos: List[DocInfo] = []
    success = []
    fail = []
    for r in readme_files:
        try:
            doc_infos.append(process_integration_doc(r, integrations_dir, content_dir))
            success.append(r)
        except Exception as ex:
            print(f'ERROR: failed processing: {r}. Exception: {ex}.\n{traceback.format_exc()}--------------------------')
            fail.append(f'{r} ({str(ex).splitlines()[0]})')
    print("Success integration docs:")
    for r in sorted(success):
        print(r)
    print("\n===========================================\nFailed integration docs:")
    for r in sorted(fail):
        print(r)
    print("\n===========================================\n")
    return doc_infos, prefix


def main():
    parser = argparse.ArgumentParser(description='Generate Content Docs',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--target", help="Target dir to generate docs at.", required=True)
    parser.add_argument("-d", "--dir", help="Content repo dir.", required=True)
    args = parser.parse_args()
    prefix = os.path.basename(args.target)
    doc_infos, integrations_full_prefix = create_integration_docs(args.dir, args.target)
    doc_infos = sorted(doc_infos, key=lambda d: d.name)  # sort by name
    index_base = f'{os.path.dirname(os.path.abspath(__file__))}/reference-index.md'
    index_target = args.target + '/index.md'
    shutil.copy(index_base, index_target)
    with open(index_target, 'a', encoding='utf-8') as f:
        f.write("\n\n## Integrations\n\n")
        f.write(index_doc_infos(doc_infos, INTEGRATIONS_PREFIX))
    integration_items = [f'{integrations_full_prefix}/{d.id}' for d in doc_infos]
    sidebar = [
        {
            "type": "doc",
            "id": f'{prefix}/index'
        },
        {
            "type": "category",
            "label": "Integrations",
            "items": integration_items
        }
    ]
    with open(f'{args.target}/sidebar.json', 'w') as f:
        json.dump(sidebar, f, indent=4)


if __name__ == "__main__":
    main()
