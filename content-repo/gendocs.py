#!/usr/bin/env python3

import argparse
import glob
import html
import json
import os
import random
import re
import shutil
import subprocess
import sys
import traceback
from datetime import datetime
from distutils.version import StrictVersion
from functools import partial
from multiprocessing import Pool
from typing import Dict, Iterator, List, Optional, Tuple, TypedDict

import yaml
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta

from CommonServerPython import tableToMarkdown  # type: ignore
from mdx_utils import (fix_mdx, fix_relative_images, normalize_id,
                       start_mdx_server, stop_mdx_server, verify_mdx_server)

# override print so we have a timestamp with each print
org_print = print


def timestamped_print(*args, **kwargs):
    org_print(datetime.now().strftime("%H:%M:%S.%f"), *args, **kwargs)


print = timestamped_print

BASE_URL = "https://xsoar.pan.dev/docs/"
MARKETPLACE_URL = "https://xsoar.pan.dev/marketplace/"
DOCS_LINKS_JSON = {}

INTEGRATION_YML_MATCH = [
    "Packs/[^/]+?/Integrations/[^/]+?/.+.yml",
    "Packs/[^/]+?/Integrations/.+.yml",
]
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
PRIVATE_PACKS_INTEGRATIONS_PREFIX = 'Integrations'
PRIVATE_PACKS_SCRIPTS_PREFIX = 'Scripts'
PRIVATE_PACKS_PLAYBOOKS_PREFIX = 'Playbooks'
RELEASES_PREFIX = 'releases'
ARTICLES_PREFIX = 'articles'
PACKS_PREFIX = 'packs'
NO_HTML = '<!-- NOT_HTML_DOC -->'
YES_HTML = '<!-- HTML_DOC -->'
BRANCH = os.getenv('HEAD', 'master')
MAX_FAILURES = int(os.getenv('MAX_FAILURES', 20))  # if we have more than this amount in a single category we fail the build
# env vars for faster development
MAX_FILES = int(os.getenv('MAX_FILES', -1))
FILE_REGEX = os.getenv('FILE_REGEX')
EMPTY_FILE_MSG = 'empty file'
DEPRECATED_INFO_FILE = f'{os.path.dirname(os.path.abspath(__file__))}/extra-docs/articles/deprecated_info.json'

# initialize the seed according to the PR branch. Used when selecting max files.
random.seed(os.getenv('CIRCLE_BRANCH'))

MIN_RELEASE_VERSION = StrictVersion((datetime.now() + relativedelta(months=-18)).strftime('%y.%-m.0'))
PACKS_INTEGRATIONS_PREFIX = 'Integrations'
PACKS_SCRIPTS_PREFIX = 'Scripts'
PACKS_PLAYBOOKS_PREFIX = 'Playbooks'


class DocInfo:
    def __init__(self, id: str, name: str, description: str, readme: str, error_msg: Optional[str] = None):
        self.id = id
        self.name = name
        self.description = description
        self.readme = readme
        self.error_msg = error_msg


class DeprecatedInfo(TypedDict, total=False):
    id: str
    name: str
    description: str
    maintenance_start: str
    eol_start: str
    note: str


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


def get_extracted_deprecated_note(description: str):
    regexs = [
        r'.*deprecated\s*[\.\-:]\s*(.*?instead.*?\.)',
        r'.*deprecated\s*[\.\-:]\s*(.*?No available replacement.*?\.)',
    ]
    for r in regexs:
        dep_match = re.match(r, description, re.IGNORECASE)
        if dep_match:
            res = dep_match[1]
            if res[0].islower():
                res = res[0].capitalize() + res[1:]
            return res
    return ""


def get_deprecated_data(yml_data: dict, desc: str, readme_file: str):
    if yml_data.get('deprecated') or 'DeprecatedContent' in readme_file or yml_data.get('hidden'):
        dep_msg = get_extracted_deprecated_note(desc)
        if dep_msg:
            dep_msg = dep_msg + '\n'
        return f':::caution Deprecated\n{dep_msg}:::\n\n'
    return ""


