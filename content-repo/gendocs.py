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
from typing import List, Optional, Dict, Tuple, Iterator
from datetime import datetime
from multiprocessing import Pool
from functools import partial
import html
from distutils.version import StrictVersion
import random
import dateutil.relativedelta

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
RELEASES_PREFIX = 'releases'
ATRICLES_PREFIX = 'articles'
NO_HTML = '<!-- NOT_HTML_DOC -->'
YES_HTML = '<!-- HTML_DOC -->'
BRANCH = os.getenv('HEAD', 'master')
MAX_FAILURES = int(os.getenv('MAX_FAILURES', 10))  # if we have more than this amount in a single category we fail the build
# env vars for faster development
MAX_FILES = int(os.getenv('MAX_FILES', -1))
FILE_REGEX = os.getenv('FILE_REGEX')

# initialize the seed according to the PR branch. Used when selecting max files.
random.seed(os.getenv('CIRCLE_BRANCH'))

MIN_RELEASE_VERSION = StrictVersion((datetime.now() + dateutil.relativedelta.relativedelta(months=-18)).strftime('%y.%-m.0'))


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


def get_deprecated_data(yml_data: dict, desc: str, readme_file: str):
    if yml_data.get('deprecated') or 'DeprecatedContent' in readme_file or yml_data.get('hidden'):
        dep_msg = ""
        dep_match = re.match(r'deprecated\s*[\.\-:]\s*(.*?)\.', desc, re.IGNORECASE)
        if dep_match and 'instead' in dep_match[1]:
            dep_msg = dep_match[1] + '\n'
        return f':::caution Deprecated\n{dep_msg}:::\n\n'
    return ""


def get_beta_data(yml_data: dict, content: str):
    if yml_data.get('beta'):
        msg = ''
        if not re.search(r'This is a beta', content, re.IGNORECASE):
            # only add the beta disclaimer if it is not in the docs
            msg = 'This is a beta Integration, which lets you implement and test pre-release software. ' \
                  'Since the integration is beta, it might contain bugs. Updates to the integration during the beta phase might '\
                  'include non-backward compatible features. We appreciate your feedback on the quality and usability of the '\
                  'integration to help us identify issues, fix them, and continually improve.\n'
        return f':::info beta\n{msg}:::\n\n'
    return ""


def process_readme_doc(target_dir: str, content_dir: str, readme_file: str) -> DocInfo:
    try:
        base_dir = os.path.dirname(readme_file)
        if readme_file.endswith('_README.md'):
            ymlfile = readme_file[0:readme_file.index('_README.md')] + '.yml'
        else:
            ymlfiles = glob.glob(base_dir + '/*.yml')
            if not ymlfiles:
                raise ValueError('no yml file found')
            if len(ymlfiles) > 1:
                raise ValueError(f'mulitple yml files found: {ymlfiles}')
            ymlfile = ymlfiles[0]
        with open(ymlfile, 'r', encoding='utf-8') as f:
            yml_data = yaml.safe_load(f)
        id = yml_data.get('commonfields', {}).get('id') or yml_data['id']
        id = normalize_id(id)
        name = yml_data.get('display') or yml_data['name']
        desc = yml_data.get('description') or yml_data.get('comment')
        if desc:
            word_break = False
            for word in re.split(r'\s|-', desc):
                if len(word) > 40:
                    word_break = True
            desc = html.escape(desc)
            if word_break:  # long words tell browser to break in the midle
                desc = '<span style={{wordBreak: "break-word"}}>' + desc + '</span>'
        doc_info = DocInfo(id, name, desc, readme_file)
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.strip():
            raise ValueError('empty file')
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
            header = f'---\nid: {id}\ntitle: {json.dumps(doc_info.name)}\ncustom_edit_url: {edit_url}\n---\n\n'
            content = get_deprecated_data(yml_data, desc, readme_file) + content
            content = get_beta_data(yml_data, content) + content
            content = header + content
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


