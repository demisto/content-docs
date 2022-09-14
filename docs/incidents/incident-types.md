---
id: incident-types
title: Working with Incident Types
---
Incident types are used to classify the events that are ingested into the Cortex XSOAR system. Each incident type can be configured to work with a dedicated playbook, which can either run automatically when an event is ingested, or can be triggered separately at a later point. In addition, you can configure dedicated SLA parameters for each incident type, as well run specific post-processing scripts for the given incident type. 

**Note**: Only events that are ingested through integrations or the REST API are processed through the classification engine and automatically assigned an incident type. Incidents that you create manually, or are created through a playbook, are not processed through the classification engine and should be assigned an incident type.

Once you define the incident type, you can configure its layout. For example, when your analysts are investigating a phishing incident, they will be interested in different information from a ransomware incident. You can customize the layout for each incident such that they will be presented with exactly the information that they need. In our phishing incident example, that might include the email headers and the email body, whereas for the ransomware you would want to see the family to which the ransomware belongs. For more information, see [Customize Incident Layouts](incident-customize-incident-layout).

As part of the planning process, you should map out the different incident types that your organization deals with, as well as the 3rd party integrations that you have. For example, out-of-the-box Cortex XSOAR comes with incident types for phishing attacks, but if you work with a dedicated integration, such as PhishMe, you can define an incident type specifically for those events. When you configure the Phishme integration, you will associate it with the Phishme incident type, which will probably also have a dedicated Phishme playbook. 

Similar to fields, defining incident types should be an iterative process. As you plan your deployment and begin working with your system, you will learn which incident types are missing. You can then add the new incident types to your system and fine tune the entire incident ingestion process.

## Create an Incident Type

1. In the Incident Types page, click **New Incident Type**.
2. Fill in the paramters. For a list of the parameters and their definitions, see Incident Type Properties, below.
3. Click **Save**.

## Incident Type Properties

The following table lists the fields for an incident type, and their descriptions.

| Field | Description | 
| ------ | ------ |
| Name | Enter a descriptive name for the task. Try to make this as informative as you can so readers of the playbook will know what the task does before viewing the task details. |
| Default playbook | Select the playbook that is associated with the incident type by default. |
| Run playbook automatically | Determine if the playbook runs when the event is ingested. |
| Auto extract incident indicators | Determine how indicators are processed. Valid values are: <br/> None - Indicators are not automatically extracted. Use this option when you do not want to further evaluate the indicators. <br/> Inline - Indicators are extracted and enriched when the incident is created, and the findings are added to the Context Data. For example, if you define auto-extract for the Phishing incident type as inline, all of the indicators for incident classified as Phishing will be extracted and enriched before anything else happens. The playbook you defined to run by default will not run until the indicators have been fully processed. Use this option when you need to have the most robust information available per indicator. <br/> Out of band - Enriched indicator data is not saved to the Context Data because the enrichment runs in parallel (or asynchronously) to other actions. The enriched data is available within the incident and can be added on a per-need basis using extended context. Use this option when you do not need the enriched data in real-time. <br/> For more information about auto-extraction, see [Auto Extract](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-6/cortex-xsoar-admin/manage-indicators/auto-extract-indicators.html). |
| Post process using | Select the script to run on these incident types after they have been processed.|
| SLA | Determine the SLA for this incident type in any combination of Weeks, Days, and Hours. |
| Set Reminder at | Optionally configure a reminder for the SLA in any combination of Weeks, Days, and Hours. |

For more information about incident types, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/incidents/customize-incident-view-layouts/create-an-incident-type).