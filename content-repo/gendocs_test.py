import json
import yaml
import re
from gendocs import DEPRECATED_INFO_FILE, DeprecatedInfo, INTEGRATION_DOCS_MATCH, findfiles, process_readme_doc, \
    index_doc_infos, DocInfo, gen_html_doc, process_release_doc, process_extra_readme_doc, \
    INTEGRATIONS_PREFIX, get_deprecated_data, insert_approved_tags_and_usecases, \
    find_deprecated_items, get_blame_date, get_deprecated_display_dates, \
    get_fromversion_data, add_deprecated_info, merge_deprecated_info, get_extracted_deprecated_note, \
    get_pack_link
from mdx_utils import verify_mdx, fix_mdx, start_mdx_server, stop_mdx_server, verify_mdx_server, fix_relative_images, \
    normalize_id
import os
import pytest
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_CONTENT = f'{BASE_DIR}/test_data/sample-content'


@pytest.fixture(scope='module')
def mdx_server():
    yield start_mdx_server()
    print('Cleaning up MDX server')
    stop_mdx_server()


@pytest.fixture()
def integration_yml_path_and_expected_content_info(request, tmp_path):
    """
    Build a minimal yml integration file and returns it.
    In addition it returns the expected content info that should be returned when adding the content info.
    """
    integration_yml_name, integration_yml_data, expected_content_info = request.param

    integration_yml_path = f'{tmp_path}/{integration_yml_name}'
    with open(integration_yml_path, 'w') as file:
        yaml.safe_dump(integration_yml_data, file)

    return integration_yml_path, expected_content_info


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
    res = fix_relative_images(content, f'{SAMPLE_CONTENT}/Integrations/Gmail', 'google-calendar', str(tmp_path),
                              'relative-test')
    assert res == content


def test_fix_relative_images_html_img(tmp_path):
    readme = f'{SAMPLE_CONTENT}/Packs/ProofpointServerProtection/Integrations/ProofpointProtectionServerV2/README.md'
    with open(readme, 'r') as f:
        content = f.read()
    res = fix_relative_images(content,
                              f'{SAMPLE_CONTENT}/Packs/ProofpointServerProtection/Integrations/ProofpointProtectionServerV2',
                              'proofpoint-test', str(tmp_path), 'relative-test')
    target_img_name = 'proofpoint-test-_-__-__-doc_imgs-api_role.png'
    assert f'relative-test/{target_img_name}' in res
    os.path.isfile(tmp_path / target_img_name)


def test_findfiles():
    res = findfiles(INTEGRATION_DOCS_MATCH, SAMPLE_CONTENT)
    assert f'{SAMPLE_CONTENT}/Packs/CortexXDR/Integrations/PaloAltoNetworks_XDR/README.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/SMIME_Messaging/readme.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/PhishLabsIOC_DRP/README.md' in res
    assert f'{SAMPLE_CONTENT}/Beta_Integrations/SymantecDLP/README.md' in res
    assert f'{SAMPLE_CONTENT}/Integrations/integration-F5_README.md' in res


@pytest.mark.parametrize(
    'integration_yml_path_and_expected_content_info', [
        (
                'deprecated-integration',
                {
                    'deprecated': True,
                    'description': 'Deprecated. Use the Generic Export Indicators Service integration instead. '
                                   'Use the Export Indicators Service integration to provide an endpoint '
                                   'with a list of indicators as a service for the system indicators.',
                    'fromversion': '6.0.0'
                },
                ':::caution Deprecated\nUse the Generic Export Indicators Service integration instead.\n:::\n\n'
        ),
        (
                '6-0-0-integration',
                {
                    'fromversion': '6.0.0',
                    'description': 'Manage Alibaba Cloud Elastic Compute Instances'
                },
                ':::info Supported versions\nSupported Cortex XSOAR versions: 6.0.0 and later.\n:::\n\n'
        )
    ],
    indirect=True
)
def test_add_content_info(integration_yml_path_and_expected_content_info):
    """
    Given -
        a minimal integration yml file.

        Case1: deprecated integration with a fromversion = 6.0.0.
        Case2: integration that is supported fromversion = 6.0.0
    When -
        trying to fetch the integration information.
    Then -
        Case1: the content info will contain only information that the integration is deprecated.
        Case2: the content info will contain only information that the integration is supported from 6.0.0 versions.
    """
    from gendocs import add_content_info

    yml_path, expected_content_string = integration_yml_path_and_expected_content_info
    with open(yml_path, 'r', encoding='utf-8') as f:
        yml_data = yaml.safe_load(f)
        content = add_content_info("", yml_data, yml_data.get("description"), '')
        assert content == expected_content_string