def get_fromversion_data(yml_data: dict):
    from_version = yml_data.get('fromversion', '')
    if from_version and not from_version.startswith(('4', '5.0')):
        return f':::info Supported versions\nSupported Cortex XSOAR versions: {from_version} and later.\n:::\n\n'
    return ''


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


def get_packname_from_metadata(pack_dir, xsoar_marketplace: bool = True):
    with open(f'{pack_dir}/pack_metadata.json', 'r') as f:
        metadata = json.load(f)
        is_pack_hidden = metadata.get("hidden", False)
        xsoar_marketplace = 'xsoar' in metadata.get('marketplaces', []) if xsoar_marketplace else False
    return metadata.get('name'), is_pack_hidden, xsoar_marketplace


def get_pack_link(file_path: str, xsoar_marketplace: bool = True) -> str:
    # the regex extracts pack name from paths, for example: content/Packs/EWSv2 -> EWSv2
    match = re.search(r'Packs[/\\]([^/\\]+)[/\\]?', file_path)
    pack_name = match.group(1) if match else ''
    pack_name_in_link = pack_name.replace('-', '')

    # the regex extracts pack path, for example: content/Packs/EWSv2/Integrations/I1/README.md -> content/Packs/EWSv2/
    match = re.match(r'.+/Packs/.+?(?=/)', file_path)
    pack_dir = match.group(0) if match else ''
    is_pack_hidden = False

    try:
        pack_name_in_docs, is_pack_hidden, xsoar_marketplace = get_packname_from_metadata(pack_dir, xsoar_marketplace)
    except FileNotFoundError:
        pack_name_in_docs = pack_name.replace('_', ' ').replace('-', ' - ')

    pack_link = f'{MARKETPLACE_URL}details/{pack_name_in_link}'
    file_types = [PACKS_SCRIPTS_PREFIX, PACKS_INTEGRATIONS_PREFIX, PACKS_PLAYBOOKS_PREFIX]
    try:
        file_type = [ft[:-1] for ft in file_types if ft in file_path][0]
    except Exception:
        file_type = ''
    if 'ApiModules' in pack_name or 'NonSupported' in pack_name:
        return ''

    # This pack is hidden, or it's not on XSOAR marketplace, don't add a link
    if is_pack_hidden or not xsoar_marketplace:
        return f"#### This {file_type} is part of the **{pack_name_in_docs}** Pack.\n\n" \
            if file_type and pack_name and pack_name_in_docs else ''
    return f"#### This {file_type} is part of the **[{pack_name_in_docs}]({pack_link})** Pack.\n\n" \
        if file_type and pack_name and pack_name_in_docs else ''


def process_readme_doc(target_dir: str, content_dir: str, prefix: str,
                       imgs_dir: str, relative_images_dir: str, readme_file: str) -> DocInfo:
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
            desc = handle_desc_field(desc)
        doc_info = DocInfo(id, name, desc, readme_file)
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.strip():
            raise ValueError(EMPTY_FILE_MSG)
        if is_html_doc(content):
            print(f'{readme_file}: detect html file')
            content = gen_html_doc(content)
        else:
            content = fix_mdx(content)
            content = fix_relative_images(content, base_dir, f'{prefix}-{id}', imgs_dir, relative_images_dir)
        # check if we have a header
        lines = content.splitlines(True)
        has_header = len(lines) >= 2 and lines[0].startswith('---') and lines[1].startswith('id:')
        if not has_header:
            readme_repo_path = readme_file
            if readme_repo_path.startswith(content_dir):
                readme_repo_path = readme_repo_path[len(content_dir):]
            edit_url = f'https://github.com/demisto/content/blob/{BRANCH}/{readme_repo_path}'
            header = f'---\nid: {id}\ntitle: {json.dumps(doc_info.name)}\ncustom_edit_url: {edit_url}\n---\n\n'
            content = add_content_info(content, yml_data, desc, readme_file)
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


