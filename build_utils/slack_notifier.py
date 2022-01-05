import os
import sys
import argparse

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def create_slack_notifier(slack_token, build_url, failed_job_name):
    print("Sending Slack messages to #dmst-dummy")
    try:
        slack_client = WebClient(token=slack_token)
        slack_client.chat_postMessage(
            channel='dan-test-channel',
            as_user=False,
            username="Content-Docs CircleCI",
            attachments=[{
                'fallback': f'Content Docs {failed_job_name} - Failure',
                'color': 'danger',
                'title': 'Content Docs - Failure',
                'title_link': build_url,
            }]
        )
    except SlackApiError as e:
        assert e.response["error"]


def main():
    slack_token = sys.argv[1]
    build_url = sys.argv[2]
    failed_job_name = sys.argv[3]
    if not slack_token:
        print('Error: Slack token is not configured')
        exit(1)

    create_slack_notifier(slack_token=slack_token, build_url=build_url, failed_job_name=failed_job_name)


if __name__ == '__main__':
    main()