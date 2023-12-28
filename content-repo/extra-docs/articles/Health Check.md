---
id: system-diagnostics-and-health-check
title: System Diagnostics and Health Check
description: The System Diagnostics and Health Check pack automatically reviews the current server and content for issues and best practices. The pack enables you to identify potential issues and remediate them before they escalate.
---


## What's in this Content Pack?
This pack includes several content items that enable you to retrieve and view data about your system status and content configuration. The pack automatically reviews the current server and content for issues and suggests best practices.
The out-of-the-box items can be easily customized to fit your specific thresholds.
- [Automations](#automations)
- [Playbooks](#playbooks)
- [Incident Layouts](#incident-layouts)
- [Incident Fields](#incident-fields)


### Automations
There are 28 automations in this pack.

| Name | Description | 
| --------------- | ------------- |
| HealthCheckAnalyzeLargeInvestigations | Analyze large investigation from previous month until current month. | 
| HealthCheckCommonIndicators | Reports on common indicators |
| HealthCheckContainersStatus | Containers status |
| HealthCheckCPU | Present or parse CPU usage stats. |
| HealthCheckDiskUsage | Present or parse Disk usage stats. |
| HealthCheckDiskUsageLine | Present Disk usage stats line widget |
| HealthCheckDockerLog | Read Docker log file |
| HealthCheckFileSystem | Read and parse filesystem.log |
| HealthCheckGetLargestInputsAndOutputsInIncidents | Returns inputs and outputs larger than 1 MB from all Cortex XSOAR investigations in the last 1 / 2 months. |
| HealthCheckIncidentsCreatedDaily | Trend graph for incidents created per day |
| HealthCheckIncidentsCreatedMonthly | Trend graph for incidents created per month |
| HealthCheckIncidentsCreatedWeekly | Trend graph for incident creation |
| HealthCheckInstalledPacks | Read the installedpacks.json. Count and get packs names |
| HealthCheckIntegrations | Trend graph for incidents created per day |
| HealthCheckLicenseData | Read the license_data.log file extracted from the log bundle |
| HealthCheckMemory | Present or analyze memory usage |
| HealthCheckNumberOfDroppedIncidents | Number of dropped incidents | 
| HealthCheckNumberOfEngines | Presenting Number of engines |
| HealthCheckOutdatedPacks | Presenting Outdated Packs |
| HealthCheckPacksInstalled | Presenting numbers of packs installed |
| HealthCheckPlaybookAnalysis | Parsing playbooks | 
| HealthCheckReadConf | Read the license_data.log file extracted from the log bundle |
| HealthCheckReadTelemetryLog | Read Telemetry log |
| HealthCheckReadVC | Read the version_control.log file extracted from the log bundle |
| HealthCheckServerConfiguration | Collect server configurations and save that into a table field |
| HealthCheckServerLog | Read server log file line by line and display warnings, fatal errors and keyword results in a table to the War Room |
| HealthCheckUnpack | Extract files from log bundle - supports tar.gz & tar. Handles unsupported use cases and unextracted files. |
| HealthCheckWorkers | Present or analyze workers usage |

### Playbooks
This pack contains a parent playbook that calls two sub-playbooks.

| Name | Description | Notes |
| --------------- | ------------- | --------- |
| HealthCheck | Healthcheck is the pack's main playbook. Healthcheck is the default playbook for the *System Diagnostics and Health Check* incident type. Run this playbook as a manual incident. The playbook collects data from the sub-playbooks and tasks and saves the data into XSOAR fields | Under the playbook inputs, you can define if custom thresholds are required, by changing *ChangeThresholdsRequired* to **true**. To change the predefined values, edit the *Set Thresholds* task. |
| Health Check - Collect Log Bundle | This playbook is executed as part of the **HealthCheck** parent playbook and is responsible for creating the Log Bundle | - | 
| Health Check - Log Analysis Read All files | This playbook is executed as part of the **HealthCheck** parent playbook and is responsible for parsing the extracted files from the Log Bundle. | - |

 ---     
### Incident Layouts
The incident type contains one layout: **System Diagnostics and Health Check**. 

### Incident Fields
There are 47 incident fields.
- **Health Check Actionable Items**
- **Health Check Docker Containers**
- **Health Check Docker Paused**
- **Health Check Docker Running**
- **Health Check Docker Stop**
- **Health Check Docker Version**
- **Health Check Enabled Instances**
- **Health Check Installed Packs**
- **Health Check Investigations bigger than 10MB**
- **Health Check Investigations bigger than 1MB**
- **Health Check Investigations input / output bigger than 10MB**
- **Health Check Investigations input / output bigger than 1MB**
- **Health Check Large Files**
- **Health Check Log Since**
- **Health Check Log Until**
- **Health Check Number Of Engines**
- **Health Check Number of investigations bigger than 10MB**
- **Health Check Number of investigations bigger than 1MB**
- **Health Check Number of investigations input / output bigger than 10MB**
- **Health Check Number of investigations input / output bigger than 1MB**
- **Health Check Number of investigations with more than 500 entries**
- **Health Check Permitted Users**
- **Health Check Restart Count**
- **Health Check Total Outdated Packs**
- **Health Check Total Packs Installed**
- **Health Check Used Users**
- **Health Check Workers Busy**
- **Health Check Workers Total**
- **XSOAR Architecture**
- **XSOAR Build**
- **XSOAR Content Version**
- **XSOAR CPU**
- **XSOAR Customer Name**
- **XSOAR Dev-Prod**
- **XSOAR Dev-Prod Mode**
- **XSOAR DR**
- **XSOAR Elastic Search**
- **XSOAR License**
- **XSOAR License Valid Till**
- **XSOAR Memory**
- **XSOAR Multi-Repo**
- **XSOAR Multi-Tenant**
- **XSOAR Number Of DB Partitions**
- **XSOAR OS**
- **XSOAR Server Configuration**
- **XSOAR Telemetry Status**
- **XSOAR Version**




  ------- 




### Prerequisites for Triggering the Playbook
The playbooks in this pack execute scripts to collect and parse information from the local system. The scripts require the **Core REST API** integration.

1. Log in to Cortex XSOAR as the **Admin** user.
2. In Cortex XSOAR, go to **Settings > INTEGRATIONS > API Keys**.
3. Click **Get Your Key**, enter a name for the API key, and click **Generate Key**.
4. **(IMPORTANT)** Copy and save the API key. You will not be able to access it again.
5. Go to **Settings > INTEGRATIONS > Servers & Services** and search for **Core REST API**.
6. Click **Add instance** and enter the required information.
    - A meaningful name for the integration instance
    - Core Server URL; use localhost URL 127.0.0.1
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