def add_content_info(content: str, yml_data: dict, desc: str, readme_file: str) -> str:
    """
    Add information about a content entity such as script/integration. regarding whether it is deprecated,
    its supported versions, whether its a beta entity, and a pack link that states to which pack this entity belongs.

    Args:
        content (str): The already built content.
        yml_data (dict): yml data of the content entity.
        desc (str): the description of the content entity
        readme_file (str): the path to the README file of the content entity.

    Returns:
        str: content entity information containing additional information.
    """
    if deprecated_data := get_deprecated_data(yml_data, desc, readme_file):
        content = deprecated_data + content
        is_deprecated = True
    else:
        is_deprecated = False
    content = get_beta_data(yml_data, content) + content
    if not is_deprecated:
        content = get_fromversion_data(yml_data) + content
    # Check if there is marketplace key that does not contain the XSOAR value.
    if marketplaces := yml_data.get('marketplaces', []):
        xsoar_marketplace = 'xsoar' in marketplaces
    else:
        xsoar_marketplace = True
    content = get_pack_link(readme_file, xsoar_marketplace) + content
    return content


def handle_desc_field(desc: str):

    word_break = False
    for word in re.split(r'\s|-', desc):
        if len(word) > 40:
            word_break = True
    desc = html.escape(desc)
    if word_break:  # long words tell browser to break in the midle
        desc = '<span style={{wordBreak: "break-word"}}>' + desc + '</span>'
    return desc


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
        content = f'---\nid: {name}\nsidebar_label: "{name}"\ncustom_edit_url: {edit_url}\n---\n\n' + content
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


def process_extra_readme_doc(target_dir: str, prefix: str, readme_file: str, private_packs=False) -> DocInfo:
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
        if desc:
            desc = handle_desc_field(desc)
        readme_file_name = os.path.basename(readme_file)
        content = content.replace(front_matter_match[0], '')

        if private_packs:
            print(f'Process README Private file: {readme_file}')
            header = f'---\nid: {file_id}\ntitle: "{name}"\ncustom_edit_url: null\n---\n\n'
        else:
            edit_url = f'https://github.com/demisto/content-docs/blob/master/content-repo/extra-docs/{prefix}/{readme_file_name}'
            header = f'---\nid: {file_id}\ntitle: "{name}"\ncustom_edit_url: {edit_url}\n---\n\n'
        content = get_deprecated_data(yml_data, desc, readme_file) + content
        content = get_beta_data(yml_data, content) + content
        content = get_fromversion_data(yml_data) + content
        content = get_pack_link(readme_file) + content
        content = header + content
        verify_mdx_server(content)
        with open(f'{target_dir}/{file_id}.md', mode='w', encoding='utf-8') as f:
            f.write(content)
        return DocInfo(file_id, name, desc, readme_file)
    except Exception as ex:
        print(f'fail: {readme_file}. Exception: {traceback.format_exc()}')
        return DocInfo('', '', '', readme_file, str(ex).splitlines()[0])


def process_extra_docs(target_dir: str, prefix: str,
                       private_packs_prefix='', private_packs=False) -> Iterator[DocInfo]:
    if private_packs:
        if private_packs_prefix == PRIVATE_PACKS_PLAYBOOKS_PREFIX:
            md_dir = f'{os.path.dirname(os.path.abspath(__file__))}/.content-bucket/Packs/*/{private_packs_prefix}/'
        else:
            md_dir = f'{os.path.dirname(os.path.abspath(__file__))}/.content-bucket/Packs/*/{private_packs_prefix}/*'

        for readme_file in glob.glob(f'{md_dir}/*.md'):
            yield process_extra_readme_doc(target_dir, private_packs_prefix, readme_file, private_packs=True)
    else:
        md_dir = f'{os.path.dirname(os.path.abspath(__file__))}/extra-docs/{prefix}'
        for readme_file in glob.glob(f'{md_dir}/*.md'):
            yield process_extra_readme_doc(target_dir, prefix, readme_file)


# POOL_SIZE has to be declared after process_readme_doc so it can find it when doing map
# multiprocess pool
POOL_SIZE = 4


def process_doc_info(doc_info: DocInfo, success: List[str], fail: List[str], doc_infos: List[DocInfo], seen_docs: Dict[str, DocInfo]):
    if doc_info.error_msg == EMPTY_FILE_MSG:
        # ignore empty files
        return
    if doc_info.error_msg:
        fail.append(f'{doc_info.readme} ({doc_info.error_msg})')
    elif doc_info.id in seen_docs:
        fail.append(f'{doc_info.readme} (duplicate with {seen_docs[doc_info.id].readme})')
    else:
        doc_infos.append(doc_info)
        success.append(doc_info.readme)
        seen_docs[doc_info.id] = doc_info


