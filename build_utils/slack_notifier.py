import os
import sys
import argparse

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def create_slack_notifier(slack_token, build_url):
    print("Sending Slack messages to #dmst-dummy")
    try:
        slack_client = WebClient(token=slack_token)
        slack_client.chat_postMessage(
            channel="dan-test-channel",
            text=build_url,
            as_user=False,
            username="Content-Docs CircleCI"
        )
    except SlackApiError as e:
        assert e.response["error"]


def main():
    slack_token = sys.argv[1]
    build_url = sys.argv[2]
    if not slack_token:
        print('Error: Slack token is not configured')
        exit(1)

    create_slack_notifier(slack_token=slack_token, build_url=build_url)


if __name__ == '__main__':
    main()