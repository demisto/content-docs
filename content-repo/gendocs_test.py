from gendocs import INTEGRATION_DOCS_MATCH, findfiles, process_readme_doc, \
    index_doc_infos, DocInfo, gen_html_doc, normalize_id, process_release_doc, process_extra_readme_doc, \
    INTEGRATIONS_PREFIX, get_deprecated_data
from mdx_utils import verify_mdx, fix_mdx, start_mdx_server, stop_mdx_server, verify_mdx_server
import os
import pytest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_CONTENT = f'{BASE_DIR}/test_data/sample-content'


@pytest.fixture(scope='module')
def mdx_server():
    yield start_mdx_server()
    print('Cleaning up MDX server')
    stop_mdx_server()


def test_verify_mdx():
    try:
        verify_mdx(f'{BASE_DIR}/test_data/bad-mdx-readme.md')
        assert False, 'should fail verify'
    except Exception as ex:
        assert 'Expected corresponding JSX closing tag' in str(ex)


def test_verify_mdx_server(mdx_server):
    with open(f'{BASE_DIR}/test_data/good-readme.md', mode='r', encoding='utf-8') as f:
        data = f.read()
        verify_mdx_server(data)
    # test bad readme
    try:
        with open(f'{BASE_DIR}/test_data/bad-mdx-readme.md', mode='r', encoding='utf-8') as f:
            data = f.read()
            verify_mdx_server(data)
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
    res = fix_mdx('multiple<br>values<br>')
    assert '<br>' not in res
    res = fix_mdx('valide br: <br></br>')
    assert '<br></br>' in res


def test_findfiles():
    res = findfiles(INTEGRATION_DOCS_MATCH, SAMPLE_CONTENT)
    assert f'{SAMPLE_CONTENT}/Packs/CortexXDR/Integrations/PaloAltoNetworks_XDR/README.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/SMIME_Messaging/readme.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/PhishLabsIOC_DRP/README.md' in res
    assert f'{SAMPLE_CONTENT}/Beta_Integrations/SymantecDLP/README.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/integration-F5_README.md' in res


def test_process_readme_doc(tmp_path):
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT, f'{SAMPLE_CONTENT}/Integrations/DomainTools_Iris/README.md')
    assert res.id == 'domain-tools-iris'
    assert res.description
    assert res.name == 'DomainTools Iris'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: "{res.name}"')
        assert f.readline().startswith('custom_edit_url: https://github.com/demisto/content/')
    res = process_readme_doc(str(tmp_path), BASE_DIR, f'{BASE_DIR}/test_data/empty-readme.md')
    assert 'no yml file found' in res.error_msg
    process_readme_doc(str(tmp_path), SAMPLE_CONTENT, f'{SAMPLE_CONTENT}/Integrations/SlashNextPhishingIncidentResponse/README.md')
    process_readme_doc(str(tmp_path), SAMPLE_CONTENT, f'{SAMPLE_CONTENT}/Integrations/Gmail/README.md')


def test_process_readme_doc_same_dir(tmp_path):
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT, f'{SAMPLE_CONTENT}/Integrations/integration-F5_README.md', )
    assert res.id == 'f5-firewall'
    assert res.description
    assert res.name == 'F5 firewall'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: "{res.name}"')
        assert f.readline().startswith('custom_edit_url: https://github.com/demisto/content/')


def test_process_readme_doc_edl(tmp_path):
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT, f'{SAMPLE_CONTENT}/Integrations/PaloAltoNetworks_PAN_OS_EDL_Management/README.md')
    assert res.name == 'Palo Alto Networks PAN-OS EDL Management'


def test_process_readme_doc_playbookl(tmp_path):
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT, f'{SAMPLE_CONTENT}/Playbooks/playbook-lost_stolen_device_README.md')
    assert res.name == 'Lost / Stolen Device Playbook'
    assert 'Initial incident details should be the name of the reporting person' in res.description


def test_process_code_script(tmp_path):
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT, f'{SAMPLE_CONTENT}/Scripts/script-IsIPInRanges_README.md')
    assert res.id == 'is-ip-in-ranges'
    assert res.description
    assert res.name == 'IsIPInRanges'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: "{res.name}"')
        assert f.readline().startswith('custom_edit_url: https://github.com/demisto/content/')


def test_table_doc_info():
    doc_infos = [
        DocInfo('test', 'Test Integration', "this is a description\nwith new line", "test/README.md")
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


def test_bad_html():
    bad_html = open(f'{SAMPLE_CONTENT}/Integrations/Vectra_v2/README.md', encoding='utf-8').read()
    assert '>=' in bad_html
    res = gen_html_doc(bad_html)
    assert '>=' not in res


def test_normalize_id():
    assert normalize_id("that's not good") == 'thats-not-good'
    assert normalize_id("have i been pwned? v2") == 'have-i-been-pwned-v2'


def test_process_release_doc(tmp_path, mdx_server):
    release_file = f'{os.path.dirname(os.path.abspath(__file__))}/extra-docs/releases/20.4.1.md'
    res = process_release_doc(str(tmp_path), release_file)
    assert res.id == '20.4.1'
    assert res.description.startswith('Published on')
    assert res.name == 'Content Release 20.4.1'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: "{res.id}"')
        assert f.readline().startswith('custom_edit_url: https://github.com/demisto/content-docs/blob/master/content-repo/extra-docs/releases')


def test_process_extra_doc(tmp_path, mdx_server):
    release_file = f'{os.path.dirname(os.path.abspath(__file__))}/extra-docs/integrations/remote-access.md'
    res = process_extra_readme_doc(str(tmp_path), INTEGRATIONS_PREFIX, release_file)
    assert not res.error_msg
    assert res.id == 'remote-access'
    assert res.description.startswith('File transfer and execute commands')
    assert res.name == 'Remote Access'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: "{res.name}"')
        assert f.readline().startswith('custom_edit_url: https://github.com/demisto/content-docs/blob/master/content-repo/extra-docs/integrations')


def test_get_deprecated_data():
    res = get_deprecated_data({"deprecated": True}, "Deprecated - We recommend using ServiceNow v2 instead.", "README.md")
    assert "We recommend using ServiceNow v2 instead" in res
    assert get_deprecated_data({"deprecated": False}, "stam", "README.md") == ""
    res = get_deprecated_data({"deprecated": True}, "Deprecated: use Shodan v2 instead. Search engine for Internet-connected devices.", "README.md")
    assert "use Shodan v2 instead" in res
    res = get_deprecated_data({"deprecated": True}, "Deprecated. Use The Generic SQL integration instead.", "README.md")
    assert "Use The Generic SQL integration instead" in res
    res = get_deprecated_data({}, "Deprecated. Add information about the vulnerability.", "Packs/DeprecatedContent/Playbooks/test-README.md")
    assert "Add information" not in res