def create_docs(content_dir: str, target_dir: str, regex_list: List[str], prefix: str, private_pack_prefix: str):
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
    relative_imgs_dir = "../../../docs/doc_imgs/reference/relative"
    imgs_dir = os.path.abspath(f'{target_sub_dir}/{relative_imgs_dir}')
    if not os.path.exists(imgs_dir):
        os.makedirs(imgs_dir)
    doc_infos: List[DocInfo] = []
    success: List[str] = []
    fail: List[str] = []
    # flush before starting multi process
    sys.stdout.flush()
    sys.stderr.flush()
    seen_docs: Dict[str, DocInfo] = {}
    with Pool(processes=POOL_SIZE) as pool:
        for doc_info in pool.map(partial(process_readme_doc, target_sub_dir, content_dir, prefix, imgs_dir, relative_imgs_dir), readme_files):
            process_doc_info(doc_info, success, fail, doc_infos, seen_docs)
    for doc_info in process_extra_docs(target_sub_dir, prefix):
        process_doc_info(doc_info, success, fail, doc_infos, seen_docs)
    for private_doc_info in process_extra_docs(target_sub_dir, prefix, private_packs=True,
                                               private_packs_prefix=private_pack_prefix):
        process_doc_info(private_doc_info, success, fail, doc_infos, seen_docs)
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
    with Pool(processes=POOL_SIZE) as pool:
        for doc_info in pool.map(partial(process_release_doc, target_sub_dir), release_files):
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


def create_articles(target_dir: str, prefix: str):
    target_sub_dir = f'{target_dir}/{prefix}'
    if not os.path.exists(target_sub_dir):
        os.makedirs(target_sub_dir)
    doc_infos: List[DocInfo] = []
    success: List[str] = []
    fail: List[str] = []
    seen_docs: Dict[str, DocInfo] = {}
    for doc_info in process_extra_docs(target_sub_dir, prefix):
        if not doc_info.description:  # fail the  build if no description for an article
            raise ValueError(f'Missing description for article: {doc_info.id} ({doc_info.name})')
        process_doc_info(doc_info, success, fail, doc_infos, seen_docs)
    org_print(f'\n===========================================\nSuccess {prefix} docs ({len(success)}):')
    for r in sorted(success):
        print(r)
    org_print(f'\n===========================================\nFailed {prefix} docs ({len(fail)}):')
    for r in sorted(fail):
        print(r)
    org_print("\n===========================================\n")
    if fail:
        print(f'{len(fail)} failed articles. Aborting!!')
        sys.exit(2)
    return sorted(doc_infos, key=lambda d: d.name.lower())  # sort by name


def insert_approved_tags_and_usecases():
    with open('approved_usecases.json', 'r') as f:
        approved_usecases = json.loads(f.read()).get('approved_list')
        approved_usecases_string = '\n        '.join(approved_usecases)
    with open('approved_tags.json', 'r') as f:
        approved_tags = json.loads(f.read()).get('approved_list')
        approved_tags_string = '\n        '.join(approved_tags)
    with open("../docs/documentation/pack-docs.md", "r+") as f:
        pack_docs = f.readlines()
        f.seek(0)
        for line in pack_docs:
            if '***Use-case***' in line:
                line += f"""
  <details>
  <summary>Pack Use-cases</summary>

        {approved_usecases_string}

  </details>
"""
            if '***Tags***' in line:
                line += f"""
  <details>
  <summary>Pack Tags</summary>

        {approved_tags_string}

  </details>
"""
            f.write(line)


def is_xsoar_supported_pack(pack_dir: str):
    with open(f'{pack_dir}/pack_metadata.json', 'r') as f:
        metadata = json.load(f)
    return 'xsoar' == metadata.get('support')


