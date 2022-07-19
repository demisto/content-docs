---
id: XSIAM-Playbooks
title: XSIAM Alert handling Playbooks
description: The XSIAM alerts handling playbooks included in this pack help you respond to Cortex XDR alerts in a timely manner. The playbooks are based on the MITRE ATT&CK tactics and techniques and the NIST framework Computer Security Incident Handling Guide.

---
The XSIAM alerts handling playbooks included in this pack help you respond to Cortex XDR alerts in a timely manner. The playbooks are based on the MITRE ATT&CK tactics and techniques and the NIST framework Computer Security Incident Handling Guide.

## MITRE ATT&CK Tactics and Techniques
MITRE ATT&CK is a globally-accessible knowledge base of the adversary [tactics](https://attack.mitre.org/tactics/enterprise/) and [techniques](https://attack.mitre.org/techniques/enterprise/) based on real-world observations.

The framework can be used by SOC and threat intelligence analysts, threat hunters, red teamers, and defenders to classify attacks better and assess risks for their organization.
Organizations can use the framework to identify gaps in their defenses, prioritize them, and take the necessary actions to remediate the threat.

Many cyber security systems classify incidents and reports based on the MITRE ATT&CK framework.

Cortex XSOAR uses the MITRE ATT&CK feed integration to ingest the information about these techniques and sub-techniques and many different integrations to retrieve indicators and incidents obtaining these techniques.

## NIST Framework - Computer Security Incident Handling Guide
[NIST's Computer Security Incident Handling Guide](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf) assists organizations in establishing computer security incident response capabilities and handling incidents efficiently and effectively. This publication provides guidelines for incident handling, particularly for analyzing incident-related data and determining the appropriate response to each incident.

## XSIAM Alerts - BIOCs and ABIOCs
Behavioral indicators of compromise (BIOCs) enable you to alert and respond to behaviors—tactics, techniques, and procedures. Instead of hashes and other traditional indicators of compromise, BIOC rules detect behavior related to processes, registry, files, and network activity.

Analytical behavioral indicators of compromise (ABIOCs) examine logs and data from your sensors on the Cortex XDR tenants to build an activity baseline and recognize abnormal activity when it occurs. The Analytics Engine accesses your logs as they are streamed to the Cortex XDR tenant, including any Firewall data forwarded by the Cortex Data Lake, and analyzes the data as soon as it arrives. Cortex XDR raises an Analytics alert when the Analytics Engine determines an anomaly.

## About this Pack
The Core pack playbooks were created to provide a dedicated response to XSIAM alerts based on MITER ATT&CK tactics and techniques or specific use cases.
The playbooks incorporate sub-playbooks which serve as modular functionality across all parent playbooks to investigate, contain, and eradicate the threat.

## Core Investigative and Response Playbooks

#### [Enrichment for Verdict](https://xsoar.pan.dev/docs/reference/playbooks/enrichment-for-verdict)
This playbook checks previous alert closing reasons and performs enrichment on different IOC types. It then returns the information needed to establish the alert's verdict.

The sub-playbooks being used as part of the verdict decision flow are:

- [File Reputation](https://xsoar.pan.dev/docs/reference/playbooks/file-reputation)
- [Domain Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/domain-enrichment---generic-v2)
- [URL Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/url-enrichment---generic-v2)
- [IP Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/ip-enrichment---generic-v2)
- [Account Enrichment - Generic v2.1](https://xsoar.pan.dev/docs/reference/playbooks/account-enrichment---generic-v21)
- [AWS IAM - User enrichment](https://xsoar.pan.dev/docs/reference/playbooks/aws-iam---user-enrichment)

The File Reputation playbook has some vital functionality you should be familiar with:

Enrichment sources and their outputs:

- XDR
    - The output is exported to a key called 'XDRFileSigners', which can be populated with 'Trusted' or 'Untrusted'. 
      
      The decision of whether the verdict is trusted is based on pre-defined input that contains trusted signers provided by the user compared to the suspicious file being analyzed.
- NSRL
    - The output is exported to a key called 'NSRLFileVerdict', which can be populated with 'isNSRL' or 'isNotNSRL'.
      
      The decision is based on an enrichment where we check if the file hash is present in the [NSRL database](https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl).
- VirusTotal
    - The outputs are exported to a key called 'VTFileSigners', which can be populated with 'Trusted' or 'Untrusted', and 'VTFileVerdict', which can be populated with 'Benign', 'Suspicious' or 'Malicious'. 
      
      The decision is based on a pre-defined input containing a threshold provided by the user, compared with the number of engined files detected as malicious.

#### [Endpoint Investigation Plan](https://xsoar.pan.dev/docs/reference/playbooks/endpoint-investigation-plan)
This playbook handles all the endpoint investigation actions available with Cortex XSIAM, including the following tasks:

- Pre-defined MITRE Tactics
- Host fields (Host ID)
- Attacker fields (Attacker IP, External host)
- MITRE techniques
- File hash (currently, the playbook supports only SHA256)

The Endpoint Investigation Plan provides a way for the analyst to hunt for suspicious activity using the XDR insights.
Insights are detectors that aim to identify suspicious or abnormal activity that is not necessarily malicious. These rules will usually come up before or after an actual alert and will be able to tell the story behind the malicious activity.

For example, creating a new task via the command prompt is not necessarily malicious. Still, it might be vital information if it is part of malicious activity detected on an endpoint.

#### [Containment Plan](https://xsoar.pan.dev/docs/reference/playbooks/containment-plan)
This playbook handles all the alert containment actions available with Cortex XSIAM, including the following tasks:

- Isolate endpoint
- Disable account
- Quarantine file
- Block indicators
- Clear user session (currently, the playbook supports only Okta)

The Containment Plan provides a way for the analyst to contain a threat in a modular way where he can turn on/off any action he would like to execute using the playbook inputs.

Executing a containment action such as 'Quarantine file' manually will prompt the user with a question already populated with files he might want to quarantine.

#### [Eradication Plan](https://xsoar.pan.dev/docs/reference/playbooks/eradication-plan)
This playbook handles all the eradication actions available with Cortex XSIAM, including the following tasks:

- Reset user password
- Delete file
- Kill process (currently, the playbook supports terminating a process by name)

The Eradication Plan provides a way for the analyst to eradicate a threat in a modular way where he can turn on/off any action he would like to execute using the playbook inputs.

Executing an eradication action such as 'Kill process' manually will prompt the user with a question already populated with processes he might want to terminate.

#### [Recovery Plan](https://xsoar.pan.dev/docs/reference/playbooks/recovery-plan)
This playbook handles all the recovery actions available with Cortex XSIAM, including the following tasks:

- Unisolate endpoint
- Restore the quarantined file

The Recovery Plan allows the analyst to revert containment actions taken on the endpoint.

#### [Handle False Positive Alerts](https://xsoar.pan.dev/docs/reference/playbooks/handle-false-positive-alerts)

This playbook handles false positive alerts, and provide the user with one or more of the following handling actions:

- Add an [alert exclusion](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-prevent-admin/investigation-and-response/investigate-endpoint-alerts/alert-exclusions/add-an-alert-exclusion)
- Add an [alert exception](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-pro-admin/endpoint-security/exceptions-security-profiles/add-exceptions-profile)
- Add the file hash to an [allow list](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/allow-list-files)

## Core Playbooks

The Core playbooks provide a tailored response to some of the most common XDR alerts. These playbooks were created after dedicated research on the relevant alert/technique and are built using a modular approach. The sub-playbooks mentioned above provide the core functionality needed as part of the incident response process with custom content relevant for each use case.

- [IOC Alert]()
- [NGFW Scan](https://xsoar.pan.dev/docs/reference/playbooks/ngfw-scan)
- [WildFire Malware](https://xsoar.pan.dev/docs/reference/playbooks/wild-fire-malware)
- [Ransomware Response](https://xsoar.pan.dev/docs/reference/playbooks/ransomware-response)
- [T1036 - Masquerading](https://xsoar.pan.dev/docs/reference/playbooks/t1036---masquerading)
- [Impossible Traveler Response](https://xsoar.pan.dev/docs/reference/playbooks/impossible-traveler-response)
- [Local Analysis Alert Investigation](https://xsoar.pan.dev/docs/reference/playbooks/local-analysis-alert-investigation)
- [AWS IAM User Access Investigation](https://xsoar.pan.dev/docs/reference/playbooks/aws-iam-user-access-investigation)
- [T1059 - Command and Scripting Interpreter](https://xsoar.pan.dev/docs/reference/playbooks/mitre-attck-co-a---t1059---command-and-scripting-interpreter)

## Playbook Flow Demonstration
### [T1059 - Command and Scripting Interpreter](https://xsoar.pan.dev/docs/reference/playbooks/mitre-attck-co-a---t1059---command-and-scripting-interpreter)

This playbook handles command and scripting interpreter alerts based on the MITRE T1059 technique. An attacker might abuse command and script interpreters to execute commands, scripts, or binaries. Most systems come with some built-in command-line interface and scripting capabilities. For example, macOS and Linux distributions include some Unix Shell, while Windows installations include the Windows Command Shell and PowerShell.

The playbook's flow is as follows:

1. Retrieves the command line.
2. Executes the 'Command-Line Analysis' sub-playbook. This playbook takes the command line from the alert and performs the following actions:

    1. Checks for a base64 string and decodes it if it exists.
    2. Extracts and enriches indicators from the command line.
    3. Checks specific arguments for malicious usage.

    At the end of the playbook, it sets a possible verdict for the command line based on the findings:

    - Indicators found in the command line.
    - Found AMSI techniques.
    - Found suspicious parameters.
    - Usage of malicious tools.
    - Indication of network activity.
3. Findings analysis.

    If the results are that the command line is malicious, the playbook proceeds to step 4. Otherwise, the playbook will proceed and execute the **Handle False Positive Alerts** sub-playbook.
4. Executes the **Containment Plan** sub-playbook based on the results of the findings.
5. Executes the **Endpoint Investigation Plan** sub-playbook to look for additional activity around the alert detection timestamp.
6. Executes the **Containment and Eradication Plan** sub-playbook based on the investigation results.
7. Executes the *Recovery Plan* if set to True in the playbook's inputs.
8. Closes the alert.

![T1059_-_Command_and_Scripting_Interpreter](https://user-images.githubusercontent.com/28757135/176421698-95fb873f-e06d-4cb4-8e09-cdb7a54ec888.png)
