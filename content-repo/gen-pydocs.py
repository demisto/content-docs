#!/usr/bin/env python3

import argparse
import sys
from io import StringIO

from pydoc_markdown import PydocMarkdown, PythonLoader


def generate_pydoc(module: str, article_id: str, article_title: str, target_dir: str) -> None:
    """
    Args:
         module (str): The Python module to parse and generate docs for.
         article_id (str): The article ID.
         article_title (str): The article title.
         target_dir (str): The target directory to generate docs at.

    Returns:
        None: No data returned.
    """
    pydocmd = PydocMarkdown()
    loader: PythonLoader = next((ldr for ldr in pydocmd.loaders if isinstance(ldr, PythonLoader)), None)
    loader.modules = [module]
    modules = pydocmd.load_modules()
    pydocmd.process(modules)

    stdout = sys.stdout
    sys.stdout = tmp_stdout = StringIO()
    pydocmd.render(modules)
    sys.stdout = stdout
    pydoc = tmp_stdout.getvalue()

    article_description = f'API reference documentation for {article_title}.'
    content = f'---\nid: {article_id}\ntitle: {article_title}\ndescription: {article_description}\n---\n\n{pydoc}'
    with open(f'{target_dir}/{article_id}.md', mode='w', encoding='utf-8') as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser(description='Generate Content Python Docs',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--dir", help="Target directory to generate docs at.", required=True)
    parser.add_argument("-i", "--article_id", help="Article ID.", required=True)
    parser.add_argument("-t", "--article_title", help="Article title.", required=True)
    parser.add_argument("-m", "--module", help="Module to generate docs for.", required=True)
    args = parser.parse_args()
    generate_pydoc(args.module, args.article_id, args.article_title, args.dir)


if __name__ == '__main__':
    main()
