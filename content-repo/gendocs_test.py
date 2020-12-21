import json

from gendocs import INTEGRATION_DOCS_MATCH, findfiles, process_readme_doc, \
    index_doc_infos, DocInfo, gen_html_doc, process_release_doc, process_extra_readme_doc, \
    INTEGRATIONS_PREFIX, get_deprecated_data, insert_approved_tags_and_usecases, get_fromversion_data
from mdx_utils import verify_mdx, fix_mdx, start_mdx_server, stop_mdx_server, verify_mdx_server, fix_relative_images, normalize_id
import os
import pytest
from datetime import datetime
import dateutil.relativedelta

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


def test_fix_relative_images(tmp_path):
    readme = f'{SAMPLE_CONTENT}/Packs/GoogleCalendar/Integrations/GoogleCalendar/README.md'
    with open(readme, 'r') as f:
        content = f.read()
    res = fix_relative_images(content, f'{SAMPLE_CONTENT}/Packs/GoogleCalendar/Integrations/GoogleCalendar',
                              'google-calendar', str(tmp_path), 'relative-test')
    target_img_name = 'google-calendar-_-__-__-doc_files-add-scope-admin-3.png'
    assert f'relative-test/{target_img_name}' in res
    os.path.isfile(tmp_path / target_img_name)
    # test a readme that shouldn't change
    readme = f'{SAMPLE_CONTENT}/Integrations/Gmail/README.md'
    with open(readme, 'r') as f:
        content = f.read()
    res = fix_relative_images(content, f'{SAMPLE_CONTENT}/Integrations/Gmail', 'google-calendar', str(tmp_path), 'relative-test')
    assert res == content


def test_findfiles():
    res = findfiles(INTEGRATION_DOCS_MATCH, SAMPLE_CONTENT)
    assert f'{SAMPLE_CONTENT}/Packs/CortexXDR/Integrations/PaloAltoNetworks_XDR/README.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/SMIME_Messaging/readme.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/PhishLabsIOC_DRP/README.md' in res
    assert f'{SAMPLE_CONTENT}/Beta_Integrations/SymantecDLP/README.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/integration-F5_README.md' in res


def test_process_readme_doc(tmp_path):
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT, 'integrations',
                             str(tmp_path), "dummy-relative", f'{SAMPLE_CONTENT}/Integrations/DomainTools_Iris/README.md')
    assert res.id == 'domain-tools-iris'
    assert res.description
    assert res.name == 'DomainTools Iris'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: "{res.name}"')
        assert f.readline().startswith('custom_edit_url: https://github.com/demisto/content/')
        content = f.read()
        assert 'dummy-relative' not in content
    res = process_readme_doc(str(tmp_path), BASE_DIR, 'integrations', str(tmp_path), "dummy-relative", f'{BASE_DIR}/test_data/empty-readme.md')
    assert 'no yml file found' in res.error_msg
    process_readme_doc(str(tmp_path), SAMPLE_CONTENT,
                       'integrations', str(tmp_path), "dummy-relative",
                       f'{SAMPLE_CONTENT}/Integrations/SlashNextPhishingIncidentResponse/README.md')
    process_readme_doc(str(tmp_path), SAMPLE_CONTENT, 'integrations',
                       str(tmp_path), "dummy-relative", f'{SAMPLE_CONTENT}/Integrations/Gmail/README.md')


def test_process_readme_doc_same_dir(tmp_path):
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT, 'integrations',
                             str(tmp_path), "dummy-relative", f'{SAMPLE_CONTENT}/Integrations/integration-F5_README.md')
    assert res.id == 'f5-firewall'
    assert res.description
    assert res.name == 'F5 firewall'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: "{res.name}"')
        assert f.readline().startswith('custom_edit_url: https://github.com/demisto/content/')
        content = f.read()
        assert 'dummy-relative' not in content


def test_process_readme_doc_edl(tmp_path):
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT,
                             'integrations', str(tmp_path), "dummy-relative",
                             f'{SAMPLE_CONTENT}/Integrations/PaloAltoNetworks_PAN_OS_EDL_Management/README.md')
    assert res.name == 'Palo Alto Networks PAN-OS EDL Management'


