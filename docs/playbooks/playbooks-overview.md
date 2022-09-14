---
id: playbooks-overview
title: Playbooks
---
Playbooks are at the heart of the Cortex XSOAR system. They enable you to automate many of your security processes, including, but not limited to handling your investigations and managing your tickets. You can structure and automate security responses that were previously handled manually. For example, you can use playbook tasks to parse the information in the incident, whether it be an email or a PDF attachment. You can interact with users in your organization using communication tasks, or remediate an incident by interacting with a 3rd party integration. 

Playbooks have different task types for each of the actions you want to take along the way. There are manual tasks where an analyst might have to confirm information or escalate an incident, and there are conditional tasks with a loop to check if certain information is present so you can proceed with your investigation. The playbook tasks can open tickets in a ticketing system, such as Jira, detonate a file using a sanbox. 

As you are building out your playbook, keep in mind the following: 

* What actions do you need to take?
* Which conditions might apply along the way? Are these conditions manual or automatic?
* Do you need to include looping?
* Are there any time-sensitive aspects to the playbook?
* When is the incident considered remediated?


## Task Types
TThe answers to the above questions will determine what kind of task you will need to create. Playbooks support the folloiwng task types:

* Standard tasks - these range from manual tasks like creating an incident or escalating an existing incident, to automated tasks such as parsing a file or enriching indicators. Automated tasks are based on scripts that exist in the system. These scripts can be something that was created by you, the user, or come pre-packaged as part of an integration. For example, the *!file* command enables you to enrich a file using any number of integrations that you have installed in your system. Alternatively, the *!ADGetUser* command is specific to the Active Directory integration.

* Conditional tasks - these tasks are used as decision trees in your flow chart. For example, were indicators found. If yes, you can have a task to enrich them, and if not you can proceed to determine that the incident is not malicious. Or, you can use conditional tasks to check if a certain integration is available and enabled in your system. If it is, you can use that integration to perform an action, and if not, you can continue to a different branch in the decision treee.

Conditional tasks can also be used to communicate with users through a single question survey, the answer to which determines how a playbook will proceed. 

* Data collection - these tasks are used to interact with users through a survey. The survey resides on an external site that does not require authentication, thereby allowing survey recipients to respond without restriction.

All responses are collected and recorded in the incident's context data, whether you receive responses from a single user or multiple users. This enables you to use the survey questions and answers as input for subsequent playbook tasks.

**Note**: You can collect responses in custom fields, for example, a Grid field.

* Section headers - these tasks are used to manage the flow of your playbook and help you organize your tasks efficiently. You create a Section Header task to group a number of related tasks under the Section Header, as you would items in a warehouse or topics in a book. 

For example, in a phishing playbook, you would have different sections for the investigative aspect of the playbook, such as indicator enrichment, and the tasks for communication with the user who reported the phising. 

## Inputs and Outputs
Depending on the task type that you select, and the script that you are running, your playbook task has inputs and outputs. 

Inputs are data pieces that are present in the playbook or task. The inputs are often manipulated or enriched and they produce outputs. Outputs are objects whose entries will serve the tasks throughout the playbook, and they can be derived from the result of a task or command. To learn more about inputs and outputs, see [Playbook Inputs and Outputs](playbooks-inputs-outputs).

## Field Mapping
You can map output from a playbook task directly to an incident field. This means that the value for an output key populates the specified field per incident. This is a good alternative to using a task with a set incident command. 

For more information about playbooks, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/playbooks).
