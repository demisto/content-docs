---
id: playbooks-create-playbook-task
title: Create a Playbook Task
---
Cortex XSOAR supports different task types for the different aspects of the playbook. Each task type requires different information and provides different capabilities. You should choose your task type based on what you want to accomplish in the task. For example, for encrichment, you might want to run an enrichment sub-playbook or a command that returns additional information for an indicator. If you are at a fork in your decision tree, you should use a conditional task to help you determine which path to continue down.

For more information about the different task types, see [Playbook Concepts](../playbooks/playbooks-overview). 

To create a task:

## Create a Task

1. In a playbook, click **+ Create Task**.

2. Select the task type.

    * Standard - select for standard manual or script-based tasks, such as closing an investigation, escalating to another analyst, or using a script to enrich data.
    * Conditional - select for decision trees, or communicating with users through an Ask task. 
    * Data Collection - select for surveying users.
    * Section Header - select to organize your data under a specific category, for example Data Enrichment or Engaging with User.

3. Enter a meaningful name for the task that corresponds to the purpose of the task.

4. Click **Save**.

For more information on playbook tasks, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/playbooks/playbook-tasks).