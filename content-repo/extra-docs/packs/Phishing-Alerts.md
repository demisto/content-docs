---
id: Phishing-Alerts
title: Phishing Alerts
description: The Phishing Alerts content pack uses out-of-the-box playbooks to handle phishing alerts received by either your Email Security Gateway or your SIEM. 
---

 # Phishing Alerts #

Email Security Gateways produce a high amount of phishing alerts, which differ according to type, severity, and handling process. It is important to address these alerts to identify campaigns, analyze their IoCs, and protect the organization from any malicious payload that was delivered within them.

`Note`: For the Phishing use case, see the [Phishing Investigation - Generic v3 playbook](https://xsoar.pan.dev/docs/reference/playbooks/phishing---generic-v3).

## In This Pack ##

The **Phishing Alerts** content pack contains several content items.
 
These content items enable you retrieve, process and analyze email files, and manage phishing alerts . The out-of-the-box items are robust enough to get you started, but are easily customizable to fit your specific requirements.


### Playbooks
This content pack contains a playbook and one sub-playbook.
 
| Playbook | Description | Notes |
|---------------- | ------------- | ------------- |
| Phishing Alerts Investigation | This is the main playbook and the default playbook for the **Phishing Alerts** incident type. Use this playbook to investigate and remediate a potential phishing incident fetched from either your Email Security Gateway or through your SIEM. One of the playbook's main tasks is to retrieve the original email file from your Email Security Gateway or Email Service Provider. <br/> The playbook's tasks include assessing the initial severity, processing results, and assessing the existence of similar phishing incidents in Cortex XSOAR. <br/> No action is taken without an initial approval by the analyst using the playbook's inputs. | Under the playbook inputs, you can add the SOC email address to send the notifications via email. |
| Phishing Alerts - Check Severity | This sub-playbook is executed as part of the **Phishing Alerts Investigation** playbook. It calculates the incident severity and notifies the SOC via email if a sensitive mailbox has been detected.| - | 

 ---
 
## Incident Types ##

The **Phishing Alerts** incident type.

## Incident Layouts
The **Phishing Alerts** incident type includes the **Phishing Alerts Layout**.

The **Phishing Alerts Layout** contains one **Investigation** tab, with the following sections:
- Email Basic Information: Email Message ID, Sender Recipient, etc.
- Email Text
- Email Headers
- Email HTML Image
- Email Attachments
- Raw Email HTML
- URL Screenshots
- Email Authenticity Information
- Critical Assets
- Indicators

 
## How to Use the Pack
To use this pack, you need to configure several integrations and map and classify your Email Security Gateway or SIEM incidents.

### Before You Start

There are several items that you must install and configure before you start using this pack.

### 1. Configure the integration 
You need to configure both the integration which fetches phishing alerts and the one that holds the original email or a copy of that email. 

**In order to fetch incident you should use:**
* Email Security Gateway
* SIEM phishing alert

**In order to retrieve the original email (eml/msg) file you should use:**
* Email Security Gateway
* Email Service Provider

**The following are the currently supported products for each phase:** 
 
 **Email Security Gateway products:** [Fetch alerts/Retrieve email files]
 * FireEye Email Security (EX) (Fetch alerts + Retrieve email files)
 * FireEye Central Management (CM) (Fetch alerts)
 * Proofpoint TAP (Fetch alerts)
 * Proofpoint Protection Server (Retrieve email files)
 * Agari Phishing Defense (Fetch alerts)
 * Mimecast (Fetch alerts + Retrieve email files)

**SIEM products:** [Fetch alerts]
 * Splunk ES 
 * QRadar

**Email Service Providers:** [Retrieve email files]
 * EWS v2
 * Microsoft Graph Mail
 * Gmail

**Note: If the Email Security Gateway doesn't hold a copy of the original email, you have to configure the Email Service Provider as well.**

### 2. Classification and Mapping  

To use the **Phishing Alerts Investigation** playbook you need to map the playbook for the relevant integration. If using a SIEM you also need to map the classifier.

1. **Email Security Gateway/SIEM Mapping** 
   1. Navigate to **Settings** > **Integrations** > **Classification and Mapping**.
   2. Mark the checkbox of the relevant integration that you want to map
   3. Click **Duplicate**.
   4. Click the copy you just created.
   5. In the **Incident Type** field, select **Phishing Alerts**.
   6. In the **Select Instance** field list, select the instance from which you want to map. 
      After selecting your instance, the data fetched from your instance appears.
   7. Map the following fields from the JSON by selecting the keys and clicking **Choose data path**: 

      * Alert Action
      * Email From
      * Email To
      * Email CC
      * Email Subject
      * Email Headers
      * Email Message ID (The original email message id and not the internal product id)
      * Email Internal Message ID (For the product internal message/alert id)
      * Email Queue ID
      * Email Source Domain (Optional)
      * Occurred
      * Severity <br/> For information about creating a mapper, see [Create a Mapper](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-admin/incidents/classification-and-mapping/create-a-mapper.html).

   8. Click **Save Version**.

2. **SIEM Classification**.
   
   1. Navigate to **Settings** > **Integrations** > **Classification and Mapping**.
   2. Mark the checkbox of the relevant integration that you want to classify.
   3. Click **Duplicate**.
   4. Click the copy you just created. 
   5. From the **Select Instance** dropdown list, select the instance that you want to classify.
   6. Choose carefully the SIEM rule json that you want to classify
   7. Click the field you would like to classify by (For example, Rule name).
   8. Under "Drag classifier values to the incident type on the right" drag the value of the field to Phishing Alerts incident type on the right.
   9. Click **Save Version**.
3.  **Add the Mapper and Classifier (if relevant) to the Incident Type.**
       1. Navigate to **Settings** > **Integration** > **Servers & Services**.
       2.  Access the relevant integration instance setting and edit it as follows:
           - In the **Incident Type** field, select **Phishing Alerts**.
           - (SIEM only) In the  **Classifier** field, select the classifier you created. 
           - In the **Mapper (incoming) field**, select the mapper you created. 


### 3. Phishing Alerts Investigation Playbook Inputs
---

| **Name** | **Description** | **Default Value** | **Required** |
| --- | --- | --- | --- |
| Role | The default role for which to assign the incident. | Administrator | Required |
| SearchAndDelete | Whether to enable the "Search and Delete" capability. Can be either: "True" or "False".<br/> In case of a malicious email, the "Search and Delete" sub-playbook looks for other instances of the email and deletes them pending analyst approval. | True | Optional |
| BlockIndicators | Whether to enable the "Block Indicators" capability. Can be either: "True" or "False".<br/> In case of a malicious email, the "Block Indicators" sub-playbook blocks all malicious indicators in the relevant integrations. | False | Optional |
| AuthenticateEmail | Whether the authenticity of the email should be verified, using SPF, DKIM and DMARC. | True | Optional |
| OnCall | Set to true to assign only user that is currently on shift. Requires Cortex XSOAR v5.5 or later. | False | Optional |
| SearchAndDeleteIntegration | Determines which product and playbook is used to search and delete the phishing email from users' inboxes.<br/> Set this to "O365" to use the O365 - Security And Compliance - Search And Delete playbook.<br/>Set this to "EWS" to use the Search And Delete Emails - EWS playbook. | EWS | Optional |
| O365DeleteType | The method by which to delete emails using the O365 - Security And Compliance - Search And Delete playbook. Could be: "Soft" (recoverable), or "Hard" (unrecoverable\). Leave empty to decide manually for each email incident.<br/>This is only applicable if the SearchAndDeleteIntegration input is set to O365. | Soft | Optional |
| O365DeleteTarget | The exchange location. Determines from where to search and delete emails searched using O365 playbooks. Use the values: <br/> - "All" to search all mailboxes, <br/> - "SingleMailbox" to search and delete the email only from the recipient's inbox, <br/> - "Manual" to decide manually for every incident. <br/> Note - searching all mailboxes may take a significant amount of time. This input is only applicable if the SearchAndDeleteIntegration input is set to O365. | SingleMailbox | Optional |
| SOCEmailAddress | The SOC email address to set in case the playbook handles phishing alert. | | Optional |
| escalationRole | The role to assign the incident to if the incident severity is critical |  | Optional |
| blockedAlertActionValue | List of optional values the email security device returns for blocked, denied, etc, emails. | block, deny, denied, delete | Optional |
| sensitiveMailboxesList | The name of a list that contains the organization's sensitive users. | lists.sensitiveMailboxesList | Optional |
| SearchThisWeek | Whether to search for similar emails in a week's time range or all time. | true | Optional |
| CheckMicrosoftHeaders | Check Microsoft's headers for BCL/PCL/SCL scores and set the "Severity" and "Email Classification" accordingly. | True | Optional |

### 4. Process Email - Generic v2 Playbook Inputs
Process Email - Generic v2 is one of the main sub-playbooks being executed in the **Phishing Alerts Investigation** playbook. You need to consider the  **EmailBrand** input.

#### EmailBrand

When this value is used, only the relevant playbook runs. Possible values:
- Gmail
- EWS v2
- MicrosoftGraphMail
- EmailSecurityGateway. The value executes the following (if enabled):
  - FireEye EX (Email Security)
  - Proofpoint TAP
  - Agari Phishing Defense
  - Mimecast<br/>

If none of the above values are supplied, all of the playbooks run. This input sets the way the original email file is retrieved. <br/>If you would like to retrieve the email (eml/msg) file directly from your Email Security Gateway, you should use the **EmailSecurityGateway** value as input, otherwise, if you would like to retrieve the email file from your **Email Service Provider**, choose one of the relevant providers values as input.


## Pre-Process Rule

As Email Security Gateways produce a high amount of alerts, consider blocking/dropping alerts using a [pre-process rule](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/6.11/Cortex-XSOAR-Administrator-Guide/Create-Pre-Process-Rules-for-Incidents). 



1. Select **Settings** > **Integrations** > **Pre-Process Rules** > **+ New Rule**.
2. Choose rule name.
3. In the **Conditions for Incoming incident** section, click **+ Add Filter**.
4. In the **Choose an incident field**, select **Alert Action**, keep the **Equals** operator, and in the **Type a value** field, type the alert action to drop. e.g. block, drop.
5. Click **+ Add Filter**.
6. Under **Choose an incident field**, select **SourceBrand**, keep the **Equals** operator and in the  **Choose a value** field, type the integration name that you fetch incidents from.
7. In the **Action** section, select **drop** from the drop-down list.
8. Click **Save**.