def test_process_readme_doc(tmp_path, mocker):
    mocker.patch('gendocs.get_packname_from_metadata', return_value=('', False, True))
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT, 'integrations',
                             str(tmp_path), "dummy-relative",
                             f'{SAMPLE_CONTENT}/Integrations/DomainTools_Iris/README.md')
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
    res = process_readme_doc(str(tmp_path), BASE_DIR, 'integrations', str(tmp_path), "dummy-relative",
                             f'{BASE_DIR}/test_data/empty-readme.md')
    assert 'no yml file found' in res.error_msg
    process_readme_doc(str(tmp_path), SAMPLE_CONTENT,
                       'integrations', str(tmp_path), "dummy-relative",
                       f'{SAMPLE_CONTENT}/Integrations/SlashNextPhishingIncidentResponse/README.md')
    process_readme_doc(str(tmp_path), SAMPLE_CONTENT, 'integrations',
                       str(tmp_path), "dummy-relative", f'{SAMPLE_CONTENT}/Integrations/Gmail/README.md')


def test_process_readme_doc_same_dir(tmp_path, mocker):
    mocker.patch('gendocs.get_packname_from_metadata', return_value=('', False, True))
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


def test_process_readme_doc_edl(tmp_path, mocker):
    mocker.patch('gendocs.get_packname_from_metadata', return_value=('', False, True))
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT,
                             'integrations', str(tmp_path), "dummy-relative",
                             f'{SAMPLE_CONTENT}/Integrations/PaloAltoNetworks_PAN_OS_EDL_Management/README.md')
    assert res.name == 'Palo Alto Networks PAN-OS EDL Management'


def test_process_readme_doc_playbookl(tmp_path, mocker):
    mocker.patch('gendocs.get_packname_from_metadata', return_value=('', False, True))
    res = process_readme_doc(str(tmp_path), SAMPLE_CONTENT,
                             'integrations', str(tmp_path), "dummy-relative",
                             f'{SAMPLE_CONTENT}/Playbooks/playbook-lost_stolen_device_README.md')
    assert res.name == 'Lost / Stolen Device Playbook'
    assert 'Initial incident details should be the name of the reporting person' in res.description


def test_process_code_script(tmp_path, mocker):
    mocker.patch('gendocs.get_packname_from_metadata', return_value=('', False, True))
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
    assert res.name == 'Remote Access (Deprecated)'
    with open(str(tmp_path / f'{res.id}.md'), 'r') as f:
        assert f.readline().startswith('---')
        assert f.readline().startswith(f'id: {res.id}')
        assert f.readline().startswith(f'title: "{res.name}"')
        assert f.readline().startswith(
            'custom_edit_url: https://github.com/demisto/content-docs/blob/master/content-repo/extra-docs/integrations')

def test_get_deprecated_data():

    res = get_deprecated_data({"deprecated": True}, "Deprecated - We recommend using ServiceNow v2 instead.",
                              "README.md")
    assert "We recommend using ServiceNow v2 instead." in res
    assert get_deprecated_data({"deprecated": False}, "stam", "README.md") == ""
    res = get_deprecated_data({"deprecated": True},
                              "Deprecated: use Shodan v2 instead. Search engine for Internet-connected devices.",
                              "README.md")
    assert "Use Shodan v2 instead" in res
    res = get_deprecated_data({"deprecated": True}, "Deprecated. Use The Generic SQL integration instead.", "README.md")
    assert "Use The Generic SQL integration instead" in res
    res = get_deprecated_data({}, "Deprecated. Add information about the vulnerability.",
                              "Packs/DeprecatedContent/Playbooks/test-README.md")
    assert "Add information" not in res


