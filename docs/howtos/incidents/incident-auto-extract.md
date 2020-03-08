---
id: incident-auto-extract
title: Auto Extract
---
The auto-extract feature extracts indicators and enriches their reputations using commands and scripts defined for the indicator type. You can automatically extract indicators in the following scenarios:

* When fetching incidents

* In a playbook task

* Using the command line

By default, Auto Extract is enabled to help you get up and running as you set up your environment. As your system matures and you start ingesting more events and have more integrations configured, using Auto Extract can adversely affect system performance.

As a result, Cortex XSOAR recommends that you turn off Auto Extract using the server configurations for the different Auto Extract options and only turn it on for those specific scenarios where it is necessary. 

## Auto-extract modes

Auto Extract supports the following modes:

* None - Indicators are not automatically extracted. Use this option when you do not want to further evaluate the indicators. 

* Inline - Indicators are extracted and enriched within the context that auto-extract runs, and the findings are added to the Context Data. For example, if you define auto-extract for the Phishing incident type as inline, all of the indicators for incident classified as Phishing will be extracted and enriched before anything else happens. The playbook you defined to run by default will not run until the indicators have been fully processed. Use this option when you need to have the most robust information available per indicator. Unless otherwise configured in a system configuration, this is the default mode in which auto-extract executes.

   **Note**: This configuration will slow down your system performance. 

* Out of band - Indicators are enriched in parallel (or asynchronously) to other actions. The enriched data is available within the incident, however, it is not available for immediate use in task inputs or outputs since the information is not available in real time. 

## Global Server Configurations for Auto Extract

You can control the default behavior for auto extract using the following server configurations. 

| Component | Key |
| ------ | ------ | 
| Incident ingestion | reputation.calc.algorithm | 
| Tasks | reputation.calc.algorithm.tasks  |
| Manual | reputation.calc.algorithm.manual |


Each configuration can accept one of the following values:

* 1 = None.
* 2 = Inline. This is the default behavior
* 3 = Out of Band.

## Disable Auto Extract for Scripts and Integrations

You can disable auto-extract for a specific automation or integration.

### Disable for an Automation
To disable Auto Extract for an automation, add the "IgnoreAutoExtract": True value to the entry return.

`entry = {
                    'Type': entryTypes['note'],
                    'Contents': { 'Echo' : demisto.args()['echo'] },
                    'ContentsFormat': formats['json'],
                    'ReadableContentsFormat': formats['markdown'],
                    'HumanReadable': hr,
                    'IgnoreAutoExtract' : True
            }`


### Disable for Integrations
To disable auto-extract for a specific integration, add the following parameter to the integration configuration.

"IgnoreAutoExtract": True


## Configure What Auto Extract Executes

When auto-extract is used, it extracts all indicators that match the regex defined in an indicator type, and enriches those indicators using its commands. For example, out-of-the-box, the URL indicator is enriched using the !url command. You can decide to further enrich IP indicators by using a script that calls multiple integrations, such as urlscan.io and URLhaus.

1. Navigate to **Setting** -> **Advanced** -> **Indicator Types**.

2. Select the indicator type for which you want to configure the command or script and click **Edit**.

   For out of the box indicators, the Name and Regex fields are disabled.

3. Under **Reputation command**, enter the command to execute when auto extracting indicators of this type.

4. Under **Exclude these integrations for the reputation command**, select which integrations should not be used when executing the reputation command.

5. Under **Reputation Script**, select the script to run when enriching indicators of this indicator type. The scripts override the reputation command.

6. Click **Save**. 

## Use Case - Auto Extract Indicators from a Phishing Email

The following scenario shows how Auto Extract is used in the *Process Email - Generic* playbook to automatically extract and enrich a very specific group of indicators. 

1. Navigate to the **Playbooks** page and search for the *Process Email - Generic* playbook. This playbook parses the headers in the original email used in a phishing attack. It is important to parse the original email used in the Phishing attack and *not* the email that was forwarded to make sure that you are only extracting and enriching the email headers from the malicious email and not the one your organization uses to report phishing attacks.

2. Open the **Add original email attachments to context** task.  

   Under the **Outputs** tab you can see all of the different data that the task extracts.

   ![Parse Email Files - Outputs tab](../../doc_imgs/howtos/incidents/Auto-Extract_ParseEmailFiles_Outputs.png)

  3. Navigate to the **Advanced** tab. 

   ![Parse Email Files - Inline](../../doc_imgs/howtos/incidents/Auto-Extract_ParseEmailFiles_Inline.png)
  
   Note that under Auto extract indicators, the Inline option is selected. This indicates that all of the outputs will be processed before the playbook moves ahead to the next task.

4. Open the **Set incident with the Email object data** task. This task receives the data from the **Add original email attachments to context** task and sets the various data points to context. 

   Under the Advanced tab, you can see that **Auto extract indicators** is set to None because the indicators have already been enriched and there is no need to do it again.

 ![Parse Email Files - Disabled](../../doc_imgs/howtos/incidents/Auto-Extract_ParseEmailFiles_Disabled.png)
   [INSERT IMAGE Auto-Extract_ParseEmailFiles_Disabled.png]

In the above example, had we set the reputation.calc.algorithm.tasks server configuration to 1, we would not have had to go into the **Advanced** tab of the **Set incident with the Email object data** task and manually tell the task not to extract the indicators. It would use the system default.
