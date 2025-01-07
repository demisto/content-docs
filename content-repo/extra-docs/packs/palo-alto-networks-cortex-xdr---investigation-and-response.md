---
id: palo-alto-networks-cortex-xdr
title: Cortex XDR by Palo Alto Networks
description: Automates Cortex XDR incident response, and includes custom Cortex XDR incident views and layouts to aid analyst investigations.
---
The Cortex XDR by Palo Alto Networks pack automates Cortex XDR incident response, and includes custom Cortex XDR incident views and layouts to aid analyst investigations.

Cortex XDR is a detection and response app that natively integrates network, endpoint, and cloud data to stop sophisticated attacks.

Effectively responding to these attacks requires security teams to consolidate data from multiple sources. Critical time is wasted switching between tools and performing repetitive tasks, allowing the attack to escalate further.

This pack can provide significant assistance.

## What does the pack do?

- **Automated Incident Synchronization**: Keeps incidents consistently updated between Cortex XDR and Cortex XSOAR, maintaining data integrity and reducing manual effort.
- **Comprehensive Alert Management**: Automates alert handling, including enrichment, severity assessment, and remediation, for a streamlined incident response process.
- **Advanced Threat Hunting**: Leverages the XQL Query Engine for in-depth data analysis, enabling proactive threat hunting and investigation.
- **Ready-to-Use Playbooks**: a range of pre-built playbooks optimized for common security workflows, allowing teams to quickly deploy effective responses with minimal configuration.

The playbooks included in this pack can help you save time and keep your incidents and indicators in sync with Cortex XDR. They also help automate repetitive tasks:

- Syncs and updates Cortex XDR incidents.
- Triggers a sub-playbook to handle each alert by type.
- Extracts and enriches all relevant indicators from the source alert.
- Hunts for related IOCs.
- Assesses the severity of the incident.
- Collaborates with the analyst to determine the appropriate remediation path or classify the incident as a false positive, based on gathered data and incident severity.
- Remediates the incident by blocking malicious indicators and isolating compromised endpoints.

## The Palo Alto Networks Cortex XDR - Investigation and Response pack enables the following flows:

