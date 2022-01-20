---
id: Change Management
title: Change Management 
description: The firewall change management is a complex and delicate process that needs to be performed with extreme caution due to the consequences that can occur due to a mistake.
If you use PAN-OS or Panorama as your enterprise firewall and Jira or ServiceNow as your enterprise ticking, this pack will assist you perform a well coordinated and documented process.

---

Change management for firewalls is a process in enterprises and organizations that enables users to change a specific network behavior. For example, if a user in an organization can’t reach an application because the firewall is blocking it, the user can raise an issue for the relevant network team to allow this traffic. 

Note: The firewall change management is a complex and delicate process that needs to be performed with extreme caution due to consequences that can occur due to a mistake.

If you use PAN-OS or Panorama as your enterprise firewall and Jira or ServiceNow as your enterprise ticketing system, this pack will assist you to perform a well coordinated and documented process.



## Playbook Triggers

The following are the possible playbook triggers:

- [Jira](#jira)
- [ServiceNow](#servicenow)



### Jira 

1. To trigger the **Change Management for FW** playbook via Jira, you need to create a new project in the Jira UI, or adjust your existing Jira project that uses the change management process to contain the following custom fields:

- Request Summary - Details
- Request Description - Description
- Destination Port - Dst Ports
- FW policy action - Policy Actions
- FW Source Zone - Source Networks
- FW Destination Zone - Destination Networks
- IP Protocol - Protocol
- FW Service - Protocol names
- Request DST - Source IPs
- Request SRC - Destination IPs

To create a project in Jira, see https://support.atlassian.com/jira-software-cloud/docs/create-a-new-project/.
To create custom fields in a Jira project, see https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/.




2. In Jira, create an issue that will be used for mapping the custom fields in Cortex XSOAR. 
3. Record the values of these fields for later use. 
4. In Cortex XSOAR, fetch this specific incident. You can use the Query in the integration settings (in JQL).
5. After the incident is fetched, go to **Setting** > **Object Setup** > **Classification and Mapping** and choose **classifier-mapper-incoming-JiraV2**.
6. Click **Duplicate**.

{incident screenshot here}




7. Edit the duplicated mapper by clicking it.
8. From the **Select Incident** dropdown list, select the incident you fetched.

{select incident screenshot here}




9. Search for the values that you previously recorded and map them accordingly. For example, if the value of *Request SRC* was 1.1.1.1 in Jira, search for it in the JSON and map it to the relevant field. Repeat this for all the custom fields.

{map fields screenshot here}



10. Create an instance of the **Atlassian Jira v2** integration.
   1. Select **FW change management** as the incident type.
   2. Select the mapper that was created above.

   {instance setting screenshot here}

   3. For the outgoing mapper, select the default **classifier-mapper-outgoing-Jira mapper**.
   4. In the Query section, enter a query to ensure the only change management incidents are fetched. (In the example below, *cm* is the detected project for change management.)

   {query screenshot here}

11. Since it is important to document all the processes in the playbook for future reference, if you are using the Jira integration, make sure all the relevant mirroring settings are enabled (https://xsoar.pan.dev/docs/reference/integrations/jira-v2#configure-incident-mirroring).




### ServiceNow


1. In *Form design* and *Layout design* in ServiceNow, edit your incident form to contain the following custom fields. See https://docs.servicenow.com/bundle/rome-it-service-management/page/product/change-management/task/t_CreateCustomField.html for details.
- Request Summary - Details
- Request Description - Description
- Destination Port - Dst Ports
- FW policy action - Policy Actions
- FW Source Zone - Source Networks
- FW Destination Zone - Destination Networks
- IP Protocol - Protocol
- FW Service - Protocol names
- Request DST - Source IPs
- Request SRC - Destination IPs
2. Create a ServiceNow incident that will be used for mapping the custom fields in Cortex XSOAR.
3. Record the values of these fields to use later.
4. In Cortex XSOAR, fetch this specific incident. You can use the Query in the integration settings (in JQL).
5. After the incident is fetched, in Cortex XSOAR go to **Settings** > **Object Setup** > **Classification and Mapping** and choose **ServiceNow - Incoming Mapper**.
6. Click **Duplicate**.

{SNOW incidents screenshot here}

7. Search for the values that you previously recorded and map them accordingly. For example, if the value of Request SRC was 1.1.1.1 in Jira, search for it in the JSON and map it to the relevant field. Repeat this for all the custom fields.

{mapping screenshot here}

8. Create an instance of the **ServiceNow v2 ** integration.
   1. Select **FW change management** as the incident type.
   2. Select the mapper that was created above.
   3. For the outgoing mapper, select the default **ServiceNow - Outgoing Mapper **.

{SNOW instance setting screenshot here}

9. In the Query section, enter a query to ensure the only change management incidents are fetched.

{query screenshot here}


10. Since it is important to documentation all the process in the playbook for future reference, if you are using the ServiceNow integration, make sure all the relevant mirroring settings are enabled (https://xsoar.pan.dev/docs/reference/integrations/service-now-v2#configure-incident-mirroring).


## Pack Workflow

After the playbook is triggered, the relevant logs are queried based on the parameters in the change request. The purpose of this action is to provide information to assist in deciding whether to approve or reject the request. If a ticketing system integration (ServiceNow or Jira)  is available, the logs are uploaded to the issue/incident and are linked to the Cortex XSOAR incident.
An email is sent to the security team asking them to approve or reject the change request. 

If the request is rejected, the issue/incident is closed with the relevant comments and the incident in Cortex XSOAR is closed.   


If the request is approved, the user receives an option to deploy the new policy in the development environment for testing before deploying it in the production environment. This option is configured in the playbook inputs.

If after testing in the development environment, the user decides to reject the change request, the issue/incident is closed with the relevant comments and the Cortex XSOAR incident is also closed.

If the user decides to approve the request, the request is forwarded to the **PAN-OS create or edit policy** playbook. This playbook is responsible for changing the existing policy. The playbook first checks which security policy matches the change request parameters. 

If there is no security policy that matches the request, a new policy is created. 

If there is a security policy that matches the request, the user can choose one of the following options: 
- Create a new hardening rule.
- Manually review the relevant rule.
- Edit the existing rule.

If the user chooses to edit the existing rule, the **PAN-OS edit existing policy** playbook is executed. This is a dedicated playbook for editing policies in PAN-OS and Panorama. A data collection form is sent to the users to retrieve the relevant details for editing the policy such as: element to change, element value, and the behavior.

After the execution of this playbook and the change in the policy, the request owner is required to validate the change. After the validation phase is completed, the issue/ticket is closed.


## Workflow documentation

As part of this pack’s workflow, all important decisions made during the change management are documented in Cortex XSOAR and mirrored to the issue\ticket in the ticketing system.


## What’s in this Content Pack?
  
### Playbooks

There are 5 playbooks in this pack.

- **Change Management for FW**

   This is the main playbook in the Change Management pack. This playbook can be triggered by 2 different options: 
   - ServiceNow
   - Jira

   The playbook guides you through all the critical stages in the process such as user request, request approval, testing, deployment, and validation. 

- **ServiceNow Change Management**

   This playbook is triggered by a fetch from ServiceNow. The playbook guides you through all the critical stages in the process such as user request, request approval, testing, deployment, and validation.

- **Jira Change Management**

   This playbook is triggered by a fetch from JIra. The playbook guides you through all the critical stages in the process such as user request, request approval, testing, deployment, and validation.

- **PAN-OS create or edit policy**

   This playbook automates the process of creating or editing a policy.

   The first task in the playbook checks if there is a security policy that matches the playbook inputs. If there is no security policy that matches the playbook inputs, a new policy will be created. If there is a security policy that matches the playbook inputs, the user will have the option to modify the existing policy or create a new hardened policy.   


- **PAN-OS edit existing policy**

   This playbook guides the user in the process of editing an existing policy. The playbook sends a data collection form to the user to retrieve the relevant parameters for editing the existing rule.

### Incident Fields
There are 5 incident fields in this pack.

- Source Networks
- Destination Networks
- Policy Actions
- Protocol Names
- Security Policy Match



### Incident Types

There is 1 incident type in this pack - **FW change management**.

### Automations
There is 1 automation - **IncidentState**.

This is a dynamic script that is used in the layout to display the incident state. The possible values are:

- Request Was Submitted
- Request Was Approved
- Request Was Rejected
- FW Policy Was Updated
- Awaiting Request Owner Validation





## Layout

This layout has three tabs.

- **Incident info tab**

| Layout sections | Description |
| --- | --- |
| Incident state | Displays the state of the incident. | 
| Security policy match | Displays the security policies that matched the change request parameters. |  
Change request details | The change request parameters. | 
Team members | A list of the analysts who participated in this incident. | 
| Decision | Filtering the decisions for the change management from the change request documentation. | 
| Change request documentation | Displays all the documented phases in the change management process. |  
| Work plan | Information regarding the playbook tasks from the Work Plan. | 
| Attachments | The firewall logs that were queried for the change request. | 
| Timeline information | Information regarding the incident timeline, such as: time occurred, last update, closed time, etc. | 
| Closing information | Information regarding the closing of the incident.| 




- **Jira tab**

| Layout sections | Description |
| --- | --- |
| Jira issue details | General details in the issue. | 
| Jira issue description | Jira issue description and summary. | 
| Jira Timeline | Jira issue timeline. | 
| Jira ticket members | The assignees to the issue in Jira. | 
| Jira attachments | Attachments in the Jira issue. | 
| XSOAR case details | Details on the incident in Cortex XSOAR | 
| Mirroring information | Mirroring setting information. | 
| Work plan | Information regarding the playbook tasks from the Work Plan. | 
| XSOAR linked incidents | Cortex XSOAR linked incidents that linked to the Jira mirrored incident. | 
| Notes | Comments entered by the user regarding the incident (mirrored with Jira).


- **ServiceNow tab**

| Layout sections | Description |
| --- | --- |
| Snow ticket status | Displays the ticket status.
| Snow ticketing handling | General information on the ticket handling. | 
| Snow ticket close notes | Displays information regarding the closure details. | 
| Snow ticket information | General information on the ticket. | 
| Snow ticket notes | Comments entered by the user regarding the incident (mirrored with ServiceNow). | 
| Attachments | Attachments in the ServiceNow ticket. | 


## Before You Start

This pack requires that you have an active instance of an email sender integration in order to send an email to the security/net-ops team for request approval and data collection tasks. If you do not have an active instance of an email sender integration, you will need to provide all the data collection tasks in the playbook flow manually.
 

## Pack Configuration  
                                       

To get up and running with this pack:

- In your relevant Panorama/PAN-OS instance for Change Management, set the **Firewall Change Management** as the incident type.  
- Configure the **Change Management for FW** playbook inputs (link to the playbook readme)
- Follow the steps in the [Playbook Triggers](#playbook-triggers) for the Jira or ServiceNow integration.
- Usage of an email sender integration is highly recommended for the pack workflow. 



## Testing the Pack

After you configure all the relevant settings that are mentioned above, Palo Alto recommends that you create a test incident (depending on the trigger that you created). Use real values that exist in your network, run the playbook, and verify that the flow that you chose runs as expected.     

## Pack Disclaimers
- Only a Panorama instance can edit Panorama rules. 
- Only a PAN-OS instance can edit PAN-OS rules.

- **PanoramaSecurityPolicyMatchWrapper** is a wrapper script for the ***panorama-security-policy-match*** command. The command receives multiple values for the *source*, *destination* and *destination-port* arguments and performs the policy match for each combination of the inputs. (Available from Cortex XSOAR 6.1.0).
For each input combination, the **PanoramaSecurityPolicyMatchWrapper** script creates a unique API call to verify which policy matches the inputs. For example, for the inputs:
Source:192.168.1.1,192.168.1.2  Destination:8.8.8.8, the script will create 3 API calls.
The default limit is 500 calls. You can modify the limit using the *limit* argument. 
