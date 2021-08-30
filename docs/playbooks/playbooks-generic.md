---
id: playbooks-generic
title: Generic Playbooks
description: Generic playbooks article.
---

The playbooks listed in this article are frequently used playbooks that are part of the Common Playbooks pack.
 
These playbooks are created out of the box to support common tasks that are a part of the analyst workflow.
 
The playbooks should be accessible and usable to different users and don’t depend on specific integrations to achieve their final goal, and they do so by supporting all of the integrations that support the specific use-case that is a part of the playbook’s flow.
 
All of the playbooks in this list can be used independently or as a sub-playbook to support a larger use-case.



## Generic playbooks mapped by use case

|  Generic Playbook   |  Description |   Use Cases | 
|---|---|---|
| [Account Enrichment - Generic v2.1](https://xsoar.pan.dev/docs/reference/playbooks/account-enrichment---generic-v21)  | Enrich accounts using one or more integrations. Supported integrations: - Active Directory | IAM |  
| [Block Account - Generic](https://xsoar.pan.dev/docs/reference/playbooks/block-account---generic)| This playbook blocks malicious usernames using all integrations that you have enabled. Supported integrations for this playbook: - Active Directory - PAN-OS (This requires PAN-OS 9.1 or higher.) | IAM | 
|[Block Email - Generic](https://xsoar.pan.dev/docs/reference/playbooks/block-email---generic)| This playbook will block emails at your mail relay integration. | Email Gateway |
| [Block File - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/block-file---generic-v2) | This playbook is used to block files from running on endpoints. This playbook supports the following integrations: - Palo Alto Networks Traps - Palo Alto Networks Cortex XDR - Cybereason - Carbon Black Enterprise Response - Cylance Protect v2 | Endpoint |
|[Block Indicators - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/block-indicators---generic-v2) | This playbook blocks malicious Indicators using all integrations that are enabled, using the following sub-playbooks: - Block URL - Generic - Block Account - Generic - Block IP - Generic v2 - Block File - Generic v2 | Data Enrichment and Threat Intelligence |
|[Block IP - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/block-ip---generic-v2) | This playbook blocks malicious IPs using all integrations that are enabled. Supported integrations for this playbook: * Check Point Firewall * Palo Alto Networks Minemeld * Palo Alto Networks PAN-OS * Zscaler * FortiGate | Network Security |
|[Block URL - Generic](https://xsoar.pan.dev/docs/reference/playbooks/block-url---generic) | This playbook blocks malicious URLs using all integrations that are enabled. Supported integrations for this playbook: * Palo Alto Networks Minemeld * Palo Alto Networks PAN-OS * Zscaler | Network Security |
|[Convert file hash to corresponding hashes](https://xsoar.pan.dev/docs/reference/playbooks/convert-file-hash-to-corresponding-hashes) | The playbook enables you to get all of the corresponding file hashes for a file even if there is only one hash type available. For example, if we have only the SHA256 hash, the playbook will get the SHA1 and MD5 hashes as long as the original searched hash is recognized by any of the threat intelligence integrations. | Forensics and Malware |
|[CVE Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/cve-enrichment---generic-v2) | This playbook performs CVE Enrichment using the following integrations: - VulnDB - CVE Search - IBM X-Force Exchange | Data Enrichment and Threat Intelligence |
|[Detonate File - Generic](https://xsoar.pan.dev/docs/reference/playbooks/detonate-file---generic) | Detonate file through active integrations that support file detonation. | Forensics and Malware |
|[Detonate URL - Generic](https://xsoar.pan.dev/docs/reference/playbooks/detonate-url---generic) | Detonate URL through active integrations that support URL detonation | Forensics and Malware |
|[Domain Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/domain-enrichment---generic-v2) | Enrich domains using one or more integrations. Domain enrichment includes: * Threat information | Data Enrichment and Threat Intelligence |
|[Email Address Enrichment - Generic v2.1](https://xsoar.pan.dev/docs/reference/playbooks/email-address-enrichment---generic-v21) | Enrich email addresses. - Get information from Active Directory for internal addresses - Get the domain-squatting reputation for external addresses | Data Enrichment and Threat Intelligence |
|[Endpoint Enrichment - Generic v2.1](https://xsoar.pan.dev/docs/reference/playbooks/endpoint-enrichment---generic-v21) | Enrich an endpoint by hostname using one or more integrations. Supported integrations: - Active Directory Query v2 - McAfee ePolicy Orchestrator - Carbon Black Enterprise Response v2 - Cylance Protect v2 - CrowdStrike Falcon Host - ExtraHop Reveal(x) | Endpoint |
|[Entity Enrichment - Generic v3](https://xsoar.pan.dev/docs/reference/playbooks/entity-enrichment---generic-v3) | Enrich entities using one or more integrations. | Data Enrichment and Threat Intelligence |
|[Extract Indicators From File - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/extract-indicators-from-file---generic-v2) | Extracts indicators from a file. Supported file types: - CSV - PDF - TXT - HTM, HTML - DOC, DOCX - PPT - PPTX - RTF - XLS | Forensics and Malware |
|[File Enrichment - File reputation](https://xsoar.pan.dev/docs/reference/playbooks/file-enrichment---file-reputation) | Get file reputation using one or more integrations. | Data Enrichment and Threat Intelligence |
|[File Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/file-enrichment---generic-v2) | Enrich a file using one or more integrations. - Provide threat information | Data Enrichment and Threat Intelligence |
|[Get endpoint details - Generic](https://xsoar.pan.dev/docs/reference/playbooks/get-endpoint-details---generic) | This playbook uses the generic command !endpoint to retrieve details on a specific endpoint. This command currently supports the following integrations: - Palo Alto Networks Cortex XDR - Investigation and Response. - CrowdStrike Falcon. | Endpoint |
|[Get File Sample By Hash - Generic v3](https://xsoar.pan.dev/docs/reference/playbooks/get-file-sample-by-hash---generic-v3) | This playbook returns a file sample correlating to a hash in the War Room using the following sub-playbooks: - Get binary file by MD5 hash from Carbon Black telemetry data - VMware Carbon Black EDR v2. - Get the threat (file) attached to a specific SHA256 hash - Cylance Protect v2. | Endpoint |
|[Get File Sample From Path - Generic V3](https://xsoar.pan.dev/docs/reference/playbooks/get-file-sample-from-path---generic-v3) | This playbook returns a file sample from a specified path and host that you input in the following playbooks: 1) PS Remote Get File Sample From Path. 2) Get File Sample From Path - VMware Carbon Black EDR (Live Response API). | Endpoint |
|[Get host forensics - Generic](https://xsoar.pan.dev/docs/reference/playbooks/get-host-forensics---generic) | This playbook retrieves forensics from hosts. The available integration: - Illusive networks. | Forensics and Malware |
|[Get Original Email - Generic](https://xsoar.pan.dev/docs/reference/playbooks/get-original-email---generic) | Use this playbook to retrieve the original email in the thread, including headers and attahcments, when the reporting user forwarded the original email not as an attachment. You must have the necessary permissions in your email service to execute global search. - EWS: eDiscovery - Gmail: Google Apps Domain-Wide Delegation of Authority | Email Gateway |
|[IP Enrichment - External - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/ip-enrichment---external---generic-v2) | Enrich IP addresses using one or more integrations. - Resolve IP addresses to hostnames (DNS) - Provide threat information - Separate internal and external addresses | Data Enrichment and Threat Intelligence |
|[IP Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/ip-enrichment---generic-v2) | Enrich IP addresses using one or more integrations. - Resolve IP addresses to hostnames (DNS) - Provide threat information - Separate internal and external IP addresses - For internal IP addresses, get host information | Data Enrichment and Threat Intelligence |
|[IP Enrichment - Internal - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/ip-enrichment---internal---generic-v2) | Enrich Internal IP addresses using one or more integrations. - Resolve IP address to hostname (DNS) - Separate internal and external IP addresses - Get host information for IP addresses | Data Enrichment and Threat Intelligence |
|[Isolate Endpoint - Generic V2](https://xsoar.pan.dev/docs/reference/playbooks/isolate-endpoint---generic-v2) | This playbook isolates a given endpoint via various endpoint product integrations. Make sure to provide the valid playbook input for the integration you are using. | Endpoint |
|[Retrieve File from Endpoint - Generic V3](https://xsoar.pan.dev/docs/reference/playbooks/retrieve-file-from-endpoint---generic-v3) | This playbook retrieves a file sample from an endpoint using the following playbooks:' - Get File Sample From Path - Generic v2. - Get File Sample By Hash - Generic v3. | Endpoint |
|[Search And Delete Emails - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/search-and-delete-emails---generic-v2) | This playbook searches and delete emails with similar attributes of a malicious email using EWS or Office 365. | Email Gateway |
|[Search Endpoint by CVE - Generic](https://xsoar.pan.dev/docs/reference/playbooks/solar-storm-and-sunburst-hunting-and-response-playbook#sub-playbooks) | Hunt for assets with a given CVE using available tools | Vulnerability Management |
|[Search Endpoints By Hash - Generic V2](https://xsoar.pan.dev/docs/reference/playbooks/search-endpoints-by-hash---generic-v2) | Hunt using available tools. | Endpoint |
|[Threat Hunting - Generic](https://xsoar.pan.dev/docs/reference/playbooks/threat-hunting---generic) | This playbook enables threat hunting for IOCs in your enterprise. This playbook currently supports the following integrations: - Splunk - Qradar - Pan-os - Cortex data lake - Autofocus | Threat Hunting |
|[Unisolate Endpoint - Generic](https://xsoar.pan.dev/docs/reference/playbooks/unisolate-endpoint---generic) | This playbook unisolates endpoints according to the endpoint ID or hostname that is provided in the playbook. Currently supports the following integrations: - Carbon Black Response - Cortex XDR - Crowdstrike Falcon - FireEye HX - Cybereason | Endpoint |
|[URL Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/url-enrichment---generic-v2) | Enrich URLs using one or more integrations. URL enrichment includes: * SSL verification for URLs * Threat information * Providing of URL screenshots | Network Security |






