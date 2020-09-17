from gen_pydocs import generate_pydoc


def test_generate_pydoc(tmp_path):
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
    module_overview = 'Test Overview'
    generate_pydoc('test_data/demistomock', article_id, article_title, str(tmp_path), func_prefix, module_overview)
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
        f.readline()
        assert f.readline().startswith('```python')
        assert f.readline().startswith(func_prefix)
