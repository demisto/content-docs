---
id: Rapid Breach Response
title: Rapid Breach Response Layout
description: Communication across and between departments is a vital component of collecting information, and managing and remediating security events. The Email Communication content pack enables security teams to automate and streamline the communication and notification process with users across your organization via email.
 
---
This Rapid Breach Response pack enables security teams to quickly evaluate the risk of trending cyber-attacks using dedicated playbooks for each scenario, such as Hafnium - Exchange 0-day Exploits, SolarStorm and PrintNightmare.




## Pack Workflow
The first step in most Rapid Breach Response playbooks is collecting indicators. The source of the indicators can be blogs, advisories and any other source which considered highly reliable.
Indicators can be in the form of text, rules and signatures.
The following step will be to extract, create and tag the indicators from the data collected.
After we are done with the data collection and indicator extraction we execute the new Rapid Breach Response layout playbook named ‘Set RapidBreachResponse Incident Info’, where we provide the following:
The link of the sites from which the data has been collected.
The playbook description.
The Indicators for numerical representation.
Upon completion of the collection and processing of the information, a Threat Hunting phase is being executed where we try to find indicators of compromise related to the attack in the customer organization. The following are the main tasks being executed in the TH phase:
PANW Hunting.
Cortex XDR signatures and XQL hunting.
SIEM hunting.
Advanced Hunting based on the attack patterns.
IOCs hunt using Endpoint Detection and Response.


## In This Pack
The Rapid Breach Response content pack includes several content items.

### Automations - Dynamic Sections
There are 8 Dynamic Sections in this pack.

New: RapidBreachResponse-RemainingTasksCount-Widget
 
 * Rapid Breach Response dynamic section, will show the updated number of remaining tasks. (Available from Cortex XSOAR 6.0.0). 
 
New: RapidBreachResponse-RemediationTasksCount-Widget
 
 * Rapid Breach Response dynamic section, will show the updated number of remediation tasks. (Available from Cortex XSOAR 6.0.0).
 
New: RapidBreachResponse-CompletedTasksCount-Widget
 
 * Rapid Breach Response dynamic section, will show the updated number of completed tasks. (Available from Cortex XSOAR 6.0.0).
 
New: RapidBreachResponse-MitigationTasksCount-Widget

 * Rapid Breach Response dynamic section, will show the updated number of mitigation tasks. (Available from Cortex XSOAR 6.0.0).
 
New: RapidBreachResponse-TotalTasksCount-Widget

 * Rapid Breach Response dynamic section, will show the updated number of tasks to complete. (Available from Cortex XSOAR 6.0.0).
 
New: RapidBreachResponse-HuntingTasksCount-Widget

 * Rapid Breach Response dynamic section, will show the updated number of hunting tasks. (Available from Cortex XSOAR 6.0.0).
 
New: RapidBreachResponse-EradicationTasksCount-Widget

 * Rapid Breach Response dynamic section, will show the updated number of eradication tasks. (Available from Cortex XSOAR 6.0.0).
 
New: RapidBreachResponse-TotalIndicatorCount-Widget

 * Rapid Breach Response dynamic section, will show the updated number of indicators found. (Available from Cortex XSOAR 6.0.0).

### Playbooks
There is 1 playbook - **Rapid Breach Response - Set Incident Info**.
This playbook is responsible for setting up the Rapid Breach Response Incident Info tab. (Available from Cortex XSOAR 6.0.0).

### Incident Fields
There are 10 incident field - 

- **Remaining Task Count**
- **Total Task Count**
- **Playbook Description**
- **Hunting Task Count**
- **Source Of Indicators**
- **Mitigation Task Count**
- **Completed Task Count**
- **Total Indicator Count**
- **Eradication Task Count**
- **Remediation Task Count**

### Incident Types
There is 1 incident type - **Rapid Breach Response**.

### Layout
There is 1 layout - **Rapid Breach Response** 

The layout has 3 main tabs:
Incident Info
IR Procedures
Hunting Results

Incident Info

The incident info tab will provide the analyst with the following information:
Case details.
The number of indicators collected.
Playbook description
The indicators with each section for each type (File, IP, Domain, URL and CVE).
Signatures files:
Yara
Sigma
Source of indicators in a link format.

The main goal is to give the analyst all the relevant information to understand the characteristics and scope of the attack.





IR Procedures

The IR Procedures tab goal is to track all the incident response tasks available in the playbook.
The layout tab is build using Dynamic Sections, 7 of them are numerical for the representation of the total number of tasks, Remaining Tasks and Completed tasks.
The main section is the ‘IR Tracking’, where an analyst or a manager can view the tasks name, status, completion time and a link to pivot to the relevant task in goal to keep track of the playbook execution.
 
 
The ‘IR Tracking’ section is built dynamically based on the following specific playbook headers name, which will take every task (excluding skipped and conditional) available under them.
These are the names of the headers the script is looking for:
Threat Hunting
Mitigation
Remediation
Eradication

In cases where the header wasn’t being used in the playbook or it doesn’t has the required tasks type, the layout will show ‘No tasks found’.

Hunting Results

The Hunting Results tab has 3 sections which will provide the analyst with the following:
The raw results of the SIEM hunting if executed.
The raw results of Panorama and Cortex Data Lake.
Threat hunting results based on unified fields for PANW, Splunk and QRadar.




 
## Set RapidBreachResponse Incident Info Playbook

This playbook is part of the Rapid Breach Response pack and is responsible for presenting the following within the layout:
Playbook description
The playbook description should be provided also as an input for the layout processing.

And provided as an input to the ‘Set RapidBreachResponse Incident Info’ sub-playbook.

Source Of Indicators
The source of indicators collected is provided using the ‘ParseHTMLIndicators’ script output.


Count Total Indicators
The total number of indicators collected. The input should take all indicators and use Unique and then Count transformers.