def test_process_readme_doc_playbookl(tmp_path):
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT,
                             'integrations', str(tmp_path), "dummy-relative",
                             f'{SAMPLE_CONTENT}/Playbooks/playbook-lost_stolen_device_README.md')
    assert res.name == 'Lost / Stolen Device Playbook'
    assert 'Initial incident details should be the name of the reporting person' in res.description


def test_process_code_script(tmp_path):
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT,
                             'integrations', str(tmp_path), "dummy-relative",
                             f'{SAMPLE_CONTENT}/Scripts/script-IsIPInRanges_README.md')
    assert res.id == 'is-ip-in-ranges'
    assert res.description
    assert res.name == 'IsIPInRanges'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: "{res.name}"')
        assert f.readline().startswith('custom_edit_url: https://github.com/demisto/content/')
        content = f.read()
        assert 'dummy-relative' not in content


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
    assert normalize_id("path/with/slash/and..-dots") == 'pathwithslashand-dots'


def test_process_release_doc(tmp_path, mdx_server):
    last_month = datetime.now() + dateutil.relativedelta.relativedelta(months=-1)
    version = last_month.strftime('%y.%-m.0')
    release_file = f'{os.path.dirname(os.path.abspath(__file__))}/extra-docs/releases/{version}.md'
    res = process_release_doc(str(tmp_path), release_file)
    assert res.id == version
    assert res.description.startswith('Published on')
    assert res.name == f'Content Release {version}'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: "{res.id}"')
        assert f.readline().startswith('custom_edit_url: https://github.com/demisto/content-docs/blob/master/content-repo/extra-docs/releases')


def test_process_release_doc_old(tmp_path, mdx_server):
    release_file = f'{os.path.dirname(os.path.abspath(__file__))}/extra-docs/releases/18.9.1.md'
    res = process_release_doc(str(tmp_path), release_file)
    # old file should be ignored
    assert res is None


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


@pytest.mark.parametrize("test_input, expected", [({'fromversion': '5.5.0'},
                                                   f':::info Supported versions\nSupported '
                                                   f'Cortex XSOAR versions: 5.5.0 and later.\n:::\n\n'),
                                                  ({'fromversion': '5.0.0'}, ''),
                                                  ({}, ''),
                                                  ({'fromversion': '4.0.0'}, '')])
def test_get_fromversion_data(test_input, expected):
    res = get_fromversion_data(test_input)
    assert res == expected


def test_insert_approved_tags_and_usecases(tmp_path):
    """
    Given:
        - Approved tags and usecases lists
        - Content docs article

    When:
        - Inserting approved tags and usecases to the content docs article

    Then:
        - Ensure the approved tags and use cases are added to the content docs article as expected
    """
    integrations_dir = tmp_path / 'docs' / 'integrations'
    integrations_dir.mkdir(parents=True)
    pack_docs = integrations_dir / 'pack-docs.md'
    pack_docs.write_text("""
    ***Use-case***

    ***Tags***
    """)
    content_repo_dir = tmp_path / 'content-repo'
    content_repo_dir.mkdir()
    approved_usecases = content_repo_dir / 'approved_usecases.json'
    approved_usecases.write_text(json.dumps({
        'approved_list': [
            'Hunting',
            'Identity And Access Management'
        ]
    }))
    approved_tags = content_repo_dir / 'approved_tags.json'
    approved_tags.write_text(json.dumps({
        'approved_list': [
            'IoT',
            'Machine Learning'
        ]
    }))
    os.chdir(str(content_repo_dir))
    insert_approved_tags_and_usecases()
    with open(str(pack_docs), 'r') as pack_docs_file:
        pack_docs_file_content = pack_docs_file.read()
        assert '***Use-case***' in pack_docs_file_content
        assert '<details>' in pack_docs_file_content
        assert '<summary>Pack Use-cases</summary>' in pack_docs_file_content
        assert 'Hunting' in pack_docs_file_content
        assert 'Identity And Access Management' in pack_docs_file_content
        assert '***Tags***' in pack_docs_file_content
        assert '<summary>Pack Tags</summary>' in pack_docs_file_content
        assert 'IoT' in pack_docs_file_content
        assert 'Machine Learning' in pack_docs_file_content
        assert '</details>' in pack_docs_file_content
