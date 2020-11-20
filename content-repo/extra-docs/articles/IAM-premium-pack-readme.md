---
id: identity-lifecycle-management
title: Identity Lifecycle Management (ILM)
description: This Identity Lifecycle Management (ILM) pack enables you to provision users from Workday into Active Directory and/or Okta by performing CRUD operations. 
---


This Identity Lifecycle Management (ILM) pack enables you to provision users from Workday into Active Directory and/or Okta by performing CRUD operations. Read these instructions carefully to first understand the workflows that this pack executes and understand how it must be implemented..

## Workday Reports

HR uses Workday to manage CRUD operations for employees in the organization. It is standard practice for HR to generate reports for these CRUD operations. For example, running a weekly report that captures all new employees and terminated employees, or a daily report that captures updates to existing employee profiles (e.g., new mailing address or phone number).

Cortex XSOAR uses the Workday integration to fetch reports and create XSOAR incidents that correspond to the CRUD operation(s) in the report. For example, if you run a full report that includes 5 new employees, 3 terminated employees, and 10 employee profiles that were updated, 18 unique incidents would be created in XSOAR.

Each report has a unique URL, which you enter in the Workday Report URL instance parameters. If you want to fetch or run associated playbooks on multiple reports, each report will require its own integration instance.


The Workday integration creates an IAM-Sync-User incident for each user profile that is in the report.. This incident runs the IAM - Sync User playbook and provisions the user into the rest of the configured integrations. The playbook determines the CRUD (create, read, update, or delete/disable) operations that need to be done according to the data retrieved from the Workday report. 
For example, if a new employee joins the company, the playbook changes the incident type to IAM-New-Hire, and runs a Create operation across the supported IAM integrations. Similarly, if an employee is terminated in Workday, the playbook changes the incident type to IAM-Terminate-User, and a Disable operation runs in the supported IAM integrations. 

## Pack Workflows

The following table shows the supported Workday operations and their corresponding XSOAR commands, which are executed in the pack playbooks.

---

| Workday Operation | XSOAR Command |
|------------------ | ------------- |
| New user hire | iam-create-user |
| User update | iam-update-user |
| User termination | iam-disable-user |
| User rehire | iam-enable-user |  
 --- 

## Before You Start

The logic of the playbooks in the ILM pack, which determine how they execute, is determined by the employment data ingested from the Workday integration.

There are several custom fields that must be populated with specific values in order for the playbooks to execute the correct CRUD operations. If your current Workday instance does not include these fields and values, you will need to add them to the instance

The following table lists these fields, what they are used for in Cortex XSOAR, and the valid values the fields accept.

| Workday fields  |  How it is Used  | Possible Values |
| ------------ |---------------| -----|
| Email address      | A unique identifier for the user. | User's work email address | 
| Employment status |  Influences the playbook flow that will run on the User Profile incident.  | Active <br/> Leave of Absence <br/> Terminated
| Rehired employee  | Used to determine whether the User rehire flow is implemented. | Yes <br/> No |
| Prehire flag | Used in conjunction with the Rehired employee field to enable the User rehire flow. | True <br/> False|

- Make sure to obtain the URL where the Workday reports are hosted. Each report has a unique URL, which you enter as one of the integration instance parameters. If you want to fetch multiple reports, each report will require its own integration instance. 

- Ensure that you have a Mail sender integration for sending email notifications.

## Pack Configurations

Cortex XSOAR stores all of employee information as User Profile indicators. User Profiles have many fields out-of-the-box, which hold data about the employee. 

*Note* The User Profiles are initially created when the Workday integration fetches incidents. User profiles for users that are added to Workday after this initial fetch are created by the IAM-Sync User playbook. 

The User Profiles are constantly synchronized with Workday, so that when a change to a user comes from a Workday report, the integration creates an incident, triggering a change in the rest of the apps used in the organization, and updating the User Profile indicator.

This pack requires that you configure the following content items in the order listed.
Playbook configuration (inputs and outputs)
Indicator and Incident fields and mappers. You only need to configure these if you are adding custom fields.
Integration configurations
### Playbooks

