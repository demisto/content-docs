#!/usr/bin/env python3

import argparse
import sys
from io import StringIO
from typing import Optional

import docspec
from nr.databind.core import Field
from pydoc_markdown import MarkdownRenderer, PydocMarkdown, PythonLoader


class DemistoMarkdownRenderer(MarkdownRenderer):

    func_prefix = Field(str, default=None)

    module_overview = Field(str, default=None)

    # Overriding header levels from MarkdownRenderer to Function header to level 2
    header_level_by_type = Field({int}, default={
        'Module': 1,
        'Class': 2,
        'Method': 4,
        'Function': 2,
        'Data': 4,
    })

    def _format_function_signature(self, func: docspec.Function, override_name: str = None,
                                   add_method_bar: bool = True) -> str:
        function_signature = super()._format_function_signature(func, override_name, add_method_bar)
        if self.func_prefix:
            function_signature = f'{self.func_prefix}{function_signature}'
        return function_signature

    def _render_header(self, fp, level, obj):
        if isinstance(obj, docspec.Module) and self.module_overview:
            fp.write(self.module_overview)
            fp.write('\n\n')
        else:
            super()._render_header(fp, level, obj)


def generate_pydoc(
        module: str,
        article_id: str,
        article_title: str,
        target_dir: str,
        func_prefix: Optional[str],
        module_overview: Optional[str]
) -> None:
    """
    Args:
         module (str): The Python module to parse and generate docs for.
         article_id (str): The article ID.
         article_title (str): The article title.
         target_dir (str): The target directory to generate docs at.
         func_prefix (str): Prefix to add to function signature.
         module_overview (str): Module overview to add to the doc header.

    Returns:
        None: No data returned.
    """
    pydocmd = PydocMarkdown()
    pydocmd.renderer = DemistoMarkdownRenderer(
        insert_header_anchors=False,
        func_prefix=func_prefix,
        module_overview=module_overview
    )
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
    parser.add_argument('-d', '--dir', help='Target directory to generate docs at.', required=True)
    parser.add_argument('-i', '--article_id', help='Article ID.', required=True)
    parser.add_argument('-t', '--article_title', help='Article title.', required=True)
    parser.add_argument('-m', '--module', help='Module to generate docs for.', required=True)
    parser.add_argument('-p', '--func_prefix', help='Prefix to add to function signature.', required=False)
    parser.add_argument('-o', '--module_overview', help='Module overview to add to the doc header.', required=False)
    args = parser.parse_args()
    generate_pydoc(args.module, args.article_id, args.article_title, args.dir, args.func_prefix, args.module_overview)


if __name__ == '__main__':
    main()
