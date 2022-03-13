---
id: courses-of-action
title: MITRE ATT&CK - Courses of Action
description: This MITRE ATT&CK - Courses of Action pack contains intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team that integrate with MITRE ATT&CK techniques and sub-techniques to automate protection against common known vectors.
---

This MITRE ATT&CK - Courses of Action pack contains intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team that integrate with MITRE ATT&CK techniques and sub-techniques to automate protection against common known vectors.
Read these instructions carefully to first understand the workflows that this pack executes and understand how the pack must be configured and implemented.

## MITRE ATT&CK Tactics and Techniques
MITRE ATT&CK is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations.
The framework can be used by SOC and threat intelligence analysts, threat hunters, red teamers, and defenders to better classify attacks and assess risks for their organization.
Organizations can use the framework to identify gaps in their defenses, prioritize them, and take the necessary actions to remediate the threat.
Many different cyber security systems classify incidents and reports based on the MITRE ATT&CK framework.
Cortex XSOAR uses the MITRE ATT&CK feed integration to ingest the information about these techniques and sub-techniques, and many different integrations to retrieve indicators and incidents obtaining these techniques.

## Courses of Action
Unit 42 is the Palo Alto Networks threat intelligence and security research team. They compile reports about different attacks, for example SolarStorm. The reports show the different techniques that are relevant for a given attack, as well as the indicators from the attack and courses of action. The courses of action are generic recommendations on how to protect your network against certain attacks. For example, blocking certain ports or being aware of an attack profile, etc. The courses of action are not specific to an attack, rather they are general recommendations for dealing with a certain technique.

## About this Pack
The COA pack receives techniques from different methods, and automates the implementation of the courses of action. The pack currently covers approximately 35 different techniques and will be updated as automation for more techniques becomes available.
Following is a list of optional dependency packs to compliment the use of this pack:

### MITRE ATT&CK Feed

Includes the MITRE ATT&CK feed integration which generates the MITRE ATT&CK technique indicators in the v1 version of the pack, and the Attack Pattern indicators in the v2 version of the pack. Also includes the dashboard to see techniques across open incidents. Using the dashboard, customers can see the top techniques in their environment and then act upon them using the CoA pack.

While this pack is not a mandatory dependency, Cortex XSOAR recommends you install it for a better user experience. Without configuring this feed, Mitre Att&ck techniques are not clickable nor do they show any details from Mitre. 

