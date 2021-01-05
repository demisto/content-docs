This MITRE ATT&CK - Courses of Action pack contains intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team that will enable you to handle MITRE ATT&CK techniques and sub-techniques in an organized and automated manner.
Read these instructions carefully to first understand the workflows that this pack executes and understand how the pack must be configured and implemented.
 
# MITRE ATT&CK Tactics and Techniques
 
MITRE ATT&CK is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. 
The framework can be used by SOC and threat intelligence analysts, threat hunters, red teamers, and defenders to better classify attacks and assess risks for their organization. 
Organizations can use the framework to identify gaps in their defenses, prioritize them, and take the necessary actions to remediate the threat.
 
Different cyber security systems classify incidents and reports based on the MITRE ATT&CK framework.
Cortex XSOAR uses the MITRE ATT&CK feed integration to ingest the information about these techniques and sub-techniques, and many different integrations to retrieve indicators and incidents obtaining these techniques.
 
# Pack Workflows
Supported most prevalent techniques:
1) T1071: Application Layer Protocol
2) T1566.001: Spearphishing Attachment
3) T1105: Ingress Tool Transfer
4) T1059: Command and Scripting Interpreter
5) T1059.001: PowerShell
6) T1547: Boot or Logon Autostart Execution
7) T1547.001: Registry Run Keys / Startup Folder"
8) T1082: System Information Discovery"

# Before You Start
The techniques that will be handled using the playbooks in this pack are determined by the techniques ID data, which can be ingested and forwarded to the playbook by methods:
Unit 42 and other Feed integrations - Fetch indicators from threat intelligence feeds that store MITRE ATT&CK techniques under the “Feed Related Indicators” grid field. 
For examples - Fetching STIX reports from the Unit42 feed integration stores the techniques that are related to the threat brief under the “Feed Related Indicators” table, and can be used as a trigger to the playbooks in this pack.
Possible indicator types to store MITRE ATT&CK techniques: STIX Report, STIX Malware, etc.
*** This method requires a Cortex XSOAR TIM license.	
From incident - For incident types that include techniques in the incident layout, the incident handling playbook can include the “MITRE ATT&CK - Courses of Action'' wrapper playbook as a sub-playbook. In this case, all of the associated techniques will be remediated by CoAs in addition to the specific IOCs.
Possible incidents: Cortex XDR incidents and alerts.
Specific technique trigger - Remediate specific techniques using their corresponding COA playbook.
Example - techniques fetched from the MITRE ATT&CK feed.
Job - Use a job to trigger the “MITRE ATT&CK - Courses of Action” wrapper playbook to keep the environment up to date with all relevant CoAs.
Pack Configurations
To configure and use the playbooks in this pack, you should do the following:
 
# Playbook Triggers and configuration:
 
Feed integrations - To use a feed integration for triggering the playbooks in this pack:
Create a playbook query to query the indicators to retrieve MITRE ATT&CK techniques from, through the “Feed Related Indicators” indicator field. 
Example: type:"STIX Report" and feedrelatedindicators.type:"MITRE ATT&CK"
Go to the “Playbook Triggered” section of the “MITRE ATT&CK - Courses of Action - Job” playbook.
Insert the query to the `Query` field in the “From Indicators” tab.
Create a job to be “Triggered by delta in feed” and choose the “MITRE ATT&CK - Courses of Action - Job” playbook in the configuration.
For documentation about Cortex XSOAR jobs, please visit https://xsoar.pan.dev/docs/incidents/incident-jobs
The job will create an incident from type “MITRE ATT&CK CoA” where you can follow the remediation process and take manual steps for engaging.
*** This method requires a Cortex XSOAR TIM license.
 
From an incident - To use an incident for triggering the playbook:
Associate the incident to one of the playbooks in this pack or use them as a sub-playbook in any incident handling playbook in the marketplace.
Pass a comma-separated list of MITRE ATT&CK techniques to the `techniqueByIncident` input in the “MITRE ATT&CK - Courses of Action” playbook or to the `technique` input in any of the other playbooks in the pack.
Specific technique trigger - Manually trigger any of the technique-specific playbooks in this pack.
Job - To use a job to trigger the playbook:
Create a playbook query to query the indicators to retrieve MITRE ATT&CK techniques from, through the “Feed Related Indicators” indicator field. 
Example: type:"STIX Report" and feedrelatedindicators.type:"MITRE ATT&CK"
Go to the “Playbook Triggered” section of the “MITRE ATT&CK - Courses of Action - Job” playbook.
Insert the query to the `Query` field in the “From Indicators” tab.
Create a job and choose the “MITRE ATT&CK - Courses of Action - Job” playbook in the configuration.
The job will create an incident from type “MITRE ATT&CK CoA” where you can follow the remediation process and take manual steps for engaging.
 
