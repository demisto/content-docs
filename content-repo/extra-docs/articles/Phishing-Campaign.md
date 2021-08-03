---
id: phishing-campaign
title: Phishing Campaign
description: How to detect and manage phishing campaigns in Cortex XSOAR using the Phishing Campaign Content Pack.
---


## Phishing Campaign

A phishing campaign is a collection of phishing incidents that originate from the same attacker, or as part of the same organized attack launched against multiple users.

As phishing campaigns are a number of phishing incidents that are similar to each other, it is important to detect and create the links between them, and look at them as a whole, rather than spend time investigating each incident separately. To see how to set up a phishing incident generally in Cortex XSOAR, go to the [Phishing Use Case Tutorial](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-tutorials/tutorials/phishing-use-case.html).

To detect and manage phishing campaigns in Cortex XSOAR, go to **Marketplace** and install the **Phishing Campaign** Content Pack. 

### How It Works

The following flow chart describes the architecture of phishing campaigns in Cortex XSOAR:

![image](https://user-images.githubusercontent.com/43602124/124762458-97eeb480-df3b-11eb-9479-2214037befea.png)

The **Phishing Campaign** Content Pack contains the following content:

 - Phishing Campaign incident type
 - Phishing Campaign layout
 - Phishing Campaign incident fields
 - `Detect & Manage Phishing Campaigns` playbook
 - `FindEmailCampaign` automation

The `FindEmailCampaign` automation iterates over previous and existing phishing incidents. By using machine learning, it is able to detect similar phishing incidents. The incidents may be deemed similar if the email subject or email body have textual similarities. The automation outputs the data to the context, which contains details about the incidents that were found to be part of the campaign, as well as populating into incident fields, summary information about the campaign.

The automation can also be customized to meet different criteria (if your email information is mapped into different fields, if your incident type has a different name, or if the similarity by which incidents are searched is too lenient or too strict). It can run to detect phishing campaigns, but to fully utilize it to detect and manage campaigns, use the `Detect & Manage Phishing Campaigns` playbook. 

The `Detect & Manage Phishing Campaigns` playbook uses the `FindEmailCampaigns` automation to detect phishing campaigns. If incidents belonging to a campaign were detected, the playbook checks whether the incidents are already linked to a Phishing Campaign incident. If so, the currently investigated incident is also added to that campaign incident. If not, a new Phishing Campaign incident is created, and all similar incidents are linked to it.

In addition, since the `FindEmailCampaign` script ran on the current phishing incident, the playbook takes the context and incident fields set by the `FindEmailCampaign` automation, and updates the Phishing Campaign incident with that data too, so that it contains the most up to date information about the phishing incidents.

Finally, the playbook marks all the similar Phishing incidents as incidents belonging to the detected Phishing Campaign incident. It sets the **Part Of Campaign** incident field in the phishing incidents, with the ID of the phishing campaign incident:

![image](https://user-images.githubusercontent.com/43602124/127866753-93e7ce42-2c11-474e-b492-0fb07dc751db.png)

This context key is used in the phishing incident>Investigation tab>dynamic section, which informs the analyst that the incident is part of a phishing campaign, and provides a quick link to the related campaign:

![image](https://user-images.githubusercontent.com/43602124/123551826-0a150b80-d77c-11eb-91ed-3325016d6935.png)


### Detect & Manage Phishing Campaigns Playbook Configuration 

Customize the inputs of the `Detect & Manage Phishing Campaigns` playbook to detect and manage phishing campaigns.  All of the playbook inputs customize the execution of the `FindEmailCampaign` automation.

You may leave the following configurations with their default value, or change them according to your needs:

|Name| Description  |
|--|--|
|`AutomaticallyLinkIncidents`| Ensures that campaign detection and linkage is correct. Default is `true`. It is recommended not to change the default. 
| `incidentTypeFieldName` |  The name of the incident field in which the incident type is stored. Change this argument only if you're using a custom field for specifying the incident type. Default is `type`.|
|`incidentTypes`|  A comma separated list of incident types by which to filter phishing incidents. By default, the value is `Phishing` because phishing incidents use the **Phishing** incident type out of the box. Specify `None` to search through all incident types. |
| `existingIncidentsLookback` | The date from which to search for similar phishing incidents. Date format is the same as the query in the **Incidents** page. For example, `3 days ago` or `2019-01-01T00:00:00 +0200`.|
| `query` | The additional text by which to query incidents to find similar phishing incidents. This uses the same language used to query incidents in the UI.|
| `limit` | The maximum number of incidents to fetch. Determines how many incidents can be checked for similarity at the time of execution.|
| `emailSubject` | The name of the incident field that contains the email subject. By default this is `emailsubject` (because the email subject is stored under `${incident.emailsubject}`).|
| `emailBody` | The name of the incident field that contains the email body.|
| `emailBodyHTML` | The name of the incident field that contains the HTML version of the email body.|
| `emailFrom` | The name of the incident field that contains the email sender.|
| `statusScope` | Whether to search for similar incidents in closed incidents, non closed incidents or all incidents. Values: `All`, `ClosedOnly`, `NonClosedOnly`. Default is `All`.|
| `threshold` | The threshold to consider incident as similar. The range of values is `0-1`. If needed, make small adjustments and continue to evaluate the required value. It is recommended not to change the default value of `0.8`.|
| `maxIncidentsToReturn`| The maximum number of incidents to display as part of a campaign. If a campaign includes a higher number of incidents, the results contain only these amounts of incidents.|
| `minIncidentsForCampaign`| The minimum number of similar incidents to consider as a campaign. For example, if you specify `10`, but only `9` similar incidents are found, the script will not find them as part of a campaign.|
| `minUniqueRecipients`| The minimum number of unique recipients of similar phishing incidents to consider as a campaign.|
| `fieldsToDisplay` | A comma separated list of incident fields of the phishing incidents that are part of the campaign to set in the context and display in the markdown fields set by the automation. For example, values: `emailclassification,closereason`. The list of fields appear as output to the context for each phishing incident, and also appear when investigating the Phishing Campaign incident to manage the campaign. <br>**NOTE**: Removing the `emailfrom`, `recipients`, or `severity` fields from this list affects the dynamic sections displayed in the **Phishing Campaign** incident layout (under **Campaign Summary**) and renders them useless. The fields in this input are incident fields, and not context fields, apart from `Recipients`, which is a context field, but it can also be displayed as an incident field.

**NOTE:** The filters are applied to the incidents in order. For example, `limit` > date (date to look back for phishing incidents, such as last 7 days > `threshold`. If the `limit` is 30, then only 30 incidents within the last  7 days are checked for similarity.

### Phishing Campaign Incident Management

After the `Detect & Manage Phishing Campaigns` runs and finds a phishing campaign, the Phishing incident continues to run  as usual. In the **Investigation** tab of the incident, you can see a link to the **Phishing Campaign** incident. This incident enables the analyst to view the incident as part of a phishing campaign and take action.

The **Phishing Campaign Incident** layout contains the following additional tabs:

- The **Campaign Overview** tab, gives the analyst an overview of the different elements of the campaign: ![image](https://user-images.githubusercontent.com/43602124/123633144-8281d800-d821-11eb-885e-980984a1af19.png)
  The **Campaign Overview** tab contains the following sections:
  - **Campaign Summary**: Includes information about the phishing incidents that make up the campaign. Some fields display the number of phishing incidents (in parenthesis) in which every detail of the campaign was observed.
  - **Campaign Snippet**: View a short version of how the campaign email looks like.
  -  **Mutual Campaign indicators**: Mutual indicators from the phishing incidents that make up the campaign.![image](https://user-images.githubusercontent.com/53567272/126163317-4be821ce-4a86-46d0-8d69-dd377b01b350.png)
  - **Dynamic sections**: On the right hand side, you can see important  information about the campaign incidents, such as **Highest Severity**, **Unique Senders**, **Campaign Duration**, etc. 
    **NOTE:** If any of the dynamic sections are empty, it's because the context is missing. This is due to running the `FindEmailCampaign` without all the necessary `fieldsToDisplay`, or without setting the context to the `Phishing Campaign` incident. This should work out of the box if the `Detect & Manage Phishing Campaigns` playbook is used.
  -  **Campaign Canvas**: From Cortex XSOAR v6.1, a canvas of the campaign is supported, which can be accessed through the canvas section:
![image](https://user-images.githubusercontent.com/43602124/125288084-68b6b980-e326-11eb-99c0-19e1b7b6af8c.png)

- **Campaign Management**: Enables the analyst to take batch actions: ![image](https://user-images.githubusercontent.com/43602124/127522742-811dceb8-5b8c-4a26-a01b-d2dff272dff4.png)
    The **Campaign Management** tab contains the following sections:
  - **Similar Incidents**: Similar phishing incidents are displayed.  The columns are the same incident fields in the `fieldToDisplay` input in the  `Detect & Manage Phishing Campaign` playbook, so analysts can decide what to see about their related incidents.
  - **Notify Recipients**: Analysts can select which incident,  recipients, etc, to send an email.  The recipients from the incidents are auto-populated in the **Campaign Email To** field. Analysts can write an email and send it to the recipients directly from the layout.
  - **Incident Actions**:  The related incidents can be linked (occurs automatically by default in the playbook), unlinked, closed and reopened.