def get_blame_date(content_dir: str, file: str, line: int):
    file_rel = os.path.relpath(file, content_dir)
    blame_out = subprocess.check_output(['git', 'blame', '-p', '-L', f'{line},+1', file_rel], text=True, cwd=content_dir)
    auth_date = re.search(r'^author-time\s+(\d+)', blame_out, re.MULTILINE)
    if not auth_date:
        raise ValueError(f'author-date not found for blame output of file: [{file}]: {blame_out}')
    return datetime.utcfromtimestamp(int(auth_date.group(1)))


def get_deprecated_display_dates(dep_date: datetime) -> Tuple[str, str]:
    """Get the deprecation start date. The 1st of the following month.

    Args:
        dep_date (datetime): The raw dep date

    Returns:
        tuple of start deprecation and end deprecation
    """
    DATE_FRMT = "%b %d, %Y"
    start = datetime(day=1, month=dep_date.month, year=dep_date.year) + relativedelta(months=+1)
    end = start + relativedelta(months=+6)
    return (datetime.strftime(start, DATE_FRMT), datetime.strftime(end, DATE_FRMT))


def find_deprecated_integrations(content_dir: str):
    files = glob.glob(content_dir + '/Packs/*/Integrations/*.yml')
    files.extend(glob.glob(content_dir + '/Packs/*/Integrations/*/*.yml'))
    res: List[DeprecatedInfo] = []
    # go over each file and check if contains deprecated: true
    for f in files:
        with open(f, 'r') as fr:
            content = fr.read()
            if dep_search := re.search(r'^deprecated:\s*true', content, re.MULTILINE):
                pack_dir = re.match(r'.+/Packs/.+?(?=/)', f)
                if is_xsoar_supported_pack(pack_dir.group(0)):  # type: ignore[union-attr]
                    yml_data = yaml.safe_load(content)
                    id = yml_data.get('commonfields', {}).get('id') or yml_data['name']
                    name: str = yml_data.get('display') or yml_data['name']
                    desc = yml_data.get('description')
                    content_to_search = content[:dep_search.regs[0][0]]
                    lines_search = re.findall(r'\n', content_to_search)
                    blame_line = 1
                    if lines_search:
                        blame_line += len(lines_search)
                    dep_date = get_blame_date(content_dir, f, blame_line)
                    maintenance_start, eol_start = get_deprecated_display_dates(dep_date)
                    dep_suffix = "(Deprecated)"
                    if name.endswith(dep_suffix):
                        name = name.replace(dep_suffix, "").strip()
                    info = DeprecatedInfo(id=id, name=name, description=desc, note=get_extracted_deprecated_note(desc),
                                          maintenance_start=maintenance_start, eol_start=eol_start)
                    print(f'Adding deprecated integration: [{name}]. Deprecated date: {dep_date}. From file: {f}')
                    res.append(info)
                else:
                    print(f'Skippinng deprecated integration: {f} which is not supported by xsoar')
    return res


def merge_deprecated_info(deprecated_list: List[DeprecatedInfo], deperecated_info_file: str):
    with open(deperecated_info_file, "rt") as f:
        to_merge_list: List[DeprecatedInfo] = json.load(f)['integrations']
    to_merge_map = {i['id']: i for i in to_merge_list}
    merged_list: List[DeprecatedInfo] = []
    for d in deprecated_list:
        if d['id'] in to_merge_map:
            d = {**d, **to_merge_map[d['id']]}  # type: ignore[misc]
        merged_list.append(d)
    merged_map = {i['id']: i for i in merged_list}
    for k, v in to_merge_map.items():
        if k not in merged_map:
            merged_list.append(v)
    return merged_list


