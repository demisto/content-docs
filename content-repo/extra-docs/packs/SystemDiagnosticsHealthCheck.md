---
id: system-diagnostics-and-health-check
title: System Diagnostics and Health Check
description: The System Diagnostics and Health Check pack automatically reviews the current server and content for issues and best practices. The pack enables you to identify potential issues and remediate them before they escalate.
---
 

## What's in this Content Pack?
This pack includes several content items that enable you to retrieve and view data about your system status and content configuration. The pack automatically reviews the current server and content for issues and suggests best practices.
The out-of-the-box items can be easily customized to fit your specific thresholds.
- [Playbooks](#Playbooks)
- [Incident Layouts](#Incident-Layouts)


### Playbooks
This pack contains a parent playbook that calls two sub-playbooks.
 
| Playbook | Description | Notes |
|---------------- | ------------- | ------------- |
| HealthCheck | Healthcheck is the pack's main playbook. Healthcheck is the default playbook for the *System Diagnostics and Health Check* incident type. Run this playbook as a manual incident. The playbook collects data from the sub-playbooks and tasks and saves the data into XSOAR fields | Under the playbook inputs, you can define if custom thresholds are required, by changing *ChangeThresholdsRequired* to **true**. To change the predefined values, edit the *Set Thresholds* task. |
| Health Check - Collect Log Bundle | This playbook is executed as part of the **HealthCheck** parent playbook and is responsible for creating the Log Bundle | - | 
| Health Check - Log Analysis Read All files | This playbook is executed as part of the **HealthCheck** parent playbook and is responsible for parsing the extracted files from the Log Bundle. | - |

 ---     
### Incident-Layouts
The incident type contains one layout: **System Diagnostics and Health Check**. 

### Before You Start

### Demisto REST API Integration
The playbooks in this pack execute scripts to collect and parse information from the local system. The scripts require the **Demisto REST API** integration.

1. Log in to Cortex XSOAR as the **Admin** user.
2. In Cortex XSOAR, go to **Settings > INTEGRATIONS > API Keys**.
3. Click **Get Your Key**, enter a name for the API key, and click **Generate Key**.
4. **(IMPORTANT)** Copy and save the API key. You will not be able to access it again.
5. Go to **Settings > INTEGRATIONS > Servers & Services** and search for **Demisto REST API**.
6. Click **Add instance** and enter the required information.
    - A meaningful name for the integration instance
    - Demisto Server URL; use localhost URL 127.0.0.1
    - API key that you generated
7. Click the **Test** button to make sure that that server and API key are reachable and valid.
8. Click **Save & exit**.

For **Multi-Tenant Deployments**

1. Create an API Key on the Main Account. 
2. Propagate the instance to either all tenants or to some tenants using propagation labels. When defining the URL in the instance settings, use https://127.0.0.1 and do not include the tenant name in the URL.

## How to Use the Pack

### 1. Start the playbook by creating a manual incident
Run the main **HealthCheck** playbook by creating a new *System Diagnostics and Health Check* incident.

### 2. Playbook Inputs

We recommend not changing the default thresholds value, unless you have a specific use case requiring a change.
You can review the playbook inputs and edit them by clicking the 'Playbook Triggered' section header of the playbook.
The **HealthCheck** playbook contains the following inputs.


| Playbook Input | Description |
|---------------- | ------------- |
| ChangeThresholdsRequired | This playbook input determines if the health check detections should be triggered by custom values. Change to **true** to enable.|
 ---


