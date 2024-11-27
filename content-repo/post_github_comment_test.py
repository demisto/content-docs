from post_github_comment import get_post_url, get_link_for_doc_file, ROOT_DIR, get_link_for_ref_file, get_modified_files
from pytest_mock import MockerFixture


def test_get_post_url_comment(mocker: MockerFixture):
    mocker.patch('subprocess.check_output', return_value='Update docs (#1111)')
    assert get_post_url() == 'https://api.github.com/repos/demisto/content-docs/issues/1111/comments'


def test_get_modified_files(mocker: MockerFixture):
    """Make sure non .md files are filtered out
    """
    mocker.patch('subprocess.check_output', return_value='''content-repo/post_github_comment.py
content-repo/post_github_comment_test.py
docs/doc_imgs/incidents/incident-fields-search.png
docs/incidents/incident-fields.md
''')
    files = get_modified_files()
    assert len(files) == 1
    assert files[0] == 'docs/incidents/incident-fields.md'


def test_get_link_for_doc_file():
    (name, url) = get_link_for_doc_file("http://localhost", f"{ROOT_DIR}/docs/integrations/code-conventions.md")
    assert name == "Python Code Conventions"
    assert url == "http://localhost/docs/integrations/code-conventions"
    (name, url) = get_link_for_doc_file("http://localhost", f"{ROOT_DIR}/docs/incidents/incident-fields.md")
    assert name == "Working with Incident Fields"
    assert url == "http://localhost/docs/incidents/incident-fields"


def test_get_link_for_ref_file():
    (name, url) = get_link_for_ref_file("http://localhost", f"{ROOT_DIR}/content-repo/extra-docs/releases/20.12.0.md")
    assert name == "Content Release 20.12.0"
    assert url == "http://localhost/docs/reference/releases/20.12.0"
    (name, url) = get_link_for_ref_file("http://localhost", f"{ROOT_DIR}/content-repo/extra-docs/integrations/syslog.md")
    assert name == "Syslog (Deprecated)"
    assert url == "http://localhost/docs/reference/integrations/syslog"
    (name, url) = get_link_for_ref_file("http://localhost", f"{ROOT_DIR}/content-repo/extra-docs/articles/IAM-premium-pack-readme.md")
    assert name == "Identity Lifecycle Management (ILM)"
    assert url == "http://localhost/docs/reference/articles/identity-lifecycle-management"
