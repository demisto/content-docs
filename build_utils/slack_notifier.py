import argparse

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def create_slack_notifier(slack_token, build_url, failed_job_name):
    print("Sending Slack messages to #dmst-content-team")
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


def options_handler():
    parser = argparse.ArgumentParser(description='Parser for slack_notifier args')
    parser.add_argument('-u', '--url', help='The circle-ci url', default='')
    parser.add_argument('-j', '--failed_job', help='The failed job name', required=True)
    parser.add_argument('-s', '--slack_token', help='The token for slack', required=True)
    options = parser.parse_args()

    return options


def main():
    options = options_handler()

    slack_token = options.slack_token
    build_url = options.build_url
    failed_job_name = options.failed_job_name
    print("failed_job_name")
    print(failed_job_name)
    if not slack_token:
        print('Error: Slack token is not configured')
        exit(1)

    create_slack_notifier(slack_token=slack_token, build_url=build_url, failed_job_name=failed_job_name)


if __name__ == '__main__':
    main()