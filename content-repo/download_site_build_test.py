from download_site_build import download_site_build
import os
import pytest


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.mark.parametrize("test_file", ['circleci-non-pr-build.json', 'circleci-non-forked-build.json'])
def test_download_site_build_non_forked_pr(requests_mock, test_file):
    with open(f'{BASE_DIR}/test_data/{test_file}', 'r') as f:
        circleci_response = f.read()
    requests_mock.get('https://circleci.com/api/v1.1/project/github/demisto/content-docs/153', text=circleci_response)
    res = download_site_build(f'{BASE_DIR}/test_data/github-status-event.json')
    assert not res
    assert requests_mock.call_count == 1


def test_download_site_build_forked_pr(requests_mock, tmp_path):
    dest_file = str(tmp_path / 'download.txt')
    with open(f'{BASE_DIR}/test_data/circleci-forked-build.json', 'r') as f:
        circleci_response = f.read()
    requests_mock.get('https://circleci.com/api/v1.1/project/github/demisto/content-docs/153', text=circleci_response)
    requests_mock.get('https://circleci.com/api/v1.1/project/github/demisto/content-docs/153/artifacts', text="""
[ {
  "path" : "build-site.tar.gz",
  "pretty_path" : "build-site.tar.gz",
  "node_index" : 0,
  "url" : "https://97-225343886-gh.circle-artifacts.com/dummy-download.txt"
} ]""")
    download_val = "dummy download"
    requests_mock.get('/dummy-download.txt', text=download_val)
    res = download_site_build(f'{BASE_DIR}/test_data/github-status-event.json', dest_file)
    assert res == 345
    assert requests_mock.call_count == 3
    with open(dest_file, 'r') as f:
        assert f.read() == download_val