def add_deprected_integrations_info(content_dir: str, deperecated_article: str, deperecated_info_file: str, assets_dir: str):
    """Will append the deprecated integrations info to the deprecated article

    Args:
        content_dir (str): content dir to search for deprecated integrations
        deperecated_article (str): deprecated article (md file) to add to
        deperecated_info_file (str): json file with static deprecated info to merge
    """
    deprecated_infos = merge_deprecated_info(find_deprecated_integrations(content_dir), deperecated_info_file)
    deprecated_infos = sorted(deprecated_infos, key=lambda d: d['name'].lower() if 'name' in d else d['id'].lower())  # sort by name
    deperecated_json_file = f'{assets_dir}/{os.path.basename(deperecated_article.replace(".md", ".json"))}'
    with open(deperecated_json_file, 'w') as f:
        json.dump({
            'description': 'Generated machine readable doc of deprecated integrations',
            'integrations': deprecated_infos
        }, f, indent=2)
    deperecated_infos_no_note = [i for i in deprecated_infos if not i['note']]
    deperecated_json_file_no_note = deperecated_json_file.replace('.json', '.no_note.json')
    with open(deperecated_json_file_no_note, 'w') as f:
        json.dump({
            'description': 'Generated doc of deprecated integrations which do not contain a note about replacement or deprecation reason',
            'integrations': deperecated_infos_no_note
        }, f, indent=2)
    with open(deperecated_article, "at") as f:
        for d in deprecated_infos:
            f.write(f'\n## {d["name"] if d.get("name") else d["id"]}\n')
            if d.get("maintenance_start"):
                f.write(f'* **Maintenance Mode Start Date:** {d["maintenance_start"]}\n')
            if d.get("eol_start"):
                f.write(f'* **End-of-Life Date:** {d["eol_start"]}\n')
            if d.get("note"):
                f.write(f'* **Note:** {d["note"]}\n')
        f.write('\n\n----\nA machine readable version of this file'
                f' is available [here](pathname:///assets/{os.path.basename(deperecated_json_file)}).\n')
    org_print("\n===========================================\n")


def normalize_item_name(item_name):
    """Removes support level from the name which will be used as a key in the json links file

    Args:
        item_name (str): The item name (display or name field in yml) to edit
    """

    remove_from_name = [" (Partner Contribution)", " (Developer Contribution)", " (Community Contribution)", " (beta)",
                        " (Beta)", " (Deprecated)"]

    for item in remove_from_name:
        item_name = item_name.replace(item, "")

    return item_name


def insert_to_dict(doc_name, doc_link):
    """ Inserts the doc link to the json docs file which will be used in the genMarketplace.js script.

    Args:
        doc_name (str): The name of the doc to insert to the dict
        doc_link (str): The suffix of the doc in the site
    """

    normalized_name = normalize_item_name(doc_name)
    DOCS_LINKS_JSON[normalized_name] = f'{BASE_URL}{doc_link}'


def generate_items(doc_infos, full_prefix):
    """ Creates a list of '{full_prefix}/{doc.id}' for every doc in the doc_infos list.
        Handling the insertion of the doc link to the json docs file.

    Args:
        doc_infos (List[DocInfo]): A list of docInfo objects
        full_prefix (str): The full prefix of the entities in the doc_infos list
    """
    items_list = []
    for d in doc_infos:
        doc_link = f'{full_prefix}/{d.id}'
        items_list.append(doc_link)

        insert_to_dict(d.name, doc_link)

    return items_list


