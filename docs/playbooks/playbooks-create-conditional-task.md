---
id: playbooks-create-conditional-task
title: Create a Conditional Task
---
Conditional tasks are used for determining different paths for your playbook. You can use conditional tasks for something simple like proceeding if a certain integration exists, or does a user account have an email address. Alternatively, you can use conditional tasks for more complex situations. For example, if an indicator was enriched and the reputation was set to bad, escalate the incident for managerial approval. However, if the indicator reputation is unknown or good, proceed down a different path.

## Create a Conditional Task

1. In a playbook, click **+ Create Task**.

2. Select the **Conditional** option.

3. Enter a meaningful name for the task that corresponds to the data you are collecting.

4. Select the option based on which the task is conditional. Valid values are:
	* Built-in - create a logical statement using an entity from within the playbook. For example, in an access investigation playbook, you can determine that if the Asset ID of the person whose account was being accessed exists in a VIP list, set the incident severity to High. Otherwise, proceed as normal.

	![Conditional Built-in](/doc_imgs/playbooks/playbook_conditional_built-in.png)

	* Manual - create a conditional task which must be manually resolved. For example, in an access incident investigation, you might ask the user if they attempted to access their account. A manual task could be to check if the user responded.

	* Choose automation - create a conditional task based on the result of a script. For example, check if an IP address is internal or external using the IsIPInRanges automation. <br/> When using an automation, the Inputs and Outputs are defined by the automation script.  

	![Conditional Automation](/doc_imgs/playbooks/playbook_conditional_automation.png)

5. Complete the task configuration in the remaining tabs. Some configurations are required, and some are optional. For detailed information for each configuration tab, see the [Playbook Field Reference](../playbooks/playbooks-field-reference).

For more information on conditional playbook tasks, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/playbooks/playbook-tasks/create-a-conditional-task).