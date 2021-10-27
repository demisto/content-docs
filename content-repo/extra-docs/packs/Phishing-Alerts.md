
---
id: Phishing Alerts
title: Phishing Alerts
description: The Phishing Alerts content pack uses out-of-the-box playbooks, to handle phishing alerts received by either your Email Security Gateway or SIEM products. 
---

 # Phishing Alerts #

Email Security Gateways produce a high amount of phishing alerts, which are different by the type, severity and handling process. It is important to address these alerts to identify campaigns, analyze their IoCs and protect the organization from any malicious payload that was delivered within them.


## In This Pack ##

The **Phishing Alerts** content pack contains several content items.
 
These content items enable you to retrieve, process and analyze email files and manage phishing alerts. The out-of-the-box items are robust enough to get started with but are easily customizable to fit your specific requirements.


### Playbooks
This pack contains a parent playbook that calls two sub-playbooks.
 
| Playbook | Description | Notes |
|---------------- | ------------- | ------------- |
| Phishing Alerts Investigation | This is the pack's parent playbook and is the default playbook for the **Phishing Alerts** incident type. YUse this playbook to investigate and remediate a potential phishing incident produced by either your Email Security Gateway or SIEM product. One of the playbook's main tasks is retrieving the original email file from your Email Security Gateway or Email Service Provider. The playbook response tasks take under consideration the initial severity, hunting results and also the existence of similar phishing incidents in XSOAR. No action will be taken without an initial approval given by the analyst using the playbook inputs. | Under the playbook inputs, you can add the SOC email address to send the notifications via email. |
| Phishing Alerts - Check Severity | This playbook is executed as part of the **Phishing Alerts Investigation** parent playbook and is responsible for calculating the incident severity and notifying the SOC via email if a sensitive mailbox has been detected.| - | 
| Get Email From Email Gateway - Generic | This playbook is executed as part of the **Get Original Email - Generic v2** sub-playbook, which is a sub-playbook of the **Process Email - Generic v2** playbook executed by the parent playbook. The playbook enables you to retrieve the eml/msg file saved in the Email Security Gateway. | -
 ---
 
## Incident Types ##

Phishing Alerts incident type.

### Incident Layouts
The incident type contains one layout: Phishing Alerts Layout

The **Phishing Alerts Layout** has one tab named **Investigation** with the following sections:
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

### 1. Configure an integration that produce phishing alerts and allows to fetch them
The main playbook in this pack relies on Email Security Gateways or SIEM phishing alerts. That means you must configure either one of them to use the pack.

Optional Email Security Gateway products:
* FireEye Email Security (EX)
* Proofpoint TAP
* Agari Phishing Protection
* Mimecast

Optional SIEM products:
* Splunk ES
* QRadar
 
 ### 2. Classification and Mapping  

To use the **Phishing Alerts Investigation** playbook we strongly recommend that you map the playbook for the relevant integration.

#### Email Security Gateway Mapping
1. Navigate to **Settings** > **Integrations** > **Classification and Mapping**.
2. Mark the checkbox of the relevant integration that you want to map.
3. Click **Duplicate**.
4. Click the copy you just created. 
5. From the *Incident Type* dropdown list, select **Phishing Alerts**.
6. From the *Select Instance* dropdown list, select the instance that you want to map.

   After selecting your instance the *Data fetched JSON* will be loaded.

7. Map the relevant fields from the JSON by selecting the keys and clicking **Choose data path**. To make this pack work, please map the following fields:

* Alert Action
* Email From
* Email To
* Email CC
* Email Subject
* Email Headers
* Email Message ID (The original email message id and not the internal product id)
* Email Internal Message ID (The product ID given to the message)
* Email Source Domain (Optional)
* Detection URL (Optional)
* Occurred
* Severity
* UUID (For the product internal message/alert id)

For information about creating a mapper, see [Create a Mapper](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-1/cortex-xsoar-admin/incidents/classification-and-mapping/create-a-mapper.html).

8. Click **Save Version**.
9. Navigate to **Settings** > **Integration** > **Servers & Services**.
10. Access the relevant integration instance setting and edit it as follows:
   - From the Incident Type dropdown list, select **Phishing Alerts**.
   - For the Mapper, select the mapper you created. 

#### SIEM Mapping
Repeat steps 1-6 as seen under "Email Security Gateway Mapping"
7. Choose carefully the right SIEM rule JSON to map.
8. Map the relevant fields from the JSON by selecting the keys and clicking **Choose data path**. To make this pack work, please map the following fields:

* Alert Action
* Email From
* Email To
* Email CC (Optional)
* Email Subject
* Email Headers (Optional)
* Email Message ID (The original email message id and not the internal product id)
* Email Internal Message ID (The product ID given to the message)
* Email Source Domain (Optional)
* Detection URL (Optional)
* Occurred
* Severity (Taken from the product or post SIEM calculation)
* UUID (For the product internal message/alert id)

For information about creating a mapper, see [Create a Mapper](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-1/cortex-xsoar-admin/incidents/classification-and-mapping/create-a-mapper.html).

