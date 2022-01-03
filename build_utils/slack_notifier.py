import os
import sys

from slackclient import SlackClient  # type: ignore


def create_slack_notifier(slack_token, job_status):
    print("Extracting content-docs build status")
    print("Sending Slack messages to #dmst-dummy")
    if job_status == 'failure' or job_status == 'success':
        slack_client = SlackClient(slack_token)
        slack_client.api_call(
            "chat.postMessage",
            channel="dmst-dummy",
            username="Content CircleCI",
            as_user="False",
        )


def main():
    slack_token = os.environ['SLACK_TOKEN']
    job_status = sys.argv[1]

    if not slack_token:
        print('Error: Slack token is not configured')
        exit(1)

    elif not job_status:
        print('Error: Job status is unknown')
        exit(1)

    create_slack_notifier(slack_token=slack_token, job_status=job_status)


if __name__ == '__main__':
    main()