1. IAM - Sync User
Under the inputs for the IAM-Sync- User playbook, make sure you configure values for the ITNotificationEmail and ServiceDeskEmail inputs. 

1. Navigate to *Playbooks* and locate that IAM - Sync User playbook.  
1. Click *Playbook Triggered* and insert values for the following inputs:
ITNotificationEmail - used to receive notifications about any errors in the provisioning process.
ServiceDeskEmail - used to receive initial temporary passwords for new hires to prepare employee laptops, etc.

### Fields and Mappers

The mappers that are provided out-of-the-box work with the assumption that you did not add any fields. 

If you want to add fields, follow the steps in the following Example section. 

1. Add the field to the mappers for the Workday, Okta, and Active Directory integrations. 

   **Note** To change the mappers, you will need to duplicate each mapper. 

   Ensure that you are adding the fields to the relevant incident types within each mapper.

   * for the Workday incoming mapper, add the field to the *IAM-Sync-User* incident type.
   * for Okta and Active Directory, add the field to the *UserProfile* incident type in both the incoming and outgoing mappers.

2. Reconfigure each integration to use the duplicated mappers you created.

#### Example

The following is an example of the flow when adding a field to work with the ILM content pack. This does not presume to cover all possible scenarios.

1.  Add an incident field.
    1. Navigate to Settings -> Advanced -> Fields and click *New Field*.
    1. Enter the name for the field and click the *Attributes* tab.
    1. Clear the *Add to all incident types* checkbox.
    1. In the *Add to incident types* drop-down, select the following:
	    - IAM - Sync User
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
    1. Select the layout to which you want to add the field, for example, *User Profile*, and click *Duplicate*.
    1. Click the User Profile_copy layout.
    1. In the *Library*, click *Fields and Buttons*, and drag the field you added above to the section in the layout in which you want it to appear. In this example, we have added the field to the *Personal and Contact Information* section.
    1. Save the layout. 
    1. Repeat this process for each of the other layouts in which you want the field to appear.

    ![Add Fields to Layout](../../../docs/doc_imgs/reference/ilm-add-fields-to-layout.png "Add Fields to Layout")

1. Map the new field in all of the mappers.
    1. Navigate to *Settings -> Integrations -> Classification and Mapping*.
    1. Select the mapper to which you want to add the field, for example, *IAM Sync User - Workday*, and click *Duplicate*. 
    1. Click *IAM Sync User - Workday_copy*.
    1. Under *Get data*, select the source from which you want to retrieve the sample data for mapping.
    1. Under *Select Instance*, select the instance of the selected source.
    1. Under *Incident Type*, select the relevant incident type, as follows:
        - for the Workday incoming mapper, add the field to the IAM-Sync-User incident type. 
        - for Okta and Active Directory, add the field to the UserProfile incident type in both the incoming and outgoing mappers.
    1. Map the field from the layout to the field in schema. For purposes of this example, we have mapped the Sample-Field-IAM field to the employee number.
    1. Repeat this process for each additional field and save the mapper. 
    1.  Repeat this process for all of the mappers. There are 5 in total:
        - Workday incoming mapper
        - Okta incoming and outgoing mappers
        - Active Directory incoming and outgoing mappers

    ![Map Fields](../../../docs/doc_imgs/reference/ilm-map-fields.png "Map Fields")

1. Configure the integration instances to use the new mappers.
    1. Navigate to *Settings -> Servers and Services* and select one of the integration instances for this pack. In our example, we are using Workday.
    1. In both *Mapper (incoming)* fields (one located under the *Incident type* field and one located under the *Use system proxy settings* checkbox) select the copy mapper that you created above. In our example, that would be **IAM Sync User - Workday_copy**. 

![Attach Mapper to Integration](../../../docs/doc_imgs/reference/ilm-attach-duplicate-mapper-to-integration.png "Attach Mapper to Integration")


### Integrations

1. Workday ILM integration (link to the integration docs).
*Note* Before running the Workday integration, ensure that you have added the fields in Workday as instructed in Before You Start.
1. IAM-compatible integrations. These integrations support execution of the generic ILM CRUD operations.

    - Workday - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/workday-iam)
    - Active Directory - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/active-directory-query-v2)
    - Okta - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/okta-iam)
