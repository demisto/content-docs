---
id: playbooks-create-communication-task
title: Create a Communication Task
---
You can use communication tasks to receive information from individuals or groups of users, which can be used in processing an incident or progressing with your case management. For information about the differences in communication tasks, see [Communication Task Concepts](playbooks-communication-task-concepts).

## Create an Ask Task

1. In a playbook, click **+ Create Task**.

2. Select the **Conditional** option.

3. Enter a meaningful name for the task that corresponds to the data you are collecting.

4. Select the **Ask** option.

![Communication Ask Task](/doc_imgs/playbooks/Communication-New-Ask-Task.png)

In the task configuration, there are several tabs that you can enter values for. Some configurations are required, and some are optional. For detailed information for each configuration tab, see the Playboook Field Reference page [INSERT LINK TO Playbook_Field_Reference.md].

## Ask Task Examples

The following shows you an example of how to configure a couple of Ask tasks.

### Send Emails to Users

In this example, the message and survey are sent by email to all users with the Analyst role, and several external users. We didn't include a message body because the message subject is the survey question we want recipients to answer. There are three reply options, Yes, No, and Not sure. In the playbook, we will only add conditions for the Yes and No replies.

![Example Ask Task](/doc_imgs/playbooks/communication_example-ask-task.png)

### Send a Survey 

In this example, the message and survey will be sent to recipients every hour for six hours, until a reply is received. The SLA is six hours. If the SLA is breached, the playbook will proceed according to the Yes condition.

![Example Ask Task - Timing](/doc_imgs/playbooks/communication_example-ask-task-timing.png)


## Create a Data Collection Task

1. In a playbook, click **+ Create Task**.

2. Select the **Data Collection** option.

3. Enter a meaningful name for the task that corresponds to the data you are collecting.

4. Determine how the message will appear to users and how the message or survey will be sent. 
   
   The survey does not appear in the message. A link to the survey is automatically placed at the bottom of the message.

5. Enter the questions that the survey will contain. 

   You can drag-and-drop questions to rearrange the order in which they display in the survey. 

   You can include two types of questions in the survey; stand-alone questions and questions based on a Cortex XSOAR field.

   * Stand alone questions are presented to users directly in the message, and from which users answer directly in the message (not an external survey).

   * Field-based questions are based on a specific Cortex XSOAR field (either system or custom), for example, a Grid field. Questions The response (data) received for these fields automatically populates the field for this incident in Cortex XSOAR.

   **Important** If responses are received from multiple users, data for multi-select fields and grid fields are aggregated. For all other field types, the most recent received response will override previous responses as it displays in the field. All responses are always viewable in the context data.

## Data Collection Task Examples

The following shows you an example of how to configure a couple of Data Collection tasks.

### Stand-alone with Multi-select Answer

In this example, we created a stand-alone question, with a multi-select answer. Note that this question is not mandatory, and we did not select the **First option is default** checkbox. Had we selected this checkbox, the Reply Option "0" would be the default value in the answer field.

![Data Collection Task](/doc_imgs/playbooks/Communication-Data-Collection-Stand-alone.png)

### Field-based using a Custom Field

In this example, we created a question based on a custom Grid field that we marked as mandatory. For the question field, we included a descriptive sentence explaining how to fill in the grid.

![Data Collection Task - Field Based](/doc_imgs/playbooks/Communication-Data-Collection-Field-based.png)


For more information about communciation tasks, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/playbooks/playbook-tasks/communication-tasks).