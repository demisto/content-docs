---
id: playbooks-communication-task-concepts
title: Communication Tasks
---
Communication tasks enable you to send surveys to users, both internal and external, to collect data for an incident. The collected data can be used for incident analysis, and also as input for subsequent playbook tasks. For example, you might want to send a scheduled survey requesting analysts to send specific incident updates, or send a single (stand-alone) question survey to determine how an issue was handled.

The configuration examples covered in this article are specific to the Communication Tasks.

## Ask Task

The conditional Ask task is a single question survey, the answer to which determines how a playbook will proceed. If you send the survey to multiple users, the first answer received is used, and subsequent responses are disregarded.

Users interact with the survey directly from the message, meaning the question appears in the message and they click an answer from the message.

The survey question and the first response is recorded in the incident's context data. This enables you to use this response as the input for subsequent playbook tasks.

Since this is a conditional task, it's important to remember to create a condition for each of the answers. For example, if the survey answers include, Yes, No, and Maybe, there should be a corresponding condition (path) in the playbook for each of these answers.

![Ask Task Message Preview](/doc_imgs/playbooks/Communication-Ask-Task-Message-Preview.png)

## Data Collection Task

The Data Collection task is a multi-question survey (form) that survey recipients access from a link in the message. The survey resides on an external site that does not require authentication, thereby allowing survey recipients to respond without restriction.

All responses are collected and recorded in the incident's context data, whether you receive responses from a single user or multiple users. This enables you to use the survey questions and answers as input for subsequent playbook tasks.

**Note**: You can collect responses in custom fields, for example, a Grid field.

For more information on communciation tasks, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/playbooks/playbook-tasks/communication-tasks).
