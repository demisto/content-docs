
from gen_top_contrib import get_external_prs, get_contributors_users, get_github_user, create_grid

INNER_PR_RESPONSE = [{
    "url": "https://api.github.com/repos/demisto/content/pulls/13801",
    "id": 694456100,
    "node_id": "MDExOlB1bGxSZXF1ZXN0Njk0NDU2MTAw",
    "html_url": "https://github.com/demisto/content/pull/13801",
    "issue_url": "https://api.github.com/repos/demisto/content/issues/13801",
    "number": 13801,
    "state": "closed",
    "locked": False,
    "title": "Test PR",
    "user": {
        "login": "powershelly",
        "id": 87646651,
        "node_id": "MDQ6VXNlcjg3NjQ2NjUx",
        "avatar_url": "https://avatars.githubusercontent.com/u/testurl",
        "url": "https://api.github.com/users/powershelly",
        "html_url": "https://github.com/powershelly",
        "received_events_url": "https://api.github.com/users/powershelly/received_events",
        "type": "User",
        "site_admin": False
    },
    "body": "## Status\r\n- [ ] In Progress\r\n- [x] Ready\r\n- [ ] In Hold - (Reason for hold)",
    "created_at": "2021-07-21T14:56:40Z",
    "updated_at": "2021-07-25T12:58:30Z",
    "closed_at": "2021-07-25T12:58:30Z",
    "merged_at": "2021-07-25T12:58:30Z",
    "merge_commit_sha": "4c5ea28581b084f5ee7bb4847a2df4c2c111111d",
    "assignee": {
        "login": "testUser",
        "id": 986532147,
        "node_id": "MDQ6VXNlcjU5NDA4NzQ1",
        "avatar_url": "https://avatars.githubusercontent.com/u/59408745?v=4",
        "url": "https://api.github.com/users/testUser",
        "html_url": "https://github.com/testUser",
        "subscriptions_url": "https://api.github.com/users/testUser/subscriptions",
        "organizations_url": "https://api.github.com/users/testUser/orgs",
        "repos_url": "https://api.github.com/users/testUser/repos",
        "type": "User",
        "site_admin": False
    },
    "assignees": [
        {
            "login": "testUser",
            "id": 59408745,
            "node_id": "MDQ6VXNlcjU5NDA4NzQ1",
            "avatar_url": "https://avatars.githubusercontent.com/u/59408745?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/testUser",
            "html_url": "https://github.com/testUser",
            "type": "User",
            "site_admin": False
        }
    ],
    "commits_url": "https://api.github.com/repos/demisto/content/pulls/13801/commits",
    "head": {
        "label": "powershelly:fix_task_run_full_action_report",
        "ref": "fix_task_run_full_action_report",
        "sha": "df2219695109f309ac7a7cce1d84b6fd4c222222",
        "user": {
            "login": "powershelly",
            "id": 87646651,
            "node_id": "MDQ6VXNlcjg3NjQ2NjUx",
            "avatar_url": "https://avatars.githubusercontent.com/u/testurl",
            "url": "https://api.github.com/users/powershelly",
            "html_url": "https://github.com/powershelly",
            "followers_url": "https://api.github.com/users/powershelly/followers",
            "type": "User",
            "site_admin": False
        },
        "repo": {
            "id": 123456789,
            "node_id": "MDEwOlJlcG9zaXRvcnkzODc0Mjk1MzM=",
            "name": "content",
            "full_name": "powershelly/content",
            "private": False,
            "owner": {
                "login": "powershelly",
                "id": 123456,
                "node_id": "MDQ6VXNlcjg3NjQ2NjUx",
                "avatar_url": "https://avatars.githubusercontent.com/u/testurl",
                "gravatar_id": "",
                "url": "https://api.github.com/users/powershelly",
                "html_url": "https://github.com/powershelly",
                "type": "User",
                "site_admin": False
            },
            "html_url": "https://github.com/powershelly/content",
            "description": "Demisto is now Cortex XSOAR. Automate and orchestrate your Security "
                           "Operations with Cortex XSOAR's ever-growing Content Repository. "
                           "Pull Requests are always welcome and highly appreciated! ",
            "fork": False,
            "url": "https://api.github.com/repos/powershelly/content",
            "forks_url": "https://api.github.com/repos/powershelly/content/forks",
            "created_at": "2021-07-19T10:45:06Z",
            "updated_at": "2021-07-19T10:45:07Z",
            "pushed_at": "2021-07-25T12:26:44Z",
            "git_url": "git://github.com/powershelly/content.git",
            "ssh_url": "git@github.com:powershelly/content.git",
            "clone_url": "https://github.com/powershelly/content.git",
            "svn_url": "https://github.com/powershelly/content",
            "homepage": "https://xsoar.pan.dev/",
            "default_branch": "master"
        }
    },
    "base": {
        "label": "demisto:contrib/powershelly_fix_task_run_full_action_report",
        "ref": "contrib/powershelly_fix_task_run_full_action_report",
        "sha": "36f065eab202be6888a5ff208b1a47159af771be",
        "user": {
            "login": "demisto",
            "id": 2345678,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjExMDExNzY3",
            "avatar_url": "https://avatars.githubusercontent.com/u/11011767?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/demisto",
            "html_url": "https://github.com/demisto",
            "followers_url": "https://api.github.com/users/demisto/followers",
            "type": "Organization",
            "site_admin": False
        },
        "repo": {
            "id": 123456,
            "node_id": "MDEwOlJlcG9zaXRvcnk2MDUyNTM5Mg==",
            "name": "content",
            "full_name": "demisto/content",
            "private": False,
            "owner": {
                "login": "demisto",
                "id": 1234123456,
                "node_id": "MDEyOk9yZ2FuaXphdGlvbjExMDExNzY3",
                "avatar_url": "https://avatars.githubusercontent.com/u/11011767?v=4",
                "url": "https://api.github.com/users/demisto",
                "html_url": "https://github.com/demisto",
                "type": "Organization",
                "site_admin": False
            },
            "html_url": "https://github.com/demisto/content",
            "description": "Demisto is now Cortex XSOAR. Automate and orchestrate your Security Operations with "
                           "Cortex XSOAR's ever-growing Content Repository. "
                           "Pull Requests are always welcome and highly appreciated! ",
            "fork": False,
            "url": "https://api.github.com/repos/demisto/content",
            "created_at": "2016-06-06T12:17:02Z",
            "updated_at": "2021-07-25T16:13:16Z",
            "pushed_at": "2021-07-25T18:59:42Z",
            "homepage": "https://xsoar.pan.dev/",
            "forks": 744,
            "open_issues": 122,
            "watchers": 661,
            "default_branch": "master"
        }
    },
    "author_association": "CONTRIBUTOR",
    "merged": True,
    "merged_by": {
        "login": "testUser",
        "id": 59408745,
        "node_id": "MDQ6VXNlcjU5NDA4NzQ1",
        "avatar_url": "https://avatars.githubusercontent.com/u/59408745?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/testUser",
        "html_url": "https://github.com/testUser",
        "type": "User",
        "site_admin": False
    }
}]


