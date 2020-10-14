from post_github_comment import get_post_url
from pytest_mock import MockerFixture
import os


def test_get_post_url_env(mocker: MockerFixture):
    mocker.patch.dict(os.environ, {'CIRCLE_PULL_REQUEST': 'https://github.com/demisto/content-docs/pull/9'})
    assert get_post_url() == 'https://api.github.com/repos/demisto/content-docs/issues/9/comments'


def test_get_post_url_comment(mocker: MockerFixture):
    mocker.patch('subprocess.check_output', return_value='Update docs (#1111)')
    assert get_post_url() == 'https://api.github.com/repos/demisto/content-docs/issues/1111/comments'
