
---
id: phishing-campaign
title: Phishing Campaign
description: How to detect and manage phishing campaigns in Cortex XSOAR using the Phishing Campaign Content Pack.
---

# Phishing Campaign #

The Phishing Campaign pack enables you to find, create and manage phishing campaigns. A phishing campaign is a collection of phishing incidents that originate from the same attacker, or as part of the same organized attack launched against multiple users.

As phishing campaigns are a number of phishing incidents that are similar to each other, it is important to detect and create the links between them, and look at them as a whole, rather than spend time investigating each incident separately. To see how to set up a phishing incident generally in Cortex XSOAR, go to the [Phishing Use Case Tutorial](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-tutorials/tutorials/phishing-use-case.html).


### How It Works

 The following flow chart describes the architecture of phishing campaigns in Cortex XSOAR:

![image](https://user-images.githubusercontent.com/43602124/124762458-97eeb480-df3b-11eb-9479-2214037befea.png)

Included in this content pack is the **Detect & Manage Phishing Campaigns** playbook. Use this playbook in the [Phishing - Generic v3](https://xsoar.pan.dev/docs/reference/playbooks/phishing---generic-v3), or use it in your custom phishing playbook. As part of the phishing incident, the playbook does the following: 
 - Finds and links related incidents to the same phishing attack (a phishing campaign).
 - Searches for an existing Phishing Campaign incident or creates a new incident for the linked Phishing incidents.
 - Links all detected phishing incidents to the Phishing Campaign incident that was found or that was previously created.
 - Updates the Phishing Campaign incident with the latest data about the campaign, and also updates all related phishing incidents to indicate that they are part of the campaign.



## In This Pack ##

The **Phishing Campaign** content pack contains several content items.

### Automations ###

- **FindEmailCampaign Automation**

  The **FindEmailCampaign** automation iterates over previous and existing phishing incidents. By using machine learning, it is able to detect similar phishing incidents. The incidents may be deemed similar if the email subject or email body have textual similarities. The automation outputs the data to the context, which contains details about the incidents that were found to be part of the campaign, as well as populating into incident fields, summary information about the campaign.

  The automation can also be customized to meet different criteria (if your email information is mapped into different fields, if your incident type has a different name, or if the similarity by which incidents are searched is too lenient or too strict). It can run to detect phishing campaigns, but to fully utilize it to detect and manage campaigns, use the [**Detect & Manage Phishing Campaigns**](https://xsoar.pan.dev/docs/reference/playbooks/detect--manage-phishing-campaigns) playbook. 
- **IsIncidentPartOfCampaign Automation**
 
  The **IsIncidentPartOfCampaign** automation takes the list of incidents detected as similar by the **FindEmailCampaign** automation, and checks whether one of them is already linked to a Phishing Campaign incident. If so, it outputs the ID of that incident so that all the similar phishing incidents can be linked to it. This automation finds whether there is an existing campaign incident or whether a new incident needs to be created.

- **SetPhishingCampaignDetails Automation**
The **SetPhishingCampaignDetails** automation updates the Phishing Campaign incident that was found, or was just created by the playbook, with new information outputted from the **FindEmailCampaign** script.
Specifically, if the current phishing incident is not already in the context of the Phishing Campaign incident, it will add that incident along with its data. It will also update the similarities of all the Phishing incidents that are part of that Phishing Campaign incident, relative to the incident that was *created* last.

**Note:** The last created incident is not necessarily the last incident that updated the Phishing Campaign. This is due to the nature of phishing campaigns, where multiple phishing incidents are typically processed at the same time. This behavior in managed through a lock mechanism which ensures that the incidents are processed synchronously (one by one). However, it cannot be guaranteed that the first ingested incident will be the first to acquire the lock and the first to be processed, since different incidents may take different amount of time to reach the Detect & Manage Phishing Campaigns subplaybook.

## Playbooks ##

[**Detect & Manage Phishing Campaigns**](https://xsoar.pan.dev/docs/reference/playbooks/detect--manage-phishing-campaigns)

The **Detect & Manage Phishing Campaigns** playbook uses the **FindEmailCampaigns** automation to detect phishing campaigns. 

If incidents belonging to a campaign are detected, the playbook checks whether the incidents are already linked to a Phishing Campaign incident. If so, the currently investigated incident is also added to that campaign incident. If not, a new Phishing Campaign incident is created, and all similar incidents are linked to it.

In addition, as the **FindEmailCampaign** automation runs on the current phishing incident, the playbook takes the context and incident fields set by the automation, and updates the Phishing Campaign incident with that data, so that it contains the most up to date information about the phishing incidents.

The playbook marks all the similar Phishing incidents as incidents belonging to the detected Phishing Campaign incident. It sets the **Part Of Campaign** incident field in the phishing incidents, with the ID of the phishing campaign incident:

![image](https://user-images.githubusercontent.com/43602124/127866753-93e7ce42-2c11-474e-b492-0fb07dc751db.png)



## Incident Types ##

Phishing Campaign incident type

## Incident Fields

- Actions on Campaign Incidents
- Campaign Close Notes
- Campaign Duration
- Campaign Email Body
- Campaign Email Subject
- Campaign Email To
- EmailCampaignSnippets
- EmailCampaignCanvas
- EmailCampaignMutualIndicators
- EmailCampaignSummary
- Is Phishing Campaign
- Part of Campaign
- Select Campaign Incidents
 

## Layouts

After the **Detect & Manage Phishing Campaigns** runs and finds a phishing campaign, the Phishing incident continues to run as usual. In the **Investigation** tab of the incident, you can see a link to the **Phishing Campaign** incident. This incident enables the analyst to view the incident as part of a phishing campaign and take action.



![image](https://user-images.githubusercontent.com/43602124/123551826-0a150b80-d77c-11eb-91ed-3325016d6935.png)

The **Phishing Campaign Incident** layout contains the following additional tabs:

**Campaign Overview** tab

  Gives the analyst an overview of the different elements of the campaign:
  
  ![image](https://user-images.githubusercontent.com/53567272/128185701-12025b48-0a2b-4e38-b4eb-c7c96fe285f6.png)

The Campaign Overview tab consists of dynamic sections. These sections are based on the context inside the Phishing Campaign incident. It uses the context to dynamically fetch information from the related Phishing incidents and display aggregated data in the Phishing Campaign incident.

The context is managed through the Detect & Manage Phishing Campaign playbook, and should not be modified manually.

  |Layout Section| Description |
  |--|--| 
  |Campaign Summary| Includes information about the phishing incidents that make up the campaign. Some fields display the number of phishing incidents (in parenthesis) in which every detail of the campaign was observed.|
  |  Campaign Snippet| View a short version of how the campaign email looks like. |
  | Mutual Campaign indicators| Mutual indicators from the phishing incidents that make up the campaign.![image](https://user-images.githubusercontent.com/53567272/126163317-4be821ce-4a86-46d0-8d69-dd377b01b350.png)|
  | Dynamic sections| On the right hand side, you can see important  information about the campaign incidents, such as **Highest Severity**, **Unique Senders**, **Campaign Duration**, etc. **NOTE:** If any of the dynamic sections are empty, it's because the context is missing. This is due to running the **FindEmailCampaign** automation, without the necessary `fieldsToDisplay` arguments, or without setting the context to the **Phishing Campaign** incident. This should work out of the box if the **Detect & Manage Phishing Campaigns** playbook is used.|
  | Campaign Canvas| From Cortex XSOAR v6.1, a canvas of the campaign is supported, which can be accessed through the canvas section:![image](https://user-images.githubusercontent.com/43602124/125288084-68b6b980-e326-11eb-99c0-19e1b7b6af8c.png)|

**The Campaign Management tab**

Enables the analyst to take batch actions:

![image](https://user-images.githubusercontent.com/43602124/127522742-811dceb8-5b8c-4a26-a01b-d2dff272dff4.png)
    
|Layout Section| Description |
|--|--|
|Similar Incidents| Similar phishing incidents are displayed.  The columns are the same incident fields in the `fieldToDisplay` input in the [Detect & Manage Phishing Campaign](https://xsoar.pan.dev/docs/reference/playbooks/detect--manage-phishing-campaigns) playbook, so analysts can decide what to see about their related incidents.|
|Notify Recipients| Analysts can select which incident, recipients, etc, to send an email.  The recipients from the incidents are auto-populated in the **Campaign Email To** field. Analysts can write an email and send it to the recipients directly from the layout.|
|Incident Actions| The related incidents can be linked (occurs automatically by default in the playbook), unlinked, closed and reopened. The user can also self-assign incidents in batch ("Take Ownership" action).|

## Before You Start ##
### Required Content Packs
- Phishing Campaign (this pack)
- Phishing
- Cortex Lock
- Base
- Common Playbooks
- Common Scripts
- Common Types

## Pack Configuration

Customize the playbook by changing the inputs of the  [Detect & Manage Phishing Campaigns](https://xsoar.pan.dev/docs/reference/playbooks/detect--manage-phishing-campaigns) playbook. All of the playbook inputs customize the execution of the **FindEmailCampaign** automation.
In addition, the Demisto Lock integration should be configured to ensure that duplicate Phishing Campaign incidents are not created for the same campaign.
