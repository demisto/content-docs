# Microsoft Azure and O365 Integrations Overview
Microsoft O365 and Azure are a very extensive platforms with a lot of different products and functionality. 
Moreover, the APIs behind them (especially Microsoft Graph API) are very vast and could not fit under one integration. 

This document is made to assist you to find the right integrations you need for the particular use case you need from Microsoft products.


## Azure Active Directory:

### Use Cases:

* Creating users and groups
* Remove a member from a group
* Remove pre-approved application 


### Azure Active Directory Users [link](https://docs.microsoft.com/en-us/graph/api/resources/users?view=graph-rest-1.0)
Manages users in Azure AD & O365. 
List, create & update users, terminating sessions, blocking users, etc. 

### Azure Active Directory Groups [link](https://docs.microsoft.com/en-us/graph/api/resources/groups-overview?view=graph-rest-1.0)
Manages groups in Azure AD & O365. 
List, create & update groups, list/add/remove members. 

### Azure Active Directory Identity And Access : [Link](https://docs.microsoft.com/en-us/graph/api/resources/azure-ad-overview?view=graph-rest-1.0) 
Managing AD roles and role members

### Azure Active Directory Applications : [Applications](https://docs.microsoft.com/en-us/graph/api/resources/application?view=graph-rest-1.0) / [Service Principals](https://docs.microsoft.com/en-us/graph/api/resources/serviceprincipal?view=graph-rest-1.0) 
Manages Applications and Service Principals 

## O365:

### Use Cases:

* Download a file from OneDrive
* Send a message via Microsoft Teams
* Add a member to an existing team
* Schedule an event in Calendar

### O365 File Management (Onedrive/Sharepoint/Teams) [link](https://docs.microsoft.com/en-us/graph/api/resources/onedrive?view=graph-rest-1.0)
Manages files in O365 (OneDrive/SharePoint/Teams)
Upload and download files, list drive and folder content, list SharePoint sites  

### Microsoft Teams: [Link](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0) 
Allows communicating and mirroring via Microsoft Teams 
Supports creating/updating channels, adding users to channel, message user, ring user, and message mirroring

### Microsoft Teams Management: [Link](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0) 
Manages teams and team members
Supports creating_updating teams, adding_removing team members

### O365 Outlook Calendar: [Link](https://docs.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0) 
Allows managing calendar events.

### Microsoft Graph API: [Link](https://docs.microsoft.com/en-us/graph/overview?view=graph-rest-1.0) 
This is a generic integration that supports running any endpoint of MS Graph API.
Since the API is very vast and not all of the endpoints are implemented, this integration can be used.


## Audit Logs 

### Use Cases:
* Find events of failed logins
* Find events of files publicly shared
* Find security events

### Microsoft Management Activity: [Link](https://docs.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference) 
Ingesting events from O365 (Azure AD, Sharepoint, EWS, etc) as incidents

### Microsoft Policy And Compliance - Office365 And Azure Audit Log: [Link](https://docs.microsoft.com/en-us/powershell/module/exchange/?view=exchange-ps#policy-and-compliance-audit)
Searching Audit logs from O365 and Azure.

-----

## Exchange & EWS 

### Use Cases:
* Find an email message
* Move an email message to a different folder
* Send email
* Modify Outlook recipient list

| Integration 	| Cloud/On-Prem 	| Usage 	| Limitations 	| Auth Method 	|
|:---:	|:---:	|:---:	|:---:	|:---:	|
| EWS Mail Sender	| On-Prem 	| Notify user by mail in a playbook<br>Fetches emails as incidents 	| Supports basic authentication only 	| Basic Auth 	|
| EWS O365 	| Cloud/Hybrid 	|  	| For O365 - Supports OAuth2<br>Only supports admin account that have access to all mailboxes 	| client_credentials<br>Using Oproxy/Self-deployed 	|
| EWS v2 	| On-Prem + Cloud 	|  	|  	| Basic Auth + NTLM 	|
| EWS Extension 	|  	| Managing junk rules and search the message trace 	| uses different APIs than EWSv2 	|  	|
| Exchange Online Powershell V2 module 	| On-Prem 	| Managing mailboxes and permissions 	|  	|  	|
| O365 Outlook Mail (Using Graph API) 	| Cloud 	|  	|  	| client_credentials<br>Using Oproxy/Self-deployed 	|
| O365 Outlook Mail Single User<br>(Using Graph API) 	| Cloud 	| Same as O365 Outlook Mail but for a single user. 	|  	| auth_code (on behalf of a user)<br>Using Oproxy/Self-deployed 	|
| Exchange 2016 Compliance Search 	| On-Prem 	| the only module allowing search of messages cross all org 	|  	| Basic Auth 	|
| O365 Security and Compliance 	| Cloud  	| Search across mailboxes and execute actions on the results. 	| Known limitation in the README’s<br>Restart auth process on  	| device-code (on behalf of a user)  	|


