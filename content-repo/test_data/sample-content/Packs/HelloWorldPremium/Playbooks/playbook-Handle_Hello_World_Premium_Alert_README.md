---
title: Handle Hello World Premium Alert
description: This is a playbook which will handle the alerts coming from the Hello World Premium service
---

This is playbook that will handle the alerts coming from Hello World Premium service

## Dependencies
This playbook uses the following sub-playbooks, integrations, and scripts.

### Sub-playbooks
This playbook does not use any sub-playbooks.

### Integrations
* HelloWorld

### Scripts
This playbook does not use any scripts.

### Commands
* helloworldpremium-get-alert

## Playbook Inputs
---

| **Name** | **Description** | **Default Value** | **Source** | **Required** |
| --- | --- | --- | --- | --- |
| AlertID | Alert ID to retrieve details for. By default retrieves from the HelloWorldPremium ID custom field in the HelloWorldPremium incident type | ${incident.helloworldpremiumid} |  | Optional |

## Playbook Outputs
---
There are no outputs for this playbook.

![Playbook Image](https://raw.githubusercontent.com/demisto/content/6bbd43a604ed992299a9db196509006da8414cf3/Packs/HelloWorld/doc_files/Handle_Hello_World_Alert.png)