def test_get_contrib_prs():
    """
    Given:
        - Mock response data - list of external prs.

    When:
        - running the get_contrib_prs function

    Then:
        - Validate that the inner pr numbers returns.
    """
    mock_response = [
        {
            "url": "https://api.github.com/repos/demisto/content/issues/13834",
            "html_url": "https://github.com/demisto/content/pull/13834",
            "id": 952269617,
            "node_id": "MDExOlB1bGxSZXF1ZXN0Njk2NDk4MDM3",
            "number": 13834,
            "title": "Test PR",
            "user": {
                "login": "content-bot",
                "id": 55035720,
                "node_id": "MDQ6VXNlcjU1MDM1NzIw",
                "avatar_url": "https://avatars.githubusercontent.com/u/55035720?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/content-bot",
                "html_url": "https://github.com/content-bot",
                "followers_url": "https://api.github.com/users/content-bot/followers",
                "following_url": "https://api.github.com/users/content-bot/following{/other_user}",
                "gists_url": "https://api.github.com/users/content-bot/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/content-bot/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/content-bot/subscriptions",
                "organizations_url": "https://api.github.com/users/content-bot/orgs",
                "repos_url": "https://api.github.com/users/content-bot/repos",
                "events_url": "https://api.github.com/users/content-bot/events{/privacy}",
                "received_events_url": "https://api.github.com/users/content-bot/received_events",
                "type": "User",
                "site_admin": False
            },
            "state": "closed",
            "locked": False,
            "assignee": {
                "login": "testUser",
                "id": 59408745,
                "node_id": "MDQ6VXNlcjU5NDA4NzQ1",
                "avatar_url": "https://avatars.githubusercontent.com/u/59408745?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/testUser",
                "html_url": "https://github.com/testUser",
                "followers_url": "https://api.github.com/users/testUser/followers",
                "following_url": "https://api.github.com/users/testUser/following{/other_user}",
                "gists_url": "https://api.github.com/users/testUser/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/testUser/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/testUser/subscriptions",
                "organizations_url": "https://api.github.com/users/testUser/orgs",
                "repos_url": "https://api.github.com/users/testUser/repos",
                "events_url": "https://api.github.com/users/testUser/events{/privacy}",
                "received_events_url": "https://api.github.com/users/testUser/received_events",
                "type": "User",
                "site_admin": False
            },
            "assignees": [
                {
                    "login": "testUser",
                    "id": 59408745,
                    "node_id": "MDQ6VXNlcjU5NDA4NzQ1",
                    "avatar_url": "https://avatars.githubusercontent.com/u/59408745?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/testUser",
                    "html_url": "https://github.com/testUser",
                    "followers_url": "https://api.github.com/users/testUser/followers",
                    "following_url": "https://api.github.com/users/testUser/following{/other_user}",
                    "gists_url": "https://api.github.com/users/testUser/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/testUser/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/testUser/subscriptions",
                    "organizations_url": "https://api.github.com/users/testUser/orgs",
                    "repos_url": "https://api.github.com/users/testUser/repos",
                    "events_url": "https://api.github.com/users/testUser/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/testUser/received_events",
                    "type": "User",
                    "site_admin": False
                }
            ],
            "milestone": "None",
            "comments": 0,
            "created_at": "2021-07-25T12:59:32Z",
            "updated_at": "2021-07-25T16:13:12Z",
            "closed_at": "2021-07-25T16:13:11Z",
            "author_association": "MEMBER",
            "active_lock_reason": "None",
            "draft": False,
            "pull_request": {
                "url": "https://api.github.com/repos/demisto/content/pulls/13834",
                "html_url": "https://github.com/demisto/content/pull/13834",
                "diff_url": "https://github.com/demisto/content/pull/13834.diff",
                "patch_url": "https://github.com/demisto/content/pull/13834.patch"
            },
            "body": "## Original External PR\r\n[external pull request](https://github.com/demisto/content/pull/13801)"
                    "\r\n\r\n## Status\r\n- [ ] In Progress\r\n- [x] Ready\r\n- [ ] In Hold - (Reason for hold)\r\n\r\n"
        },
        {
            "url": "https://api.github.com/repos/demisto/content/issues/13829",
            "repository_url": "https://api.github.com/repos/demisto/content",
            "labels_url": "https://api.github.com/repos/demisto/content/issues/13829/labels{/name}",
            "comments_url": "https://api.github.com/repos/demisto/content/issues/13829/comments",
            "events_url": "https://api.github.com/repos/demisto/content/issues/13829/events",
            "html_url": "https://github.com/demisto/content/pull/13829",
            "id": 952208287,
            "node_id": "MDExOlB1bGxSZXF1ZXN0Njk2NDUxMTE1",
            "number": 13829,
            "title": "Another test PR",
            "user": {
                "login": "content-bot",
                "id": 55035720,
                "node_id": "MDQ6VXNlcjU1MDM1NzIw",
                "avatar_url": "https://avatars.githubusercontent.com/u/55035720?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/content-bot",
                "html_url": "https://github.com/content-bot",
                "followers_url": "https://api.github.com/users/content-bot/followers",
                "following_url": "https://api.github.com/users/content-bot/following{/other_user}",
                "gists_url": "https://api.github.com/users/content-bot/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/content-bot/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/content-bot/subscriptions",
                "organizations_url": "https://api.github.com/users/content-bot/orgs",
                "repos_url": "https://api.github.com/users/content-bot/repos",
                "events_url": "https://api.github.com/users/content-bot/events{/privacy}",
                "received_events_url": "https://api.github.com/users/content-bot/received_events",
                "type": "User",
                "site_admin": False
            },
            "state": "closed",
            "locked": False,
            "assignee": {
                "login": "TestUser",
                "id": 70005542,
                "node_id": "MDQ6VXNlcjcwMDA1NTQy",
                "avatar_url": "https://avatars.githubusercontent.com/u/70005542?v=4",
                "gravatar_id": "",
                "url": "https://api.github.com/users/TestUser",
                "html_url": "https://github.com/TestUser",
                "followers_url": "https://api.github.com/users/TestUser/followers",
                "following_url": "https://api.github.com/users/TestUser/following{/other_user}",
                "gists_url": "https://api.github.com/users/TestUser/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/TestUser/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/TestUser/subscriptions",
                "organizations_url": "https://api.github.com/users/TestUser/orgs",
                "repos_url": "https://api.github.com/users/TestUser/repos",
                "events_url": "https://api.github.com/users/TestUser/events{/privacy}",
                "received_events_url": "https://api.github.com/users/TestUser/received_events",
                "type": "User",
                "site_admin": False
            },
            "assignees": [
                {
                    "login": "TestUser",
                    "id": 70005542,
                    "node_id": "MDQ6VXNlcjcwMDA1NTQy",
                    "avatar_url": "https://avatars.githubusercontent.com/u/70005542?v=4",
                    "gravatar_id": "",
                    "url": "https://api.github.com/users/TestUser",
                    "html_url": "https://github.com/TestUser",
                    "followers_url": "https://api.github.com/users/TestUser/followers",
                    "following_url": "https://api.github.com/users/TestUser/following{/other_user}",
                    "gists_url": "https://api.github.com/users/TestUser/gists{/gist_id}",
                    "starred_url": "https://api.github.com/users/TestUser/starred{/owner}{/repo}",
                    "subscriptions_url": "https://api.github.com/users/TestUser/subscriptions",
                    "organizations_url": "https://api.github.com/users/TestUser/orgs",
                    "repos_url": "https://api.github.com/users/TestUser/repos",
                    "events_url": "https://api.github.com/users/TestUser/events{/privacy}",
                    "received_events_url": "https://api.github.com/users/TestUser/received_events",
                    "type": "User",
                    "site_admin": False
                }
            ],
            "milestone": "None",
            "comments": 0,
            "created_at": "2021-07-25T06:31:57Z",
            "updated_at": "2021-07-25T12:19:42Z",
            "closed_at": "2021-07-25T12:19:42Z",
            "author_association": "MEMBER",
            "active_lock_reason": "None",
            "draft": False,
            "pull_request": {
                "url": "https://api.github.com/repos/demisto/content/pulls/13829",
                "html_url": "https://github.com/demisto/content/pull/13829",
                "diff_url": "https://github.com/demisto/content/pull/13829.diff",
                "patch_url": "https://github.com/demisto/content/pull/13829.patch"
            },
            "body": "## Original External PR\r\n[external pull request](https://github.com/demisto/content/pull/13614)"
                    "\r\n\r\n## Contributing to Cortex XSOAR Content",
        }
    ]

    res = get_external_prs(mock_response)
    expected_output = [{'pr_number': '13801',
                        'pr_body': '## Original External PR\r\n[external pull request]'
                                   '(https://github.com/demisto/content/pull/13801)\r\n\r\n## Status\r\n- [ ] In '
                                   'Progress\r\n- [x] Ready\r\n- [ ] In Hold - (Reason for hold)\r\n\r\n'},
                       {'pr_number': '13614', 'pr_body': '## Original External PR\r\n[external pull request]'
                                                         '(https://github.com/demisto/content/pull/13614)\r\n\r\n## '
                                                         'Contributing to Cortex XSOAR Content'}]
    assert expected_output == res