OR
Populate the `techniqueByIncident`input in the “MITRE ATT&CK - Courses of Action - Job” playbook.
Create a job and choose the “MITRE ATT&CK - Courses of Action - Job” playbook in the configuration.
For documentation about Cortex XSOAR jobs, please visit https://xsoar.pan.dev/docs/incidents/incident-jobs
The job will create an incident from type “MITRE ATT&CK CoA” where you can follow the remediation process and take manual steps for engaging.
 
# Playbooks:

## MITRE ATT&CK Parent playbook - Containing all phases:
MITRE ATT&CK: MITRE ATT&CK - Courses of Action

This is the parent playbook, which contains all phases and remediates MITRE ATT&CK techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. The playbook utilizes several other MITRE ATT&CK remediation playbooks.
 
The playbook follows the MITRE ATT&CK kill chain phases and takes action to protect the organization from the inputted techniques, displaying and implementing security policy recommendations for Palo Alto Networks products.
 
***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs).
Possible playbook triggers:
The playbook can be triggered by a feed integration fetching indicators that contain MITRE ATT&CK techniques as “Feed Related Indicators”, using the playbook query.
The playbook can be triggered manually for specific MITRE ATT&CK techniques using the ‘techniqueByIncident’ playbook input.
An incident that contains MITRE ATT&CK technique IDs using the ‘techniqueByIncident’ playbook input.

## MITRE ATT&CK Kill Chain phases remediation playbooks:
Example: MITRE ATT&CK: Courses of Action - Collection


This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team.
 
***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs).
 
Techniques Handled:
T1005 - Data from Local System
Kill Chain phase:
Collection
MITRE ATT&CK Description:
 
The adversary is attempting to gather data of interest to accomplish their goal.
 
Collection consists of techniques adversaries may use to gather information and the sources information is collected from that are relevant to following through on the adversary’s objectives. Frequently, the next goal after collecting data is to steal (exfiltrate) the data. Common target sources include various drive types, browsers, audio, video, and email. Common collection methods include capturing screenshots and keyboard input.
Possible playbook triggers:
The playbook can be used as a part of the “Courses of Action - Collection” playbook to remediate techniques based on kill chain phase.
The playbook can be used as a part of the “MITRE ATT&CK - Courses of Action” playbook, that can be triggered by different sources and accepts the technique MITRE ATT&CK ID as an input.

# Technique specific remediation playbooks:

##Example: MITRE ATT&CK: T1003 - OS Credential Dumping - Courses of Action

This playbook Remediates the OS Credential Dumping technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team.
 
***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs).
Techniques Handled:
T1003: OS Credential Dumping
Kill Chain phases:
Defense Evasion
MITRE ATT&CK Description:
 
Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password, from the operating system and software. Credentials can then be used to perform Lateral Movement and to access restricted information.
Possible playbook uses:
The playbook can be used independently to handle and remediate the specific technique.
The playbook can be used as a part of the “Courses of Action - Defense Evasion” playbook to remediate techniques based on the kill chain phase.
The playbook can be used as a part of the “MITRE ATT&CK - Courses of Action” playbook, which can be triggered by different sources and accepts the technique MITRE ATT&CK ID as an input.
 
## PAN-OS Best Practices playbooks:
 
Name: PAN-OS - Enforce Anti-Spyware Best Practices Profile
 
This playbook enforces the Anti-Spyware Best Practices Profile as defined by Palo Alto Networks BPA.
 
The playbook performs the following tasks:
Check for DNS Security license (If license is not activated, the playbook refers users to their Palo Alto Networks account manager for further instructions).
Get the existing profile information.
Get the best practices profile information.
Check if the best practices profile set by Cortex XSOAR is enforced. (If not, the playbook allows the user to compare the existing profile with the best practices and decide on the action to take).
Create best practices profile.
Apply profile to policy rules on PAN-OS firewall or Panorama.
