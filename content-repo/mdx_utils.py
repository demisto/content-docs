import shutil
import subprocess
import re
import os
import time
from typing import Optional
import requests
import inflection

MDX_SERVER_PROCESS: Optional[subprocess.Popen] = None


def normalize_id(id: str):
    id = inflection.dasherize(inflection.underscore(id)).replace(' ', '-')
    # replace all non word characters (dash is ok)
    return re.sub(r'[^\w-]', '', id)


def fix_mdx(txt: str) -> str:
    replace_tuples = [
        ('<br>(?!</br>)', '<br/>'),
        ('<hr>(?!</hr>)', '<hr/>'),
        ('<pre>', '<pre>{`'),
        ('</pre>', '`}</pre>'),
        ('<br/>*', '<br/> *'),
        (' {', ' \\{'),
        (" '{", " '\\{"),
    ]
    for old, new in replace_tuples:
        txt = re.sub(old, new, txt, flags=re.IGNORECASE)
    # remove html comments
    txt = re.sub(r'<\!--.*?-->', '', txt, flags=re.DOTALL)
    return txt


def fix_relative_images(txt: str, base_dir: str, id: str, images_dir: str, relative_images_dir: str) -> str:
    regexes = (
        r'\!\[.*?\]\((?!http)(.*?)\)',
        r"""<img\s+.*?src=["'](?!http)(.*?)["'].*?>""",
    )
    for r in regexes:
        res = list(re.finditer(r, txt, re.IGNORECASE))
        # we use reverse to start from the end so when we replace the links we don't change the indexes of the other replacements
        res.reverse()
        for m in res:
            full_link = m.group(0)
            img = m.group(1)
            # check if img exists
            full_img = f'{base_dir}/{img}'
            if os.path.isfile(full_img):
                # replace all dots except last with _ and / with -
                # see: https://stackoverflow.com/questions/47813099/replace-all-but-last-occurrences-of-a-character-in-a-string-with-pandas
                name = re.sub(r'\.(?=.*?\.)', '_', img).replace('/', '-')
                name = f'{id}-{name}'
                shutil.copy(full_img, f'{images_dir}/{name}')
                # now replace the reference
                target_link = f'{relative_images_dir}/{name}'
                full_link = full_link.replace(img, target_link)
                txt = txt[:m.start()] + full_link + txt[m.end():]
    return txt


def verify_mdx(readme_file: str):
    mdx_parse = f'{os.path.dirname(os.path.abspath(__file__))}/../mdx-parse.js'
    res = subprocess.run(['node', mdx_parse, '-f', readme_file], text=True, timeout=10, capture_output=True)
    if res.returncode != 0:
        raise ValueError(f'Failed verfiying: {readme_file}. Error: {res.stderr}')


def verify_mdx_server(readme_content: str):
    response = requests.post('http://localhost:6060', data=readme_content.encode('utf-8'), timeout=10)
    if response.status_code != 200:
        raise ValueError(f'Failed verfiying via MDX server. Status: {response.status_code}. Error: {response.text}')


def start_mdx_server():
    global MDX_SERVER_PROCESS
    if not MDX_SERVER_PROCESS:
        node_version_res = subprocess.run(["node", "--version"], capture_output=True, text=True)
        print(f'starting mdx server with node version: {node_version_res}')
        mdx_parse_server = f'{os.path.dirname(os.path.abspath(__file__))}/../mdx-parse-server.js'
        MDX_SERVER_PROCESS = subprocess.Popen(['node', mdx_parse_server], stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
        time.sleep(2)  # let the node process complete startup


def stop_mdx_server():
    global MDX_SERVER_PROCESS
    if MDX_SERVER_PROCESS:
        MDX_SERVER_PROCESS.terminate()
        MDX_SERVER_PROCESS = None