- [Lite Incident Handling](#lite-incident-handling) - A lite playbook for handling Palo Alto Networks Cortex XDR incidents, which encompasses incident enrichment, investigation, and response for each incident.
- [Device Control Violations](#device-control-violations) - Fetch device control violations from XDR and communicate with the user to determine the reason the device was connected.
- [XDR Incident Handling](#xdr-incident-handling) - Compare incidents in Palo Alto Networks Cortex XDR and Cortex XSOAR, and update the incidents appropriately.
- [Cloud IAM User Access Investigation](#cloud-iam-user-access-investigation) - Investigates and responds to Cortex XDR Cloud alerts where an Cloud IAM user's access key is used suspiciously to access the cloud environment.
- [Cortex XDR Cloud Cryptomining](#Cortex-XDR-Cloud-Cryptomining) - Investigates and responds to Cortex XDR XCloud
  Cryptomining alerts. The playbook Supports AWS, Azure and GCP.

### Lite Incident Handling
This playbook is a lite default playbook to handle XDR incidents, and it doesn't require additional integrations to run.
The [Palo Alto Networks Cortex XDR - Investigation and Response](#palo-alto-networks-cortex-XDR---investigation-and-response) integration fetches Cortex XDR incidents and runs the [Cortex XDR Lite - Incident Handling](#cortex-xdr-lite---incident-handling) playbook. 

First, the playbook runs the ***xdr-get-incident-extra-data*** command to retrieve data fields of the specific incident including a list of alerts with multiple events, alerts, and key artifacts.

Then, the playbook uses the [Entity Enrichment Generic v3](https://xsoar.pan.dev/docs/reference/playbooks/entity-enrichment---generic-v3) sub-playbook which takes all the entities in the incidents and enriches them with the available products in the environment.

In the investigation phase, the playbook uses the [Command-Line Analysis](https://xsoar.pan.dev/docs/reference/playbooks/command-line-analysis) sub-playbook to analyze the command line if it exists to determine whether the command line usage was malicious or suspicious.

The playbook also uses the [Cortex XDR - Get entity alerts by MITRE tactics](https://xsoar.pan.dev/docs/reference/playbooks/get-entity-alerts-by-mitre-tactics) sub-playbook to search for alerts related to the endpoint and to the username from Cortex XDR, on a given timeframe, based on MITRE tactics.

Based on the enrichment and the investigation results, the playbook sets the verdict of the incident. Whether the incident verdict is not malicious, the analyst decides whether the incident verdict is malicious or benign.

Whether the verdict is set to malicious by the playbook or by the analyst's decision the playbook will perform remediation actions by isolating the endpoint and blocking all the indicators that were extracted from the incident either manually or automatically using the [Block Indicators - Generic v3](https://xsoar.pan.dev/docs/reference/playbooks/block-indicators---generic-v3) sub-playbook. After the remediation stage, the playbook will close the incident.

If the verdict is set to benign, the playbook will close the incident.

As part of this playbook, you'll receive a comprehensive layout that presents incident details, analysis, investigation findings, and the final verdict. Additionally, the layout offers convenient remediation buttons for quicker manual actions.

To utilize this playbook as the default for handling XDR incidents, the classifier should be empty, and the selected incident type should be `Cortex XDR - Lite`.
The selected Mapper (incoming) should be `XDR - Incoming Mapper`, and the selected Mapper (outgoing) should be Cortex `XDR - Outgoing Mapper`.

### Device Control Violations
If a user connects an unauthorized device to the corporate network, such as a USB dongle or a portable hard disk drive, the connection creates an event in Cortex XDR. 
The [Cortex XDR device control violations](#cortex-xdr-device-control-violations) playbook queries Cortex XDR for device control violations for specified hosts, IP addresses, or XDR endpoint IDs. It then communicates via email with the involved users to understand the nature of the incident and if the user connected the device. 

The playbook can enrich data for XDR incidents and determine if there were any device control violations prior to this incident or if there is a correlation between this incident and another one. 

You can create a job to periodically query Cortex XDR for device control violations. The dedicated [JOB - Cortex XDR query endpoint device control violations](#job---cortex-xdr-query-endpoint-device-control-violations) playbook enriches the data associated with the endpoint device control events, and creates an incident if any violations are found.  The [Cortex XDR device control violations](#cortex-xdr-device-control-violations) playbook is the response playbook for the violations found.

The [Cortex XDR device control violations](#cortex-xdr-device-control-violations) playbook can be used to enrich data for the involved hosts/users in XDR and other incidents.

All collected data is displayed in the XDR device control incident layout.

### XDR Incident Handling

The [Palo Alto Networks Cortex XDR - Investigation and Response](#palo-alto-networks-cortex-XDR---investigation-and-response) integration fetches Cortex XDR incidents and runs the [Cortex XDR incident handling v3](#cortex-xdr-incident-handling-v3) playbook. This playbook will be triggered by fetching a Palo Alto Networks Cortex XDR incident, but only if the classifier is set to 'Cortex XDR - Classifier' and the incident type is left empty during the integration configuration.

The playbook runs the ***xdr-get-incident-extra-data*** command to retrieve data fields of the specific incident including a list of alerts with multiple events, alerts, and key artifacts.  

The playbook then searches for similar incidents in Cortex XSOAR to link to the current incident. If a similar incident is found, the analyst will be asked whether to close the current incident as a duplicate since there is an older incident already being handled. The analyst will review the linked incident and decide if the incident should be resolved and closed as a duplicate incident. 

If no similar incidents are found, or if the analyst does not want to close the incident as a duplicate, the workflow continues.

The [Cortex XDR Alerts Handling](#cortex-xdr-alerts-handling) sub-playbook loops through and checks the category of the alerts.
Currently, this sub-playbook handles Malware, Port Scan and Cloud Cryptomining alerts only. If the category is Malware, the 
[Cortex XDR - Malware Investigation](#cortex-xdr---malware-investigation) sub-playbook will run. If the category is Port Scan, the [Cortex XDR - Port Scan - Adjusted](#cortex-xdr---port-scan---adjusted) sub-playbook will run and if the category is Cloud Cryptomining, the [Cortex XDR - Cloud Cryptomining](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---cloud-cryptomining) sub-playbook will run. After the Malware, Port Scan or Cloud Cryptomining sub-playbook runs or if the alert is in any other category, the main playbook will continue to further investigate. It counts the number of alerts in the incident and displays this information in the layout. It then executes the [Cortex XDR device control violations](#cortex-xdr-device-control-violations) sub-playbook. 

Then the [Entity Enrichment Generic v3](https://xsoar.pan.dev/docs/reference/playbooks/entity-enrichment---generic-v3) sub-playbook runs which takes all the entities in the incidents and enriches them with the available products in the environment. The SOC team will then do a manual in-depth analysis of the incident. 

You can then choose to optionally run the [Palo Alto Networks - Hunting And Threat Detection](https://xsoar.pan.dev/docs/reference/playbooks/palo-alto-networks---hunting-and-threat-detection) sub-playbook to extract IOCs from the investigation and run them across the organization to check if there are any other compromised accounts or endpoints with the same information that was detected in this alert.

The severity of the incident is calculated by the [Calculate Severity - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/calculate-severity---generic-v2) sub-playbook.

Based on the severity, the analyst decides whether to continue to the remediation stage or close the investigation as a false positive. The remediation blocks all the indicators that were extracted from the incident either manually or automatically using the [Block Indicators - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/block-indicators---generic-v2) sub-playbook.

If this was a port scan alert, the analyst will manually block the ports used for the exploitation on the scanned hosts.

After the remediation, if there are no new alerts, the playbook stops the alert sync and closes the XDR incident and investigation.

To utilize this playbook for handling XDR incidents, the classifier that should be selected is `Cortex XDR - Classifier`.
The selected Mapper (incoming) should be `XDR - Incoming Mapper`, and the selected Mapper (outgoing) should be Cortex `XDR - Outgoing Mapper`.

### Sync Indicators between Cortex XSOAR and Cortex XDR

The [Cortex XDR - IOCs](https://xsoar.pan.dev/docs/reference/integrations/cortex-xdr---ioc) feed integration syncs indicators between Cortex XSOAR and Cortex XDR. The integration syncs indicators according to the defined fetch interval. At each interval, the integration pushes new and modified indicators defined in the Sync Query from Cortex XSOAR to Cortex XDR. Additionally, the integration checks if there are manual modifications of indicators on Cortex XDR and syncs back to Cortex XSOAR. Once per day, the integration performs a complete sync which also removes indicators that have been deleted or expired in Cortex XSOAR, from Cortex XDR.

### Cloud IAM User Access Investigation
The [Cloud IAM user access investigation](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---cloud-iam-user-access-investigation) playbook investigates and responds to Cortex XDR Cloud alerts where an Cloud IAM user's access key is used suspiciously to access the cloud environment. 

The playbook fetches data from the incident and then retrieves additional cloud alert data that was not available in the incident. It then checks if the alerts are one of the following XCLOUD supported alerts: 
- Penetration testing tool attempt
- Penetration testing tool activity
- Suspicious API call from a Tor exit node

If the alert is not one of the supported alerts, the playbook ends.
Otherwise, the incident type is set to XCLOUD and the playbook starts to collect additional information pertaining to the alert.

First the source IP addresses are enriched. These are the IP addresses that are used to connect to the environment. 

Then the playbook enriches information about the user who connected to the environment through the relevant IAM integration using the [Cloud IAM Enrichment - Generic](https://xsoar.pan.dev/docs/reference/playbooks/cloud-iam-enrichment---generic) sub-playbook. The sub-playbook lists the user access keys and retrieves information about the IAM user, including the user's creation date, path, unique ID, and ARN.  From this, it can be seen if these user keys are active and the analyst can block these keys later in the investigation if they are causing malicious activities.

Based on the enrichment and the analysis results, the playbooks sets the verdict of the incident. If malicious indicators are found, the playbook takes action using [Cloud Response - Generic](https://xsoar.pan.dev/docs/reference/playbooks/cloud-response---generic) sub-playbook.
If the verdict not determined, it lets the analyst decide whether to continue to the remediation stage or close the investigation. 

The analyst looks at any persistence, for example, a new user or key creation or for any lateral movement operations. For example, an operation can be = AsumeRole.
As an extra validation step, it is recommended to query the user and/or the user’s manager regarding the investigated suspicious activity.

Based on this investigation, the analyst manually decides if the alert is a false or true positive.  If false, the playbook ends.

### Cortex XDR Cloud Cryptomining
The [Cortex XDR - Cloud Cryptomining](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---cloud-cryptomining) playbook 
enriches, investigates, and responds to Cortex XDR XCloud Cryptomining alerts. The playbook flow is triggered based on the 
'Unusual 
allocation of multiple cloud compute resources' alert. If the alert isn't present in the incident, the playbook will exit the IR flow.

First, the playbook will fetch and map the raw JSON of the alert to context.

Then the playbook enters the [Cortex XDR - Cloud Enrichment](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---cloud-enrichment) playbook and collects and enriches the following:
 - Resource enrichment
   - Previous activity is seen in the specified region or project
 - Account enrichment
 - Network enrichment
   - Attacker IP
   - Geolocation
   - ASN

Also, the playbook will collect data for later usage in the layout.

After collecting and enriching the data, the playbook enters the [Cortex XDR - Cryptomining - Set Verdict](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---cryptomining---set-verdict) playbook. This playbook will set the incident verdict as Unknown or Malicious based on the following decision tree logic:

- If the source IP address is malicious.
- If the incident includes both "Unusual allocation of multiple cloud compute resources" AND "Cloud identity reached a 
     throttling API rate" (medium/high severity).
- If the incident includes both "Unusual allocation of multiple cloud compute resources" AND "Suspicious heavy allocation of compute resources - possible mining activity".
- If the incident includes "Unusual allocation of multiple cloud compute resources" with medium/high severity, the source ASN isn't known, and the source IP isn't known.
- If the incident includes both "Unusual allocation of multiple cloud compute resources" AND "A cloud compute instance was created in a dormant region".
- If none of the conditions is true, the playbook will wait for an analyst's decision.

If the analyst approves the activity, the False Positive flow will be executed, and the incident severity will be set as 'low'.

If the activity is not approved by the analyst or the [Cortex XDR - Cryptomining - Set Verdict](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---cryptomining---set-verdict) playbook final verdict is malicious, the response flow is executed. These are the primary response steps:
- Setting the incident severity as 'high'.
- Sending a message to the SOC.
- Executing the [Cloud Response - Generic](https://xsoar.pan.dev/docs/reference/playbooks/cloud-response---generic) playbook.

The **Cloud Response - Generic** playbook provides response playbooks for:

- AWS
- Azure
- GCP

The response actions available are:

- Terminate/Shut down/Power off an instance.
- Delete/Disable a user.
- Delete/Revoke/Disable credentials.
- Block indicators.

The playbook will move forward for the analyst's resolution when the response phase has finished.

## What does this pack include?

The Palo Alto Networks Cortex XDR - Investigation and Response content pack includes several content items.

### Automations

- **CortexXDRAdditionalAlertInformationWidget**: This script retrieves additional alert information from the context.
- **CortexXDRCloudProviderWidget**: This script returns an HTML result of the cloud providers in the incident.
- **CortexXDRIdentityInformationWidget**: This widget displays Cortex XDR identity information.
- **CortexXDRInvestigationVerdict**: This widget displays the incident verdict based on the 'Verdict' field.
- **CortexXDRRemediationActionsWidget**: This widget displays Cortex XDR remediation action information.
- **DBotGroupXDRIncidents**: This script uses a train clustering model on Cortex XDR incident type.
- **EntryWidgetNumberHostsXDR**: Entry widget that returns the number of hosts in a Cortex XDR incident.
- **EntryWidgetNumberRegionsXCLOUD**: Entry widget that returns the number of regions in a Cortex XDR incident.
- **EntryWidgetNumberResourcesXCLOUD**: Entry widget that returns the number of resources in a Cortex XDR incident.
- **EntryWidgetNumberUsersXDR**: Entry widget that returns the number of users that participated in a specified Cortex XDR incident.
- **EntryWidgetPieAlertsXDR**: Entry widget that returns a pie chart of alerts for a specified Cortex XDR incident by alert severity (low, medium, and high).
- **XCloudRegionsPieWidget**: XCLOUD dynamic section, showing the top ten regions types in a pie chart.
- **XCloudResourcesPieWidget**: XCLOUD dynamic section, showing the top ten resource types in a pie chart.
- **XDRConnectedEndpoints**: The widget returns the number of the connected endpoints using xdr-get-endpoints command.
- **XDRDisconnectedEndpoints**: The widget returns the number of the disconnected endpoints using xdr-get-endpoints command.
- **XDRSyncScript**: Deprecated. The incoming and outgoing mirroring feature added in XSOAR version 6.0.0 is used instead to sync XDR. After the Calculate Severity - Generic v2 sub-playbook’s run, Cortex XSOAR will be treated as the single source of truth for the severity field, and it will sync only from Cortex XSOAR to XDR, so manual changes for the severity field in XDR will not update in the XSOAR incident.

### Classifiers

- **Cortex XDR - Classifier**: Classifies Cortex XDR incidents.
- **Cortex XDR - Incoming Mapper**: Maps incoming Cortex XDR incidents fields.
- **Cortex XDR - Outgoing Mapper**: Maps outgoing Cortex XDR incidents fields.
- **Cortex XDR Incident Handler - Classifier**: Classifies Cortex XDR incidents.

### Incident Types

- **Cortex XDR - Lite**
- **Cortex XDR Device Control Violations**
- **Cortex XDR Disconnected endpoints**
- **Cortex XDR Incident**
- **Cortex XDR Port Scan**
- **Cortex XDR - XCLOUD**
- **Cortex XDR - XCLOUD Cryptomining**

### Incident Fields

- **LastMirroredInTime**
- **XDR Alert Category**
- **XDR Alert Count**
- **XDR Alert Name**
- **XDR Alert Search Results**
- **XDR Alerts**
- **XDR Assigned User Email**
- **XDR Assigned User Pretty Name**
- **XDR Description**
- **XDR Detection Time**
- **XDR device control violations**
- **XDR Disconnected endpoints**
- **XDR File Artifacts**
- **XDR File Name**
- **XDR File SHA256**
- **XDR High Severity Alert Count**
- **XDR Host Count**
- **XDR Incident ID**
- **XDR Investigation results**
- **XDR Low Severity Alert Count**
- **XDR manual severity**
- **XDR Medium Severity Alert Count**
- **XDR MITRE Tactics**
- **XDR MITRE Techniques**
- **XDR Modification Time**
- **XDR Network Artifacts**
- **XDR Notes**
- **XDR Resolve Comment**
- **XDR Risky Host Count**
- **XDR Risky Hosts**
- **XDR Risky User Count**
- **XDR Risky Users**
- **XDR Similar Incidents**
- **XDR Starred**
- **XDR Status v2**
- **XDR URL**
- **XDR User Count**
- **XDR Users**

### Indicator Fields

- XDR status: The indicator status in XDR.
- Fields from the **Common Types** pack.

### Indicator Types

- Types from the **Common Types** pack (such as File, Email, Domain, URL and more).

### Integrations

#### Cortex XDR - IOC

Allows to manage Indicators of Compromise (IOCs) seamlessly within Cortex XDR from Cortex XSOAR. This integration enables security teams to add, update, and remove IOCs efficiently, streamlining threat intelligence workflows and bolstering incident response capabilities.

#### Palo Alto Networks Cortex XDR - Investigation and Response

Allows security teams to automate and streamline incident response workflows by interacting directly with Cortex XDR. With this integration, users can investigate, respond to, and manage incidents efficiently within the Cortex XSOAR platform.
Key capabilities include retrieving incidents, isolating endpoints, executing remediation actions, and fetching forensic data to enhance incident investigation and resolution.

#### Cortex XDR - XQL Query Engine

Enables to execute XQL queries on your data sources within Cortex XSOAR, facilitating advanced threat hunting and data analysis.

### Layouts

- There are 6 layouts in this pack.
- The additional layouts, such as those for indicators, are sourced from the **Common Types** pack.
- The information displayed in the layouts is similar with minor changes as detailed below:

![XDR Case Info Tab](../../../docs/doc_imgs/reference/XDRLayout.png)

#### Cortex XDR Device Control Violations

| Layout sections | Description |
|------------------ | ------------- |
| Case Details | Displays the following information associated with the incident: Type, Severity, and Playbook. |
| XDR Device Control Violations | A table displaying the following information about the incident: host name, user name, IP address, violation type, and the date the violation occurred. |
| Affected Hosts Count | Color-coded field that displays the number of hosts affected by the incident. The color indication is as follows: green - 0 hosts, orange - 1-3 hosts, red - 4 or more hosts. |
| Affected Users Count | Color-coded field that displays the number of users affected by the incident. The color indication is as follows: green - 0 users, orange - 1-3 users, red - 4 or more users. |
| Notes | Comments entered by the user regarding the incident. |
| Linked Incidents | Displays any incident that is linked to the current incident. |
| Child Incidents | Displays any incident that is a child of the current incident. |


#### Cortex XDR Disconnected endpoints

| Layout sections | Description |
|------------------ | ------------- |
| Case Details | Displays the following information associated with the incident: Type, Source Instance, Severity, Owner, Playbook, and Source Brand.  |
| Affected Users Count | Color-coded field that displays the number of users affected by the incident. The color indication is as follows: green - 0 users, orange - 1-3 users, red - 4 or more users.  |
| Affected Hosts Count | Color-coded field that displays the number of hosts affected by the incident. The color indication is as follows: green - 0 hosts, orange - 1-3 hosts, red - 4 or more hosts.  |
| Notes | Comments entered by the user regarding the incident. |
| XDR Disconnected endpoints | Displays a table with the following information for the disconnected endpoints: Endpoint Name, Endpoint Status, Endpoint OS, Endpoint ID, and Endpoint Last Seen. |
| Disconnected endpoints report | Displays a report for the disconnected endpoints. |
| Linked Incidents | Displays any incident that are linked to this incident. |
| Child Incidents | Displays any incident that is a child of the current incident. |


#### Cortex XDR Incident
This layout has two tabs:

##### Case Info Tab

| Layout sections | Description |
|------------------ | ------------- |
| Case Details | Displays the following information associated with the incident: Type, Source Instance, Source Brand, Severity, Owner, and Playbook. |
| XDR Basic Information | Displays XDR basic information that includes: XDR description, XDR Incident ID, XDR Status v2, XDR Host Count, XDR User Count, XDR Notes, XDR URL, XDR Alert Count. |
| Related Alerts Severity | Displays the alerts severity in the XDR incident. |
| Affected Hosts Count | Color-coded field that displays the number of hosts affected by the incident. The color indication is as follows: green - 0 hosts, orange - 1-3 hosts, red - 4 or more hosts. |
| Affected Users Count | Color-coded field that displays the number of users affected by the incident. The color indication is as follows: green - 0 users, orange - 1-3 users, red - 4 or more users. |
| Timeline Information | Displays general information about the handling of the incident.|
| Team Members | Displays a list of the analysts who worked on this incident. |
| Notes | Comments entered by the user regarding the incident. |
| Evidence | Displays the data that analysts marked as evidence for this incident. |
| Linked Incidents | Displays the incidents that were linked to the current incident. |
| Child Incidents | Displays any incident that is a child of the current incident. |
| Closing Information | Displays the information that the analyst reported about closing the incident. |
| Mirroring Information | Displays general mirroring information for this incident. |

##### Investigation Tab

| Layout sections | Description |
|------------------ | ------------- |
| XDR Alerts | Displays the following XDR alert information: Alert ID, Detection Timestamp, Severity, Name, Category, Action, Action Pretty, Description, Host IP, Host Name, User Name, MITRE ATTACK TACTIC, and MITRE ATTACK TECHNIQUE, |
| XDR File Artifacts | Displays the following information about the XDR file artifacts: File Name, File SHA256, Alert Count, File Wildfire Verdict, File Signature Vendor Name, and File Signature Status. |
| XDR Network Artifacts | Displays the following information about the XDR network artifacts: Type, Alert Count, Is Manual, Network Domain, Network Remote IP, Network Remote Port, and Network Country. |
| XDR Endpoint Device Control Violations | Displays the following information about the XDR endpoint device control violations: Hostname, Username, IP, XdR endpoint ID, Violation type, and Date. |
| Indicators | Displays the following information about the indicators: Type, Value, Reputation, First Seen, and Last Seen. |
| Incident Files | Displays the Incident Files that can be seen in the War Room. |


#### Cortex XDR Port Scan

| Layout sections | Description |
|------------------ | ------------- |
| Case Details | Displays the following information associated with the incident: Type, Source Instance, Source Brand, Owner, and Playbook. |
| XDR Basic Information | Displays XDR basic information that includes: XDR Description, XDR Incident ID, XDR Status, XDR Host Count, XDR User Count, XDR Notes, XDR URL, XDR Alert Count, XDR High Severity, XDR Medium Severity, XDR Assigned User Email, Source IP, and Source Hostname. |
| Related Alerts Severity | Displays the alerts severity in the XDR incident. |
| Affected Hosts Count | Color-coded field that displays the number of hosts affected by the incident. The color indication is as follows: green - 0 hosts, orange - 1-3 hosts, red - 4 or more hosts. |
| Affected Users Count | Color-coded field that displays the number of users affected by the incident. The color indication is as follows: green - 0 users, orange - 1-3 users, red - 4 or more users. |
| Timeline Information | Displays general information about the handling of the incident. |
| Team Members | Displays a list of the analysts who worked on this incident. |
| Notes | Comments entered by the user regarding the incident. |
| Evidence | Displays the data that analysts marked as evidence for this incident. |
| Linked Incidents | Displays the incidents that were linked to the current incident. |
| Closing Information | Displays the information that the analyst reported about closing the incident. |

#### Cortex XDR - XCLOUD layout
This layout has two tabs:

##### Incident Info Tab

| Layout sections | Description |
|------------------ | ------------- |
|Incident Information | Displays XDR basic information that includes: XDR Description, XDR Incident ID, XDR URL, XDR Alert Category, XDR Alert Name, Created, XDR Host Count, XDR User Count, XDR Alert Count, XDR High Severity Alert Count, XDR Medium Severity Alert Count, and XDR Low Severity Count. | 
| Case Details | Displays the following information associated with the incident: Type, Severity, Source Brand, Source Instance, and Playbook. |
| Alert Severity | Displays the alert severity in the XDR incident. |
| Cloud Provider | Displays the host's cloud provider. |
| Users Count | Color-coded field that displays the number of users affected by the incident. The color indication is as follows: green - 0 users, orange - 1-3 users, red - 4 or more users. |
| Work Plan | Information regarding the playbook tasks from the Work Plan. You can view details by clicking the Tasks Pane or Work Plan links.  |
| Team Members | Displays a list of the analysts who worked on this incident. |
| Linked Incidents | Displays any incident that is linked to the current incident. |
| Notes | Comments entered by the user regarding the incident. |
| Mirroring Information | Displays general mirroring information for this incident, including Mirror Instance, Mirror Direction, Mirror External ID, Mirror Last Sync, Mirror Tags, and Incoming Mirror Error. |
| Closing Information | Displays the information that the analyst reported about closing the incident. |

##### Alert Info Tab

| Layout sections | Description |
|------------------ | ------------- |
| XDR Alerts | Displays alert information including: Alert ID, Detection Timestamp, Severity, Name, Category, Action, Action Pretty, Description, Host IP, Host Name, User Name, MITRE ATTACK TACTIC, and MITRE ATTACK TECHNIQUE. |
| Original Alert Additional Information | Displays the following information: Alert Full Description, Detection Module, Vendor, Provider, Log Name, Event Type, Caller IP, Caller IP Geo Location, Resource Type, Identity Name, Operation Name, Operation Status, and User Agent. |
| Identity Information | Displays the following information: Name, Type, Sub Type, Uuid, Provider, and Access Keys. |
| Remediation Actions Information | Displays the Inactive Access keys, and the Deleted Login Profiles. |
| Indicators | Displays the following information: Type, Value, Verdict, First Seen, Last Seen, Source Time Stamp Related Incidents, Source Brands, Source Instances, Expiration Status, and Expiration. |

### Dashboards

#### Cortex XDR

The dashboard includes 19 common widgets:

- Cortex XDR Top 10 MITRE Tactics
- Cortex XDR Top 10 MITRE Techniques
- Cortex XDR Top 10 Users
- Cortex XDR Unique User Count In Active Incidents
- Cortex XDR Top 10 Files
- Cortex XDR Connected Endpoints
- Cortex XDR Closed Incidents
- Cortex XDR Unique Host Count In Active Incidents
- Cortex XDR Disconnected Endpoints
- Cortex XDR Top 10 Categories
- Cortex XDR Active High Severity Incidents
- Cortex XDR Active Medium Severity Incidents
- Cortex XDR Top 10 File SHA 256
- Cortex XDR Active Low Severity Incidents
- Cortex XDR Top 10 Hosts
- Cortex XDR Unassigned Incidents
- Cortex XDR Active Device Control Violations Incidents
- Cortex XDR Closed Device Control Violations Incidents
- Cortex XDR Top 10 Alerts

### Playbooks
There are several playbooks in this pack.

#### [Cortex XDR - Check Action Status](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---check-action-status)
Checks the action status of an action ID. Enter the action ID of the action whose status you want to know.


#### [Cortex XDR - Isolate Endpoint](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---isolate-endpoint)
Accepts an XDR endpoint ID and isolates it using the [Palo Alto Networks Cortex XDR - Investigation and Response](https://xsoar.pan.dev/docs/reference/integrations/cortex-xdr---ir) integration.

#### [Cortex XDR - Unisolate Endpoint](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---unisolate-endpoint)
Accepts an XDR endpoint ID and unisolates it using the [Palo Alto Networks Cortex XDR - Investigation and Response](https://xsoar.pan.dev/docs/reference/integrations/cortex-xdr---ir) integration.

#### [Cortex XDR - Malware Investigation](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---malware-investigation)
Investigates a Cortex XDR incident containing  malware alerts. The playbook:
- Enriches the infected endpoint details.
- Lets the analyst manually retrieve the malicious file.
- Performs file detonation.

The playbook is used as a sub-playbook in the following playbooks:
- [Cortex XDR Incident Handling - v3](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-incident-handling-v3)
- [Cortex XDR Alerts Handling](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-alerts-handling)

#### [Cortex XDR - Port Scan](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---port-scan)
Investigates a Cortex XDR incident containing internal port scan alerts. The playbook:
- Syncs data with Cortex XDR.
- Enriches the hostname and IP address of the attacking endpoint.
- Notifies management about host compromise.
- Escalates the incident in case of lateral movement alert detection.
- Hunts malware associated with the alerts across the organization.
- Blocks detected malware associated with the incident.
- Blocks IPs associated with the malware.
- Isolates the attacking endpoint.
- Allows manual blocking of ports that were used for host login following the port scan.


The playbook is used as a sub-playbook in the following playbooks:
- [Cortex XDR Incident Handling - v3](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-incident-handling-v3)
- [Cortex XDR Alerts Handling](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-alerts-handling)

#### [Cortex XDR - Port Scan - Adjusted](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---port-scan---adjusted)
Investigates a Cortex XDR incident containing internal port scan alerts. The playbook:
- Syncs data with Cortex XDR.
- Notifies management about a compromised host.
- Escalates the incident in case of lateral movement alert detection.

#### [Cortex XDR - quarantine file](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---quarantine-file)
Accepts file paths, file hashes, and endpoint IDs in order to quarantine a selected file.

#### [Cortex XDR - Retrieve File Playbook](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---retrieve-file-playbook)
Retrieves files from selected endpoints. You can retrieve up to 20 files, from no more than 10 endpoints.
Inputs for this playbook are:
- A comma-separated list of endpoint IDs.
- A comma-separated list of file paths for your operating system, either Windows, Linux, or Mac. At least one file path is required.

#### [Cortex XDR Alerts Handling](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-alerts-handling)
Loops over every alert in a Cortex XDR incident. It is used as a sub-playbook in the [Cortex XDR incident handling v3](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-incident-handling-v3) playbook.
Currently, the supported alert categories are:
- Malware
- Port Scan

#### [Cortex XDR device control violations](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-device-control-violations)
Queries Cortex XDR for device control violations for the specified hosts, IP address, or XDR endpoint ID. It then communicates via email with the involved users to understand the nature of the incident and if the user connected the device. 
All the collected data is displayed in the XDR device control incident layout.
This playbook is also used as the response playbook for the [JOB - Cortex XDR query endpoint device control violations](https://xsoar.pan.dev/docs/reference/playbooks/job---cortex-xdr-query-endpoint-device-control-violations) playbook or as a sub-playbook in the [Cortex XDR Incident Handling - v3](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-incident-handling-v3). 

#### [JOB - Cortex XDR query endpoint device control violations](https://xsoar.pan.dev/docs/reference/playbooks/job---cortex-xdr-query-endpoint-device-control-violations)
A job to periodically fetch endpoint device control events and enrich the data associated with the endpoint device control events. It creates an incident if any violations are found.  The [Cortex XDR device control violations](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-device-control-violations) playbook is the response playbook for the violations found.

#### [Cortex XDR disconnected endpoints](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-disconnected-endpoints)
A job to periodically query disconnected Cortex XDR endpoints with a provided last seen time range playbook input.
The collected data generates a CSV report, including a detailed list of the disconnected endpoints.
The report will be sent to email addresses provided in the playbook input.
The playbook includes an incident type with a dedicated layout to visualize the collected data.

#### [Cortex XDR Lite - Incident Handling](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-lite---incident-handling)
This playbook is a lite default playbook to handle XDR incidents, and it doesn't require additional integrations to run.
The playbook is triggered by fetching a Palo Alto Networks Cortex XDR incident.
First, The playbook performs enrichment on the incident’s indicators.
Then, the playbook performs investigation and analysis on the command line and search for related Cortex XDR alerts by Mitre tactics to identify malicious activity performed on the endpoint and by the user.
Based on the enrichment and the investigation results, the playbooks sets the verdict of the incident. If malicious indicators are found, the playbook takes action to block these indicators and isolate the affected endpoint to prevent further damage or the spread of threats.
If the verdict not determined, it lets the analyst decide whether to continue to the remediation stage or close the investigation as benign. 
As part of this playbook, you'll receive a comprehensive layout that presents incident details, analysis, investigation findings, and the final verdict. Additionally, the layout offers convenient remediation buttons for quicker manual actions.

#### [Cortex XDR Incident Handling](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-incident-handling)
This playbook is triggered by fetching a Palo Alto Networks Cortex XDR incident. 
Syncs and updates new XDR alerts that construct the incident. It enriches indicators using Threat Intelligence integrations and Palo Alto Networks AutoFocus. The incident's severity is then updated based on the indicators' reputation and an analyst is assigned for manual investigation. If chosen, automated remediation with Palo Alto Networks FireWall is initiated. After a manual review by the SOC analyst, the XDR incident is closed automatically.

***Note*** - The **XDRSyncScript** used by this playbook sets data in the XDR incident fields that were released to content from the Cortex XSOAR server version 5.0.0. For Cortex XSOAR versions under 5.0.0, follow the Palo Alto Networks Cortex XDR documentation to upload the new fields manually.

#### [Cortex XDR incident handling v2](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-incident-handling-v2)
This playbook is triggered by fetching a Palo Alto Networks Cortex XDR incident.
The playbook syncs and updates new XDR alerts that construct the incident and triggers a sub-playbook to handle each alert by type.
Then, the playbook performs enrichment on the incident's indicators and hunting for related IOCs.
Based on the severity, it lets the analyst decide whether to continue to the remediation stage or close the investigation as a false positive. 
After the remediation, if there are no new alerts, the playbook stops the alert sync and closes the XDR incident and investigation.

#### [Cortex XDR incident handling v3](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-incident-handling-v3)
This playbook is triggered by fetching a Palo Alto Networks Cortex XDR incident, but only if the classifier is set to 'Cortex XDR - Classifier' and the incident type is left empty during the integration configuration.
The playbook syncs and updates new XDR alerts that construct the incident and triggers a sub-playbook to handle each alert by type.
Then, the playbook performs enrichment on the incident’s indicators and hunts for related IOCs.
Based on the severity, it lets the analyst decide whether to continue to the remediation stage or close the investigation as a false positive.
After the remediation, if there are no new alerts, the playbook stops the alert sync and closes the XDR incident and investigation. For performing the bidirectional sync, the playbook uses the incoming and outgoing mirroring feature added in XSOAR version 6.0.0. After the Calculate Severity - Generic v2 sub-playbook’s run, Cortex XSOAR will be treated as the single source of truth for the severity field, and it will sync only from Cortex XSOAR to XDR, so manual changes for the severity field in XDR will not update in the XSOAR incident.

#### [Cortex XDR Incident Sync](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-incident-sync)
Deprecated. Do not use this playbook when enabling the incident mirroring feature added in XSOAR version 6.0.0. Compares incidents in Palo Alto Networks Cortex XDR and Cortex XSOAR, and updates the incidents appropriately. When an incident is updated in Cortex XSOAR, the XDRSyncScript will update the incident in XDR. When an incident is updated in XDR, the XDRSyncScript will update the incident fields in Cortex XSOAR and rerun the current playbook.

#### [Cortex XDR - Block File](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---block-file)
Adds files to the Cortex XDR block list with a given file SHA256 playbook input.

#### [Cortex XDR - Delete file](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---delete-file)
Deletes the specified file and retrieves the results.

#### [Cortex XDR - Execute snippet code script](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---execute-snippet-code-script) 
Initiates a new endpoint script execution action using the provided snippet code and retrieve the file results. 

#### [Cortex XDR - Run script](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---run-script)
Initiates a new endpoint script execution action using a provided script unique ID from the Cortex XDR script library.

#### [Cortex XDR - check file existence](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---check-file-existence)
Checks if the specified file exists.

#### [Cortex XDR - execute commands](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---execute-commands)
Executes specified shell commands.

#### [Cortex XDR - kill process](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---kill-process)
Kills the specified process.

#### [Cortex XDR - Cloud IAM user access investigation](https://xsoar.pan.dev/docs/reference/playbooks/cloud-iam-user-access-investigation)
Investigates and responds to Cortex XDR Cloud alerts where an Cloud IAM user`s access key is used suspiciously to access the cloud environment.

The following alerts are supported for all cloud environments:
- Penetration testing tool attempt
- Penetration testing tool activity
- Suspicious API call from a Tor exit node

## Before You Start

### Required Content Packs
This Content Pack may require the following additional Content Packs:
- Active Directory Query
- Base
- Common Playbooks
- Common Types
- Core Alert Fields
- Malware Investigation and Response

### Optional Content Packs
- AutoFocus
- Core REST API
- EWS
- EWS Mail Sender
- Gmail
- Gmail Single User (Beta)
- Mail Sender (New)
- Microsoft Graph Mail Single User
- Microsoft Graph Mail
- PANW Comprehensive Investigation
- Port Scan
- ServiceNow
- Common Scripts
- Active Directory Query
- AWS - IAM
- Atlassian Jira
- Cloud Incident Response

### Pack Configurations
- [Creating an API Key and retrieve URL](#create-a-xdr-api-key-and-retrieve-url)
- [Device Control Violations Workflow](#device-control-violations-workflow)
- [Query Disconnected Cortex XDR Endpoints Workflow](#query-disconnected-cortex-xdr-endpoints-workflow)

#### Device Control Violations Workflow
1. Create a job to query for device control violations.  

   1. Click **Jobs**. 
   2. Click **New Job**.
   3. Configure the recurring schedule.
   3. Enter a name for the job.
   4. In the Type field, select *XDR Device Control Violations*.
   5. In the Playbook field, select **JOB - Cortex XDR query endpoint device control violations**. 
   6. Click **Create new job**.
   
      Note: For detailed information about creating jobs, see [Jobs](https://xsoar.pan.dev/docs/incidents/incident-jobs).

2. Define the inputs for the [JOB - Cortex XDR query endpoint device control violations](https://xsoar.pan.dev/docs/reference/playbooks/job---cortex-xdr-query-endpoint-device-control-violations).

   Note: The scheduled run time and the timestamp playbook input must be identical. If the job recurs every 7 days, the timestamp should be 7 days as well.
3. To run the response playbook for the violations found, define the inputs for the [Cortex XDR device control violations](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-device-control-violations).

#### Query Disconnected Cortex XDR Endpoints Workflow
1. Create a job to query the disconnected endpoints.
   1. Click **Jobs**.
   2. Click **New Job**.
   3. Configure the recurring schedule.
   3. Enter a name for the job.
   4. In the Type field, select *Cortex XDR disconnected endpoints*.
   5. In the Playbook field, select **Cortex XDR disconnected endpoints**.
   6. Click **Create new job**.

       Note: For detailed information about creating jobs, see [Jobs](https://xsoar.pan.dev/docs/incidents/incident-jobs).
2. Define the inputs for the [Cortex XDR disconnected endpoints](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-disconnected-endpoints) playbook.

   Note: The scheduled run time and the timestamp playbook input must be identical. If the job recurs every 7 days, the timestamp should be 7 days as well.

### Create A XDR API Key and Retrieve URL

#### Generate an API Key and Key ID

To enable secure communication with Cortex XDR, you need to generate an API Key and Key ID. Follow these steps:

1. In your Cortex XDR platform, go to **Settings** > **Configurations** > **API Keys**.
2. Click the **+New Key** button in the top right corner.
3. Set the **Security Level** to **Advanced** and select a **Role** appropriate for your permissions.
4. Copy the API Key displayed in the **Generated Key** field.
5. From the **ID** column, copy the Key ID.

#### Note 1

When configuring a role for the API Key's permission you can create a custom role or use a built-in role. The highest privileged built-in role is the Instance Admin. If you wish to use a built-in role with less permission but maximum command capabilities, use the Privileged Responder role.

#### Note 2

Securely store the API Key, as it will not be displayed again.

#### Retrieve API URL

1. In the Cortex XDR platform, go to **Settings**> **Configurations** > **API Keys**.
2. Click the **Copy API URL** button in the top-right corner.