## Azure Cloud:

### Use Cases:
Spin a VM in Azure
Block traffic from Azure to a certain IP
Search for Sentinel events in Log Analytics

### Azure Compute: [Link](https://docs.microsoft.com/en-us/rest/api/compute/)
Creates and manages Azure VMs

### Azure Network Security Groups: [Link](https://docs.microsoft.com/en-us/rest/api/virtualnetwork/network-security-groups) 
Manages security groups to filter network traffic to and from Azure resources

### Azure Log Analytics: [Link](https://docs.microsoft.com/en-us/rest/api/loganalytics/)
Allows querying data generated from Azure resources.

## Security-focused integrations:

### Use Cases:
Ingest security alerts 
Search files in Box
Isolate an endpoint
Wipe a mobile device that has a suspicious activity 
Run a critical windows update on all the endpoints in the organization  

### Azure Security Center: [Link](https://docs.microsoft.com/en-us/rest/api/securitycenter/)
Unified Azure security management.
Fetching alerts, managing auto-provisioning.

### Azure Sentinel: [Link](https://docs.microsoft.com/en-us/rest/api/securityinsights/)
Managing the SIEM by Microsoft. 
Fetching and managing incidents. listing entities 

### Azure WAF: [Link](https://docs.microsoft.com/en-us/rest/api/apimanagement/2021-01-01-preview/api-policy)
Managing the Azure web application firewall.
List create and update policies

### Microsoft Cloud App Security: [Link](https://docs.microsoft.com/en-us/cloud-app-security/api-introduction) 
Microsoft CASB solution
Fetching and managing alerts, searching activity and files in cloud applications.


|   Integration                      |     Use Cases                                                      |   
|:-------------:|:------------------------------------------------------:|
|Microsoft 365 Defender (Beta) [Link](https://docs.microsoft.com/en-us/microsoft-365/security/defender/api-overview?view=o365-worldwide)         |  Fetch incidents on email, collaboration, identity, and device threats Advanced hunting - querying 30 days of raw data    |   |
| Microsoft Defender for Endpoint (Defender ATP) [Link](https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/apis-intro?view=o365-worldwide) |                                                                Microsoft’s EDR  Fetching alerts, running a scan on an endpoint, remediating an endpoint, managing indicators                                                                |   |
|            Microsoft Graph Security: [Link](https://docs.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0)           | Unified gateway to security insights Fetching alerts from various Microsoft security sources: **Azure ATP**/**Azure Security Center**/**Microsoft CAS**/**Azure Active Directory Identity Protection**/**Azure Sentinel**/**Microsoft Defender for Endpoint (ATP)**  |



### Microsoft Endpoint Configuration Manager (SCCM): [Link](https://docs.microsoft.com/en-us/powershell/sccm/overview?view=sccm-ps) 
Allowing execution of scripts on multiple endpoints. 

### Microsoft Graph Device Management (Intune): [Link](https://docs.microsoft.com/en-us/powershell/sccm/overview?view=sccm-ps) 
Managing devices - lock device, wipe a device, locate device, etc. 
 

## Feeds

### Use Cases:
Fetch Indicators from Microsoft Defender

### Office 365 Feed : [Link](https://techcommunity.microsoft.com/t5/office-365-blog/announcing-office-365-endpoint-categories-and-office-365-ip/ba-p/177638)
Office 365 IP Address and URL feed 

### Microsoft Intune Indicator Feed :
 Indicator feed from Microsoft Intune (Defender for Endpoint)


