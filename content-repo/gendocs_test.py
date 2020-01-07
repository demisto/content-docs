from gendocs import INTEGRATION_DOCS_MATCH, findfiles, process_integration_doc, \
    verify_mdx, index_doc_infos, fix_mdx, DocInfo, gen_html_doc
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_CONTENT = f'{BASE_DIR}/test_data/sample-content'


def test_findfiles():
    res = findfiles(INTEGRATION_DOCS_MATCH, SAMPLE_CONTENT)
    assert f'{SAMPLE_CONTENT}/Packs/CortexXDR/Integrations/PaloAltoNetworks_XDR/README.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/SMIME_Messaging/readme.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/PhishLabsIOC_DRP/README.md' in res
    assert f'{SAMPLE_CONTENT}/Beta_Integrations/SymantecDLP/README.md' in res


def test_verify_mdx():
    try:
        verify_mdx(f'{BASE_DIR}/test_data/bad-mdx-readme.md')
        assert False, 'should fail verify'
    except Exception as ex:
        assert 'Expected corresponding JSX closing tag' in str(ex)


def test_fix_mdx():
    res = fix_mdx('this<br>is<hr>')
    assert '<br/>' in res
    assert '<hr/>' in res
    res = fix_mdx('<!-- html comment \n here --> some text <!-- another comment here-->')
    assert 'some text ' in res
    assert '<!--' not in res
    assert '-->' not in res
    assert 'html comment' not in res


def test_process_integration_doc(tmp_path):
    res = process_integration_doc(f'{SAMPLE_CONTENT}/Integrations/DomainTools_Iris/README.md', str(tmp_path), SAMPLE_CONTENT)
    assert res.id == 'domain-tools-iris'
    assert res.description
    assert res.name == 'DomainTools Iris'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: {res.name}')
        assert f.readline().startswith(f'custom_edit_url: https://github.com/demisto/content/')
    try:
        process_integration_doc(f'{BASE_DIR}/test_data/empty-readme.md', str(tmp_path), BASE_DIR)
        assert False, 'empty file should fail'
    except Exception as ex:
        assert 'empty' in str(ex)
    process_integration_doc(f'{SAMPLE_CONTENT}/Integrations/SlashNextPhishingIncidentResponse/README.md', str(tmp_path), SAMPLE_CONTENT)
    process_integration_doc(f'{SAMPLE_CONTENT}/Integrations/Gmail/README.md', str(tmp_path), SAMPLE_CONTENT)


def test_table_doc_info():
    doc_infos = [
        DocInfo('test', 'Test Integration', "this is a description\nwith new line")
    ]
    res = index_doc_infos(doc_infos, 'integrations')
    assert '<br/>' in res
    assert '(integrations/test)' in res  # verify link


def test_gen_html():
    res = gen_html_doc("""
This is line 1
This is line 2
        """)
    assert 'This is line 1\\n' in res
