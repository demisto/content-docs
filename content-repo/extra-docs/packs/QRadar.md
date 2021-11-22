---
id: QRadar
title: QRadar 
description: This pack contains all the content objects you need to interact with your QRadar SIEM, including integrations, playbooks, mappers, incident types, layouts, and scripts.
---

Use this pack's content to ingest offenses from your QRadar system and to run playbooks that perform searches and add indicators to reference sets.
Although we recommend enabling the integration to fetch offenses from QRadar, you can use the integration even without fetching since this pack has content such as playbooks that are not related to offenses.


## Pack Workflow


### Fetch Workflow
Configure XSOAR to fetch incidents/offenses from QRadar to make the most of your integration.
Configure your QRadar integration as described in this [article](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-tutorials/tutorials/ingest-incidents-from-a-siem.html). 
You can use the default settings such as the default incident type and playbook, or create a classifier to use additional incident types and playbooks.

A sample fetch flow is:
- Set up your QRadar integration to fetch an incident. 
- Run the default playbook ***QRadar Generic*** to:
   - Manage the incident
   - Provide additional logs
   - Exclude indicators in XSOAR
   - Notify the SIEM admin which rules need to be adjusted or which indicators need to be excluded in QRadar

### TIM Workflow

With XSOAR TIM you can automate the process of pushing ingested indicators to QRadar reference sets, for example to alert or ignore specific indicators.

A sample TIM flow is:
- Configure feeds to fetch, tag, and process indicators.
- Configure the **TIM - Add All Indicator Types To SIEM** playbook indicator query to use the proper query for the relevant indicators.
- Configure the **TIM - QRadar Add XXX Indicators** playbook to have the proper reference set names you wish to populate.
- Configure a job to run the **TIM - Add All Indicator Types To SIEM** playbook to push the indicators to the relevant QRadar reference sets.

### Additional Flows

You can also use this pack to perform threat hunting using dedicated playbooks which search for dynamically defined indicators.

## In This Pack

The QRadar content pack includes several content items.

### Playbooks

* **QRadarFullSearch**
This basic playbook receives an AQL query as an input and executes it on the QRadar search API. It is often used as a sub-playbook.

* **QRadar - Get Offense Logs**
This playbook can fetch a larger number of offense logs than the limit specified in the integration instance default settings.
Notice that the integration can fetch offense log events according to the specified limit defined in the instance settings. This playbook enables you to define an additional search to query a larger number of logs. For example, the integration is configured to fetch 20 events but you can run this playbook to fetch 100 events.
Default playbook inputs use QRadar incident fields such as idoffense and starttime. These fields can be replaced but need to point to relevant offense ID and starttime fields. 

* **QRadar Generic**
This is the default playbook provided with the QRadar Generic incident type. It enables all the basic functionality of an offense lifecycle, including
notifying the SOC, enriching the data for indicators and users, running an additional search, calculating the severity, assigning the incident, and notifying the SIEM admin for false positives.

* **QRadar Indicator Hunting V2**
This playbook enables searching QRadar for indicators such as IP, URL/Domain, and file hashes. It provides outputs such as detected users, host names and IP addresses. You can configure which fields to search in QRadar or use free text searches.


### Automations

