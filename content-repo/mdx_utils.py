import subprocess
import re
import os


def fix_mdx(txt: str) -> str:
    replace_tuples = [
        ('<br>', '<br/>'),
        ('<hr>', '<hr/>'),
        ('<pre>', '<pre>{`'),
        ('</pre>', '`}</pre>'),
    ]
    for old, new in replace_tuples:
        txt = txt.replace(old, new)
    # remove html comments
    txt = re.sub(r'<\!--.*?-->', '', txt, flags=re.DOTALL)
    return txt


def verify_mdx(readme_file: str):
    mdx_parse = f'{os.path.dirname(os.path.abspath(__file__))}/../mdx-parse.js'
    res = subprocess.run(['node', mdx_parse, '-f', readme_file], text=True, timeout=10, capture_output=True)
    if res.returncode != 0:
        raise ValueError(f'Failed verfiying: {readme_file}. Error: {res.stderr}')
