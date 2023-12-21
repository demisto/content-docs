---
id: Rapid-Breach-Response
title: Rapid Breach Response
description: Analyzing cyber attacks risk is a vital component of managing and remediating security events. The Rapid Breach Response Layout content pack enables security teams to automate and streamline cyber attacks risk analysis with a dedicated playbook for each scenario.
 
---
This content pack enables security teams to quickly evaluate cyber attack risk using dedicated playbooks for each scenario, such as Hafnium - Exchange 0-day Exploits, SolarStorm, and PrintNightmare.

## Pack Requirements
You must install and configure the **Core Rest API** before you start using this pack.

### Core REST API Integration
The IR Tracking dynamic section is built using the server Rest API and is vital for layout functionality. The scripts require that you install the **Core REST API** integration and configure an integration instance.

1. In Cortex XSOAR, go to **Settings** > **INTEGRATIONS** > **API Keys**.
2. Click **Get Your Key**, enter a name for the API key, and click **Generate Key**.
3. **(IMPORTANT)** Copy and save the API key, you will not be able to access it again.
4. Go to **Settings** > **INTEGRATIONS** > **Servers & Services** and search for **Core REST API**.<br/>
    Note: <br/>
    In multi-tenant environments the **Core REST API** integration should be configured at the parent level and propagated down to the child.
5. Click **Add instance** and enter the required information.
    - A meaningful name for the integration instance
    - The Core Server URL
    - The API key you generated
7. Click **Test** to make sure that that server and API key are reachable and valid.
8. Click **Save & exit**.

## Playbook Workflow
### Collect indicators
The first step in most Rapid Breach Response playbooks is collecting indicators. Indicator sources can be blogs, advisories, or any other highly reliable reference. Indicator format can be text, rules, and signatures.
### Extract, create, and tag the indicators
After completing data collection and indicator extraction, execute the new **Set RapidBreachResponse Incident Info** playbook, which provides:
- Links to sites from which the data was collected
- The playbook description
- The total number of indicators extracted
### Execute threat hunting
After completing information collection and processing, execute threat hunting to find indicators of compromise (IOC) related to the attack in the customer organization. This includes the following tasks:
- PANW Hunting
- Cortex XDR signatures and XQL hunting
- SIEM hunting
- Advanced Hunting based on attack patterns
- IOC hunt using Endpoint Detection and Response
### Remediate and Eradicate the Threats
With the results of indicator collection and threat hunting, remediation and eradication tasks are executed which include:
- Containment using in most cases Block Indicators or Endpoint Isolation
- Mitigation using the detection rules downloaded at phase 1 and any other recommended technique
- Eradication, including removing/quarantining malicious files and validating compromised machines are patched

## In This Pack
The Rapid Breach Response Layout content pack includes several content items.

### Layout

The **Rapid Breach Response** layout has 3 main tabs:
- Incident Info
- IR Procedures
- Hunting Results

#### Incident Info

The Incident Info tab provides the analyst with all the relevant information to understand the characteristics and scope of the attack:
- Case details
- The number of indicators collected
- Playbook description
- The indicators with a section for each type (File, IP, Domain, URL, and CVE)
- Signatures files:
    - Yara
    - Sigma
- The links the indicators were fetched from

![image](https://raw.githubusercontent.com/demisto/content-docs/456ed4f4796529c77f4d5903419145263e0b6c00/docs/doc_imgs/reference/RapidBreachResponseLayout/Incident_Info.png)

#### IR Procedures

The IR Procedures tab tracks all the incident response tasks available in the playbook.
The layout consists of dynamic sections, including:
- The total number of tasks
- Remaining tasks
- Completed tasks
- IR Tracking - The main section where an analyst or a manager can view task name, status, completion time and a link to the relevant task to track the playbook execution. This section is built dynamically and takes every task (excluding skipped and conditional) available under the following playbook header names:
    - Threat Hunting
    - Mitigation
    - Remediation
    - Eradication
    
If the header is not used in the playbook or it doesn't have the required task type, the layout shows ‘No tasks found’.

![image](https://raw.githubusercontent.com/demisto/content-docs/456ed4f4796529c77f4d5903419145263e0b6c00/docs/doc_imgs/reference/RapidBreachResponseLayout/IR_Procedures.png)
  
#### Hunting Results

The Hunting Results tab has 3 sections which provide the analyst with:
- The raw results of the SIEM hunting if executed
- The raw results of Panorama and Cortex Data Lake
- Threat hunting results based on unified fields for PANW, Splunk, and QRadar

![image](https://raw.githubusercontent.com/demisto/content-docs/4da8f27ab1863b7100396bdfa2d2bb6671886a45/docs/doc_imgs/reference/RapidBreachResponseLayout/Hunting_Results.png)

### Automations - Dynamic Sections
The following new dynamic sections are available from Cortex XSOAR 6.0.0.

- **RapidBreachResponse-RemainingTasksCount-Widget** - Shows the updated number of remaining tasks. 
 
- **RapidBreachResponse-RemediationTasksCount-Widget** - Shows the updated number of remediation tasks.
 
- **RapidBreachResponse-CompletedTasksCount-Widget** - Shows the updated number of completed tasks.
 
- **RapidBreachResponse-MitigationTasksCount-Widget** - Shows the updated number of mitigation tasks.
 
- **RapidBreachResponse-TotalTasksCount-Widget** - Shows the updated number of tasks to complete.
 
- **RapidBreachResponse-HuntingTasksCount-Widget** - Shows the updated number of hunting tasks.
 
- **RapidBreachResponse-EradicationTasksCount-Widget** - Shows the updated number of eradication tasks.
 
- **RapidBreachResponse-TotalIndicatorCount-Widget** - Shows the updated number of indicators found.

### Playbooks
**Rapid Breach Response - Set Incident Info**<br/>
This playbook presents the following information in the layout:
- The Playbook description - The playbook description should be provided also as an input for the layout processing and provided as an input to the **Set RapidBreachResponse Incident Info** sub-playbook.
- The Source of the indicators - The collected indicator sources are provided using the **ParseHTMLIndicators** script output.
- The Sum of Total Indicators collected - The total number of collected indicators. The input should take all indicators and use **Unique** and then **Count** transformers.


### Incident Fields

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
**Rapid Breach Response**
