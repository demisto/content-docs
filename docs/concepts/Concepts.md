---
id: concepts-xsoar-concepts
title: Cortex XSOAR Concepts
---
It is important to familiarize yourself with Cortex XSOAR components, UI terminology, and key concepts.

## Incidents

Potential security data threat that SOC administrators identify and remediate. There are several incident triggers, including:

* SIEM alerts
* Mail alerts
* Security alerts from third-party services, such as SIEM, mail boxes, data in CSV format, or from the Cortex XSOAR RESTful API.

Cortex XSOAR includes several out-of-the-box incident types, and users can add custom incident types with custom fields, as necessary. 

## Incident Fields

Incident Fields are used for accepting or populating incident data coming from incidents. You create fields for information you know will be coming from 3rd party integrations and in which you want to insert the information. 

## Incident Lifecycle

Cortex XSOAR is an orchestration and automation system used to bring all of the various pieces of your security apparatus together. Using Cortex XSOAR, you can define integrations with your 3rd-party security and incident management vendors. You can then trigger events from these integrations that become incidents in Cortex XSOAR. Once the incidents are created, you can run playbooks on these incidents to enrich them with information from other products in your system, which helps you complete the picture. In most cases, you can use rules and automation to determine if an incident requires further investigation or can be closed based on the findings. This enables your analysts to focus on the minority of incidents that require further investigation.

## Integrations

Third-party tools and services that the Cortex XSOAR platform orchestrates and automates SOC operations. In addition to third-party tools, you can create your own integration using the Bring Your Own Integration (BYOI) feature.

The following lists some of the integration categories available in Cortex XSOAR. The list is not exhaustive, and highlights the main categories:

* Analytics and SIEM
* Authentication
* Case Management
* Data Enrichment
* Threat Intelligence
* Database
* Endpoint
* Forensics and Malware Analysis
* IT Services
* Messaging
* Network Security
* Vulnerability Management

## Integration Instance

A configuration of an integration. You can have multiple instances of an integration, for example, to connect to different environments. Additionally, if you are an MSSP and have multiple tenants, you could configure a separate instance for each tenant. 

## Playbooks

Cortex XSOAR Playbooks are self-contained, fully documented prescriptive procedures that query, analyze, and take action based on the gathered results. Playbooks enable you to organize and document security monitoring, orchestration, and response activities. There are several out-of-the-box playbooks that cover common investigation scenarios. You can use these playbooks as-is, or customize them according to your requirements. Playbooks are written in YAML file format using the COPS standard.

Playbooks are made up of tasks, each of which perform a specific action. Tasks are either manual or automatic. Manual tasks are actions that are not associated with scripts. Automated tasks are associated with scripts, written in Python or JavaScript.

A key feature of Playbooks is the ability to structure and automate security responses, which were previously handled manually. You can reuse Playbook tasks as  building blocks for new playbooks, saving you time and streamlining knowledge retention.

For more information on Playbooks, see the Playbooks documentation.

## Automations

The Automation section is where you manage, create, and modify scripts. These scripts perform a specific action, and are comprised of commands associated with an integration. You write scripts in either Python or JavaScript. Scripts are used as part of tasks, which are used in playbooks and commands in the War Room.

Scripts can access all Cortex XSOAR APIs, including access to incidents, investigations, share data to the War Room, and so on. Scripts can receive and access arguments, and you can password protect scripts.

The Automation section includes a Script Helper, which provides a list of available commands and scripts, ordered alphabetically.

## Commands

Cortex XSOAR has two different kinds of commands:

* system commands - Commands that enable you to perform Cortex XSOAR operations, such as clearing the playground or closing an incident. These commands are not specific to an integration. System commands are entered in the command line using a /. 

* external commands - Integration-specific commands that enable you to perform actions specific to an integration. For example, you can quickly check the repuration of an ip. External commands are entered in the command line using a !. For example, !ip. 

## War Room

The War Room is a collection of all investigation actions, artifacts, and collaboration pieces for an incident. It is a chronological journal of the incident investigation. You can run commands and playbooks from the War Room and filter the entries for easier viewing.

## Indicators and Indicator Types

DBot can simplify your incident investigation process by collecting and analyzing information and artifacts found in War Room entries. Cortex XSOAR analyzes indicators to determine whether they are malicious. Using indicator types reveals predefined, regular expressions in the War Room.

Hits are indicators that are determined to have a bad reputation, and were previously identified in the network. The reputation is the indicator's level of maliciousness, determined manually or by hypersearch scripts. If a hypersearch script identifies an indicator, the source is DBot.

There are many out-of-the-box indicator types, but you can add custom indicator types as necessary. The following is a list of some of the indicator types, but the list is not exhaustive:

* IP address (IP4, IP6)
* Registry path
* URL
* Email
* File hash (SHA-1, MD5)
* Domains
* CIDR 

When you add an indicator type, you can add enhancement and reputation scripts. Enhancement scripts enable you to gather additional data about the highlighted entry in the War Room. Reputation scripts calculate the reputation score for an entry that DBot analyzed, for example, DataIPReputation, which calculates the reputation of an IP address.

## Playground

The playground is a non-production environment where you can safely develop and test automation scripts, APIs, commands, and more. It is an investigation area that is not connected to a live (active) investigation. 

To erase a playground and create a new one, in the Cortex XSOAR CLI run the /playground_create command.

## Jobs

You can create scheduled events in Cortex XSOAR using jobs. Jobs are triggered either by time-triggered events or feed-triggered events. For example, you can define a job to trigger a playbook when a specified TIM feed finishes a fetch operation that included a modification to the list. 

