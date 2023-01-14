---
id: MS_Azure_Integrations
title: Microsoft Azure and O365 Integrations Overview  
description: The following maps all of Microsoft integrations and their use cases. it also emphasizes the differences between similar integrations.
---


# Microsoft Azure and O365 Integrations Overview
Microsoft O365 and Azure are extensive platforms with many different products and functionality.
Moreover, the APIs behind them (especially the Microsoft Graph API) are vast and do not fit under one integration.

Review this document to determine the Microsoft integrations you need for your use case.


## Azure Active Directory

### Use Cases

- Create users and groups.
- Remove a member from a group.
- Remove a pre-approved application.

### Playbooks
- Get Manager Details.
- Active Directory Investigation playbook.


### [Azure Active Directory Users](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-user)
Manage users in Azure Active Directory and O365.

- List, create, and update users.
- Terminate sessions.
- Block users, etc.

### [Azure Active Directory Groups](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-groups)
Manage groups in Azure Active Directory and O365.
- List, create, and update groups.
- List, add, and remove members.

### [Azure Active Directory Identity And Access](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-identityand-access)
Manage Active Directory roles and role members.

### [Azure Active Directory Applications / Service Principals](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-applications)
Manage applications and service principals.

## O365

### Use Cases

- Download a file from OneDrive.
- Send a message via Microsoft Teams.
- Add a member to an existing team.
- Schedule an event in the calendar.

### [O365 File Management (Onedrive/Sharepoint/Teams)](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-files)
Manage files in O365 (OneDrive/SharePoint/Teams).
- Upload and download files.
- List drive and folder content.
- List SharePoint sites.  

### [Microsoft Teams](https://xsoar.pan.dev/docs/reference/integrations/microsoft-teams)
Enable communicating and mirroring via Microsoft Teams.
- Create and update channels.
- Add users to channel
- Message users.
- Ring user.
- Message mirroring.

### [Microsoft Teams Management](https://xsoar.pan.dev/docs/reference/integrations/microsoft-teams-management)
Manage teams and team members.
- Create and update teams.
- Add and remove team members.

### [O365 Outlook Calendar](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-calendar)
Manage calendar events.

### [Microsoft Graph API](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-api)
This is a generic integration that supports running any endpoint of MS Graph API.
Since the API is very vast and not all of the endpoints are implemented, this integration can be used.


## Audit Logs

### Use Cases:
- Find failed login events.
- Find publicly shared files events.
- Find security events.

### Playbooks
- Office 365 and Azure Hunting.
- Office 365 and Azure Configuration Analysis.

### [Microsoft Management Activity](https://xsoar.pan.dev/docs/reference/integrations/microsoft-management-activity-api-o365-azure-events)
Ingest events from O365 (Azure AD, SharePoint, EWS, etc) as incidents.

-----

## Exchange and EWS

### Use Cases
- Find an email message.
- Move an email message to a different folder.
- Send an email.
- Delete Email.
- Modify your Outlook recipient list.
- Process Emails.
- Retrieve and update Tenant Allow/Block List items.
- Search mailboxes
- Compliance search - Start, Remove, Check Status, Get Results

