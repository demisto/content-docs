---
id: email-communication
title: Email Communication
description: Communication across and between departments is a vital component of collecting information, and managing and remediating security events. The Email Communication content pack enables security teams to automate and streamline the communication and notification process with users across your organization via email.
 
---
This Email Communication pack enables security teams to reply to an email as part of an incident. The SOC team is able to communicate directly through the Cortex XSOAR platform as part of the remediation process. 




## Pack Workflow
When an email is sent to the email address configured in your email integration, your email listener fetches the incoming email in Cortex XSOAR. 

If the email is in response to an existing incident, an 8-digit number will appear next to the subject of the email, for example <93075875> Incident1.

The pre-process script searches for '#' followed by an incident id, for example, #1234, in the subject of the email to link to the incident. 

If there is no 8-digit number in the subject of the email or if the pre-process rule is unable to locate the 8-digit number, a new incident is created and a random 8-digit number is generated for the incident. 

If there is a 8-digit number in the subject of the email, and the pre-process rule is able to locate the incident associated with the 8-digit number, the email is added to the existing email thread and not as a separate unlinked email. 

You can view the email thread in the War Room or in the incident layout. You can also reply to the email thread in the incident layout. 


 


## In This Pack
The Email Communication content pack includes several content items.

### Automations
There are 3 Automations in this pack.
* [DisplayEmailHtml](https://xsoar.pan.dev/docs/reference/scripts/display-email-html): Displays the original email in HTML format in the incident layout.

* [PreprocessEmail](https://xsoar.pan.dev/docs/reference/scripts/preprocess-email): Pre-process script for Email Communication layout. This script checks if the incoming email contains an 8-digit number to link the mail to an existing incident, and tags the email as "email-thread". 

* [SendEmailReply](https://xsoar.pan.dev/docs/reference/scripts/send-email-reply): Sends the email reply. 

### Classifiers
There are 6 Classifiers in this pack. When you configure an instance of the Gmail integration, EWS V2 integration or MS Graph Mail integration, use the following classifiers.

* **EWS - Classifier - Email Communication**:  Classifies EWS email messages.
* **EWS - Incoming Mapper - Email Communication**:  Maps incoming EWS email message fields. 
* **Gmail - Classifier - Email Communication**:   Classifies Gmail email messages. 
* **Gmail - Incoming Mapper - Email Communication**: Maps incoming Gmail email message fields.
* **MS Graph Mail - Classifier - Email Communication**:   Classifies MS Graph Mail email messages. 
* **MS Graph Mail - Incoming Mapper - Email Communication**: Maps incoming MS Graph Mail email message fields.

### Incident Fields
There is 1 incident field - **Add CC To Email**. 

### Incident Types
There is 1 incident type - **Email Communication**.

### Layout
There is 1 layout - **Email Communication** 

There are 3 interactive sections in which you can specify 1 or more email addresses to add as a CC to the email, create the body of the email, and add attachments. The remaining 3 sections are for viewing the original email and all the email communications and attachments associated with the incident.



![Layout](https://raw.githubusercontent.com/demisto/content/84e7bc89c8757544804540e6711d4b9aba210ec1/Packs/EmailCommunication/doc_files/Email_Communication_layout.png)

You can use the layout as-is for email communication. It can also be used for new email incident types by adding the **Email Communication** layout to an incident type. See [Add the Email Communication Layout to an Incident Type](#add-the-email-communication-layout-to-an-incident-type) for details. 
 
>**Important:** 
- In order to add CC recipients or an attachment to the email reply, you must select the *Show empty fields* checkbox. 
- You must customize the *service_mail* parameter in the **Send Reply** button with the mailbox from which emails are sent. See [Customize *service_mail* Parameter in the **Send Reply** Button](#customize-*service_mail-parameter-in-the-**send-reply**-button).


| Layout sections | Description |
|------------------ | ------------- |
| Add CC to email | Add 1 or more CC recipients to the email as a comma-separated list of email addresses.  |
| Message body | Write the body of the email reply. It is sent as an email and added to the War Room entry. |
| Attachments | Add attachments to the email reply.  |
| Email thread | Displays the entire email thread including the original email and all email replies. |  
| Original Email HTML | Displays in HTML format the original email that opened the incident. |  
| Mail Attachments | Displays the metadata of the email attachments. Contains the Send Reply button.  |  
 ---

> Note: If an email cannot be sent to a specified address, no notification will appear in Cortex XSOAR.
 
## Before You Start

This pack requires that you must have active instances of both a mail listener and mail sender integration in order to send and receive emails, and an active instance of the Demisto REST API integration. Configure either the [Gmail integration](https://xsoar.pan.dev/docs/reference/integrations/gmail) or the [MS Graph Mail integration](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-mail) or both the [EWS Mail Sender](https://xsoar.pan.dev/docs/reference/integrations/ews-mail-sender) and [EWS V2](https://xsoar.pan.dev/docs/reference/integrations/ews-v2) integrations. In addition, configure the Demisto REST API integration which requires a Demisto API key.



 
The out-of-the-box classification and mapping (for EWS ,Gmail and MS Graph Mail) in the pack map the incident data to custom incident fields.
Those custom incident fields are populated with specific values for the Email Communication scripts to execute.
 
If an EWS or Gmail or MS Graph Mail instance is already configured for other incident types, create a new instance for the email communication type with the associated classification and mapping. 
 

 


 
## Pack Configurations
To get up and running with this pack, you must do the following: 
- [Configure Demisto REST API Integration](#demisto-rest-api-integration)
- [Create a pre-process rule that will link the emails to an existing incident](#pre-process-rule).
- [Add the Email Communication Layout to an Incident Type](#add-the-email-communication-layout-to-an-incident-type).
- [Configure the *service_mail* parameter](#configure-the-*service_mail*-parameter).

### Demisto REST API Integration
The scripts in the pack require that you install the **Demisto REST API** integration and configure an integration instance.

1. In Cortex XSOAR, go to **Settings > INTEGRATIONS > API Keys**.
2. Click the **Get Your Key**, enter a name for the API key, and click **Generate Key**.
3. **(IMPORTANT)** Copy and save the API key, you will not be able to access it again.
4. Go to **Settings > INTEGRATIONS > Servers & Services** and search for **Demisto REST API**.
5. Click **Add instance** and enter the required information.
    - A meaningful name for the integration instance
    - Demisto Server URL
    - API key that you generated
7. Click the **Test** button to make sure that that server and API key are reachable and valid.
8. Click **Done**.

### Pre-Process Rule
 
This pack requires that you configure a pre-process rule to link the email communications with the incident. (The email reply will be linked to the same incident and will not create a new one). To configure the pre-process rule:

1.  Navigate to **Settings -> Integrations -> Pre-Process Rules**. 
2.  Click **New Rule**.
3.  Enter a name for the rule.
1. In the Conditions for Incoming Incident section, enter the following:  
**Type** - **Equals** - **Email Communication**. 
2. If you are using a Gmail instance, you should add another condition:  
**Email Labels** -  **Doesn't Contain** - **SENT**.
3. In the Action section, select: **Run a script**.
4. In the Choose a script section, select: **PreprocessEmail**.
5. Click **Save**.


![Preprocess-rule](https://raw.githubusercontent.com/demisto/content/84e7bc89c8757544804540e6711d4b9aba210ec1/Packs/EmailCommunication/doc_files/pre-process-rule.png)

See [(pre-processing rules)](https://demisto.developers.paloaltonetworks.com/docs/incidents/incident-pre-processing) for additional information.
 
### Add the Email Communication Layout to an Incident Type
 
The following adds the Email Communication layout to a new incident type. If you add this layout to an existing incident type it will override the current layout.

#### For XSOAR version 5.5
1. Create a new incident type.
    1. Navigate to **Settings -> Advanced -> Incident Types** and click **New Incident Type**.
    2. Enter the name for the new incident type.
    2. Click **Save**.
2. Add the Email Communication layout as a tab to the layout for an incident type.
     1. Navigate to **Settings -> Advanced -> Incident Types** and select the incident type.
     2. Click **Edit Layout**.
     2. Click **Copy Layout** and choose the **Email Communication** layout.
     3. Click **Save**.

#### For XSOAR version 6 and above
**Add the layout to a new incident type**

1. Navigate to **Settings -> Advanced -> Incident Types** and click **New Incident Type**.
2. Enter the name for the new incident type.
2. Select the **Email Communication** layout.
3. Click **Save**.


**Add the layout to an existing incident type**
  1. Navigate to **Settings -> Advanced -> Incident Types**.
  2. Select the incident type to which you want to add the layout, click **Edit** and choose the **Email Communication** layout.
  3. Click **Save**.

**Edit the layout for an existing incident type**  
To edit a layout, you must duplicate the layout and then edit the copy.
  1. Navigate to **Settings -> Advanced -> Layouts**.
  2. Select the layout you want to edit and click **Duplicate**.
  3. Click the duplicate layout.
  4. From the Library, select **Tabs** and search for **Email Communication**.
  5. Drag and drop the Email Communication tab on the layout's tabs.
  5. Click **Save**.


### Configure the *service_mail* Parameter 
The *service_mail* parameter contains the sender's email address. This parameter is optional.

The **SendEmailReply** script runs the ***reply-mail*** command and all the supported integrations send the email. 
If the *service_mail* parameter is empty and only one mail sender integration is configured, an email will be sent from the email address configured in the integration. If several integrations are configured, an email will be sent from each integration (not for each instance).

You can configure the *service_mail* parameter for the following uses:
- Send the email from one default email address - If multiple email-sender integrations or instances are configured, you can configure the *service_mail* parameter to a default sender email address.
- Send the emails from a different sender each time - This is particularly useful for MSSPs when the sender address changes per customer, incident type, etc. You can configure the parameter to be *mandatory*, so each time you click **send reply** in the layout, a pop-up will appear in which you will need to enter the service_mail email address.

![EmailCommunication_PopUp](https://raw.githubusercontent.com/demisto/content-docs/9ee7e60da13af63c323b67d3c6673110ded60faa/docs/doc_imgs/reference/EmailCommunication_PopUp.png)
		
#### To configure the service_mail parameter
1. Navigate to **Settings -> Advanced -> Automation**.
2. Select the *SendEmailReply* automation and click the three vertical dots and select the **Detach Automation** option.
3. Click **Detach** in the message that appears.
4. In the *Script Setting* dialog box, expand the *Arguments* section. 
5. Expand the *service_mail* argument and do one of the following:
   - To send the email from one default email address: In the *Initial value* field, enter the email address from which emails are sent.
   - To send the email from a different sender each time: Mark the *mandatory* checkbox and leave the *Initial value* empty.
![EmailCommunication_ServuceMailSettings](https://raw.githubusercontent.com/demisto/content-docs/9ee7e60da13af63c323b67d3c6673110ded60faa/docs/doc_imgs/reference/EmailCommunication_ServuceMailSettings.png)
6. Click **Save**.
7. Click the three vertical dots and select the **Reattach Automation** option.


## Testing the Pack
After you configure the integrations and the pre-process rule, create an incident type and add the Email Communication layout to an incident type. Now test the pack to ensure that everything was configured correctly.
1. Send an email to the email address configured in your email listener integration.
2. Go to the Incidents page and check that an incident was created.
3. Click the incident. 
4. In the Email Communication layout create and send a reply to the email. 
5. Refresh the page and see that your reply appears in the Email Thread section.
6. Reply to the reply email sent from Cortex XSOAR and verify that your reply email was added to the email thread.



## Integrations

Although these integration are not included in the pack, either the Gmail or both the EWS Mail Sender and EWS V2 integrations are required for the pack to work. In addition, configure the Demisto REST API integration.
- Gmail - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/gmail)
- EWS Mail Sender - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/ews-mail-sender)
- EWS V2 - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/ews-v2)
- MS Graph Mail - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-mail)
- Demisto REST API

## Demo Video
<video controls>
    <source src="https://github.com/demisto/content-assets/raw/9285feda43d336f68082d4931452bdd9cc38d889/Assets/EmailCommunication/EmailCommunication_demo.mp4"
            type="video/mp4"/>
    Sorry, your browser doesn't support embedded videos. You can download the video at: https://github.com/demisto/content-assets/blob/9285feda43d336f68082d4931452bdd9cc38d889/Assets/EmailCommunication/EmailCommunication_demo.mp4
</video>