def test_get_github_user(requests_mock):
    """
    Given:
        - http response from get_user call to github.

    When:
        - running the get_github_user function

    Then:
        - Validate that a tuple of the user avatar and profile returned.
    """
    user_response = {
        "login": "jacksparow",
        "id": 987654,
        "node_id": "MDQ6VXNlcjQ3MTE2MzM=",
        "avatar_url": "https://avatars.githubusercontent.com/u/4711633?v=4",
        "url": "https://api.github.com/users/jacksparow",
        "html_url": "https://github.com/jacksparow",
        "followers_url": "https://api.github.com/users/jacksparow/followers",
        "organizations_url": "https://api.github.com/users/jacksparow/orgs",
        "repos_url": "https://api.github.com/users/jacksparow/repos",
        "events_url": "https://api.github.com/users/jacksparow/events{/privacy}",
        "received_events_url": "https://api.github.com/users/jacksparow/received_events",
        "type": "User",
        "site_admin": False,
        "name": "Jack Sparow",
        "location": "Tel Aviv, Israel",
        "hireable": True,
        "bio": "Hello World️",
        "public_repos": 70,
        "followers": 16,
        "following": 12,
        "created_at": "2013-06-16T15:42:41Z",
        "updated_at": "2021-07-17T20:25:39Z"
    }
    username = 'jacksparow'
    requests_mock.get(f'https://api.github.com/users/{username}', json=user_response)
    res = get_github_user(username)
    assert user_response == res