* [QRadarFetchedEventsSum](https://xsoar.pan.dev/docs/reference/scripts/q-radar-fetched-events-sum): 
This script displays the count of fetched events vs the total number of events in the offense.

* [QRadarMagnitude](https://xsoar.pan.dev/docs/reference/scripts/q-radar-magnitude): 
This script applies colors to the events field based on the following scale: 1-3 green, 4-7 yellow, 8-10 red

* [QRadarMirroringEventsStatus](https://xsoar.pan.dev/docs/reference/scripts/q-radar-mirroring-events-status):
This script displays the the mirroring event status in the offense.

* [QRadarPrintAssets](https://xsoar.pan.dev/docs/reference/scripts/q-radar-print-assets):
This script prints the assets fetched from the offense in a table format.

* [QRadarPrintEvents](https://xsoar.pan.dev/docs/reference/scripts/q-radar-print-events):
This script prints the events fetched from the offense in a table format.

### Incident Fields

- **Credibility - Offense**
- **Description - Offense**
- **Destination Hostname**
- **Destination MAC Address**
- **Domain - Offense**
- **ID - Offense**
- **Link To Offense**
- **List of Rules - Offense**
- **Low Level Categories - Offense**
- **Magnitude - Offense**
- **Number Of Events In Offense**
- **Number Of Fetched Events**
- **Number Of Flows**
- **Offense Inactive**
- **Relevance - Offense**
- **Severity - Offense**
- **Source IP - Offense**
- **Source Network - Offense**
- **Status - Offense**
- **Type - Offense**
- **Username Count - Offense**

### Incident Types
There is 1 incident type - **QRadar Generic**.

### Layout
There is 1 layout - **QRadar Generic*** 

There are 3 custom tabs in the *QRadar Generic* layout. This layout displays offense data so the user does not need to use the QRadar console. It includes a summary of the offense, logs, and asset details.   

![Layout](.//docs/doc_imgs/reference/QRadar/QRadar_offense_summary.png)

| Layout sections | Description |
|------------------ | ------------- |
| Offense Summary | Displays all the critical data for the offense. Some of the data is summarized from the offense data and some from the events data. |
| Event Log Sources  | A list of the log source types and names for the fetched logs. |
| Offense Network Data | The network data derived from the offense. |
| Fetched events Widget | Provides a count of how many events were fetched from the total events related to the offense. |
| Event Details | Summary of critical data derived from the fetched events. |
| Event Network Data | The network data derived from the fetched events. |
| Offense Magnitude Widget | Applies colors to the field based on the following scale: 1-3 green, 4-7 yellow, 8-10 red. |
| Additional Offense Data | Provides data such as offense severity, relevance, and credibility. |
| Offense Closing Details | Data about the offense closing such as closing reason and user |
| Asset Summary | Summary of the assets related to the offense derived from the QRadar assets API. |
| Event Nat Data | The network NAT data derived from the fetched events. |

## Before You Start
- **[Configure QRadar](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-tutorials/tutorials/ingest-incidents-from-a-siem.html)**.
- **(Optional) Configure email integrations**. If you want to enable playbooks to send emails, you need an active mail sender integration instance. For example, you may need to email the SOC shift manager to provide a briefing if it wasn't provided in the incident creation form. Configure either the [Gmail integration](https://xsoar.pan.dev/docs/reference/integrations/gmail)  or both the [EWS Mail Sender integration](https://xsoar.pan.dev/docs/reference/integrations/ews-mail-sender) and [EWS V2 integration](https://xsoar.pan.dev/docs/reference/integrations/ews-v2) or the [MS-Graph integration](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-mail). If you do not activate a mail sender integration instance, The playbooks won't send notifications to the SOC or SIEM teams.
- **Configure enrichment integrations**. We highly recommend using the following enrichment integrations to gain all the benefits from this pack:

## Testing the Pack
After you configure the integrations, test the pack to ensure everything is configured correctly.

1. Either use the default ***QRadar Generic*** incident type or duplicate it.
2. Either use the default ***QRadar Generic Incoming Mapper*** or duplicate it.
3. Validate that fetching offenses from QRadar to XSOAR is enabled and working.
4. Validate the layout contains all the relevant sections and fields.


## Integrations

Although email integrations are not included in the pack, they are required for the pack to be able to send emails to the SOC or SIEM admins or to use the messaging apps section in the layout:   
- [Gmail integration](https://xsoar.pan.dev/docs/reference/integrations/gmail)
- [EWS Mail Sender integration](https://xsoar.pan.dev/docs/reference/integrations/ews-mail-sender) and [EWS V2 integration](https://xsoar.pan.dev/docs/reference/integrations/ews-v2)
- [Microsoft Graph Mail integration](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-mail)
