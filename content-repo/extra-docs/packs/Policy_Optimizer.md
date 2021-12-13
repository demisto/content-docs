---
id: policy-optimizer
title: PAN-OS Policy Optimizer
description: Automate your AppID Adoption by using the PAN-OS Policy Optimizer integration and playbooks together with your Palo Alto Networks Next-Generation Firewall or Panorama.
---

Automate your AppID Adoption by using the PAN-OS Policy Optimizer integration and playbooks together with your Palo Alto Networks Next-Generation Firewall or Panorama.

## What does this pack do?
The Policy Optimizer integration in this content pack provides you with a simple way to gain visibility into, control usage of, and safely enable applications in Security policy rules.
- Identifies port-based rules so you can convert them to application-based rules that allow traffic or adds applications to existing rules without compromising application availability.
- Identifies rules configured with unused applications.
- Helps you to analyze rule characteristics and prioritize which rules to migrate or clean up first.
- 
The playbooks in the pack will help you automate the procedures listed above, to reduce the attack surface and safely enable applications on your network.

# In this Pack
## Automations
**EntryWidgetPortBasedRules** -  Entry widget that returns the number of port based rules found by PAN-OS policy optimizer.

**EntryWidgetUnusedApplications** - Entry widget that returns the number of rules with unused applications found by PAN-OS policy optimizer.

**EntryWidgetUnusedRules** - Entry widget that returns the number of unused rules found by PAN-OS policy optimizer.

## Integrations

The pack contains the PAN-OS Policy Optimizer integration. Read more about the integration in the [PAN-OS Policy Optimizer](https://xsoar.pan.dev/docs/reference/integrations/pan-os-policy-optimizer) article.

## Playbooks
The pack contains the following playbooks: (LINK TO PLAYBOOK DOCS)

**Policy Optimizer - Generic** - This playbook is triggered by the PAN-OS Policy Optimizer incident type, and can go through any of the following sub-playbooks.

**Policy Optimizer - Manage Port Based Rules** - Migrate port-based rules to application-based allow rules to reduce the attack surface and safely enable applications on your network.

**Policy Optimizer - Manage Rules with Unused Applications** - If you have application-based Security policy rules that allow a large number of applications, you can remove unused applications (applications never seen on the rules) from those rules to tighten them so that they only allow applications actually seen in the rule’s traffic. Identifying and removing unused applications from Security policy rules is a best practice that strengthens your security posture by reducing the attack surface.

**Policy Optimizer - Manage Unused Rules** - Use this playbook to understand if you have unused rules that do not pass traffic in your environment, see the rules’ information and have the option to remove them from your policy.

**Policy Optimizer - Add Applications to Policy Rules** - This playbook is used in the PAN-OS - Policy Optimizer playbooks to edit rules with unused applications or rules that are port based, and add an application to the rule.
The playbook uses communication task to get a rule name and the application to edit from the user.

## Incident types
**Policy Optimizer** - The incident type that triggers the `Policy Optimizer - Generic` playbook. Creating this incident will let you choose which of the PAN-OS Policy Optimizer use-cases you would like to trigger. (Multi-select option).

## Layouts
After creating the `Policy Optimizer` incident, it will automatically trigger the `Policy Optimizer - Generic` playbook, and you will be able to see all of the relevant use-cases data in the different layout tabs.

_**Incident Info tab**_ - This tab will have all of the incidents metadata information, an explanation about the use-case, open manual tasks that await user-actions, and the number of rules that are a part of the one of the violations you chose to follow. 
![image](https://user-images.githubusercontent.com/43776787/145776941-f07d2965-86fd-4b5c-8512-1184ff66df77.png)

_**Unused Rules tab**_ - Shows unused firewall rules found by PAN-OS Policy Optimizer.
![image](https://user-images.githubusercontent.com/43776787/145777037-b5ce1273-f17c-414a-9016-77831c139fed.png)

_**Port Based Rules tab**_ -  Shows port based firewall rules found by PAN-OS Policy Optimizer.

_**Unused Applications tab**_ -  Shows firewall rules with unused applications found by PAN-OS Policy Optimizer.

# Pack Workflow and Configuration
To run the use-cases in this pack, you need to:

1) Create an incident and choose the type “Policy Optimizer”.
2) In the incident creation form, choose the use-cases(one or more)  you would like to trigger:

- Manage Rules with Unused Applications
- Manage Unused Rules
- Add Applications to Policy Rules

After creating the incident, the playbooks will be triggered and you will be able to see all of the statistics of the chosen use-case, and manage it using the playbook’s tasks.

## Before You Start
Configure the playbook inputs for the “Policy Optimizer - Generic” playbook for the pack to work best for you:

_**Slack_user**_- Slack user to notify about unused rules.

_**Email_address**_ - Email address user to notify about unused rules.

_**Auto_commit**_ - Specify whether you want to auto-commit the configuration for the PAN-OS policy changes automatically (Yes/No).
