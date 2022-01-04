import os
import sys
import argparse

from slackclient import SlackClient  # type: ignore


def create_slack_notifier(slack_token):
    print("Sending Slack messages to #dmst-dummy")
    slack_client = SlackClient(slack_token)
    slack_client.api_call(
        "chat.postMessage",
        channel="dmst-dummy",
        username="Content-Docs CircleCI",
        as_user="False",
    )


def main():
    slack_token = sys.argv[1]

    if not slack_token:
        print('Error: Slack token is not configured')
        exit(1)

    create_slack_notifier(slack_token=slack_token)


if __name__ == '__main__':
    main()