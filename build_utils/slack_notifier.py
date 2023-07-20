import argparse
import requests
import re

from circleci.api import Api as circle_api
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_CHANNEL = '#dmst-build'


def get_circle_failed_steps(ci_token: str, build_number: int) -> tuple[list[str], list[str]]:
    """
    Get the circle ci failed steps if there are any.

    Args:
        ci_token (str): The circle-ci token.
        build_number (int): The build number.

    Returns:
        (tuple[list[str], list[str]): Returns tuple of lists:
        failed_steps_list - List of failed steps in the given build. Returns empty list if not failed steps were found.
        failed_docs_list - List of failed docs in 'NPM Build content-repo docs' step. Returns empty list if not failed steps were found.
    """
    failed_steps_list = []
    failed_docs_list = []
    circle_client = circle_api(ci_token)
    vcs_type = 'github'
    build_report = circle_client.get_build_info(username='demisto', project='content-docs', build_num=build_number,
                                                vcs_type=vcs_type)

    for step in build_report.get('steps', []):
        step_name = step.get('name', '')
        actions = step.get('actions', [])
        for action in actions:
            action_status = action.get('status', '')
            action_name = action.get('name', '')

            if action_status and action_status == 'failed':
                if action_name != step_name:
                    failed_steps_list.append(f'{step_name}: {action_name}')
                else:
                    failed_steps_list.append(f'{step_name}')

            if action_name == 'NPM Build content-repo docs' and action.get('has_output', False):
                if output_url := action.get('output_url'):
                    with requests.get(output_url) as response:
                        failed_docs_list = re.findall(r"Failed [a-z\s]* \([1-9]\d*\)", response.text)

    return failed_steps_list, failed_docs_list


def create_slack_notifier(slack_token: str, build_url: str, ci_token: str, build_number: int):
    """
        Sends a build report via slack.

        Args:
            slack_token (str): The slack token.
            build_url (str): The build URL.
            ci_token (str): The circle-ci token.
            build_number (int): The build number.
    """

    print(f"Sending Slack messages to {SLACK_CHANNEL}")

    steps_fields = []
    try:
        failed_entities, failed_docs = get_circle_failed_steps(ci_token=ci_token, build_number=build_number)

        if failed_docs:
            steps_fields = get_entities_fields('Warning:', failed_docs)

        if failed_entities:
            steps_fields += get_entities_fields(f'Failed Steps - ({len(failed_entities)})', failed_entities)
            color = 'danger'
            workflow_status = 'Failure'
        else:
            color = 'good'
            workflow_status = 'Success'

        slack_client = WebClient(token=slack_token)
        slack_client.chat_postMessage(
            channel=SLACK_CHANNEL,
            username="Content-Docs CircleCI",
            attachments=[{
                'color': color,
                'title': f'Content Docs Nightly Build - {workflow_status}',
                'title_link': build_url,
                'fields': steps_fields
            }]
        )
    except SlackApiError as e:
        assert e.response["error"]


def get_entities_fields(entity_title: str, entities: list[str]) -> list[dict]:
    """
    Builds an entity from given entity title and entities list
    Args:
        entity_title (str): Title of the entity.
        entities (list[str]): List of the entities.

    Returns:
        (list[dict]): List of dict containing the entity. List is needed because it is the expected format by Slack API.
    """
    return [{
        "title": f'{entity_title}',
        "value": '\n'.join(entities),
        "short": False
    }]


def options_handler():
    parser = argparse.ArgumentParser(description='Parser for slack_notifier args')
    parser.add_argument('-u', '--build_url', help='The circle-ci url', default='')
    parser.add_argument('-s', '--slack_token', help='The token for slack', required=True)
    parser.add_argument('-b', '--build_number', help='The build number', required=True)
    parser.add_argument('-c', '--ci_token', help='The token for circleci/gitlab', required=True)
    options = parser.parse_args()

    return options


def main():
    options = options_handler()
    slack_token = options.slack_token
    build_url = options.build_url
    ci_token = options.ci_token
    build_number = options.build_number

    if not slack_token:
        print('Error: Slack token is not configured')
        exit(1)

    create_slack_notifier(slack_token=slack_token, build_url=build_url, ci_token=ci_token, build_number=build_number)


if __name__ == '__main__':
    main()