def main():
    parser = argparse.ArgumentParser(description='''Generate Content Docs. You should probably not call this script directly.
See: https://github.com/demisto/content-docs/#generating-reference-docs''',
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
    articles_full_prefix = f'{prefix}/{ARTICLES_PREFIX}'
    packs_articles_full_prefix = f'{prefix}/{PACKS_PREFIX}'
    integration_doc_infos = create_docs(args.dir, args.target, INTEGRATION_DOCS_MATCH, INTEGRATIONS_PREFIX,
                                        private_pack_prefix=PRIVATE_PACKS_INTEGRATIONS_PREFIX)
    playbooks_doc_infos = create_docs(args.dir, args.target, PLAYBOOKS_DOCS_MATCH, PLAYBOOKS_PREFIX,
                                      private_pack_prefix=PRIVATE_PACKS_PLAYBOOKS_PREFIX)
    script_doc_infos = create_docs(args.dir, args.target, SCRIPTS_DOCS_MATCH, SCRIPTS_PREFIX,
                                   private_pack_prefix=PRIVATE_PACKS_SCRIPTS_PREFIX)
    release_doc_infos = create_releases(args.target)
    article_doc_infos = create_articles(args.target, ARTICLES_PREFIX)
    packs_articles_doc_infos = create_articles(args.target, PACKS_PREFIX)
    if os.getenv('SKIP_DEPRECATED') not in ('true', 'yes', '1'):
        add_deprected_integrations_info(args.dir, f'{args.target}/{ARTICLES_PREFIX}/deprecated.md', DEPRECATED_INFO_FILE,
                                        f'{args.target}/../../static/assets')
    index_base = f'{os.path.dirname(os.path.abspath(__file__))}/reference-index.md'
    index_target = args.target + '/index.md'
    articles_index_target = args.target + '/articles-index.md'
    articles_index_base = f'{os.path.dirname(os.path.abspath(__file__))}/articles-index.md'
    shutil.copy(index_base, index_target)
    shutil.copy(articles_index_base, articles_index_target)
    with open(index_target, 'a', encoding='utf-8') as f:
        if MAX_FILES > 0:
            f.write(f'\n\n# =====<br/>BUILD PREVIEW only {MAX_FILES} files from each category! <br/>=====\n\n')
        f.write("\n\n## Integrations\n\n")
        f.write(index_doc_infos(integration_doc_infos, INTEGRATIONS_PREFIX))
        f.write("\n\n## Playbooks\n\n")
        f.write(index_doc_infos(playbooks_doc_infos, PLAYBOOKS_PREFIX))
        f.write("\n\n## Scripts\n\n")
        f.write(index_doc_infos(script_doc_infos, SCRIPTS_PREFIX))
        f.write("\n\n## API Reference\n\n")
        api_docs: List[DocInfo] = [
            DocInfo('demisto-class', 'Demisto Class',
                    'The object exposes a series of API methods which are used to retrieve and send data to the Cortex XSOAR Server.', ''),
            DocInfo('common-server-python', 'Common Server Python',
                    'Common functions that will be appended to the code of each integration/script before being executed.', ''),
        ]
        f.write(index_doc_infos(api_docs, 'api'))
        f.write("\n\n## Content Release Notes\n\n")
        f.write(index_doc_infos(release_doc_infos, RELEASES_PREFIX, headers=('Name', 'Date')))
        f.write("\n\nAdditional archived release notes are available"
                " [here](https://github.com/demisto/content-docs/tree/master/content-repo/extra-docs/releases).")
    with open(articles_index_target, 'a', encoding='utf-8') as f:
        if MAX_FILES > 0:
            f.write(f'\n\n# =====<br/>BUILD PREVIEW only {MAX_FILES} files from each category! <br/>=====\n\n')
        f.write(index_doc_infos(article_doc_infos, ARTICLES_PREFIX))

    integration_items = generate_items(integration_doc_infos, integrations_full_prefix)
    playbook_items = generate_items(playbooks_doc_infos, playbooks_full_prefix)
    script_items = generate_items(script_doc_infos, scripts_full_prefix)
    packs_articles_items = [f'{packs_articles_full_prefix}/{d.id}' for d in packs_articles_doc_infos]

    article_items = [f'{articles_full_prefix}/{d.id}' for d in article_doc_infos]
    article_items.insert(0, f'{prefix}/articles-index')
    release_items = [f'{releases_full_prefix}/{d.id}' for d in release_doc_infos]
    sidebar = [
        {
            "type": "doc",
            "id": f'{prefix}/index'
        },
        {
            "type": "category",
            "label": "Packs",
            "items": packs_articles_items
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
            "label": "Content Release Notes",
            "items": release_items
        },
    ]
    with open(f'{args.target}/sidebar.json', 'w') as f:
        json.dump(sidebar, f, indent=4)
    articles_sidebar = article_items
    with open(f'{args.target}/articles-sidebar.json', 'w') as f:
        json.dump(articles_sidebar, f, indent=4)
    print('Stopping mdx server ...')
    stop_mdx_server()
    if os.getenv('UPDATE_PACK_DOCS') or os.getenv('CI'):
        # to avoid cases that in local dev someone might checkin the modifed pack-docs.md we do this only if explicityl asked for or in CI env
        insert_approved_tags_and_usecases()

    print("Writing json links into contentItemsDocsLinks.json")
    with open('contentItemsDocsLinks.json', 'w') as file:
        json.dump(DOCS_LINKS_JSON, file)


if __name__ == "__main__":
    main()