@pytest.mark.parametrize("test_input, expected", [({'fromversion': '5.5.0'},
                                                   ':::info Supported versions\nSupported '
                                                   'Cortex XSOAR versions: 5.5.0 and later.\n:::\n\n'),
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
    documentation_dir = tmp_path / 'docs' / 'documentation'
    documentation_dir.mkdir(parents=True)
    pack_docs = documentation_dir / 'pack-docs.md'
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
        'approved_list': {'common': ['IoT', 'Machine Learning'], 'xsoar': [], 'marketplacev2': [], 'xpanse': []}
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


def test_get_blame_date():
    res = get_blame_date(SAMPLE_CONTENT,
                         f'{SAMPLE_CONTENT}/Packs/DeprecatedContent/Integrations/integration-AlienVaultOTX.yml', 6)
    assert res.month == 1
    assert res.year == 2021


SAMPLE_CONTENT_DEP_INTEGRATIONS_COUNT = 7


def test_find_deprecated_integrations():
    res = find_deprecated_items(SAMPLE_CONTENT)
    for info in res:
        assert '2021' in info['maintenance_start']
    assert len(res) == SAMPLE_CONTENT_DEP_INTEGRATIONS_COUNT


def test_add_deprecated_integrations_info(tmp_path):
    deprecated_doc = tmp_path / "deprecated_test.md"
    deprecated_info = tmp_path / "deprecated_info_test.json"
    with open(deprecated_info, "wt") as f:
        json.dump({"integrations": []}, f)
    add_deprecated_info(SAMPLE_CONTENT, str(deprecated_doc), str(deprecated_info), str(tmp_path))
    with open(deprecated_doc, "rt") as f:
        dep_content = f.read()
        assert len(re.findall('Maintenance Mode Start Date', dep_content)) == SAMPLE_CONTENT_DEP_INTEGRATIONS_COUNT
    with open(tmp_path / "deprecated_test.json", 'r') as f:
        dep_json = json.load(f)
        assert len(dep_json['integrations']) == SAMPLE_CONTENT_DEP_INTEGRATIONS_COUNT


def test_merge_deprecated_info():
    infos = [
        DeprecatedInfo(id="mssql", name="test1 name"),
        DeprecatedInfo(id="test2", name="test2 name")
    ]
    res = merge_deprecated_info(infos, DEPRECATED_INFO_FILE)
    res_map = {i['id']: i for i in res}
    assert res_map['mssql']['name'] == 'SQL Server'
    assert res_map['test2']['name'] == "test2 name"
    assert res_map['slack']['name'] == "Slack"


def test_get_deprecated_display_dates():
    (start, end) = get_deprecated_display_dates(datetime(2020, 12, 30))
    assert start == "Jan 01, 2021"
    assert end == "Jul 01, 2021"


def test_get_extracted_deprecated_note():
    res = get_extracted_deprecated_note(
        'Human-vetted, Phishing-specific Threat Intelligence from Phishme. Deprecated. Use the Cofense Intelligence integration instead.')
    assert res == 'Use the Cofense Intelligence integration instead.'
    res = get_extracted_deprecated_note('Deprecated. Vendor has stopped this service. No available replacement.')
    assert res == 'Vendor has stopped this service. No available replacement.'


@pytest.mark.parametrize("test_input, expected, metadata_name", [
    ('Packs/TestPack/Integrations/TestIntegration/README.md',
     '#### This Integration is part of the **[TestPack](https://cortex.marketplace.pan.dev/marketplace/details/TestPack)** Pack.\n\n',
     'TestPack'),
    ('tmp_path/Packs/TestPack/Playbooks/TestIntegration/README.md',
     '#### This Playbook is part of the **[TestPack](https://cortex.marketplace.pan.dev/marketplace/details/TestPack)** Pack.\n\n',
     'TestPack'),
    ('content/Packs/TestPack/Scripts/TestIntegration/README.md',
     '#### This Script is part of the **[TestPack](https://cortex.marketplace.pan.dev/marketplace/details/TestPack)** Pack.\n\n',
     'TestPack'),
    ('Packs/Test-Pack/Scripts/TestIntegration/README.md',
     '#### This Script is part of the **[Test - Pack](https://cortex.marketplace.pan.dev/marketplace/details/TestPack)** Pack.\n\n',
     'Test - Pack'),
    ('Packs/Test_Pack/Scripts/TestIntegration/README.md',
     '#### This Script is part of the **[Test Pack](https://cortex.marketplace.pan.dev/marketplace/details/Test_Pack)** Pack.\n\n',
     'Test Pack')
])
def test_get_pack_link(test_input, expected, metadata_name, mocker):
    """
        Given:
            - Readme file path

        When:
            - Generating readme docs

        Then:
            - Ensure the link to pack in marketplace generated as expected
        """
    mocker.patch('gendocs.get_packname_from_metadata', return_value=(metadata_name, False, True))
    assert expected == get_pack_link(test_input)


def error_raising_func(pack_dir, xsoar_marketplace):
    raise FileNotFoundError


@pytest.mark.parametrize("test_input, expected", [
    ('Packs/TestPack/Integrations/TestIntegration/README.md',
     '#### This Integration is part of the **[TestPack](https://cortex.marketplace.pan.dev/marketplace/details/TestPack)** Pack.\n\n'
     ),
    ('tmp_path/Packs/TestPack/Playbooks/TestIntegration/README.md',
     '#### This Playbook is part of the **[TestPack](https://cortex.marketplace.pan.dev/marketplace/details/TestPack)** Pack.\n\n'
     ),
    ('content/Packs/TestPack/Scripts/TestIntegration/README.md',
     '#### This Script is part of the **[TestPack](https://cortex.marketplace.pan.dev/marketplace/details/TestPack)** Pack.\n\n'
     ),
    ('Packs/Test-Pack/Scripts/TestIntegration/README.md',
     '#### This Script is part of the **[Test - Pack](https://cortex.marketplace.pan.dev/marketplace/details/TestPack)** Pack.\n\n'
     ),
    ('Packs/Test_Pack/Scripts/TestIntegration/README.md',
     '#### This Script is part of the **[Test Pack](https://cortex.marketplace.pan.dev/marketplace/details/Test_Pack)** Pack.\n\n'
     )
])
def test_get_pack_link_no_metadata(mocker, test_input, expected):
    """
    Given:
        - Readme file path

    When:
        - Generating readme docs

    Then:
        - Ensure the link to pack in marketplace generated as expected
    """
    mocker.patch('gendocs.get_packname_from_metadata', side_effect=error_raising_func)
    assert expected == get_pack_link(test_input)