def test_get_contribution_users():
    """
    Given:
        - Mock response data - inner PR response.

    When:
        - running the get_contributors_users function

    Then:
        - Validate that contribution user was returned as necessary.
    """

    user_info = [{
            "login": "powershelly",
            "id": 87646651,
            "node_id": "MDQ6VXNlcjg3NjQ2NjUx",
            "avatar_url": "https://avatars.githubusercontent.com/u/testurl",
            "url": "https://api.github.com/users/powershelly",
            "html_url": "https://github.com/powershelly",
            "received_events_url": "https://api.github.com/users/powershelly/received_events",
            "type": "User",
            "site_admin": False
    }]
    res = get_contributors_users(user_info, last_update='')
    assert {'powershelly':
                {'user': 'powershelly', 'github_profile': 'https://github.com/powershelly',
                 'github_avatar': 'https://avatars.githubusercontent.com/u/testurl',
                 'number_of_contributions': 1}} == res


def test_create_grid():
    """
   Given:
       - List of users as data to create the table from.

   When:
       - running the create_grid function

   Then:
       - Validate that the table was created successfully.
   """
    response = [
        "<img src='https://avatars.githubusercontent.com/u/testurl'/><br></br> " +
        "<a href='https://github.com/powershelly' target='_blank'>powershelly</a><br></br>5 Contributions",
        "<img src='https://avatars.githubusercontent.com/u/jacksparow'/><br></br> " +
        "<a href='https://github.com/powershelly' target='_blank'>jacksparow</a><br></br>8 Contributions"
    ]

    res = create_grid(response)
    expected = "<tr>\n<td><img src='https://avatars.githubusercontent.com/u/testurl'/><br></br> " \
               "<a href='https://github.com/powershelly' target='_blank'>powershelly</a><br></br>5 Contributions </td>"

    assert expected in res
