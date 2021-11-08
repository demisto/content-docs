---
id: QRadar
title: QRadar 
description: This packs contains all the content objects needed to make the most of your QRadar SIEM. Including Integrations, playbooks, mappers, incident types, layouts, scripts and more.
---

Use this pack's content to both ingest offenses coming in from your QRadar system and in addition run playbooks in order to perform searches, add indicators to reference sets
This pack provides a all of the content you need to interact with your QRadar SIEM.
Although we recommend to enable the integration to fetch offenses from QRadar you can make use of the integration even without fetching as this pack has content such as playbook that are not related to offenses.


## Pack Workflow


### Fetch workflow
Configure XSOAR to fetch incidents/offenses from QRadar to make the most of your integration.
Configure your QRadar integration as described in this [article](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-tutorials/tutorials/ingest-incidents-from-a-siem.html): 
As explained in the article you can use the default settings such as the default incident type and playbook or create a classifier to use additional incident types and playbooks.

An example flow will be. Set up your QRadar integration to fetch incident. Run the default playbook ***QRadar Generic*** to manage the incident, provide additional logs, exclude indicators in XSOAR, notify the SIEM admin which rules need to be adjusted or which indicators also need to be excluded in QRadar.

### TIM workflow

In case your using XSOAR TIM you can automate the process of pushing indicators ingested from feeds to QRadar reference sets in order to alert or ignore specific indicators etc.
Configure feeds to fetch indicators and tag and process them accordingly.
Configure your **TIM - Add All Indicator Types To SIEM** playbook indicator query to use the proper query for the relevant indicators.
Configure the various **TIM - QRadar Add XXX Indicators** playbook to have the proper reference set names you wish to populate.
Configure a job to run the **TIM - Add All Indicator Types To SIEM** playbook in order to push the indicators to the relevant QRadar reference sets.

### Additional flows

In addition you can also use this pack to perform threat hunting using dedicated playbooks which search for dynamically defined indicators.

## In This Pack

The QRadar content pack includes several content items.

### Playbooks

* **QRadarFullSearch**
This is a very basic playbook that receives an AQL query as an input and executes it on the QRadar search API. This playbook is often used as a sub-playbook for other use cases.

* **QRadar - Get Offense Logs**
Note that for QRadar v2 and v3 you can use the integration to fetch the events with the offense however it will fetch the events according to the specified limit defined in the instance settings. By using this playbook you can define an additional search to query a larger number of logs.
Default playbook inputs use the QRadar incident fields such as idoffense, starttime. These fields can be replaced but need to point to relevant offense ID and starttime fields. A key note about this playbook is that it can be used in addition to the default event fetching enabled by the integration itself. For example the integration is configured to fetch just 20 events with the offense but we would like to run this playbook in order to fetch 100 events.

* **QRadar Generic**
This is the default playbook provided with the QRadar Generic incident type. Is allows you to get all the basic functionality of an offense lifecycle. Including
notifying the SOC, enriching the data for indicators and users, running as additional search, calculating the severity, assigning the incident, notifying the SIEM admin for false positives and more.

* **QRadar Indicator Hunting V2**
This playbook enables to search QRadar for indicators such as IP, URL/Domain and file hashes and provide outputs such as detected users, host names and IP addresses. The user can configure which fields to search in QRadar or utilize free text searches.

**TBD**
* **QRadar Build Query and Search**


### Automations

* [QRadarFetchedEventsSum](https://xsoar.pan.dev/docs/reference/scripts/q-radar-fetched-events-sum): 
This script displays the amount of fetched events vs the total number of events in the offense.

* [QRadarMagnitude](https://xsoar.pan.dev/docs/reference/scripts/q-radar-magnitude): 
This script applies colors to the field according to the magnitude based on the following scale: 1-3 green 4-7 yellow 8-10 red

* [QRadarMirroringEventsStatus](https://xsoar.pan.dev/docs/reference/scripts/q-radar-mirroring-events-status):
This script displays the the mirroring events status in the offense.

* [QRadarPrintAssets](https://xsoar.pan.dev/docs/reference/scripts/q-radar-print-assets):
This script prints the assets fetched from the offense in a table format.

* [QRadarPrintEvents](https://xsoar.pan.dev/docs/reference/scripts/q-radar-print-events):
This script prints the events fetched from the offense in a table format.

**TBD**
* [CreateQRadarQuey](XXX):
The script created a QRadar AQL query based on the inputs provided by the user such as which values to search and in which fields. The script can handle very complex queries including multiple sub conditions using the OR operator and main conditions utilizing the AND operator. Searches can be done with an exact or partial match and using exact field name or free text searches.


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

There are 3 custom tabs in the *QRadar Generic* layout. The emphasis of this layout is the displaying of the Offense data to save the user the need to use the QRadar console in order to get data about the offense. This includes a summary of the offense, the logs and asset details.   

![Layout]()

| Layout sections | Description |
|------------------ | ------------- |
| Offense Summary | Displays all the critical data for the offense, some of the data is summarized from the offense data and some from the events data. |
| Event Log Sources  | A list of the log sources types and names for the fetched logs. |
| Offense Network Data | The network data derived from the offense. |
| Fetched events Widget | Provides a count of how many events were fetched from the total events related to the offense. |
| Event Details | Summary of critical data derived from the fetched events. |
| Event Network Data | The network data derived from the fetched events. |
| Offense Magnitude Widget | Applies colors to the field according to the magnitude based on the following scale: 1-3 green 4-7 yellow 8-10 red. |
| Additional Offense Data | Provides data such as offense severity, relevance and credibility. |
| Offense Closing Details | Data about the offense closing such as closing reason, user, etc. |
| Asset Summary | Summary about the assets related to the offense as derived from the QRadar assets API. |
| Event Nat Data | The network NAT data derived from the fetched events. |

## Before You Start
This pack optionally requires you have an active instance of an mail sender integration in order to send an email to the SOC shift manager to provide a briefing if it wasn't provided in the incident creation form. Configure either the [Gmail integration](https://xsoar.pan.dev/docs/reference/integrations/gmail)  or both the [EWS Mail Sender](https://xsoar.pan.dev/docs/reference/integrations/ews-mail-sender) and [EWS V2](https://xsoar.pan.dev/docs/reference/integrations/ews-v2) or the [MS-Graph](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-mail) integrations. If you do not activate an instance of the mail sender integration, The playbooks wont send notifications to the SOC or SIEM teams.

In addition, it is highly recommend to use the following enrichment enrichment integrations to gain all the benefits from this pack:

This pack also requires the following to be configured:

- [QRadar](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-tutorials/tutorials/ingest-incidents-from-a-siem.html).

## Testing the Pack
After you configure the integrations, test the pack to ensure that everything was configured correctly.

1. Either use the default ***QRadar Generic*** incident type or duplicate it.
2. Either use the default ***QRadar Generic Incoming Mapper*** or duplicate it.
3. Validate that fetching of offenses is enabled and working from QRadar to XSOAR.
4. Validate the the layout contains all of the relevant sections and fields.

   
## Integrations

- Although these integrations are not included in the pack, such as Gmail, EWS or Grpah Mail Sender integrations are required for the pack to be able to send emails to the SOC or SIEM admins.
To be able using the messaging apps section in the layout you will be needed to configure them as well:   
   - Gmail - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/gmail)
   - EWS Mail Sender - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/ews-mail-sender)
   - Microsoft Graph Mail - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/microsoft-graph-mail)