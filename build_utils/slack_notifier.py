import argparse

from circleci.api import Api as circle_api
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def get_circle_failed_steps(ci_token, build_number):
    failed_steps_list = []
    circle_client = circle_api(ci_token)
    vcs_type = 'github'
    build_report = circle_client.get_build_info(username='demisto', project='content-docs', build_num=build_number,
                                                vcs_type=vcs_type)
    for step in build_report.get('steps', []):
        step_name = step.get('name', '')
        actions = step.get('actions', [])
        for action in actions:
            action_status = action.get('status', '')
            if action_status and action_status == 'failed':
                action_name = action.get('name', '')
                if action_name != step_name:
                    failed_steps_list.append(f'{step_name}: {action_name}')
                else:
                    failed_steps_list.append(f'{step_name}')

    return failed_steps_list


def create_slack_notifier(slack_token, build_url, failed_job_name, ci_token, build_number):
    print("Sending Slack messages to #dmst-content-team")
    steps_fields = []
    try:
        if failed_entities := get_circle_failed_steps(ci_token=ci_token, build_number=build_number):
            steps_fields = get_entities_fields(f'Failed Steps - ({len(failed_entities)})', failed_entities)
        slack_client = WebClient(token=slack_token)
        slack_client.chat_postMessage(
            channel='dan-test-channel',
            as_user=False,
            username="Content-Docs CircleCI",
            attachments=[{
                'color': 'danger',
                'title': f'Content Docs {failed_job_name.title()} - Failure',
                'title_link': build_url,
                'fields': steps_fields
            }]
        )
    except SlackApiError as e:
        assert e.response["error"]


def get_entities_fields(entity_title: str, entities: List[str]) -> List[Dict]:
    """
    Builds an entity from given entity title and entities list
    Args:
        entity_title (str): Title of the entity.
        entities (List[str]): List of the entities.

    Returns:
        (List[Dict]): List of dict containing the entity. List is needed because it is the expected format by Slack API.
    """
    return [{
        "title": f'{entity_title}',
        "value": '\n'.join(entities),
        "short": False
    }]


def options_handler():
    parser = argparse.ArgumentParser(description='Parser for slack_notifier args')
    parser.add_argument('-u', '--build_url', help='The circle-ci url', default='')
    parser.add_argument('-j', '--failed_job', help='The failed job name', required=True)
    parser.add_argument('-s', '--slack_token', help='The token for slack', required=True)
    parser.add_argument('-b', '--build_number', help='The build number', required=True)
    parser.add_argument('-c', '--ci_token', help='The token for circleci/gitlab', required=True)
    options = parser.parse_args()

    return options


def main():
    options = options_handler()
    slack_token = options.slack_token
    build_url = options.build_url
    failed_job_name = options.failed_job
    ci_token = options.ci_token
    build_number = options.build_number
    print("build_number")
    print(build_number)
    if not slack_token:
        print('Error: Slack token is not configured')
        exit(1)

    create_slack_notifier(slack_token=slack_token, build_url=build_url, failed_job_name=failed_job_name, ci_token=ci_token, build_number=build_number)


if __name__ == '__main__':
    main()