| Integration 	| Cloud/On-Prem 	| Usage 	| Limitations 	| Auth Method 	|
|:---:	|:---:	|:---:	|:---:	|:---:	|
| [EWS Mail Sender](https://xsoar.pan.dev/docs/reference/integrations/ews-mail-sender)	| On-Prem 	| Notify user by mail in a playbook.<br/>Fetch emails as incidents. 	| Supports basic authentication only 	| Basic Auth 	|
| [EWS O365](https://xsoar.pan.dev/docs/reference/integrations/ewso365) 	| Cloud/[Hybrid](https://docs.microsoft.com/en-us/exchange/exchange-hybrid#hybrid-deployment-example)	| Manage and search mailboxes	| For O365 - Supports OAuth2.<br/>Only supports admin accounts that have access to all mailboxes.| client_credentials<br/>Using Oproxy/Self-deployed. 	|
| [EWS v2](https://xsoar.pan.dev/docs/reference/integrations/ews-v2) 	| On-Prem + Cloud 	| Manage and search mailboxes.<br/>Manage compliance searches. 	|  	| Basic Auth + NTLM 	|
| [EWS Extension](https://xsoar.pan.dev/docs/reference/integrations/ews-extension) 	|  	| Manage junk rules and search the message trace. 	| Uses different APIs than EWSv2 	|  	|
| [Exchange Online Powershell V2 module](https://xsoar.pan.dev/docs/reference/integrations/ews-extension#enable-or-disable-access-to-exchange-online-powershell) 	| On-Prem 	| Manage mailboxes and permissions.<br/>Edit Tenant Allow/Block lists.	|  	|  	|
| [O365 Outlook Mail (Using Graph API)](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-mail) 	| Cloud 	| Manage and send email on behalf of a different user that was configured  	|  	| client_credentials<br/>Using Oproxy/Self-deployed. 	|
| [O365 Outlook Mail Single User (Using Graph API)](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-mail-single-user)	| Cloud 	|  	| Can manage the mailbox of the configured user only  	| auth_code (on behalf of a user)<br/>Using Oproxy/Self-deployed.	|
| [Exchange 2016 Compliance Search](https://xsoar.pan.dev/docs/reference/integrations/exchange-2016-compliance-search) 	| On-Prem 	| The only module that enables searching messages across the entire organization. 	|  	| Basic Auth 	|
| [O365 Security and Compliance](https://xsoar.pan.dev/docs/reference/integrations/security-and-compliance) 	| Cloud  	| Search across mailboxes and execute actions on the results. 	| Known limitation in the README<br/>Restart authentication process on  	| device-code (on behalf of a user). 	|


## Azure Cloud

### Use Cases
- Spin up a VM in Azure.
- Block traffic from Azure to a certain IP address.
- Search for Sentinel events in Log Analytics.

### [Azure Compute](https://xsoar.pan.dev/docs/reference/integrations/azure-compute-v2)
Create and manage Azure VMs.

### [Azure Network Security Groups](https://xsoar.pan.dev/docs/reference/integrations/azure-network-security-groups)
Manage security groups to filter network traffic to and from Azure resource

### [Azure Log Analytics](https://xsoar.pan.dev/docs/reference/integrations/azure-log-analytics)
Enable querying data generated from Azure resources.

## Security-focused Integrations

### Use Cases
- Ingest security alerts.
- Search files in Box.
- Isolate an endpoint.
- Wipe a mobile device that has suspicious activity.
- Run a critical Windows update on all the endpoints in the organization. 
- Threat Hunting.
- Add/Search for indicators.
- Add indicators to allow list / block list.
- Trigger scans on specified hosts.
- Get information for a specified host. 

### [Azure Security Center](https://xsoar.pan.dev/docs/reference/integrations/azure-security-center-v2)
Unified Azure security management.
- Fetch alerts.
- Manage auto-provisioning.

### [Azure Sentinel](https://xsoar.pan.dev/docs/reference/integrations/azure-sentinel)
Manage the SIEM by Microsoft.
- Fetch and manage incidents.
- List entities.

### [Azure WAF](https://xsoar.pan.dev/docs/reference/integrations/azure-waf)
Manage the Azure web application firewall.

List, create, and update policies.

### [Microsoft Cloud App Security](https://xsoar.pan.dev/docs/reference/integrations/microsoft-cloud-app-security)
Microsoft CASB solution.
- Fetch and manage alerts.
- Search activity and files in cloud applications.


|   Integration                      |     Use Cases                                                      |   
|:-------------:|:------------------------------------------------------:|
|[Microsoft 365 Defender ](https://xsoar.pan.dev/docs/reference/integrations/microsoft-365-defender)         |  Fetch incidents on email, collaboration, identity, and device threats. <br/>Advanced hunting - querying 30 days of raw data    |   |
| [Microsoft Defender for Endpoint (Defender ATP)](https://xsoar.pan.dev/docs/reference/integrations/microsoft-defender-advanced-threat-protection) |                                                                Microsoft’s endpoint, detection, and response (EDR). <br/>Fetch alerts, run a scan on an endpoint, remediate an endpoint, manage indicators, get machine action status.<br/> Advanced Hunting - open query and OOTB ready to use queries for malware investigation.<br/>Live-Response - instantaneous access to a machines using a remote shell connection.                                   |   |
|            [Microsoft Graph Security](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph)           | Unified gateway to security insights.<br/> Fetch alerts from various Microsoft security sources: **Azure ATP**/**Azure Security Center**/**Microsoft CAS**/**Azure Active Directory Identity Protection**/**Azure Sentinel**/**Microsoft Defender for Endpoint (ATP)**  |   |
|[O365 Defender SafeLinks](https://xsoar.pan.dev/docs/reference/integrations/o365-defender-safe-links) | SafeLinks policy and rule management.<br/>Retrieve reports. |


### [Microsoft Endpoint Configuration Manager (SCCM)](https://xsoar.pan.dev/docs/reference/integrations/microsoft-endpoint-configuration-manager)
Enable execution of scripts on multiple endpoints.

### [Microsoft Graph Device Management (Intune)](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-device-management)
Manage devices.
- Lock a device.
- Wipe a device.
- Locate a device, etc.


## Feeds

### Use Cases:
Fetch Indicators from Microsoft Defender.

### [Office 365 Feed](https://xsoar.pan.dev/docs/reference/integrations/office-365-feed)
Office 365 IP Address and URL feed.

### Microsoft Intune Indicator Feed
 Indicator feed from Microsoft Intune (Defender for Endpoint).
