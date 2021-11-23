
---
id: identity-lifecycle-management
title: Identity Lifecycle Management (ILM)
description: This Identity Lifecycle Management (ILM) pack automates user provisioning by performing management operations like creating, updating, enabling or disabling users in applications used by the organization.
---


The Identity Lifecycle Management (ILM) pack enables 4 flows. 
- [User provisioning](#user-provisioning) - provision users from an HR system (Workday) into all supported applications used by the organization.
- [App sync](#app-sync) - sync users to applications based on app assignments in Okta.
- [Group sync](#group-sync) - sync user memberships in groups to applications based on group creations in Okta.
- [Group membership update](#group-membership-update) - update user permissions in applications based on their group memberships in Okta.

User provisioning can be used by itself, but it is a prerequisite for the App Sync, Group Sync, and Group Membership Update flows.

Read the instructions for each flow carefully to first understand the workflows that this pack executes and understand how it must be implemented. 


## User Provisioning

The ILM pack enables you to provision users from Workday into various applications such as Active Directory and/or Okta by performing management operations like creating, reading, updating, and deleting users.

### Workday Reports

HR uses Workday to manage operations for employees in the organization. It is standard practice for HR to generate a report for these maintenance operations. For example, running a weekly report that captures all new and terminated employees, or a daily report that captures updates to existing employee profiles (e.g., new mailing address or phone number).

Cortex XSOAR uses the Workday integration to fetch report updates and create XSOAR incidents that correspond to the management operation(s) in the report. For example, if you run a full report that includes 5 new employees, 3 terminated employees, and 10 employee profiles that were updated, 18 unique incidents would be created in XSOAR.

Each report has a unique URL, which you enter in the Workday Report URL instance parameters. If you want to fetch or run associated playbooks on multiple reports, each report will require its own integration instance.

### Fetch Incidents with Workday IAM Integration

Workday IAM integration creates incidents based on employee information included in the report such as the employee's hire date, termination date (or last day of work), prehire flag and more. Depending on the incident type, the *IAM - Sync User*, *IAM - Activate User In Active Directory* or *IAM - Deactivate User In Active Directory* playbook runs provisions and manages the employee users in all of the applications used by the organization, respectively.

We use the ***fetch-incidents*** command to detect changes in the report identifying the incident type. An execution of the ***fetch-incidents*** command behaves in one of the following ways:

#### Fetching Samples
Marking the *Fetch Samples* parameter will enable creating sample incidents for the first 5 entries from the report. Use this option to see how fields are mapped through *IAM Sync User - Workday* Incoming Mapper Editor for preliminary preparation for use, or in order to test the whole provisioning flow.
> <i>Note:</i> Avoid using the *Fetch Samples* parameter with a report containing real employee information.

#### First Sync
If *Sync user profiles on first run* parameter is checked, then in the first fetch, no incidents will be created, but only the User Profile indicators representing the active users in the report will be synced to XSOAR.

#### Workday Report Processing Cycle
After the first sync, the fetch command will start the report processing cycle:

At every first fetch of the cycle, the entire report entries are collected and stored in the *Last Run* object.
On each subsequent run of the command, a certain amount of entries will be processed (based on the *Fetch Limit* and the *Percentage of entries to process per fetch* parameters), and only the remaining entries will be stored for the next runs, until we finish processing all of the entries in the report. The processed entries, if containing changes, will cause incidents to be created, in one of the following types:
[IAM - New Hire](#iam---new-hire)
[IAM - AD User Activation](#iam---ad-user-activation) 
[IAM - Terminate User](#iam---terminate-user)
[IAM - AD User Deactivation](#iam---ad-user-activation)
[IAM - Rehire User](#iam---rehire-user)
[IAM - Update User](#iam---update-user)

When no more entries are left to process, we detect Orphan Users (i.e., active User Profile indicators with no corresponding Workday report entry) by collecting all User Profiles of employees with a non-disabled *AD Account Status*, from whom there is no record in Workday report. For all those users, an *IAM - Terminate User* incident is triggered.

### Possible Incident Types in Workday

#### IAM - New Hire
This incident type is detected for an active employee who hasn’t yet been synced to XSOAR.
An employee in a Workday report is considered active when all of the following apply:
- The *Employment Status* is not “Terminated”.
- The *Hire Date* is at most X days from today, where X is determined by the *Number of days before hire date to sync hires* parameter.
- They have a future deactivation date (either *Termination Date* or *Last Day of Work*, determined by the *Deactivation date field* parameter).

##### Partial Name Match
When a new hire is detected and its display name is already used by another User Profile, a *mergeduserprofile* attribute is added to the user profile and is later used in the *IAM - Sync User* playbook.

#### IAM - AD User Activation
This incident type is detected for an active employee synced to XSOAR with an *AD Account Status* field “Pending” who reached Y days before their hire date. (Y is determined by the *Number of days before hire date to enable Active Directory account* parameter.)

#### IAM - Terminate User
Detected for an employee with a Cortex XSOAR User Profile with an *AD Account Status* field different from “Disabled”, when one of the following changes occurs in the employee’s entry in Workday report:
- *Employment Status* is “Terminated” and *Prehire Flag* is False.
- Deactivation date field is a past date.

#### IAM - AD User Deactivation
This incident type is detected when a User Profile of an employee synced to XSOAR *AD Account Status* field is “Enabled”, but their actual hire date is in more than Y days. (Y is determined by the *Number of days before hire date to enable Active Directory account* parameter.)
This occurs when a new hire is already activated, but at the last moment, their hire date is postponed.

#### IAM - Rehire User
Detected for an employee with a Cortex XSOAR User Profile with an *AD Account Status* field “Disabled”, when one of the following changes occurs in the employee’s report entry:
- *Prehire Flag* is True and *Rehired Employee* is “Yes”.
- Deactivation date field was either removed from the entry or changed to a future date.

#### IAM - Update User
When any other employee information of an active employee who is synced to XSOAR is changed (surname, manager name, etc.), or when the User Profile’s *Force Sync* field is changed to True, this incident type is detected.
Whenever an update event is detected, an *olduserdata* attribute is added to the user profile data and is later used in IAM integrations in order to support username/email changes.


### Important User Profile Indicator Fields
- *AD Account Status* - can be “Enabled”, “Disabled” or “Pending” (after sync date but before activation date).
- *Is Processed* - indicates whether there is an active incident for this user profile. Only report entries of employees whose user profile’s *Is Process* field value is False, are processed (unless a new change in the report was detected).
- *Is Temporary User* - in the **IAM - Sync User** playbook, there are cases where a temporary User Profile is created and only after a manual action is taken (an admin approval) we decide whether to keep the User Profile or remove it. This field indicates those user profiles.
Unless a new change in the report is detected for such users, we don’t process them until a decision is made.
- *Source Priority* and *Source of Truth* fields - for Workday, defaults to “1” and “Workday”. Whenever there is an additional source of truth, the source with the lower Source Priority value gets the higher priority.
- *Conversion Hire* - a boolean field indicating whether this User Profile was originally mastered by another source of truth. When an employee is a conversion hire, even if their AD Account Status is “Enabled” and their Hire Date is in more than Y days (Y determined by the *Number of days before hire date to enable Active Directory account* parameter), we will not trigger an AD Deactivation incident for them.


### Playbooks

> <i>Note:</i> The playbooks provision user information into different applications. The integration instances used for those applications, and the exact action taken when provisioning those users is determined by a Cortex XSOAR list named *app-provisioning-settings*. This list needs to be created by the user before beginning the provisioning process. The list allows specifying which actions can happen on each instance, and whether every new employee should have a new user on that instance or it’s reserved to a group of select members. The list also allows specifying emails that should be notified about users being created, enabled and so on, in a certain instance.
The structure of the list should be in JSON format. For example:
[
  {
    "instance_name": "ExceedLMS",
    "create_user_enabled": false,
    "create_user_group": "All",
    "update_user_enabled": false,
    "disable_user_enabled": true,
    "create_user_email_notification_ids": "test1@paloaltonetworks.com,test2@paloaltonetworks.com",
    "enable_user_email_notification_ids": "test1@paloaltonetworks.com,test2@paloaltonetworks.com",
    "disable_user_email_notification_ids": "test1@paloaltonetworks.com,test2@paloaltonetworks.com"
  },
  {
    "instance_name": "OktaIAM-panw-test",
    "create_user_enabled": true,
    "create_user_group": "All",
    "update_user_enabled": true,
    "disable_user_enabled": true,
    "create_user_email_notification_ids": "test1@paloaltonetworks.com,test2@paloaltonetworks.com",
    "enable_user_email_notification_ids": "test1@paloaltonetworks.com,test2@paloaltonetworks.com",
    "disable_user_email_notification_ids": "test1@paloaltonetworks.com,test2@paloaltonetworks.com"
  }
]


#### IAM - Sync User

General explanation:
- The **IAM - Sync User** playbook determines the management operations (create, read, update, or delete/disable) that need to be done according to the data retrieved from the Workday report. 
For example, if a new employee joins the company, Workday will create an *IAM - New Hire* incident, and the playbook runs a Create operation across the supported IAM integrations. Similarly, if an employee is terminated in Workday, the incident type will be *IAM - Terminate User*, and a Disable operation runs in the supported IAM integrations.
- The **IAM - Activate User In Active Directory** playbook will run when an *IAM - AD User Activation* event is created. This incident is created for new or rehired employees, before the hire date or immediately, depending on the days configured in the Workday integration parameters.
- The **IAM - Deactivate User In Active Directory** playbook runs when the employee was already activated, but then the hire date was postponed.

Flow walkthrough:
Most changes in the HR system report will trigger an event that runs the **IAM - Sync User** playbook. This playbook creates, updates, enables or disables users in different applications. The playbook starts by searching for previous, duplicate incidents of the same type for the same users, and closes them if any were found.
Then, the playbook searches for a User Profile indicator that corresponds to the data coming from the HR system report. If a User Profile was not found in XSOAR, then in most cases the playbook will proceed with a new hire flow and create a new User Profile indicator, as well as provision all the user data from the report into the rest of apps.
However, in some cases, the employee name (also called “Display Name”) may already be taken. This can happen naturally, but can also be the result of a human error in the HR report. In that case, the playbook pauses and allows the user to decide what to do with the information from the report - should it provision a new account, should it update the conflicting account with the new information from the report, or should the playbook do nothing while the report is being fixed by HR? Based on the user’s decision, the playbook would continue with the provisioning process which will be described later.

If a User Profile indicator was found in the system, then 2 scenarios are possible: in most cases, the new information will be provisioned normally (terminate, update, etc). However, if the user’s email is changed, a different approach is required. Since XSOAR stores all User Profile indicators with their email as the indicator *value* which is a unique identifier, then in order to change a User Profile’s email, the deletion of the old User Profile and creation of a new one is required. The scenario in this case is detected automatically based on the information coming from the Workday integration.
If an email change was detected, a manual task allows an admin to approve or disapprove the change. Afterwards, the provisioning process continues.

After the above tasks are executed, the provisioning process begins. Depending on the incident type which is mostly detected in Workday, but may be changed depending on the situation (for example - a “new hire” with a partial name match turns out to be an update event for an existing user), a corresponding sub-playbook will run. The sub-playbooks are described below.

Finally, the playbook notifies about any instances that failed in the **IAM - Send Failed Instances Notification** playbook, and displays the provisioning data in the layout. If any instance failed, it creates an error and waits for the error to be fixed. Once the error is fixed, the playbook can be re-run safely, as the sub-playbooks will be able to determine which actions have already been executed successfully so as not to repeat them.

#### IAM - New Hire

Creates a new user using the ***iam-create-user*** command in the integration instances that are enabled and configured in the *app-provisioning-settings*, and have their *create_user_enabled* field in the list set to *true*, as well as the *create_user_group* field set to *all*.

Additionally, the playbook runs the **IAM - Create User In Active Directory** sub-playbook to create a new user in Active Directory with more custom steps required specifically for Active Directory.

Finally, the playbook runs the **IAM - Send Provisioning Notification Email** sub-playbook to notify the users configured in the *app-provisioning-settings* list about the provisioning process.

#### IAM - Update User

Updates the user using the ***iam-update-user*** command in the integration instances that are enabled and configured in the *app-provisioning-settings*, and have their *update_user_enabled* field in the list set to *true*.
Finally, the playbook runs the **IAM - Send Provisioning Notification Email** sub-playbook to notify the users configured in the *app-provisioning-settings* list about the provisioning process.

#### IAM - Terminate User

Determines the source of the termination based on the incident context generated by the Workday integration.
In most cases, a user will be simply disabled in the flow that will be described below.
However, 2 additional scenarios are possible:
1. The user is an “Orphan User” - this happens when the employee record is simply deleted from the HR system report. In that case, a manual task allows an admin to determine whether the user should  really be terminated or not.
2. The user was terminated involuntarily through the Okta integration - also known as “TUFE”. In that case, whether the user is currently active in Okta is checked. If the user is really disabled in Okta, the termination process proceeds normally. However, if the user is actually enabled in Okta, a manual task allows the admin to decide whether that termination was intentional or not, and if the user should be terminated or kept as is.
> In order to enable TUFE detection, it is required to fetch *user.lifecycle.deactivate* log events from Okta IAM, using the *Fetch Query Filter* parameter. In addition, a pre-process rule to drop non-TUFE events should be specified, e.g., drop all Okta IAM incident of type *IAM - Terminate User* by the actor who performed the operation.

After those checks, the termination process proceeds:

It disables the user using the ***iam-disable-user*** command in the integration instances that are enabled and configured in the *app-provisioning-settings*, and have their *disable_user_enabled* field in the list set to *true*.
Finally, the playbook runs the **IAM - Send Provisioning Notification Email** sub-playbook to notify the users configured in the *app-provisioning-settings* list about the provisioning process.

#### IAM - Rehire User

Enables the user using the ***iam-update-user*** command with the *allow-enable* argument set to *True*, in the integration instances that are enabled and configured in the *app-provisioning-settings*, and have their *enable_user_enabled* field in the list set to *true* and their *create_user_group* field set to *all*.

Additionally, the playbook runs the **IAM - Create User In Active Directory** sub-playbook to create or initialize an existing user in Active Directory.
Finally, the playbook runs the **IAM - Send Provisioning Notification Email** sub-playbook to notify the users configured in the *app-provisioning-settings* list about the provisioning process.

#### IAM - Create User In Active Directory

Based on the current status of the user in Active Directory, the playbook creates and/or initializes the user in Active Directory. Initializing the user consists of generating a password for the user dynamically, using a password generation script configured in the playbook inputs, and sending an email with the password to IT to prepare the laptop for the user, and to the user’s manager to provide that password to the user when their hire date arrives. At the end of the playbook, the User Profile's AD Account Status is set to *Enabled* if the user is already enabled, or to *Pending* if the user is pending activation (either immediately or on a future date). When the Workday integration sees this, it may decide whether the user needs to be activated or not.

#### IAM - Activate User In Active Directory

Based on whether the user exists in Active Directory or not, the playbook runs the **IAM - Create User In Active Directory** playbook or continues with the user activation process respectively.
The activation process starts by checking whether the hire date of the employee is a past date. If it’s a past date, the playbook allows an admin to decide whether the user should be activated or not. Otherwise, the playbook continues with the normal flow.
If the user should be activated, the playbook enables the user by using the ***iam-update-user*** command with the *allow-enable* argument set to *True*. If the user was enabled successfully, a welcome email is sent to them and to their manager (configured in the HR system report), and the User Profile’s AD Account Status is set to *Enabled* to signify that the user is now enabled in Active Directory.

#### IAM - Deactivate User In Active Directory
??Ido - add info here

#### IAM - Send Provisioning Notification Email**

Allows sending email notifications using a custom HTML template configured in an XSOAR list, for every user provisioned successfully. The recipients of the email are configured in the  *app-provisioning-settings*. This playbook is used in the **IAM - New Hire**, **IAM - Update User**, **IAM - Terminate User**, and **IAM - Rehire User** playbooks. This playbook is used in a loop to notify the correct stakeholder separately about every instance.

#### IAM - Send Failed Instances Notification

Sends an email notification to the email configured in the playbook inputs for every integration instance where provisioning fails and needs to be fixed. Uses a preconfigured HTML template for the email. This playbook is used in a loop in the **IAM - Sync User** playbook to send a separate email for every failed instance.

#### IAM - Custom User Sync, IAM - Custom Pre-provisioning, IAM - Custom Post-provisioning
Playbooks used as placeholders to allow the user to create custom steps before, during, or after the provisioning process, while being able to keep the existing system playbooks locked, thus being able to receive future updates.

### Before You Start - User Provisioning

The logic of the playbooks in the ILM pack, which controls how they execute, is determined by the employment data ingested from the Workday integration.

To start working with the **Workday** integration, download the **Workday** pack from Marketplace and configure the [Workday IAM](https://xsoar.pan.dev/docs/reference/integrations/workday-iam) integration.

There are several custom fields that must be populated with specific values in order for the playbooks to execute the correct management operations. If your current Workday instance does not include these fields and values, you will need to add them to the instance.

The following table lists these fields, what they are used for in Cortex XSOAR, and the valid values the fields accept.

| Workday fields  |  How it is Used  | Possible Values |
| ------------ |---------------| -----|
| Email address      | A unique identifier for the user. | User's work email address | 
| Employment status |  Influences the playbook flow that will run on the IAM - Sync User incident.  | Active <br/> Leave of Absence <br/> Terminated
| Rehired employee  | Used in conjunction with the prehire flag to determine whether a user should be rehired. | Yes <br/> No |
| Prehire flag | If True, indicates a pre-hire status of the employee (i.e., a future hire or rehire). | True <br/> False|
| Hire date | Used to determine when a user will be created for the employee. | Any date format is supported. <br/> The format should match the format chosen in the integration parameter. |
| Termination date / Last day of work | Used in conjunction with the prehire flag to determine whether a user should be terminated. | Any date format is supported. <br/> The format should match the format chosen in the integration parameter. |

- Make sure to obtain the URL where the Workday reports are hosted. Each report has a unique URL, which you enter as one of the integration instance parameters. If you want to fetch multiple reports, each report will require its own integration instance. 

- Ensure that you have a **Mail sender** integration for sending email notifications.

### Initial Sync and User Profiles

Cortex XSOAR stores all employee information as *User Profile* indicators. User Profiles have many fields out-of-the-box, which hold data about the employee. 

> <i>Note:</i> The User Profiles are initially created when Workday's ***fetch-incident*** command is executed for the first time and the *Sync user profiles on first run* parameter is checked. The profiles are created without triggering an incident. User Profiles for users that are added to Workday **after** this initial fetch are created by the **IAM - Sync User** playbook. This syncs all existing employees to XSOAR without running incidents for them, as they are already provisioned in the apps used by the organization.

The User Profiles are constantly synchronized with Workday, so that when a change to a user comes from a Workday report, the integration creates an incident, triggering a change in the rest of the apps used in the organization, and updating the User Profile indicator.

### Pack Configurations

This pack requires that you configure the following content items in the order listed.

1. Playbook configuration (inputs).
2. Indicator and Incident fields and mappers. You only need to configure these if you are adding custom fields which you want to store in Cortex XSOAR and/or provision into additional applications.
3. Integration configurations.

#### Playbooks

##### IAM - Sync User

Under the inputs for the **IAM - Sync User** playbook, make sure you configure values for the *ITNotificationEmail* and *ServiceDeskEmail* inputs.

1. Navigate to *Playbooks* and locate the **IAM - Sync User** and **IAM - Activate User In Active Directory** playbooks.  
2. Click *Playbook Triggered* and insert values for the following inputs, in both playbooks, where applicable:
    - *ITNotificationEmail* - used to receive notifications about any errors in the provisioning process.
    - *PasswordGenerationScriptName* - The name of the automation script that will be used to generate a random password for newly created Active Directory users. The default script used for this is GeneratePassword, but depending on your password complexity policy, you may or may not want to use it.
 
##### IAM - Activate User In Active Directory

Configure all of the playbook inputs according to the descriptions.

##### IAM - Create User In Active Directory

Configure the *ManagerEmailHTMLList*, *ServiceDeskEmailHTMLList*, *ADNotificationEmails*, *PasswordGenerationScriptName*, *ServiceDeskEmail*, and *SendEmail* inputs.

**Do not change or delete** the *CreatedIndicator*, *indicator*, *SuccessfulVendors*, and *sAMAccountName* inputs, as they are already configured to work in places where this playbook is used as a sub-playbook.

##### IAM - Deactivate User In Active Directory

Configure the *ITNotificationEmail* playbook input.

##### IAM - Group Membership Update
Configure all of the desired playbook inputs according to the descriptions.

##### IAM - Send Provisioning Notification Email

Configure the *NotificationEmailHTMLList* input if you want to use custom HTML templates for notifications about users that were provisioned successfully in the different applications.


### Integrations

- Workday IAM integration [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/workday-iam).

 > <i>Note:</i> Before running the Workday integration, ensure that you have added the fields in Workday as instructed in [Before You Start](#before-you-start).
- IAM-compatible integrations. These integrations support execution of the generic ILM management operations.

    - Active Directory - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/active-directory-query-v2)
    - Okta - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/okta-iam)
    - ServiceNow - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/service-now-iam)
    - GitHub - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/git-hub-iam)
    - Slack - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/slack-iam)
    - Salesforce - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/salesforce-iam)
  
    
> <i>Note:</i> If you choose to run any of the basic management operations, such as create, delete, etc. manually from the CLI, make sure to include the email and username fields in the user profile.


## App Sync

The app-sync feature provides automated app provisioning in applications (such as ServiceNow, GitHub, and Slack) for users created in Okta. App-sync consists of 2 main features:
- Create/Enable/Disable users in apps they are assigned to or unassigned from through Okta.
- Update users in apps when their information changes, either directly through Okta, or indirectly through a change in Workday which in turn updates the information in Okta and then in the rest of the apps.

### App Sync Process

The app-sync process starts when one of the following scenarios happens:
- A user is assigned/unassigned to an application in Okta.
- A user is part of a group that was assigned/unassigned to an application in Okta.
- The user's information changed in Okta, directly or indirectly (through an IAM - Update User incident).

The **Okta IAM** integration fetches the following Okta log event types and proceeds with the applicable flow:
* The *application.user_membership.add* / *application.user_membership.remove* Okta event results in *IAM - App Add* / *IAM - App Remove* incidents respectively, which run the **IAM - App Sync** playbook. The playbook uses the integration context (that is transparent to the user) of the Okta instance, which maps Okta App IDs to integration instances in Cortex XSOAR, in order to determine to which instance to sync the user. It then runs either the ***iam-update-user*** command with the *allow-enable* argument set to *True*, or the ***iam-disable-user*** command, depending on the detected incident type.
> <i>Note:</i>  The behavior for when a user account does not exist in the app is configurable through the relevant integration configuration. For example, if the user does not exist in the app to which they are assigned and the integration's *create if not exists* parameter is unchecked, then the command will be skipped. If the parameter is checked,- the account will be created. 

* The *user.account.update_profile* Okta event results in *IAM - App Update* incidents which run the **IAM - App Update** playbook. The playbook checks which apps the user is assigned to, and maps it to integration instances in Cortex XSOAR in which the user will be updated. The mapping is done using the integration context (that is transparent to the user) of the Okta instance, which maps Okta App IDs to integration instances in Cortex XSOAR, in order to determine which instance to update the user in. It then runs the ***iam-update-user*** command in all of the available instances of the apps to which the user is currently assigned.

Both the **IAM - App Sync** and **IAM - App Update** playbooks also update the applications that the user is assigned to in the User Profile indicator. To properly update the field and avoid race conditions, the playbooks use the Demisto Lock integration which gets a lock before updating the field, and releases the lock afterwards. This is used to allow only one incident to update the field at a time.


## Group Sync

This flow allows syncing user memberships in groups to applications based on group creations in Okta.

### Prerequisites
1. In Okta IAM *Fetch Query Filter* parameter, specify the "group.user_membership.add" and "group.user_membership.remove" event types, as well as all the relevant Okta group IDs. Example:
```
(eventType eq "group.user_membership.add" or eventType eq "group.user_membership.remove") and (target.id eq "00gfg6oa3f5GGUxTjLP0h7" or target.id eq "00g12il5v3GaoeRgD0h8")
```
2. Add the *app-group-sync-settings* list that is used later in the playbooks to determine which IAM instance should be used for given Okta group IDs. Example:
```
{
"instance_name": "Slack Sandbox",
    "okta_groups": [
      {
        "id": "00gfg6oa3f5GGUxTjLP0h7",
        "displayName": "Slack_Group"
      }
   ]
"instance_name": "OracleIAM_XSOAR",
    "okta_groups": [
      {
        "id": "00g12il5v3GaoeRgD0h8",
        "displayName": "Oracle_Group"
      }
   ]
}
```
3. Configure a recurring job for the **IAM - App Group Sync Trigger** playbook.

When an incident running the **IAM - App Group Sync Trigger** playbook is triggered, for each instance in the *app-group-sync-settings* list, an incident of type *IAM - App Group Sync* is created. This incident runs the **IAMAppProvisioningSyncGroup** automation for every group, in order to collect which users were added or removed from the Okta group and accordingly add or remove them from the corresponding group in the application, using the following generic commands:

| Group Command |  Description |
| ------------ |---------------|
| iam-create-group | Creates an empty group. |
| iam-update-group | Updates an existing group resource. |
| iam-delete-group | Permanently removes a group. |
| iam-get-group | Retrieves the group information, including members. |

### Supported Integrations

 Okta IAM - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/okta-iam)
 Slack IAM - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/slack-iam)
 Oracle IAM - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/oracle-iam)
 AWS IAM - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/aws---iam)



## Group Membership Update

The Group Membership Update feature provides automated provisioning of user permissions derived from Okta groups that the user is assigned to or unassigned from.


### Group Membership Update Process

The Group Membership Update process starts when a scenario of this type happens:
A user is added to the “Admins” group of the Smartsheet app in Okta → an *IAM - Group Membership Update* incident is created → the user receives the same permissions in the Smartsheet application itself.

When an *IAM - Group Membership Update* is fetched from Okta, the **IAM - Group Membership Update** playbook runs.
The playbook uses a Cortex XSOAR list called *app-provisioning-settings* that the user should create and configure.
It then fetches the current app assignments of the user in Okta. Then, in order to determine in which integration instance the user permissions need to be updated, the playbook looks for the instance name which corresponds to the Okta App ID in which the user has had their permissions change.
Afterwards, the playbook gets the User Profile indicator of the user and extends it with the additional information of the app. After asking for admin approval via email, the playbook either updates the new user information in the app, or continues without doing anything.
If the update fails for any reason, a user is assigned to the incident and an error is raised intentionally to stop the playbook execution and allow the user to fix the issue.


### Before You Start

Before using the app-sync feature with Okta, you need to perform the [initial synchronization of users from Workday into XSOAR User Profiles](#user-provisioning).

### Pack Configurations

To trigger the app-sync *IAM - App Add*, *IAM - App Remove* and *IAM - App Update* incident types, you need to configure an [Okta IAM integration](#okta-iam-integration) to fetch incidents. Before enabling the integration, create an [IAM Configuration](#iam-configuration) incident from which to make connections between Okta applications and IAM integration instances. When a user is added to or removed from a connected Okta application, XSOAR will call the relevant management command from its connected IAM instance in XSOAR.


#### Okta IAM Integration
Configure the following information in your Okta IAM integration instance.

| Field | Value | Notes |
| ---- | ----| ----|
| Classifier | Okta IAM - App Sync | Select this from the drop-down list and not the textbox configuration, where “User Profile - Okta (Incoming)” and “User Profile - Okta (Outgoing)” should be. |
| Mapper | Okta IAM - App Sync | Select this from the drop-down list and not the textbox configuration, where “User Profile - Okta (Incoming)” and “User Profile - Okta (Outgoing)” should be. |
|Query only application events configured in IAM Configuration | Checked/Unchecked | Select this option to let the integration fetch all supported event types. Unselect this only if you are sure you don't want to fetch specific Okta events.
| Fetch Query Filter | “eventType eq "application.user_membership.add" or eventType eq "application.user_membership.remove" or eventType eq "user.account.update_profile" | Only configure this if the *Query only application events configured in  IAM Configuration* parameter is unchecked. This allows you to manually specify which Okta event types to fetch. |
| Fetches incidents | Select this option. | |
| Automatically creates a user if not found in the update command | Select this option | |




#### IAM Configuration 

The app-sync process requires that you have a mapping of Okta App IDs to Cortex XSOAR integration instance names. This mapping allows you to decide what app assignments trigger the creation or removal of users in which instance.

For example, you may have an Okta App ID “0oau408dvkn96MwHc0h3” and want to map it to the **ServiceNow_Users_Instance1** integration so that every time a user is assigned to an app that has this App ID, a user will be created in ServiceNow using the generic IAM commands in Cortex XSOAR.

Configuring the app-sync settings is a one-time configuration that you can do using an out-of-the-box dedicated incident type. Create an incident of type *IAM - Configuration*, choose your Okta instance, and enter the Okta App names and your Cortex XSOAR integration instance names in the relevant fields.

![Okta IDs](../../../docs/doc_imgs/reference/ilm-configuration.png)


You can obtain the app integration instance name from the integration page in Cortex XSOAR:

![Instance Name](../../../docs/doc_imgs/reference/ilm-integration-instance.png)


By creating this incident and entering the app and instance information, a configuration will be saved in the integration context. This is transparent to the user. Once the configuration is set, the playbooks will use it automatically. Additionally, you will be able to use the ***okta-iam-get-configuration*** command to view the configuration at any time. If you ever decide to run the ***okta-iam-get-configuration*** command manually, make sure to use the *using* parameter with the correct instance name of Okta in which you made the configuration to receive the configuration that you're expecting.


#### IAM - App Sync & IAM - App Update playbooks
These playbooks contain error handling tasks where a user is assigned to review the incident if app-sync fails for any reason. You can assign a user to the incident using the playbook inputs. If you want, you can configure the *UserRoleToAssignForFailures*, *UserAssignmentMethod*, and *AssignOnlyOnCall* playbook inputs according to your needs. Otherwise, a user will be randomly assigned.

### Integrations

 Okta IAM - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/okta-iam)
 
 
 ## Advanced

### Playbooks
Throughout the playbooks, different advanced mechanisms are used to deal with edge-cases and to reflect certain data to the Workday integration which prevents excessive incidents from being generated. For example, when incidents fail or wait for user input, since Workday detects that the User Profile was not fully synced, it attempts to sync the data again, as the HR system report shows different information from that of the User Profile indicator. Although the Workday integration has a deduplication mechanism of itself, some cases are still not covered in it and require the playbooks to make some adjustments. Another example is Orphan Users where the incident fails for any reason in the middle of the termination process. Since the HR system report holds no record for that user, its normal deduplication mechanism of not creating additional users that had no new changes in the report does not work.

### *Is Processed* Indicator Field

Generally, incidents from the User Provisioning flow begin by setting the User Profile indicator’s *Is Processed* field to *True* - to signify that no new incidents should be created for that user unless something else changes in the HR system report.
For example, when an email/username change is detected, admin approval is required. During that time, Workday detects that the existing User Profile was not updated yet. To overcome this issue, a temporary User Profile indicator is created with the *Is Processed* field set to *True*, and holds the new data from the Workday report.
Towards the end of the provisioning process, the User Profile’s *Is Processed* field is set to *False*.

### Temporary User Profiles

As mentioned previously, in email/username change scenario, a temporary User Profile is created. Temporary User Profiles are User Profiles for which a decision whether to keep them or delete them has not yet been determined, so they do not necessarily represent a real user in the system. If the admin decides to proceed with the change, the existing User Profile indicator has to be deleted, and a temporary User Profile becomes the new one (because the unique indicator value is the employee’s email address). At the end of the provisioning process, the User Profile is set to appear as non-temporary.

### Merged User Profile 
When a partial name match is detected in the Workday integration, the **IAM - Sync User** playbook detects that the ${incident.userprofile} key in the context, which is the key that holds the new data to provision both to the User Profile indicator and to the rest of the apps, contains a *mergeduserprofile* key. That key holds data that combines the detected User Profile with the new information from the HR system report.
If the admin decision was to overwrite the existing account then in order to ensure that the existing user is updated, the playbook takes the email and username from the *mergeduserprofile* key, and sets them in the email and username incident fields respectively, which are later used to search for the existing, conflicting User Profile in XSOAR and then to update that user. Also, according to the AD Account Status of the existing user - the incident type is changed.

### AD Account Status 
The AD Account Status generally represents the current status of the account in Active Directory. In addition to being *Enabled* or *Disabled*, there will be cases where the AD Account Status is also empty - which means that the status has not yet been determined, for example, if a playbook started execution and has not yet determined the new status, resetting the AD Account Status is a measure taken to ensure that the Workday integration performs the wrong operation (activation/deactivation) of the user, as it is already being handled.
Also, it’s important to note that when a user is terminated (gone through the *IAM - Terminate User* flow) then the AD Account Status will be shown as *Disabled*. However, if the user was hired and had their hire date postponed, the user will simply go through an AD Deactivation flow (rather than full termination flow), and their AD Account Status will be changed to *Pending*, as they are actually pending a new activation, and were not really terminated.


### Fields and Mappers

The mappers that are provided out-of-the-box work with the assumption that you did not add any fields. 

The following provides a general idea of how to include additional information in the user profile indicator, and provision it to your available IAM applications. The [Example](#example) below provides detailed instructions for adding a field to work with the ILM content pack.

1. Add the field to the mappers for Workday, Okta, Active Directory, and for any other IAM integration configured. 

   > <i>Note:</i> To change the mappers, you will need to duplicate both the incoming and outgoing mappers. 

   Ensure that you are adding the fields to the relevant incident types within each mapper.

   * For the Workday incoming mapper, add the field to the *IAM - Sync User* incident type.
   * For Okta and Active Directory, add the field to the *UserProfile* incident type in both the incoming and outgoing mappers.
   
        > <i>Note:</i> As part of the configuration of the Active Directory mapper, you must map a value to the OU (organizational unit) required field. To do this, create a transformer that maps a user attribute of your choice to an OU value.
   
   * For GitHub, the relevant mappers are in the *IAM-SCIM* pack and can be used in any integrations that uses SCIM.


2. Reconfigure each integration to use the duplicated mappers you created.

#### Example

The following is an example of the flow when adding a field to work with the ILM content pack. This example does not presume to cover all possible scenarios.

1.  Add an incident field.
    1. Navigate to **Settings** > **Advanced** > **Fields** and click *New Field*.
    1. Enter the name for the field and click the *Attributes* tab.
    1. Clear the *Add to all incident types* checkbox.
    1. In the *Add to incident types* drop-down, select the following:
        - User Profile
	    - IAM - Sync User
	    
	    You can also add the following incident types if you would like to display the new field in the incident layout (the new fields will be shown regardless in the User Profile indicator).
	    - IAM - New Hire
	    - IAM - Update User
	    - IAM - Terminate User
	    - IAM - Rehire User
    1. Click *Save*.

    ![Create Incident Field](../../../docs/doc_imgs/reference/ilm-create-new-incident-field.png "Create Incident Field")

1. Add an indicator field.
    1. Change the field type to *Indicator*.

       ![Show Indicator Fields](../../../docs/doc_imgs/reference/ilm-toggle-indicators.png "Show Indicator Fields")

    1. Click *New Field*. 
    1. Give the same name as you entered for the Incident field. In this example, we have used Sample-Field-IAM.
    1. Click the *Attributes* tab.
    1. Clear the *Add to all incident types* checkbox.
    1. In the *Add to incident types* drop-down, select the User Profile indicator type. 
    1. Click *Save*. 

    ![Create Indicator Fields](../../../docs/doc_imgs/reference/ilm-create-indicator-field.png "Create Indicator Fields")

1. Add the fields to the respective layouts.
    1. Navigate to *Settings -> Advanced -> Layouts*.
    1. Select the incident or indicator layout to which you want to add the field, for example, *User Profile*, and click *Duplicate*.
    1. Click the User Profile_copy layout.
    1. In the *Library*, click *Fields and Buttons*, and drag the field you added above to the section in the layout in which you want it to appear. In this example, we have added the field to the *Personal and Contact Information* section.
    1. Save the layout. 
    1. Repeat this process for each of the other layouts in which you want the field to appear.
    1. Go to *Indicator Types*, select the User Profile indicator type, click edit and then change the layout to the new layout you have just created.

    ![Add Fields to Layout](../../../docs/doc_imgs/reference/ilm-add-fields-to-layout.png "Add Fields to Layout")

1. Map the new field in all of the mappers.
    1. Navigate to *Settings -> Integrations -> Classification and Mapping*.
    1. Select the mapper to which you want to add the field, for example, *IAM Sync User - Workday*, and click *Duplicate*. 
    1. Click *IAM Sync User - Workday_copy*.
    1. For the incoming mapper:
       1. In the Playground, run the ***!get-mapping-fields*** command.
       1. Locate the results for you integration.
       1. Click **View full JSON in a new tab**.
       1. Click **Download as a file**. The file will be downloaded to your Downloads folder.
       1. Copy only the attributes/values of the *User Profile* field of the downloaded JSON file, and save it in a separate JSON file. 
       1. Under *Get data*, select **Upload JSON** and upload the saved JSON file.
    1. For the outgoing mapper:
        1. Under *Get data*, select the source from which you want to retrieve the sample data for mapping.
        2. Under *Select Instance*, select the instance of the selected source.
    3. Under *Incident Type*, select the relevant incident type. 
        - for the Workday incoming mapper, add the field to the *IAM - Sync User*, *IAM - New Hire*, *IAM - Rehire User*, *IAM - Update User* and *IAM - Terminate User* incident types. 
        - for Okta, Active Directory, ServiceNow, GitHub and the rest of the IAM integrations, add the field to the UserProfile incident type in both the incoming and outgoing mappers.
    1. Map the new field you have created to the field in the schema. For purposes of this example, we have mapped the Sample-Field-IAM field to the employee number.
    1. Repeat this process for each additional field and save the mapper. 
    1. Repeat this process for all of the mappers. For example:
        - Workday incoming mapper
        - Okta incoming and outgoing mappers
        - Active Directory incoming and outgoing mappers
        - ServiceNow incoming and outgoing mappers
        - GitHub that uses the IAM-SCIM incoming and outgoing mappers
    ![Map Fields](../../../docs/doc_imgs/reference/ilm-map-fields.png "Map Fields")

1. Configure the integration instances to use the new mappers.
    1. Navigate to *Settings -> Servers and Services* and select one of the integration instances for this pack. In our example, we are using Workday.
    1. In both *Mapper (incoming)* fields (one located under the *Incident type* field and one located under the *Use system proxy settings* checkbox) select the copy mapper that you created above. In our example, that would be **IAM Sync User - Workday_copy**. 

![Attach Mapper to Integration](../../../docs/doc_imgs/reference/ilm-attach-duplicate-mapper-to-integration.png "Attach Mapper to Integration")

 
## Demo Video
<video controls>
    <source src="https://github.com/demisto/content-assets/raw/master/Assets/xsoar.pan.dev/IAM__Full_Demo.mp4"
            type="video/mp4"/>
    Sorry, your browser doesn't support embedded videos. You can download the video at: https://github.com/demisto/content-assets/raw/master/Assets/xsoar.pan.dev/IAM__Full_Demo.mp4 
</video>


## Troubleshooting

##### Why are my new fields not shown in the layout?
Make sure of the following: 
* You've created an incident field **and** an indicator field with the exact same name.
* The incident fields are associated to the IAM incident types, and the indicator fields are associated to the User Profile indicator type, as described in the Fields and Mappers section. 
* The fields are mapped in the Workday mapper under all the relevant incident types
* The mapper configured in the Workday integration is the correct one.
* The fields were added to the layout where you want them to appear
* The incident types were configured to use the new layout that you've created

##### Why are incidents not being created from Workday?
There could be several reasons for this:
* The integration is being run for the first time, at which point only the initial user sync is run - which is when the User Profile indicators are created as described in the "Initial Sync & User Profiles" section.
* You keep resetting the last run timestamp in the Workday integration while "Sync user profiles on first run" option in the Workday integration configuration is checked. You should not reset the last run timestamp or you should uncheck that option if you've already performed the initial sync.
* Your Workday report is missing required fields. Please refer to the table in the "Before You Start - User Provisioning" section and make sure that the report holds all of those fields for every employee.
* Nothing has changed in the Workday report since the initial sync, so there is nothing to provision.

##### Why are duplicate incidents being created?
There could be several reasons for this:
* There were changes to an employee in the Workday report, but the employee's incident in XSOAR failed before updating the User Profile indicator of that employee. As long as there is a discrepancy between the Workday report and the User Profile indicator, the Workday integration will keep trying to update it. Search for the incident of the employee and fix the cause of error. Then - the next incident should complete and no duplicate incidents should follow.
* The field is missing in one of the incident types in the Workday mapper

##### Why does user creation fail in Active Directory?
There could be several reasons for this. Inspect the error message in the Process Details tab to understand why the creation failed. If you cannot determine the cause of the error, make sure that:
* You've added a transformer script which determines the OU where the user will be created, in the Active Directory outgoing mapper, in the User Profile incident type and schema type, under the "ou" field.
* You're using LDAPS in the Active Directory (port 636) integration.
* You've specified a password generation script in the *IAM - Activate User In Active Directory* playbook inputs, under the *PasswordGenerationScriptName*, and that script complies with your domain's password complexity policy.

##### Why am I getting unwanted IAM - App Update incidents?
You may have rules configured in Okta which automatically update user information for every new user. If you want to have those updates provisioned to the rest of the apps, you will need to follow the process of adding additional fields under the "Advanced" section.