The Courses of Action pack and playbooks work with both versions of the MITRE ATT&CK pack.
- See v1 integration documentation here: [MITRE ATT&CK Feed](https://xsoar.pan.dev/docs/reference/integrations/mitre-attck)
- See v2 integration documentation here: [MITRE ATT&CK Feed v2](https://xsoar.pan.dev/docs/reference/integrations/mitre-attck-v2)

### Unit 42 Feed

Palo Alto Networks' research team, Unit42, publishes Actionable Threat Objects and Mitigations (ATOMs). These ATOMs can be viewed in their playbook viewer - https://pan-unit42.github.io/playbook_viewer/.

When configuring the feed, indicators of type STIX report are created in XSOAR. In the v1 version of the Unit 42 integration, MITRE Techniques are referenced as feed-related indicators under this STIX report indicator. Each MITRE Technique is clickable and provides a quick view. You can click a specific technique for more information from MITRE. 

In the v2 version of the Unit 42 integration, each report stores relationships with campaign indicator objects, and under the campaigns you will see relationships with many other indicator objects, including MITRE ATT&CK - Attack Patterns.

The Courses of Action pack and playbooks work with both versions of the Unit 42 pack.
- See v1 integration documentation here: [Unit42 Feed](https://xsoar.pan.dev/docs/reference/integrations/unit42-feed)
- See v2 integration documentation here: [Unit 42 ATOMs Feed](https://xsoar.pan.dev/docs/reference/integrations/unit42v2-feed)

### Palo Alto Networks PAN-OS

Licenses are needed in order to set certain profiles for protection:
- DNS Security
- Threat Prevention
- URL filtering
- Wildfire

If you have questions about your licenses, contact your Palo Alto Networks account manager for future guidance and assistance.

***Policy changes should be done carefully. Each playbook has an approval flow. You can choose to manually do them or automate parts of the flow after approval is granted.***

***All flows are supported for both FW and Panorama and will be executed according to the PAN-OS integration instance configuration settings.***

See integration documentation - https://xsoar.pan.dev/docs/reference/integrations/panorama

### Palo Alto Networks Cortex XDR - Investigation and Response

See integration documentation - https://xsoar.pan.dev/docs/reference/integrations/cortex-xdr---ir

## Before You Start
The techniques that will be handled using the playbooks in this pack are determined by the technique ID data, which can be ingested and forwarded to the playbook using any of the following methods:
* Specific technique trigger - Remediate specific techniques using their corresponding CoA playbook. For example, techniques fetched from the MITRE ATT&CK feed.
* From an incident - For incident types that include techniques in the incident layout, the incident handling playbook can include the **MITRE ATT&CK - Courses of Action** wrapper playbook as a sub-playbook. In this case, all of the associated techniques will be remediated by CoAs in addition to the specific IOC. 
Possible incidents: Cortex XDR incidents and alerts.
* Unit 42 and other Feed integrations - Fetch indicators from threat intelligence feeds that store MITRE ATT&CK techniques under the “Feed Related Indicators” grid field.
For example, fetch STIX reports from the Unit42 feed integration and store the techniques that are related to the threat brief under the “Feed Related Indicators” table, which can be used as a trigger to the playbooks in this pack.
Possible indicator types that are used to store MITRE ATT&CK techniques include STIX Report, STIX Malware, etc.

***This method requires a Cortex XSOAR TIM license.*** 

* Job - Use a job to trigger the **MITRE ATT&CK - Courses of Action** wrapper playbook to keep the environment up to date with all relevant CoAs.
## Trigger CoA Playbooks
The CoA playbooks can be triggered in several ways:

### Investigate specific techniques using manual trigger

Manually create an incident with type "MITRE ATT&CK CoA". Insert a technique ID or a comma-separated list of technique IDs to the **Techniques List** incident field in the incident's creation form. This incident will automatically trigger the **MITRE ATT&CK - Courses of Action** playbook which handles the techniques.

Users can form a list of their techniques of interest using any source that is relevant to their environment.

Cortex XSOAR recommends using the MITRE ATT&CK dashboard (from the MITRE ATT&CK pack), so you can see the top techniques by incidents in your environment and then act upon them using the CoA pack using this method.

### Embedded within existing incident workflow -  Sub-Playbook

The **MITRE ATT&CK - Courses of Action** playbook can be used as a sub-playbook in any incident handling playbook for a 3rd party tool that is mapping it's incidents to MITRE ATT&CK techniques. This way, the incident will be handled in 2 directions:
- The specific "IOCs-driven" approach - Investigating and remediating IOCs that are linked to the incident (block IP, isolate endpoint, file quarantine, etc.)
- A more holistic approach taking actions against MITRE ATT&CK techniques which can be used in many different incidents.

For example, the Cortex XDR incidents from the Cortex XDR integration now include the MITRE techniques, so remediation can include the Courses of Action approach.

### Scheduled Job - Compliance

You can ensure that your environment is protected against MITRE ATT&CK techniques in a time-triggered recurring manner. Use the **MITRE ATT&CK Courses of Action Trigger Job** to trigger the technique handling playbook and make sure you stay compliant.

### Intelligence Feed triggered Job - Act upon threat reports *(TIM License recommended)*

Trigger the **MITRE ATT&CK Courses of Action Trigger Job** playbook with a feed query, using a job triggered by a delta in the feed to act upon threat intelligence reports received from TIM feed integrations. The query comes predefined and is specific to the Unit 42 Feed, but you can edit the query to use any threat intelligence feed.

For example, use the Unit 42 feed integration to fetch Unit 42 ATOMs and remediate the techniques used by recent malware and threat actors.

After the relevant playbooks execute, the pack-specific incident types show the number of techniques that need to be handled, techniques that were already addressed, and pending tasks.

## In this Pack
### Automations
- **EntryWidgetCoAHandled** - Entry widget that returns the number of handled techniques in a Courses of Action incident.
- **EntryWidgetCoATechniquesList** - Entry widget that returns the number of unhandled techniques in a Courses of Action incident.

### Incident types
**MITRE ATT&CK CoA** - The incident type that is created manually or by the **MITRE ATT&CK Courses of Action Trigger Job** playbook, triggering the **MITRE ATT&CK: MITRE ATT&CK - Courses of Action** playbook that performs remediations on the given techniques.

### Layouts
After an incident is created, the MITRE Layout is associated to the **MITRE ATT&CK CoA** incident type. The incident's layout gathers all of the remediation data and allows the analysts to take action.

The MITRE Layout incidents layout contains the following tabs:

- **Incident Info tab** - Gives the analyst the general information about the incident. It displays the techniques that were already handled by the playbooks, the incidents that were not handled, the indicators that are a part of the incident, and all other general data.

   This tab also displays the Work Plan section, which allows the analyst to take action on manual and conditional tasks that require their attention.

![image](https://user-images.githubusercontent.com/43776787/129564272-12055211-5ea3-4202-b0a1-4db83fc9ffc4.png)

- **Executed Remediation Summary tab** - This layout tab displays information about the products that were used for remediating techniques in each of the MITRE ATT&CK kill chain phases.

![image](https://user-images.githubusercontent.com/43776787/129564814-f942b6ea-df10-4f74-9681-e1c2590505f5.png)

- **Best Practices tab** - This layout tab displays information about best practices profiles in PAN-OS.
In this section you will be able to see what profiles were created through the remediation playbook's run, and the BPA scan results for best practices enforcement in your environment.

![image](https://user-images.githubusercontent.com/43776787/129565110-ecfbd8c2-334b-4c46-bedf-77cf892f5be1.png)


## Playbooks
### MITRE ATT&CK Parent Playbook - Containing all phases
**Name: MITRE ATT&CK - Courses of Action**

This is the parent playbook, which contains all phases and remediates MITRE ATT&CK techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks' Unit 42 team. The playbook utilizes several other MITRE ATT&CK remediation playbooks.

The playbook follows the MITRE ATT&CK kill chain phases and takes action to protect the organization from the inputted techniques, displaying and implementing security policy recommendations for Palo Alto Networks products.

***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs).***

**Possible playbook triggers:**
* The playbook can be triggered by a feed integration fetching indicators that contain MITRE ATT&CK techniques as “Feed Related Indicators”, using the playbook query.
* The playbook can be triggered manually for specific MITRE ATT&CK techniques using the *techniqueByIncident* playbook input.
* An incident that contains MITRE ATT&CK technique IDs using the *techniqueByIncident* playbook input.
### MITRE ATT&CK Kill Chain Phases Remediation Playbooks
**Example: Courses of Action - Collection**

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks' Unit 42 team.

***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs).***

**Techniques Handled:** - T1005 - Data from Local System

**Kill Chain phase:** - Collection

**MITRE ATT&CK Description:** - 
The adversary attempts to gather data of interest to accomplish their goal.

Collection consists of techniques adversaries may use to gather information, as well as the sources from which information is collected, to follow through on the adversary’s objectives. Frequently, the next goal after collecting data is to steal (exfiltrate) the data. Common target sources include various drive types, browsers, audio, video, and email. Common collection methods include capturing screenshots and keyboard input.

**Possible playbook triggers:**

The playbook can be used as a part of the **Courses of Action - Collection** playbook to remediate techniques based on kill chain phase.

The playbook can be used as a part of the **MITRE ATT&CK - Courses of Action** playbook, that can be triggered by different sources and accepts the technique MITRE ATT&CK ID as an input.
### Technique Specific Remediation Playbooks
**Example: MITRE ATT&CK: T1003 - OS Credential Dumping**

This playbook remediates the OS Credential Dumping technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks' Unit 42 team.

***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs).***

**Techniques Handled:** - T1003: OS Credential Dumping

**Kill Chain phases:** - Defense Evasion

**MITRE ATT&CK Description:** - 
Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password, from the operating system and software. Credentials can then be used to perform lateral movement and to access restricted information.

**Possible playbook uses:**
* The playbook can be used independently to handle and remediate the specific technique.
* The playbook can be used as a part of the **Courses of Action - Defense Evasion** playbook to remediate techniques based on the kill chain phase.
* The playbook can be used as a part of the **MITRE ATT&CK - Courses of Action** playbook, which can be triggered by different sources and accepts the technique MITRE ATT&CK ID as an input.
### PAN-OS Best Practices Playbooks
**Name: PAN-OS - Enforce Anti-Spyware Best Practices Profile**

This playbook enforces the Anti-Spyware Best Practices Profile as defined by Palo Alto Networks BPA.

The playbook performs the following tasks:
* Checks for DNS Security license (If license is not activated, the playbook refers users to their Palo Alto Networks account manager for further instructions).
* Gets the existing profile information.
* Gets the best practices profile information.
* Checks if the best practices profile set by Cortex XSOAR is enforced. (If not, the playbook allows the user to compare the existing profile with the best practices and decide on the action to take).
* Creates a best practices profile.
* Applies the profile to policy rules on the PAN-OS firewall or Panorama.
### Palo Alto Networks BPA - Submit Scan
This playbook accepts a list of BPA checks, triggers a job and returns the checks results. It will be triggered if the **Best Practice Assessment** integration is available, through the Courses of Action remediation stages playbooks, to return information about the best practices enforcement in your environment, which are a part of the remediation workflow. The results from this playbook will be shown in the *Best Practices* layout tab.

## Demo Video
<video controls>
    <source src="https://github.com/demisto/content-assets/raw/master/Assets/MITRECoA/coa_demo.mp4"
            type="video/mp4"/>
    Sorry, your browser doesn't support embedded videos. You can download the video at: https://github.com/demisto/content-assets/raw/master/Assets/MITRECoA/coa_demo.mp4 
</video>


