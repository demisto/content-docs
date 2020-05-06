import subprocess
import re
import os
import time
from typing import Optional
import requests

MDX_SERVER_PROCESS: Optional[subprocess.Popen] = None


def fix_mdx(txt: str) -> str:
    replace_tuples = [
        ('<br>(?!</br>)', '<br/>'),
        ('<hr>(?!</hr>)', '<hr/>'),
        ('<pre>', '<pre>{`'),
        ('</pre>', '`}</pre>'),
    ]
    for old, new in replace_tuples:
        txt = re.sub(old, new, txt, flags=re.IGNORECASE)
    # remove html comments
    txt = re.sub(r'<\!--.*?-->', '', txt, flags=re.DOTALL)
    return txt


def verify_mdx(readme_file: str):
    mdx_parse = f'{os.path.dirname(os.path.abspath(__file__))}/../mdx-parse.js'
    res = subprocess.run(['node', mdx_parse, '-f', readme_file], text=True, timeout=10, capture_output=True)
    if res.returncode != 0:
        raise ValueError(f'Failed verfiying: {readme_file}. Error: {res.stderr}')


def verify_mdx_server(readme_content: str):
    response = requests.post('http://localhost:6060', data=readme_content.encode('utf-8'), timeout=5)
    if response.status_code != 200:
        raise ValueError(f'Failed verfiying via MDX server. Status: {response.status_code}. Error: {response.text}')


def start_mdx_server():
    global MDX_SERVER_PROCESS
    if not MDX_SERVER_PROCESS:
        mdx_parse_server = f'{os.path.dirname(os.path.abspath(__file__))}/../mdx-parse-server.js'
        MDX_SERVER_PROCESS = subprocess.Popen(['node', mdx_parse_server], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)  # let the node process complete startup


def stop_mdx_server():
    global MDX_SERVER_PROCESS
    if MDX_SERVER_PROCESS:
        MDX_SERVER_PROCESS.terminate()
        MDX_SERVER_PROCESS = None
