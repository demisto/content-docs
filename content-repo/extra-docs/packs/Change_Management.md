---
id: Change Management
title: Change Management 
description: The firewall change management is a complex and delicate process that needs to be performed with extreme caution due to the consequences that can be caused due to a mistake.
If you use Pan-Os or Panorama as your enterprise firewall and Jira or ServiceNow as your enterprise ticking this pack will assist you perform a well coordinated and documented process.

---





## Pack Workflow:

Playbook triggers:

XSOAR - 

When there is a need for change request you can create manually change  management incident by choosing the “FW change management” incident type in the incident creation form you will receive dedicated form for your change request that will contain the next inputs:

Request Summary
Request Description
Destination Port
FW policy action
FW Source Zone
FW Destination Zone
Protocol
FW Service
Request DST
Request SRC






After providing the inputs above the “Change Management for FW” will be triggered.  

Email - 

You can trigger the “Change Management for FW” playbook by fetching email using the following integrations:

Mail Listener v2
EWS O365
EWS v2
Gmail
Gmail Single User
Microsoft Graph Mail
Microsoft Graph Mail Single User

As part of the change management pack there are 4 OOTB calcifer one for each mail integration:

EWS change management
Gmail change management
Microsoft Graph Mail change management
Mail Listener change management

You can set the relevant classifier in the relevant integration in the integration settings:




 
The classifier is defined to execute the “Change Management for FW” playbook when the email subject is set to “change management”

Note: in case you wish to use different phrases for the classifier you will need to create a new classifier or edit the existing one.

When the incident is fetched and classified, an email will be sent to the relevant security team (this email will be provided as a playbook input) with a form to retrieve all the relevant inputs to execute the “Change Management for FW” playbook.    

     
 








Jira - 

First you will need to create new project in Jira UI or adjust your you existing project that use for change management process to contain the following custom fields:

Request Summary
Request Description
Destination Port
FW policy action
FW Source Zone
FW Destination Zone
Protocol
FW Service
Request DST
Request SRC




Mapper  - After creating the described above, create in Jira issue that will be used for mapping the fields above in XSOAR record the values for later use, fetch this specific incident to XSOAR you can use Query in the integration settings (in JQL).
After the incident was fetched go to setting > object setup > classification and mapping, choose the classifier-mapper-incoming-JiraV2 and duplicate it:





Edit the duplicated mapper and load the incident you fetched:





Now you can search for the values that you recorded previously and map accordingly, for example if you provided the value 1.1.1.1 for Request SRC in Jira search it in the JSON and map it to the relevant field perform this action for all related fields to change management:

Request Summary
Request Description
Destination Port
FW policy action
FW Source Zone
FW Destination Zone
Protocol
FW Service
Request DST
Request SRC


  
 






Setting the integration -  

Add Atlassian Jira v2 instance with “FW change management” as the incident type and set the mapper the was created as mentioned above, for the outgoing mapper use the default classifier-mapper-outgoing-Jira mapper:


  

In the query section make sure to fetch only the relevant incident for change management:
(In the example below the “cm” is detected project for change management)













 
Mirror - 