8. Click **Save Version**.
9. Navigate to **Settings** > **Integration** > **Servers & Services**.
10. Access the relevant integration instance setting and edit it as follows:
   - From the Incident Type dropdown list, select **Phishing Alerts**.
   - For the Mapper, select the mapper you created. 

#### SIEM Classification

1. Navigate to **Settings** > **Integrations** > **Classification and Mapping**.
2. Mark the checkbox of the relevant integration that you want to classify.
3. Click **Duplicate**.
4. Click the copy you just created. 
5. From the *Select Instance* dropdown list, select the instance that you want to classify.
6. Choose carefully the SIEM rule JSON that you want to classify
7. Click the field you would like to classify by. (Rule name will be a good fit)
8. Under "Drag classifier values to the incident type on the right" drag the value of the field to Phishing Alerts incident type on the right.
8. Click **Save Version**.
9. Navigate to **Settings** > **Integration** > **Servers & Services**.
10. Access the relevant integration instance setting and edit it as follows:
   - For the Mapper, select the mapper you created in the previous step.
   - For the Classifier, select the classifier you created.


### 3. Playbook Inputs
---

| **Name** | **Description** | **Default Value** | **Required** |
| --- | --- | --- | --- |
| Role | The default role to assign the incident to. | Administrator | Required |
| SearchAndDelete | Enable the "Search and Delete" capability \(can be either "True" or "False"\).<br/>In case of a malicious email, the "Search and Delete" sub-playbook will look for other instances of the email and delete them pending analyst approval. | True | Optional |
| BlockIndicators | Enable the "Block Indicators" capability \(can be either "True" or "False"\).<br/>In case of a malicious email, the "Block Indicators" sub-playbook will block all malicious indicators in the relevant integrations. | False | Optional |
| AuthenticateEmail | Whether the authenticity of the email should be verified, using SPF, DKIM and DMARC. | True | Optional |
| OnCall | Set to true to assign only user that is currently on shift. Requires Cortex XSOAR v5.5 or later. | False | Optional |
| SearchAndDeleteIntegration | Determines which product and playbook will be used to search and delete the phishing email from users' inboxes.<br/>Set this to "O365" to use the O365 - Security And Compliance - Search And Delete playbook.<br/>Set this to "EWS" to use the Search And Delete Emails - EWS playbook. | EWS | Optional |
| O365DeleteType | The method by which to delete emails using the O365 - Security And Compliance - Search And Delete playbook. Could be "Soft" \(recoverable\), or "Hard" \(unrecoverable\). Leave empty to decide manually for each email incident.<br/>This is only applicable if the SearchAndDeleteIntegration input is set to O365. | Soft | Optional |
| O365DeleteTarget | The exchange location. Determines from where to search and delete emails searched using O365 playbooks. Use the value "All" to search all mailboxes, use "SingleMailbox" to search and delete the email only from the recipient's inbox, or specify "Manual" to decide manually for every incident. Note - searching all mailboxes may take a significant amount of time. This input is only applicable if the SearchAndDeleteIntegration input is set to O365. | SingleMailbox | Optional |
| SOCEmailAddress | The SOC email address to set in case the playbook handles phishing alerts. | demistoadmin@demisto.int | Optional |
| closeIfBlocked | Whether to close the investigation in cases where the email has already been blocked. | False | Optional |
| escalationRole | The role to assign the incident to if the incident severity is critical |  | Optional |
| blockedAlertActionValue | List of optional values the email security device returns for blocked\\denied\\etc. emails. | block, deny, denied, delete | Optional |
| allowedAlertActionValue | List of optional values the email security device returns for allowed\\passed\\etc. emails. | pass, allow, notify, notified | Optional |
| sensitiveMailboxesList | The name of a list that contains the organization's sensitive users. | lists.sensitiveMailboxesList | Optional |
| SearchThisWeek | Whether to search for similar emails in a week's time range or all time. | true | Optional |
| CheckMicrosoftHeaders | Check Microsoft's headers for BCL/PCL/SCL scores and set the "Severity" and "Email Classification" accordingly. | True | Optional |


## Pre-Process Rule

Knowing the Email Security Gateways produce a high amount of alerts, a customer can consider dropping alerts which has an action value of blocked/dropped alert.
To do so, please do the following:

#### Step 1 - Conditions for Incoming Incident
1. Navigate to **Settings** > **Integrations** > **Pre-Process Rules**.
2. Click **+ New Rule**.
3. Choose the rule name.
4. Click **+ Add Filter**.
5. Under **Choose an incident field** choose **Alert Action**, keep the **Equals** operator and under **Type a value** type the alert action to drop. e.g. block, drop.
6. Click **+ Add Filter**.
7. Under **Choose an incident field** choose **SourceBrand**, keep the **Equals** operator and under **Type a value** type the integration name that you fetch incidents from.

#### Step 2 - Action
1. From the drop-down list choose **drop**.

Click the **Save** button.
