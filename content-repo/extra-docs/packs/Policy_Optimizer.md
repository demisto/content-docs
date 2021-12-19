---
id: policy-optimizer
title: PAN-OS Policy Optimizer
description: Automate your AppID Adoption by using the PAN-OS Policy Optimizer integration and playbooks together with your Palo Alto Networks Next-Generation Firewall or Panorama.
---

Automate your AppID Adoption by using the PAN-OS Policy Optimizer integration and playbooks together with your Palo Alto Networks Next-Generation Firewall or Panorama.

## What Does This Pack Do?
The Policy Optimizer integration in this content pack enables you to gain visibility into and control usage of Security policy rules.

The playbooks in this pack also help you automate the following procedures to reduce the attack surface and safely enable applications on your network.

- Identify port-based rules so you can convert them to application-based rules that allow traffic or add applications to existing rules without compromising application availability.
- Identify rules configured with unused applications.
- Analyze rule characteristics and prioritize which rules to migrate or clean up.
 

# In This Pack
## Automations
- **EntryWidgetPortBasedRules** -  Entry widget that returns the number of port based rules found by PAN-OS policy optimizer.

- **EntryWidgetUnusedApplications** - Entry widget that returns the number of rules with unused applications found by PAN-OS policy optimizer.

- **EntryWidgetUnusedRules** - Entry widget that returns the number of unused rules found by PAN-OS policy optimizer.

## Integrations

This content pack contains the [PAN-OS Policy Optimizer integration](https://xsoar.pan.dev/docs/reference/integrations/pan-os-policy-optimizer).

## Playbooks
This content pack contains the following playbooks: (LINK TO PLAYBOOK DOCS)

- **Policy Optimizer - Generic** - This playbook is triggered by the **Policy Optimizer** incident type, and can execute any of the following sub-playbooks.

- **Policy Optimizer - Manage Port Based Rules** - This playbook migrates port-based rules to application-based allow rules to reduce the attack surface and safely enable applications on your network.

- **Policy Optimizer - Manage Rules with Unused Applications** - This playbook helps identify and remove unused applications from Security policy rules. If you have application-based Security policy rules that allow a large number of applications, you can remove unused applications (applications never seen on the rules) from those rules to allow only applications actually seen in the rule’s traffic. This strengthens your security posture by reducing the attack surface.

- **Policy Optimizer - Manage Unused Rules** - This playbook helps identify and remove unused rules that do not pass traffic in your environment.

- **Policy Optimizer - Add Applications to Policy Rules** - This playbook edits rules with unused applications or rules that are port based, and adds an application to the rule. It is used in PAN-OS - Policy Optimizer playbooks and includes communication tasks to get a rule name and the application to edit from the user.

## Incident Types
**Policy Optimizer** - The incident type that triggers the **Policy Optimizer - Generic** playbook. Creating this incident lets you select which of the **PAN-OS Policy Optimizer** use-cases you want to trigger (Multi-select option).

## Layouts
After creating the **Policy Optimizer** incident, it automatically triggers the **Policy Optimizer - Generic** playbook, and you can see all relevant use-case data in the different layout tabs.

- _**Incident Info**_ tab - Contains all the incident metadata information, an explanation about the use-case, open manual tasks that await user-actions, and the number of rules that are part of the one of the violations you are following. 
![image](https://user-images.githubusercontent.com/43776787/145776941-f07d2965-86fd-4b5c-8512-1184ff66df77.png)

- _**Unused Rules**_ tab - Shows unused firewall rules found by PAN-OS Policy Optimizer.
![image](https://user-images.githubusercontent.com/43776787/145777037-b5ce1273-f17c-414a-9016-77831c139fed.png)

- _**Port Based Rules**_ tab - Shows port based firewall rules found by PAN-OS Policy Optimizer.

- _**Unused Applications**_ tab - Shows firewall rules with unused applications found by PAN-OS Policy Optimizer.

# Pack Workflow and Configuration
To run the use-cases in this pack, you need to:

1) Create an incident and choose the type **Policy Optimizer**.

2) In the incident creation form, select the use-cases (one or more) you want to trigger:

- Manage Rules with Unused Applications
- Manage Unused Rules
- Add Applications to Policy Rules

After creating the incident, the playbooks are triggered and you can see all the statistics of the selected use-case(s), and manage them using the playbook tasks.

## Before You Start
Configure the playbook inputs for the **Policy Optimizer - Generic** playbook for your specific needs:
- _**Slack_user**_- Slack user to notify about unused rules.

- _**Email_address**_ - User email address to notify about unused rules.

- _**Auto_commit**_ - Specifies whether you want to auto-commit the configuration for the PAN-OS policy changes automatically (Yes/No).
