---
id: 
title: 
description: 
---

Shift management and shift handover are crucial processes of SOC team management.
This pack provides a single interface to communicate all essential elements to prevent loss of data in the shift handover process.

## Pack Workflow

When there is a shift change, a shift management incident is created. This incident can be created automatically through a [shift handover job](#create-a-shift-handover-job) that runs every time there is a shift change, or manually by the SOC manager or one of the analysts.

Before creating a new incident, you must configure the playbook inputs according to your needs and integrated apps. 

When creating a manual incident, make sure to select *shift handover* in the incident type selection section. The SOC manager can provide handover information in the *Shift manager briefing* field of the *Create Incident* form. If the SOC manager does not provide this information in the *Create Incident* form, then when the incident is created, an email is sent to the SOC manager requesting the briefing information. The email address of the SOC manager is configured in the playbook inputs.

After the incident is created, the **Shift Handover** playbook runs. The out-of-office list is updated with the names of the analysts for the incoming shift who are currently unavailable (for example, on PTO). A list of the available analysts is also created along with the list of active incidents. Pending incidents are not included in the list. The available analysts are assigned to the active incidents. 

The *Incident info* tab of the incident layout is populated with the following:
- List of active incidents and the analysts who are assigned to them.
- List of out-of-office analysts.
- SOC manager briefing instructions.

Analysts can retrieve details of their incidents by clicking the incidents assigned to them. Their incident opens in the incident dashboard.

In the incident layout, the SOC manager can create a channel in Slack or Microsoft Teams to send notifications to the analysts about an upcoming briefing session for the shift handover. The SOC manager can start the briefing session in Zoom by clicking *To start the meeting* link in the incident layout. Analysts can join the Zoom session by clicking the *To join the meeting* link.

## In This Pack

The Shift Management content pack includes several content items.

### Playbooks

* **Shift handover**
This is the main playbook of the shift handover. This playbook is used to set up shift handover meetings and provides details of the shift handover. By modifying the playbook inputs you can configure whether to activate the **Assign Active Incidents to Next Shift** sub-playbook.
You can run this playbook as a job a few minutes after the scheduled shift change occurs.

* **Assign Active Incidents to Next Shift**
This sub-playbook reassigns active incidents to the current users who are on call. 

* **Set a Shift handover meeting**
This sub-playbook creates an online meeting in the integrated app for shift handover. Currently this playbook supports Zoom.

### Automations

* [AssignToNextShiftOOO](https://xsoar.pan.dev/docs/reference/scripts/assign-to-next-shift-ooo): 
Reassigns the active incidents to the next shift. 
This automation works with the other out-of-office automations to ensure only available users are assigned to the active incidents.
The incident IDs of the active incidents should be passed as a comma-separated list.

* [AssignAnalystToIncidentOOO](https://xsoar.pan.dev/docs/reference/scripts/assign-analyst-to-incident-ooo): Assigns all on-call analysts to the active incidents. This automation will not assign users who appear in the out-of-office list. 

* [OutOfOfficeListCleanup](https://xsoar.pan.dev/docs/reference/scripts/out-of-office-list-cleanup):
Removes users from the out-of-office list whose *off until day* value has passed.   

* [ManageOOOusers](https://xsoar.pan.dev/docs/reference/scripts/manage-ooo-users): Gets all the out-of-office users. When you  first run the **ManageOOOusers** automation, an out-of-office list is created. This list manages the out-of-office users. By default, the name of this list is *OOO List*. We recommend that you use this list. However, if you create a list to use with a different name and if the name of the list does not begin with OOO, this script automatically prefixes OOO to the script name. For example, if you name the out-of-office list *newList*, the script will automatically change the name to *OOO newList*.  
Important: Do not delete this list!

* [TimeToNextShift](https://xsoar.pan.dev/docs/reference/scripts/time-to-next-shift): Gets the time until the next shift.

* [CreateChannelWrapper](https://xsoar.pan.dev/docs/reference/scripts/create-channel-wrapper): Creates a channel in Slack v2 or in Microsoft Teams. If both of them are available, it creates the channel in both Slack v2 and Microsoft Teams.

* [GetNumberofUsersOnCall](https://xsoar.pan.dev/docs/reference/scripts/get-number-of-users-on-call): Retrieves the number of users who are currently on call.

* [GetOnCallHoursPerUser](https://xsoar.pan.dev/docs/reference/scripts/get-on-call-hours-per-user): Retrieves the number of on call hours per user.

* [GetRolesPerShift](https://xsoar.pan.dev/docs/reference/scripts/get-role-per-shift): Retrieves the roles per shift.

* [GetUsersOOO](https://xsoar.pan.dev/docs/reference/scripts/get-users-ooo): Retrieves users who are currently out of office. The script use the **OutOfOfficeListCleanup** script to remove users whose *off until day* is in the past.

* [GetUsersOnCall](https://xsoar.pan.dev/docs/reference/scripts/get-users-on-call): Retrieves users who are on call.



### Incident Fields
There are 5 incident fields.
- **Out Of The Office**
- **Shift Manager Briefing**
- **Shift Open Incidents**
- **To Join The Meeting**
- **To Start The Meeting**

### Incident Types
There is 1 incident type - **Shift handover**.

### Layout
There is 1 layout - **Shift handover** 

There are 9 sections in the *Shift Handover* layout. The emphasis of this layout is the communication for the shift handover process - creating an online meeting, sending a notification in the integration app, displaying the SOC manager briefing, and the display of active incidents, on-call users, and out-of-office users.       

![Layout](LINK to image)

| Layout sections | Description |
|------------------ | ------------- |
| SOC shift manager briefing | SOC manager provided information for the new shift. This information can be provided manually when the incident is created, or by email if this section is left empty in the incident creation form.  |
| Shift open incidents  | Displays a table of all active incidents. This table includes the incident ID, incident name, incident owner, and a link to the incident. Pending incidents are not listed. |
| Messaging apps section | Action buttons to create a channel in the integrated app (Slack or Microsoft Teams), send a notification in the integrated app regarding the shift handover, and close the channel.  |
| Online meeting section | Links for starting and joining a meeting in Zoom for the remote shift handover. |  
| On call team members | Displays all team members who are on call. |  
| OOO team members | Displays a table of the out-of-office team members. The table includes the name of the user who is out of the office, the date until when the user is off, and the name of the person who added the user to the list. |  
| Attachments | The SOC manager can attach files for the shift handover. |
| To-Do tasks | You can create a task and due date and assign it to an analyst. |
| War Room entries | Displays the information that appears in the War Room in regards to this incident. |


### List

When you first run the **ManageOOOusers** automation, an out-of-office list called *OOO List* is created. This list manages the out-of-office users.
Do not delete this list.
We strongly recommend using the default list name (OOO List). If you change the name of the list, you will need to update the arguments in the *Shift handover* and **Assign Active Incidents to Next Shift V2** playbooks.



## Before You Start
This pack requires that you have an active instance of an mail sender integration in order to send an email to the SOC shift manager to provide a briefing if it wasn't provided in the incident creation form. Configure either the [Gmail integration](https://xsoar.pan.dev/docs/reference/integrations/gmail)  or both the [EWS Mail Sender](https://xsoar.pan.dev/docs/reference/integrations/ews-mail-sender) and [EWS V2](https://xsoar.pan.dev/docs/reference/integrations/ews-v2) integrations. If you do not activate an instance of the mail sender integration, the SOC shift manager briefing can only be provided when creating a manual incident. 

In addition, it is highly recommend to use the following messaging and communication apps to gain all the benefits from this pack:
- Zoom - for creating online meetings for remote shift handover.
- Slack/Microsoft Teams - integrate your messaging apps to improve your team communication in the handover process.

This pack also requires the following to be configured:

- [shift management](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/users-and-roles/shift-management.html). 
- An out of office [list](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/lists.html)

## Pack Configuration
To get up and running with this pack, you must do the following:
- [Configure Shift Handover playbook inputs](https://xsoar.pan.dev/docs/reference/playbooks/).
>**Important:** By configuring *Yes* for the **AssignActiveIncidentsToNextShift** playbook input, incidents will be reassigned to the on-call analysts.  

- [Create a Shift Handover Job](#create-a-shift-handover-job) to create an incident automatically through a scheduled task that runs every time there is a shift change (optional).

### Create a Shift Handover Job
Create a shift management handover job if you want an incident to be created automatically through a scheduled task that runs every time there is a shift change.

1. Navigate to **Jobs**.
2. Click **New Job**.
3. Select **Time triggered**. 
4. Configure the following job parameters.

| Parameter | Value |
| ----| ----|
| Name | Provide a name for this job. |
| Type | Shift handover |
| Playbook | Shift handover |
| Queue handling | Select **Don't trigger a new job instance**. |

5. Click **Create new job**.

## Testing the Pack
After you configure the integrations, test the pack to ensure that everything was configured correctly.

1. Go the **Shift Handover** playbook and edit the playbook inputs according to your integrated apps data (for example, your Slack channel name or the SOC manager email address).
2. Create a new incident and set Shift handover as the incident type. Fill the SOC manager briefing section (one word or short sentence will be enough).
3.Create the incident and open the *Incident info* tab of the incident layout.
4.Check that the SOC manager briefing you provided appears in the *SOC manager briefing* section. 
5. In the *Shift open incidents* section, check that all the active incidents was reassigned to on-call analysts.
6. If in the playbook inputs you provided your messaging app details (currently supports only Slack and Microsoft Teams):
   1. Click **Create channel** to create the channel.
   2. Click **Notify the team about the meeting** to send a notification to the on-call users.
   3. Click **Close channel** to close the channel. 
7. If you use Zoom and its integration is enabled, go to the online meeting section and start a meeting have someone join.
8. In the *On-call team members* section, make sure that all on-call users appear.
9. In the *OOO teams members* section, make sure that all out of the office team members appear. 
10. Run the **ManageOOOusers** automation and add for remove users from the OOO list. Go to **Settings > Lists > OOO list**, and make sure the users you add or remove appears in the list.
11. Create a new incident and set shift handover as the incident type. Leave the SOC manager briefing section empty. You should receive an email to the SOC manager email address that was provided in the playbook input (SOCManagerEmail). When the email received enter the URL of the incident in the email and create a reply (one word or short sentence will be enough). Verify that the reply appears in the SOC shift manager briefing section.
   
## Integrations

- Although these integrations are not included in the pack, either the Gmail or EWS Mail Sender integrations are required for the pack to be able to send to the SOC manager email request to provide a briefing for the team in case it wasn't provided when the incident was created.
To be able using the messaging apps section in the layout you will be needed to configure them as well:   
   - Gmail - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/gmail)
   - EWS Mail Sender - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/ews-mail-sender)
- Slack V2 -  [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/slack-v2)
- Microsoft Teams -  [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/microsoft-teams)

