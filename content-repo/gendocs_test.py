from gendocs import INTEGRATION_DOCS_MATCH, findfiles, process_integration_doc, \
    verify_mdx, index_doc_infos, fix_mdx, DocInfo, gen_html_doc


def test_findfiles():
    res = findfiles(INTEGRATION_DOCS_MATCH, "test_data/sample-content")
    assert 'test_data/sample-content/Packs/CortexXDR/Integrations/PaloAltoNetworks_XDR/README.md' in res
    assert 'test_data/sample-content/Integrations/SMIME_Messaging/readme.md' in res
    assert 'test_data/sample-content/Integrations/PhishLabsIOC_DRP/README.md' in res
    assert 'test_data/sample-content/Beta_Integrations/SymantecDLP/README.md' in res


def test_verify_mdx():
    try:
        verify_mdx('test_data/bad-mdx-readme.md')
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
    res = process_integration_doc('test_data/sample-content/Integrations/DomainTools_Iris/README.MD', str(tmp_path))
    assert res.id == 'domain-tools-iris'
    assert res.description
    assert res.name == 'DomainTools Iris'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
    try:
        process_integration_doc('test_data/empty-readme.md', str(tmp_path))
        assert False, 'empty file should fail'
    except Exception as ex:
        assert 'empty' in str(ex)
    process_integration_doc('test_data/sample-content/Integrations/SlashNextPhishingIncidentResponse/README.md', str(tmp_path))
    process_integration_doc('test_data/sample-content/Integrations/Gmail/README.md', str(tmp_path))


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