def process_release_doc(target_dir: str, release_file: str) -> Optional[DocInfo]:
    try:
        name = os.path.splitext(os.path.basename(release_file))[0]
        if name < MIN_RELEASE_VERSION:
            print(f'Skipping release notes: {release_file} as it is older than: {MIN_RELEASE_VERSION}')
            return None
        with open(release_file, 'r', encoding='utf-8') as f:
            content = f.read()
        desc_match = re.search(r'Published on .*', content, re.IGNORECASE)
        if not desc_match:
            raise ValueError('Published on... not found for release: ' + name)
        doc_info = DocInfo(name, f'Content Release {name}', desc_match[0], release_file)
        edit_url = f'https://github.com/demisto/content-docs/blob/master/content-repo/extra-docs/releases/{name}.md'
        #  replace the title to be with one # so it doesn't appear in the TOC
        content = re.sub(r'^## Demisto Content Release Notes', '# Demisto Content Release Notes', content)
        content = f'---\nid: {name}\ntitle: "{name}"\ncustom_edit_url: {edit_url}\nhide_title: true\n---\n\n' + content
        download_msg = "Download"
        packs_download = ""
        if name > StrictVersion('20.8.0'):
            # from 20.8.1 we also add a link to the marketplace zips
            download_msg = "Download Content Zip (Cortex XSOAR 5.5 and earlier)"
            packs_download = '* **Download Marketplace Packs (Cortex XSOAR 6.0 and later):** ' + \
                f'[content_marketplace_packs.zip](https://github.com/demisto/content/releases/download/{name}/content_marketplace_packs.zip)\n'
        content = content + \
            f'\n\n---\n### Assets\n\n* **{download_msg}:** ' + \
            f'[content_new.zip](https://github.com/demisto/content/releases/download/{name}/content_new.zip)\n'
        if packs_download:
            content = content + packs_download
        content = content + \
            f'* **Browse the Source Code:** [Content Repo @ {name}](https://github.com/demisto/content/tree/{name})\n'
        verify_mdx_server(content)
        with open(f'{target_dir}/{name}.md', mode='w', encoding='utf-8') as f:
            f.write(content)
        return doc_info
    except Exception as ex:
        print(f'fail: {release_file}. Exception: {traceback.format_exc()}. Message: {ex}')
        # We shouldn't have failing release docs. Breack the build
        raise
    finally:
        sys.stdout.flush()
        sys.stderr.flush()


def index_doc_infos(doc_infos: List[DocInfo], link_prefix: str, headers: Optional[Tuple[str, str]] = None):
    if not headers:
        headers = ('Name', 'Description')
    if not doc_infos:
        return ''
    table_items = []
    for d in doc_infos:
        name = html.escape(d.name)
        link_name = f'[{name}]({link_prefix}/{d.id})'
        for word in re.split(r'\s|-', name):
            if len(word) > 25:  # we have a long word tell browser ok to break it
                link_name = '<span style={{wordBreak: "break-word"}}>' + link_name + '</span>'
                break
        table_items.append({
            headers[0]: link_name,
            headers[1]: d.description
        })
    res = tableToMarkdown('', table_items, headers=headers)
    return fix_mdx(res)


def process_extra_readme_doc(target_dir: str, prefix: str, readme_file: str) -> DocInfo:
    try:
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
        front_matter_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
        if not front_matter_match:
            raise ValueError(f'No front matter. Extra docs must have description and title front matter. File: {readme_file}')
        yml_matter = front_matter_match[1]
        yml_data = yaml.safe_load(yml_matter)
        name = yml_data['title']
        file_id = yml_data.get('id') or normalize_id(name)
        desc = yml_data.get('description')
        readme_file_name = os.path.basename(readme_file)
        edit_url = f'https://github.com/demisto/content-docs/blob/master/content-repo/extra-docs/{prefix}/{readme_file_name}'
        content = content.replace(front_matter_match[0], '')
        content = f'---\nid: {file_id}\ntitle: "{name}"\ncustom_edit_url: {edit_url}\n---\n\n' + content
        verify_mdx_server(content)
        with open(f'{target_dir}/{file_id}.md', mode='w', encoding='utf-8') as f:
            f.write(content)
        return DocInfo(file_id, name, desc, readme_file)
    except Exception as ex:
        print(f'fail: {readme_file}. Exception: {traceback.format_exc()}')
        return DocInfo('', '', '', readme_file, str(ex).splitlines()[0])


