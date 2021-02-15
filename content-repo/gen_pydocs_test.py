import os
import sys

from gen_pydocs import (generate_common_server_python_docs,
                        generate_demisto_class_docs)


class CWD:
    def __init__(self, directory):
        self.current = os.getcwd()
        self.directory = directory

    def __enter__(self):
        os.chdir(self.directory)

    def __exit__(self, *args):
        os.chdir(self.current)


def test_generate_pydoc_demisto_class(tmp_path):
    """
    Given:
     - Module demistomock to generate API docs of
     - Article ID and title
     - Function name prefix to add to function signatures
     - Module overview to add to article header

    When:
     - Generate Python API docs

    Then:
     - Ensure article header
     - Ensure overview
     - Ensure function signature
    """
    article_id = 'demisto-class'
    article_title = 'Demisto Class'
    func_prefix = 'demisto.'
    partial_module_overview = 'All Python integrations and scripts have available as part of the runtime the ' \
                              '`demisto` class'

    demisto_class = tmp_path / 'demisto.py'
    with open('./test_data/demistomock.py') as demistomock_file:
        demisto_class.write_text(demistomock_file.read())
    sys.path.append(str(tmp_path))
    with CWD(str(tmp_path)):
        generate_demisto_class_docs(str(tmp_path))
        with open(str(tmp_path / f'{article_id}.md'), 'r') as f:
            assert f.readline().startswith('---')
            assert f.readline().startswith(f'id: {article_id}')
            assert f.readline().startswith(f'title: {article_title}')
            assert f.readline().startswith(f'description: API reference documentation for {article_title}')
            assert f.readline().startswith('---')
            f.readline()
            assert f.readline().startswith(partial_module_overview)
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            f.readline()
            assert f.readline().startswith('## ')
            f.readline()
            assert f.readline().startswith('```python')
            assert f.readline().startswith(func_prefix)


def test_generate_pydoc_common_server_python(tmp_path):
    """
    Given:
     - Module CommonServerPython module to generate API docs of
     - Article ID and title
     - Function name prefix to add to function signatures
     - Module overview to add to article header

    When:
     - Generate CommonServerPython API docs

    Then:
     - Ensure article header
     - Ensure overview
     - Ensure function signature
    """
    article_id = 'common-server-python'
    article_title = 'Common Server Python'
    module_overview = 'Common functions that will be appended to the code of each integration/script before being ' \
                      'executed.'

    csp = tmp_path / 'CommonServerPython.py'
    with open('./test_data/CommonServerPython.py') as csp_file:
        csp.write_text(csp_file.read())
    sys.path.append(str(tmp_path))
    with CWD(str(tmp_path)):
        generate_common_server_python_docs(str(tmp_path))
        with open(str(tmp_path / f'{article_id}.md'), 'r') as f:
            assert f.readline().startswith('---')
            assert f.readline().startswith(f'id: {article_id}')
            assert f.readline().startswith(f'title: {article_title}')
            assert f.readline().startswith(f'description: API reference documentation for {article_title}')
            assert f.readline().startswith('---')
            f.readline()
            assert f.readline().startswith(module_overview)
            f.readline()
            assert f.readline().startswith('## ')
