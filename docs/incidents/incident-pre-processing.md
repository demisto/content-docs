---
id: incident-pre-processing
title: Pre-processing Rules
---
Pre-processing rules enable you to perform certain actions on incidents as they are ingested into Cortex XSOAR directly from the user interface. Through these rules, you can select incoming events on which to perform actions, for example, link the incoming incident to an existing incident, or under pre-configured conditions, drop the incoming incident altogether.

**Notes**: Rules are applied in descending order, and only one rule is applied per incident.

## Creating Rules

To create a rule:

1. Navigate to **Settings > Integrations > Pre-Process Rules**.
2. Click **New Rule**.
3. Enter a name for the rule.
   Cortex XSOAR recommends that you give meaningful names that will help you identify what the rule does when viewing the list of rules.
4. Determine under which conditions the rule is applied to an incoming incident.
   For example, if you know that there is a phishing campaign, you can create a rule for emails with a specific subject.
   **Note**: You can add multiple conditions within a filter, and also add multiple filters. 
5. Determine which action to take in the event that the incoming incident matches the rule. For information about the valid actions, see Rule Actions.

## Rule Actions
| Option | Description | Next Steps | 
| ------ | ------ | ------ |
| Drop | Drop the incoming incident.| Click **Save**. |
| Drop and update| Drops the incoming event and updates the Dropped Duplicate Incidents table of the existing incident that you define. In addition, a War Room entry is created.   <br/>If an existing incident matching the defined criteria is not found, an incident is created for the incoming event. | 1. Determine if you want to update the oldest or newest incident within a time range.<br/> 2. Click **Save**. |
| Link | Creates an entry in the Linked Incidents table of the existing incident to which you link. | 1. Determine if you want to update the oldest or newest incident within a time range.<br/> 2. Click **Save**. |
| Link and close | Creates an entry in the Linked Incidents table of the existing incident to which you link, and closes the incoming incident. <br/>If an existing incident matching the defined criteria is not found, an incident is created for the incoming event. | 1. Determine if you want to update the oldest or newest incident within a time range.<br/> 2. Click **Save**. |
| Run a script | Select a script to run on the incoming incident. <br/>**Note**: When you create a script, you need to add the preProcessing tag for the script to appear in the list of available scripts. | 1. Select the script to run on the incoming incident. Only scripts that were tagged preProcessing appear in the drop-down list. <br/> 2. Click **Save**.

## Testing Rules
You can test your rules before saving them to make sure that they are effective and efficient. This is useful for ensuring that you are receiving the desired results before putting a rule in production.

To test a rule:

1. Follow the procedure outlined in Creating Rules.
2. Instead of clicking **Save**, click **Test**.
3. Provide an existing incident as a sample incident against which the rule can run.
4. Click **Test**.

## Example
The following example creates a rule for processing an incoming incident that is part of a phishing campaign.

![Parse Email Files - Outputs tab](/doc_imgs/incidents/PreProcessingRules.png)

In most cases, in a phishing campaign, the email subject will be similar. Therefore, we created, a condition for incoming incidents that have a subject line that contains the text, this is a phishing email.

As we know that this is a campaign, we are going to ask to close the incoming incident and link it to an already existing incident.

Lastly, we have to tell Cortex XSOAR to which incident to link the incoming incident, so we've asked to link to the oldest incident, since we want to link to the first incident in the campaign.

For more information about incident pre-process rules, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/incidents/incident-management/incident-de-duplication/creating-pre-process-rules-for-incidents).