def process_extra_docs(target_dir: str, prefix: str) -> Iterator[DocInfo]:
    md_dir = f'{os.path.dirname(os.path.abspath(__file__))}/extra-docs/{prefix}'
    for readme_file in glob.glob(f'{md_dir}/*.md'):
        yield process_extra_readme_doc(target_dir, prefix, readme_file)


# POOL has to be declared after process_readme_doc so it can find it when doing map
# multiprocess pool
POOL_SIZE = 4
POOL = Pool(POOL_SIZE)


def process_doc_info(doc_info: DocInfo, success: List[str], fail: List[str], doc_infos: List[DocInfo], seen_docs: Dict[str, DocInfo]):
    if doc_info.error_msg:
        fail.append(f'{doc_info.readme} ({doc_info.error_msg})')
    elif doc_info.id in seen_docs:
        fail.append(f'{doc_info.readme} (duplicate with {seen_docs[doc_info.id].readme})')
    else:
        doc_infos.append(doc_info)
        success.append(doc_info.readme)
        seen_docs[doc_info.id] = doc_info


def create_docs(content_dir: str, target_dir: str, regex_list: List[str], prefix: str):
    print(f'Using BRANCH: {BRANCH}')
    # Search for readme files
    readme_files = findfiles(regex_list, content_dir)
    print(f'Processing: {len(readme_files)} {prefix} files ...')
    if MAX_FILES > 0:
        print(f'PREVIEW MODE. Truncating file list to: {MAX_FILES}')
        random.shuffle(readme_files)
        readme_files = readme_files[:MAX_FILES]
    if FILE_REGEX:
        print(f'PREVIEW MODE. Matching only files which match: {FILE_REGEX}')
        regex = re.compile(FILE_REGEX)
        readme_files = list(filter(regex.search, readme_files))
    target_sub_dir = f'{target_dir}/{prefix}'
    if not os.path.exists(target_sub_dir):
        os.makedirs(target_sub_dir)
    doc_infos: List[DocInfo] = []
    success: List[str] = []
    fail: List[str] = []
    # flush before starting multi process
    sys.stdout.flush()
    sys.stderr.flush()
    seen_docs: Dict[str, DocInfo] = {}
    for doc_info in POOL.map(partial(process_readme_doc, target_sub_dir, content_dir), readme_files):
        process_doc_info(doc_info, success, fail, doc_infos, seen_docs)
    for doc_info in process_extra_docs(target_sub_dir, prefix):
        process_doc_info(doc_info, success, fail, doc_infos, seen_docs)
    org_print(f'\n===========================================\nSuccess {prefix} docs ({len(success)}):')
    for r in sorted(success):
        print(r)
    org_print(f'\n===========================================\nFailed {prefix} docs ({len(fail)}):')
    for r in sorted(fail):
        print(r)
    org_print("\n===========================================\n")
    if len(fail) > MAX_FAILURES:
        print(f'MAX_FAILURES of {len(fail)} exceeded limit: {MAX_FAILURES}. Aborting!!')
        sys.exit(2)
    return sorted(doc_infos, key=lambda d: d.name.lower())  # sort by name


def create_releases(target_dir: str):
    releases_dir = f'{os.path.dirname(os.path.abspath(__file__))}/extra-docs/{RELEASES_PREFIX}'
    target_sub_dir = f'{target_dir}/{RELEASES_PREFIX}'
    if not os.path.exists(target_sub_dir):
        os.makedirs(target_sub_dir)
    release_files = glob.glob(f'{releases_dir}/*.md')
    doc_infos: List[DocInfo] = []
    success = []
    fail = []
    # flush before starting multi process
    sys.stdout.flush()
    sys.stderr.flush()
    for doc_info in POOL.map(partial(process_release_doc, target_sub_dir), release_files):
        if not doc_info:  # case that we skip a release doc as it is too old
            continue
        if doc_info.error_msg:
            fail.append(f'{doc_info.readme} ({doc_info.error_msg})')
        else:
            doc_infos.append(doc_info)
            success.append(doc_info.readme)
    org_print(f'\n===========================================\nSuccess release docs ({len(success)}):')
    for r in sorted(success):
        print(r)
    org_print(f'\n===========================================\nFailed release docs ({len(fail)}):')
    for r in sorted(fail):
        print(r)
    org_print("\n===========================================\n")
    if fail:
        print(f'{len(fail)} failed releases. Aborting!!')
        sys.exit(3)
    return sorted(doc_infos, key=lambda d: StrictVersion(d.name.lower().partition('content release ')[2]), reverse=True)


