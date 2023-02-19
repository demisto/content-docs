---
id: integrations-and-incident-health-check
title: Integrations and Incidents Health Check
description: The Health Check for Integrations and Incidents content pack uses out-of-the-box playbooks, scheduled as a job, to check for, return, and display information about failed integrations and incidents with errors. As part of the playbook run, users will be sent an email notification when failed incidents and/or integrations are discovered.
---
 

## What's in this Content Pack?
 
This pack includes several content items that enable you to retrieve and view data about failed integrations and incidents. The out-of-the-box items are robust enough to get started with, but are easily customizable to fit your specific requirements.
- [Playbooks](#Playbooks)
- [Incident Layouts](#Incident-Layouts)
- [Dashboards & Lists](#Dashboards-and-Lists)


### Playbooks
This pack contains a parent playbook that calls two sub-playbooks.
 
| Playbook | Description | Notes |
|---------------- | ------------- | ------------- |
| JOB - Integrations and Incidents Health Check | This is the pack's parent playbook and is the default playbook for the **Integrations and Incidents Health Check** incident type. You should run this playbook as a scheduled job. The playbook checks the health of all enabled integrations and open incidents | Under the playbook inputs, you can add recipients to send the health check report via email. See below for additional features of this playbook. |
| Integrations and Incidents Health Check - Running Scripts | This playbook is executed as part of the **JOB - Integrations and Incidents Health Check** parent playbook and is responsible for running scripts that check the system for failed integrations and failed incidents.  | You can run the playbook on its own (not only as a sub-playbook of the parent playbook) to run health checks on enabled integrations and open incidents. |
| JOB - Integrations and Incidents Health Check - Lists handling | This playbook is executed as part of the **JOB - Integrations and Incidents Health Check** parent playbook and is responsible for creating or updating related XSOAR lists. | - |
 ---
 
In addition to running the sub-playbooks, the **JOB - Integrations and Incidents Health Check** parent playbook performs the following functions:
- Send the health check report to the recipients from the playbook inputs.
- If another health check investigation is open (either an incident or a running job), the playbook will:
  - Check if analyst notes were added to the failed integrations and failed incidents grids and **copy** them to the new investigation.
  - Link the old investigation to the new one and close the old investigation due to irrelevance.
- Re-run the health check tests. This is a manual action because you will want to re-run the health checks only after fixing the issues, not before.
 
### Incident Layouts
The incident type contains two layouts: one for **failed integration instances** and one for **failed incidents**. 

 **Failed integrations layout**
- Total number of failed instances
- Incident category
- Total number of checked instances (enabled instances)
- Why the instances/incidents failed
- Analyst notes


**Failed incidents layout**
- Total number of failed incidents
- Total number of errors
- Total number of unassigned incidents that failed
- Top 10 failed commands and playbook names that failed
- Analyst notes
 
Note: When the parent playbook copies the analyst note from the integration\incident to the new investigation, the old investigation's date is added.
 
### Dashboards and Lists
The dashboard displays data collected from the last playbook run, either from the job or manually executed.
The dashboard **isn't** a real-time, dynamic view, it only displays the results of the last playbook run.
For example, if the job/playbook runs once a day, the dashboard data will be updated once a day (at the same time the playbook is running).
 
## How to Use the Pack
In order to use this pack, you need to configure several integrations and to schedule the main playbook as a recurring job. Although you can run the parent playbook as an incident with the **Integrations and Incidents Health Check** incident type, the most common way to execute it is as a scheduled job.

There are several prerequisite requirements that you need to handle before you can start with this pack.

### Before You Start

There are several items that you must install and configure before you start using this pack.

### 1. Demisto REST API Integration
The playbooks in the pack use execute scripts to check the system for failed integrations and incidents. The scripts require that you install the **Demisto REST API** integration and configure an integration instance.

1. In Cortex XSOAR, go to **Settings > INTEGRATIONS > API Keys**.
2. Click the **Get Your Key**, enter a name for the API key, and click **Generate Key**.
3. **(IMPORTANT)** Copy and save the API key, you will not be able to access it again.
4. Go to **Settings > INTEGRATIONS > Servers & Services** and search for **Demisto REST API**.
    - Note: in Multi Tenant environments the **Demisto REST API** integration should be configured at the parent level and propagated down to the child.
5. Click **Add instance** and enter the required information.
    - A meaningful name for the integration instance
    - Demisto Server URL
    - API key that you generated
7. Click the **Test** button to make sure that that server and API key are reachable and valid.
8. Click **Save & exit**.
 
 ### 2. (Optional) Configure a Mail Sender and Mail Listener Integration  
 The main playbook has the ability to send an email notification to specified users. In order for this function to work you first need to configure the mail integrations. 

 **Supported mail integrations**
 
 - [Gmail](https://xsoar.pan.dev/docs/reference/integrations/gmail)
 - [Gmail Singe User (BETA)](https://xsoar.pan.dev/docs/reference/integrations/gmail-single-user)
 - [Mail Sender](https://xsoar.pan.dev/docs/reference/integrations/mail-sender-new)
 - [Microsoft Graph Mail](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-mail)
 - [Microsoft Mail Single User](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-mail-single-user)
 - [EWS v2](https://xsoar.pan.dev/docs/reference/integrations/ews-v2)
 - [EWS O365](https://xsoar.pan.dev/docs/reference/integrations/ewso365)
 - [EWS Mail Sender](https://xsoar.pan.dev/docs/reference/integrations/ews-mail-sender)
 

 
### 3. Configure a Job
Although you can run the parent playbook as an incident, the most common way to execute it is as a scheduled job. In both cases, the incident type must be **Integrations and Playbooks Health Check**.

 There are additional optional configurations that you can specify. For more information, see detailed instructions on how to [configure a job](https://xsoar.pan.dev/docs/incidents/incident-jobs). Below we specify the required configurations and the values you should enter.

Although not required, we recommend that you create a recurring schedule for the job. The schedule should accomplish your health check monitoring goals. For example, you might want to check for failed integrations and incidents every 12 hours, which means that no integration or incident will be failed for more than 12 hours.

| Parameter Name | Value |
| ------------- | ----- |
| Type | Integrations and Incidents Health Check |
| Playbook | JOB - Integrations and Incidents Health Check. This playbook should automatically populate when you select the incident type. If it does not, make sure you select this playbook. |



### 4. Playbook Inputs
The **JOB - Integrations and Incidents Health Check** playbook contains the following inputs.
You can review the playbook inputs and edit them by clicking the 'Playbook Triggered' section header of the playbook.


| Playbook Input | Description |
|---------------- | ------------- |
| SendHealthCheckReport | This input determines if the health check report should be sent automatically after running the playbook. |
| EmailReportTo | If the *SendHealthCheckReport* input is set to 'True', the email address the health check report will be sent to.  |
| AutoCloseInvestigation | This input determines if the investigation should close automatically after rerunning the scripts.|
 ---

## Notes
1. Integration instances in which the *Do not use by default* checkbox was selected, are not supported by this pack. This is due to XSOAR platform limitations and in order to prevent exceeding quota limits.

## Troubleshooting
The Health Check for Integrations and Incidents  pack contains several incident fields which are associated with the **Integrations and Incidents Health Check** incident type. 

In order to use this flow, the incident type must be set accordingly when creating a new incident or job.

If the incident type **Integrations and Incidents Health Check** is not chosen, fields will not be displayed correctly and the playbook will fail with this error:

![griderror](https://raw.githubusercontent.com/demisto/content-docs/master/docs/doc_imgs/reference/HealthCheck_GridError.png)
 

## Limitations
Testing the following OAuth integrations is currently not supported:
  * ServiceNow v2
  * ServiceNow CMDB
  * Gmail Single User
  * Versa Director

Additionally, when using a self-deployed application for Microsoft/Azure integrations, testing the following integrations is not supported:
  * Microsoft Graph API
  * Microsoft Graph User
  * Microsoft Graph Mail Single User
  * Microsoft 365 Defender
  * Microsoft Defender for Cloud Apps
  * O365 Defender SafeLinks - Single User
  * Microsoft Teams Management
  * Microsoft Policy And Compliance (Audit Log)
  * O365 - EWS - Extension
  * Azure Active Directory Applications 
  * Azure Active Directory Identity And Access
  * Azure Data Explorer
  * Azure DevOps
  * Azure Firewall
  * Azure Kubernetes Services
  * Azure Network Security Groups
  * Azure Risky Users
  * Azure SQL Management
  * Azure Storage
  * Azure WAF