One of the core logic in this use case in the documentation of the all process for future reference, therefore if you using Jira integration make sure all the relevant setting for mirror and enabled (https://xsoar.pan.dev/docs/reference/integrations/jira-v2#configure-incident-mirroring):












ServiceNow - 


Edit your incident form in ServiceNow that will contain the following fields (in Form design and Layout design in ServiceNow):

Request Summary
Request Description
Destination Port
FW policy action
FW Source Zone
FW Destination Zone
Protocol
FW Service
Request DST
Request SRC  

Mapper  - After creating the described above, create a ServiceNow incident that will be used for mapping the fields above in XSOAR record the values for later use, fetch this specific incident to XSOAR you can use “The query to use when fetching incidents”
After the incident was fetched go to setting > object setup > classification and mapping, choose the ServiceNow - Incoming Mapper and duplicate it:











Now you can search for the values that you recorded previously and map accordingly, for example if you provided the value 1.1.1.1 for Request SRC in Jira search it in the JSON and map it to the relevant field perform this action for all related fields to change management:

Request Summary
Request Description
Destination Port
FW policy action
FW Source Zone
FW Destination Zone
Protocol
FW Service
Request DST
Request SRC





Setting the integration -  

Add ServiceNow v2 instance with “FW change management” as the incident type and set the mapper the was created as mentioned above, for the outgoing mapper use the default ServiceNow - Outgoing Mapper mapper:




In the query section make sure to fetch only the relevant incident for change management:





Mirror - 

One of the core logic in this use case in the documentation of the all process for future reference, therefore if you using ServiceNow integration make sure all the relevant setting for mirror and enabled (https://xsoar.pan.dev/docs/reference/integrations/service-now-v2#configure-incident-mirroring)









## Use case workflow:


After the playbook will be triggered by one of the options that mentioned above, the relevant logs will be queried based on the parameters in the change request for the purpose of this action is to assist in the decision of approving or rejecting, in case the ticketing system integration (ServiceNow or Jira)  is available the logs will be uploaded to issue/incident and link to XSOAR incident will added as well.
An email will be sent to to retrieve the answer of approval or rejection to the change request pending to the decision two path will available:

Reject - 
In case that the request was rejected the issue/incident will be closed with the relevant comments and the incident in XSOAR will be closed as well.   
 Approve - 
In case that the request was approved the user will receive an option to deploy the new policy first to the DEV environment for testing (this option will be determined by the playbook inputs).
If the decision for the change request after the testing in the DEV environment was rejected please refer to the reject path above.
After the approval the request will be forward to the to the “PAN-OS create or edit policy” playbook that is responsible for actual change in the existing policy, this playbook will check first which security policy matches the change request parameters, if there isn't security policy that match the request a new rule will be created, if there is security policy that matches the user can choose to modify/harden the policy or not, in case the user will choose to modify he will be needed to choose between three options: create new harden rule, manually review the relevant rule or edit the existing rule, if the user will choose edit the existing rule then “PAN-OS edit existing policy” playbook will be executed this is a dedicate playbook for editing policy in Pan-os and Panorama, data collection form will be sent to users to retrieve all the relevant details for the policy editing such as: element to change, element value and the behavior.
After the execution of this playbook and the change in the policy the request owner is required to validate the change, after the validation phase will be completed the issue/ticket will be closed.

Flow documentation:

 As part of this pack work flow all important decisions during the change management will be documented in XSOAR and mirrored to the issue\ticket in the ticketing system.







In this pack:
  
## Playbooks:

Change Management for FW - 

This is the main playbook in the change management pack, this playbook can be triggered by 4 different options: XSOAR, Email, ServiceNow, Jira.
The playbook will guide you through all the critical stages in the process such as user request, request approval, testing, deployment and validation. 

ServiceNow Change Management

This playbook will be triggered by fetch from ServiceNow and guide you through all the critical stages in the process such as user request, request approval, testing, deployment and validation.

Jira Change Management

This playbook will be triggered by fetch from JIra and guide you through all the critical stages in the process such as user request, request approval, testing, deployment and validation.

PAN-OS create or edit policy

This playbook will automate the process of creating or editing policy.
First task in the playbook will check if there is security policy that matches the playbook inputs in case there is no security policy that matches a new policy will be created, in case there is security policy that matches the user will be able to modify the existing policy or create a new hardened policy.   


PAN-OS edit existing policy

This playbook will guide the user in the process of editing existing policy, the playbook will send a data collection form that will retrieve the relevant parameters for editing the existing rule.









Incident Fields:


FW policy action
FW Service
FW Source Zone
Request Description
Request DST
Request SRC
Request Summary
Security Policy Match



Incident Types:

There is 1 incident type - FW change management

Automations:

IncidentState - dynamic script that is used in the layout to display the insicient state contains 5 states:
Request Was Submitted
Request Was Approved
Request Was Rejected'
FW Policy Was Updated
Awaiting Request Owner Validation



## Layout

This layout has three tabs 

Incident info tab

Layout sections
Description
Incident state
Displays the state of the incident 
Security policy match
Displays the security policies that matched the change request parameters  
Change request details
the change request parameters
Team members 
A list of the analysts who participated in this incident.
Decision
Filtering the decisions for the change management from the Change request documentation 
Change request documentation
Displays all the documented phases in the change management process.  
Work plan
Information regarding the playbook tasks from the Work Plan.
Attachments 
The FW logs that were queried for the change request
Timeline information
Information regarding the incident timeline, such as: time occurred, last update, closed time, etc.
Closing information
Information regarding the closing of the incident.




Jira tab


Layout sections
Description
Jira issue details
General details in the issue 
Jira issue description
Jira issue description and summary 
Jira Timeline
Jira issue Timeline
Jira ticket members
The assignees to the issue in Jira
Jira attachments
Attachments in the Jira issue
XSOAR case details
Details on the incident in XSOAR 
Mirroring information
Mirroring setting information
Work plan
Information regarding the playbook tasks from the Work Plan.
XSOAR linked incidents
XSOAR linked incidents that linked to the Jira mirrored incident. 
Notes
Comments entered by the user regarding the incident (mirrored with Jira).


ServiceNow tab

Snow ticket status
Displays the ticket status
Snow ticketing handling
General information on the ticket handling
Snow ticket close notes
Displays information regarding the closure details 
Snow ticket information
General information on the ticket
Snow ticket notes
Comments entered by the user regarding the incident (mirrored with SNOW).
Attachments 
Attachments in the ServiceNow ticket






## Before You Start



This pack requires that you have an active instance of an email sender integration in order to send an email to the security/net-ops team for request approval and data collection tasks, if none of the email sender integration will be available all the data collection tasks in the playbook flow will have to be provided manually.

Email sender integration could be used as change management playbook triggers as well,please refer to the playbook trigger section in this article.  
 
If your organization uses Jira or ServiceNow as an enterprise ticketing system this will be a great addition to the change management pack, please refer to the playbook trigger section in this article.


Pack Configuration  
                                       

To get up and running with this pack, you must do the following:

- In your relevant panorama/Pan-os instance for change management, set the FW change management as the incident type.  
- Configure Change Management for FW playbook inputs (link to the playbook readme)
In case of using Jira/ServiceNow integration follow the steps in the playbook triggers section.
Usage of email sender integration is highly recommended for the pack workflow, in case you wish that the FW change management incident type will be triggered by mail please follow the steps in playbook triggers section.










## Testing the Pack:

After you configure all the relevant settings that are mentioned above, creating a test incident (depends on the trigger that you created) is recommend to provide real values that are existing in your network, run the playbook and verify that the flow that you choose is working as expected.     



       