def create_articles(target_dir: str):
    target_sub_dir = f'{target_dir}/{ATRICLES_PREFIX}'
    if not os.path.exists(target_sub_dir):
        os.makedirs(target_sub_dir)
    doc_infos: List[DocInfo] = []
    success: List[str] = []
    fail: List[str] = []
    seen_docs: Dict[str, DocInfo] = {}
    for doc_info in process_extra_docs(target_sub_dir, ATRICLES_PREFIX):
        process_doc_info(doc_info, success, fail, doc_infos, seen_docs)
    org_print(f'\n===========================================\nSuccess {ATRICLES_PREFIX} docs ({len(success)}):')
    for r in sorted(success):
        print(r)
    org_print(f'\n===========================================\nFailed {ATRICLES_PREFIX} docs ({len(fail)}):')
    for r in sorted(fail):
        print(r)
    org_print("\n===========================================\n")
    if fail:
        print(f'{len(fail)} failed articles. Aborting!!')
        sys.exit(2)
    return sorted(doc_infos, key=lambda d: d.name.lower())  # sort by name


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
    releases_full_prefix = f'{prefix}/{RELEASES_PREFIX}'
    articles_full_prefix = f'{prefix}/{ATRICLES_PREFIX}'
    integration_doc_infos = create_docs(args.dir, args.target, INTEGRATION_DOCS_MATCH, INTEGRATIONS_PREFIX)
    playbooks_doc_infos = create_docs(args.dir, args.target, PLAYBOOKS_DOCS_MATCH, PLAYBOOKS_PREFIX)
    script_doc_infos = create_docs(args.dir, args.target, SCRIPTS_DOCS_MATCH, SCRIPTS_PREFIX)
    release_doc_infos = create_releases(args.target)
    article_doc_infos = create_articles(args.target)
    index_base = f'{os.path.dirname(os.path.abspath(__file__))}/reference-index.md'
    index_target = args.target + '/index.md'
    shutil.copy(index_base, index_target)
    with open(index_target, 'a', encoding='utf-8') as f:
        if MAX_FILES > 0:
            f.write(f'\n\n# =====<br/>BUILD PREVIEW only {MAX_FILES} files from each category! <br/>=====\n\n')
        f.write("\n\n## Integrations\n\n")
        f.write(index_doc_infos(integration_doc_infos, INTEGRATIONS_PREFIX))
        f.write("\n\n## Playbooks\n\n")
        f.write(index_doc_infos(playbooks_doc_infos, PLAYBOOKS_PREFIX))
        f.write("\n\n## Scripts\n\n")
        f.write(index_doc_infos(script_doc_infos, SCRIPTS_PREFIX))
        f.write("\n\n## Articles\n\n")
        f.write(index_doc_infos(article_doc_infos, ATRICLES_PREFIX))
        f.write("\n\n## Content Release Notes\n\n")
        f.write(index_doc_infos(release_doc_infos, RELEASES_PREFIX, headers=('Name', 'Date')))
        f.write("\n\nAdditional archived release notes are available [here](https://github.com/demisto/content-docs/tree/master/content-repo/extra-docs/releases).")
    integration_items = [f'{integrations_full_prefix}/{d.id}' for d in integration_doc_infos]
    playbook_items = [f'{playbooks_full_prefix}/{d.id}' for d in playbooks_doc_infos]
    script_items = [f'{scripts_full_prefix}/{d.id}' for d in script_doc_infos]
    article_items = [f'{articles_full_prefix}/{d.id}' for d in article_doc_infos]
    release_items = [f'{releases_full_prefix}/{d.id}' for d in release_doc_infos]
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
        },
        {
            "type": "category",
            "label": "Articles",
            "items": article_items
        },
        {
            "type": "category",
            "label": "Content Release Notes",
            "items": release_items
        },
    ]
    with open(f'{args.target}/sidebar.json', 'w') as f:
        json.dump(sidebar, f, indent=4)
    print('Stopping mdx server ...')
    stop_mdx_server()


if __name__ == "__main__":
    main()
