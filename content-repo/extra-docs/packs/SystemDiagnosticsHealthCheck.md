---
id: system-diagnostics-and-health-check
title: System Diagnostics and Health Check
description: The XSOAR Health Check pack automatically reviewing the current server and content for issues and best practices. The pack goal is to identify potential issues and remediate them before they become a real issue.
---
 

## What's in this Content Pack?
 The XSOAR Health Check pack automatically reviewing the current server and content for issues and best practices. 
The pack goal is to identify potential issues and remediate them before they become a real issue.

This pack includes several content items that enable you to retrieve and view data about your system status and content configuration. It is automatically reviewing the current server and content for issues and suggest best practices procedures.
The out-of-the-box items can easily customizable to fit your specific threasholds.
- [Playbooks](#Playbooks)
- [Incident Layouts](#Incident-Layouts)


### Playbooks
This pack contains a parent playbook that calls two sub-playbooks.
 
| Playbook | Description | Notes |
|---------------- | ------------- | ------------- |
| HealthCheck | This is the pack's main playbook and is the default playbook for the **System Diagnostics and Health Check** incident type. You should run this playbook as a manual incident. The playbook collects the data from all other subplaybooks and tasks and save it into XSOAR fields | Under the playbook inputs, you can define if custom thresholds are required change ```ChangeThresholdsRequired``` to ```true```. To change the predefined values it is required to change ```Set Threasholds``` task. |
| Health Check - Collect Log Bundle | This playbook is executed as part of the **HealthCheck** parent playbook and is responsible creating Log Bundle | - | 
| Health Check - Log Analysis Read All files | This playbook is executed as part of the **HealthCheck** parent playbook and is responsible for parsing the extracted files from Log Bundle. | - |

 ---     
### Incident-Layouts
The incident type contains single layout: **System Diagnostics and Health Check**. 

 **System Diagnostics and Health Check**
- System Overview
- Packs & Integrations
- Hardware Resources
- Actionable Items
 
## How to Use the Pack
In order to use this pack, you need to configure **"Demisto REST API"** Integration Instance with **Admin** user

For **Multi-Tenants Deployment**

1. Create API Key on Main Tenant 
2. Propogate the instance to All tenants or to the required tenant using the labels. in the instance settings define as URL https://127.0.0.1
make sure not to define the tenant name in the URL.

There are several prerequisite requirements that you need to handle before you can start with this pack.

### Before You Start

There are several items that you must install and configure before you start using this pack.

### 1. Demisto REST API Integration
The playbooks in the pack use execute scripts to collect and parse from information from the local system. The scripts require that you install the **Demisto REST API** integration and configure an integration instance.

1. Login with **Admin** user
2. In Cortex XSOAR, go to **Settings > INTEGRATIONS > API Keys**.
3. Click the **Get Your Key**, enter a name for the API key, and click **Generate Key**.
4. **(IMPORTANT)** Copy and save the API key, you will not be able to access it again.
5. Go to **Settings > INTEGRATIONS > Servers & Services** and search for **Demisto REST API**.
6. Click **Add instance** and enter the required information.
    - A meaningful name for the integration instance
    - Demisto Server URL; use localhost URL 127.0.0.1
    - API key that you generated
7. Click the **Test** button to make sure that that server and API key are reachable and valid.
8. Click **Save & exit**.

For **Multi-Tenants Deployment**

1. Create API Key on Main Tenant 
2. Propogate the instance to All tenants or to the required tenant using the labels. in the instance settings define as URL https://127.0.0.1
make sure not to define the tenant name in the URL.

 
### 2. Start playbook by creatint manual incident
Now you need to run the main 'HealthCheck' playbook as an mew incident by creating new **System Diagnostics and Health Check** incident.


### 3. Playbook Inputs

We advice not to change the default threasholds value, in case it is needed
The **HealthCheck** playbook contains the following inputs.
You can review the playbook inputs and edit them by clicking the 'Playbook Triggered' section header of the playbook.


| Playbook Input | Description |
|---------------- | ------------- |
| ChangeThresholdsRequired | This input determines if the health check detections should be triggered by custom values change to **true** to enable it|
 ---


