---
id: playbooks-field-reference
title: Playbook Task Field Reference
---
This page lists all of the fields that are available when defining a playbook task. The fields that appear depend on the task type you select. 

## Manual task settings Fields

| Name | Description | 
| ------ | ------ |
| Default assignee | Assign an owner to this task. |
| Only the assignee can complete the task | Stop the playbook from proceeding until the task assignee completes the task. By default, in addition to the task assignee, the default administrator can also complete the blocked task. You can also block tasks until a user with an external email address completes the task. |
| Set task reminder | Define a reminder for the task, in weeks, days, or hours. |


## Field Mapping
Map output from a playbook task directly to an incident field. 

**Note**: The output value is dynamic and is derived from the context at the time that the task is processed. As a result, parallel tasks that are based on the same output, might return inconsistent results.

1. In the **Field mapping** tab, click **Add custom output mapping**.
1. Under **Outputs**, select the output parameter whose output you want to map. Click the curly brackets to see a list of the output parameters available from the automation.
1. Under **Field to fill**, select the field that you want to populate with the output.
1. Click **Ok**.

## Advanced Fields
| Name | Description | 
| ------ | ------ |
| Using | Determine which integration instance processes the script you select for this task. |
| Extend context | Determine which information from the raw JSON you want to add to the Context Data. This must be entered as contextKey=RawJsonOutputPath. |
| Ignore outputs | When selected, this takes the results from the Extend context field and overwrites existing output. |
| Execution timeout | Define how long a command waits, in seconds, before it times out. |
| Only the assignee can complete the task | Stop the playbook from proceeding until the task assignee completes the task. By default, in addition to the task assignee, the default administrator can also complete the blocked task. You can also block tasks until a user with an external email address completes the task. |
| Number of retries | Determine how many times the script attempts to run before generating an error. |
| Retry interval | Determine the wait time (in seconds) between each execution of the script. |
| Auto extract indicators | Determines whether or not indicators from this task should be automatically extracted, and if so, using which method. Valid values are: <br/> * Use system default - use the option defined in the system configuration. For more information, see [Auto Extract](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-6/cortex-xsoar-admin/manage-indicators/auto-extract-indicators.html). <br/> * * None - Indicators are not automatically extracted. Use this option when you do not want to automatically extract and enrich the indicators. <br/> * Inline - Indicators are extracted and enriched within the task. Use this option when you need to have the most robust information available per indicator. **Note**: This configuration slows down your system performance. <br/> * Out of band - Indicators are enriched in parallel (or asynchronously) to other actions. The enriched data is available within the incident, however, it is not available for immediate use in task inputs or outputs since the information is not available in real time. |
| Mark results as note | Select to make the task results available as a note. Notes are viewable in the War Room. |
| Mark results as evidence | Select to make the task results available as evidence. Evidence is viewable in the War Room. |
| Run without a worker | Select to execute this task without requiring a worker. When cleared, this task will only execute when there is a worker available. |
| Skip this branch if this automation/playbook is unavailable | Select to enable the playbook to continue executing if an instance of the automation, playbook, or sub-playbook is not available.
| Quiet Mode| Determine if this task operates in Quiet Mode. When in Quiet Mode, tasks do not display inputs and outputs, nor do they auto-extract indicators. Errors and Warnings are still documented. You can determine to turn Quiet Mode on or off for a given task or control Quiet Mode by what is defined at the playbook level. |

## Details Fields
| Name | Description | 
| ------ | ------ |
| Tag the result with | Add a tag to the task result. You can use the tag to filter entries in the War Room. |
| Task description| Provide a description of what this task achieves. |

## Timers Fields
| Name | Description | 
| ------ | ------ |
| Timer action | Determine which action to take when the timer is triggered. Valid values are:Start, Stop, and Pause. |
| Select timer field | Select the field on which the timer is applied. |


## Message Body Fields

| Field | Description | Required |
| ------ | ------ |
| Ask by | The method for sending the message and survey.<br/> * Email <br/> * Slack <br/> Mattermost <br/> If you do not specify this parameter, the Allow from workplan method will be enforced, meaning users can complete the survey from the workplan. | Optional |
| To | The message and survey recipients. There are several ways to define the recipients. <br/> * **User role**: Click inside the field to select a user role. All users assigned to the role will receive the message and survey. <br/> * **Email address**: Manually type email addresses for Cortex XSOAR users and/or external users. <br/> * **Context**: Click the context icon to define recipients from context data. | Required |
| Subject | The message subject that displays to message recipients. You can make the survey question the subject, but if you don't write the question here, you should write the question in the message body field. | Required |
| Message body | The text that displays in the body of the message. Although this field is optional, if you don't write the survey question in the Subject field, you should include it in the message body. This is a long-text field. | Optional |
| Reply Options | The answers that display in the message, which users can select directly from the message. | Required |
| Set task reminder | The schedule, in weeks, days, or hours, to resend the message and survey to recipients before. | Optional |

## Timing Fields

The configuration options in the Timing tab define the frequency that the message and survey are resent to recipients before the first response is received, and the task SLA.

| Field | Description | Default |
| ------ | ------ |
| Retry interval |  Determine the wait time between each execution of a command. For example, the frequency (in minutes) that a message and survey are resent to recipients before the response is received. | 360 minutes |
| Number of retries | Determine how many times a command attempts to run before generating an error. For example, the maximum number of times a message is sent. If a reply is received, no additional retry messages will be sent. | 2 |
| Task SLA | Define the deadline for the task, in weeks, days, or hours. | N/A |
| SLA Breach | Select this checkbox to complete the task if the SLA is breached before a reply is received. You can select which condition is applied to continue the playbook. | N/A |


## Questions Fields

**Stand-alone questions**

| Field | Description | Required |
| ------ | ------ |
| Question | A question to ask recipients. | Required |
| Answer Type | The field type for the answer field. Valid values are: <br/> * Short text <br/> * Long text <br/> * Number <br/> * Single select - requires you to define a reply option. <br/> * Multi select - requires you to define a reply option. <br/> * Date picker <br/> * Attachments | Required |
| Mandatory | If this checkbox is selected for a question, survey recipients will not be able to submit the survey until they answer this question. | Optional |
| Help Message | The message that displays when users hover over the question mark help button for the survey question. | Optional |
| Placeholder | The empty value text that displays in the question's answer field. | Optional |

**Field-based questions**

| Field | Description | Required |
| ------ | ------ |
| Question | The question that displays before the field for users to complete. This field doesn't necessarily need to be a question, it can also be a descriptive sentence explaining how users should complete the field. | Required |
| Field associated with this question | The field associated with the question will automatically take all the parameters from the field definition, unless otherwise defined.| Required |
| Mandatory | If this checkbox is selected for a question, survey recipients will not be able to submit the survey until they answer this question. | Optional |
| Help Message | The message that displays when users hover over the question mark help button for the survey question. | Optional |