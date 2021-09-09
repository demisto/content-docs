---
id: playbooks-generic
title: Generic Playbooks
description: Generic playbooks article.
---

The playbooks listed in this article are frequently used playbooks that are part of the Common Playbooks pack.
 
These playbooks are created out-of-the-box to support common tasks that are a part of the analyst workflow.
 
The playbooks should be accessible and usable to different users. They don’t depend on specific integrations to achieve their final goal. The playbooks support all of the integrations that support use-cases that are part of the playbook’s flow.
 
All of the playbooks in this list can be used independently or as a sub-playbook to support a larger use-case.



## Generic playbooks mapped by use case

|  Generic Playbook   |  Description |   Use Cases | 
|---|---|---|
| [Account Enrichment - Generic v2.1](https://xsoar.pan.dev/docs/reference/playbooks/account-enrichment---generic-v21)  | Enriches accounts using all enabled account management integrations. | IAM |  
| [Block Account - Generic](https://xsoar.pan.dev/docs/reference/playbooks/block-account---generic)| Blocks malicious usernames using all enabled integrations. | IAM | 
|[Block Email - Generic](https://xsoar.pan.dev/docs/reference/playbooks/block-email---generic)| Blocks emails at your mail relay integration. | Email Gateway |
| [Block File - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/block-file---generic-v2) | Blocks files from running on endpoints using all enabled Endpoint integrations. | Endpoint |
|[Block Indicators - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/block-indicators---generic-v2) |Blocks malicious indicators using all integrations that are enabled, using the following sub-playbooks: <br/>- Block URL - Generic <br/>- Block Account - Generic <br/>- Block IP - Generic v2 <br/>- Block File - Generic v2 | Data Enrichment and Threat Intelligence |
|[Block IP - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/block-ip---generic-v2) |Blocks malicious IPs using all enabled network security integrations. | Network Security |
|[Block URL - Generic](https://xsoar.pan.dev/docs/reference/playbooks/block-url---generic) | Blocks malicious URLs using all enabled network security integrations. | Network Security |
|[Convert file hash to corresponding hashes](https://xsoar.pan.dev/docs/reference/playbooks/convert-file-hash-to-corresponding-hashes) | Enables you to get all of the corresponding file hashes for a file even if there is only one hash type available. For example, if you have only the SHA256 hash, the playbook will get the SHA1 and MD5 hashes as long as the original searched hash is recognized by any of the threat intelligence integrations. | Forensics and Malware |
|[CVE Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/cve-enrichment---generic-v2) | Performs CVE Enrichment using all enabled vulnerability management integrations. | Data Enrichment and Threat Intelligence |
|[Detonate File - Generic](https://xsoar.pan.dev/docs/reference/playbooks/detonate-file---generic) | Detonates files through active integrations that support file detonation. | Forensics and Malware |
|[Detonate URL - Generic](https://xsoar.pan.dev/docs/reference/playbooks/detonate-url---generic) | Detonates URLs through active integrations that support URL detonation. | Forensics and Malware |
|[Domain Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/domain-enrichment---generic-v2) | Enriches domains using all enabled Data Enrichment and Threat Intelligence integrations.<br/>Domain enrichment includes: Threat information | Data Enrichment and Threat Intelligence |
|[Email Address Enrichment - Generic v2.1](https://xsoar.pan.dev/docs/reference/playbooks/email-address-enrichment---generic-v21) | Enriches email addresses. <br/>- Gets information from Active Directory for internal addresses. <br/>- Gets the domain-squatting reputation for external addresses. | Data Enrichment and Threat Intelligence |
|[Endpoint Enrichment - Generic v2.1](https://xsoar.pan.dev/docs/reference/playbooks/endpoint-enrichment---generic-v21) | Enriches an endpoint by hostname using all enabled Endpoint integrations. | Endpoint |
|[Entity Enrichment - Generic v3](https://xsoar.pan.dev/docs/reference/playbooks/entity-enrichment---generic-v3) | Enriches entities using one or more integrations. | Data Enrichment and Threat Intelligence |
|[Extract Indicators From File - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/extract-indicators-from-file---generic-v2) | Extracts indicators from a file. <br/>Supported file types: <br/>- CSV <br/>- PDF <br/>- TXT <br/>- HTM, HTML <br/>- DOC, DOCX <br/>- PPT, PPTX <br/>- RTF <br/>- XLS | Forensics and Malware |
|[File Enrichment - File reputation](https://xsoar.pan.dev/docs/reference/playbooks/file-enrichment---file-reputation) | Gets the file reputation using one or more integrations. | Data Enrichment and Threat Intelligence |
|[File Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/file-enrichment---generic-v2) | Enriches a file using one or more integrations. <br/>Provides threat information. | Data Enrichment and Threat Intelligence |
|[Get endpoint details - Generic](https://xsoar.pan.dev/docs/reference/playbooks/get-endpoint-details---generic) | Uses the generic command ***!endpoint*** to retrieve details on a specific endpoint. | Endpoint |
|[Get File Sample By Hash - Generic v3](https://xsoar.pan.dev/docs/reference/playbooks/get-file-sample-by-hash---generic-v3) | Returns a file sample correlating to a hash in the War Room using the following sub-playbooks: <br/>- VMware Carbon Black EDR v2 - Get binary file by MD5 hash from Carbon Black telemetry data. <br/>- Cylance Protect v2 - Get the threat (file) attached to a specific SHA256 hash. | Endpoint |
|[Get File Sample From Path - Generic V3](https://xsoar.pan.dev/docs/reference/playbooks/get-file-sample-from-path---generic-v3) | Returns a file sample from a specified path and host that you input in the following playbooks: <br/>- PS Remote Get File Sample From Path. <br/> - Get File Sample From Path - Carbon Black Enterprise Response. | Endpoint |
|[Get host forensics - Generic](https://xsoar.pan.dev/docs/reference/playbooks/get-host-forensics---generic) | Retrieves forensics from hosts using all enabled forensice & malware analysis integrations. | Forensics and Malware |
|[Get Original Email - Generic](https://xsoar.pan.dev/docs/reference/playbooks/get-original-email---generic) | Retrieve the original email in the thread, including headers and attachments, when the reporting user forwarded the original email not as an attachment. You must have the necessary permissions in your email service to execute global search. <br/>- EWS: eDiscovery <br/>- Gmail: Google Apps Domain-Wide Delegation of Authority | Email Gateway |
|[IP Enrichment - External - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/ip-enrichment---external---generic-v2) | Enriches IP addresses using one or more integrations. <br/>- Resolves IP addresses to host names (DNS)<br/> - Provides threat information <br/>- Separates internal and external addresses | Data Enrichment and Threat Intelligence |
|[IP Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/ip-enrichment---generic-v2) | Enriches IP addresses using one or more integrations. <br/>- Resolves IP addresses to host names (DNS) <br/>- Provides threat information <br/>- Separates internal and external IP addresses<br/> - For internal IP addresses, get host information | Data Enrichment and Threat Intelligence |
|[IP Enrichment - Internal - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/ip-enrichment---internal---generic-v2) | Enriches internal IP addresses using one or more integrations. <br/>- Resolves IP address to hostname (DNS) <br/>- Separates internal and external IP addresses <br/>- Gets host information for IP addresses | Data Enrichment and Threat Intelligence |
|[Isolate Endpoint - Generic V2](https://xsoar.pan.dev/docs/reference/playbooks/isolate-endpoint---generic-v2) | Isolates a given endpoint via various endpoint product integrations. | Endpoint |
|[Retrieve File from Endpoint - Generic V3](https://xsoar.pan.dev/docs/reference/playbooks/retrieve-file-from-endpoint---generic-v3) | Retrieves a file sample from an endpoint using the following playbooks: <br/>- Get File Sample From Path - Generic v2. <br/>- Get File Sample By Hash - Generic v3. | Endpoint |
|[Search And Delete Emails - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/search-and-delete-emails---generic-v2) | Searches and deletes emails with similar attributes of a malicious email using EWS or Office 365. | Email Gateway |
|[Search Endpoint by CVE - Generic](https://xsoar.pan.dev/docs/reference/playbooks/solar-storm-and-sunburst-hunting-and-response-playbook#sub-playbooks) | Hunts for assets with a given CVE using available tools. | Vulnerability Management |
|[Search Endpoints By Hash - Generic V2](https://xsoar.pan.dev/docs/reference/playbooks/search-endpoints-by-hash---generic-v2) | Hunts using all available tools. | Endpoint |
|[Threat Hunting - Generic](https://xsoar.pan.dev/docs/reference/playbooks/threat-hunting---generic) |Enables threat hunting for IOCs in your enterprise using all enabled supported integrations. | Threat Hunting |
|[Unisolate Endpoint - Generic](https://xsoar.pan.dev/docs/reference/playbooks/unisolate-endpoint---generic) | Unisolates endpoints according to the endpoint ID or hostname that is provided in the playbook. | Endpoint |
|[URL Enrichment - Generic v2](https://xsoar.pan.dev/docs/reference/playbooks/url-enrichment---generic-v2) | Enriches URLs using one or more integrations. URL enrichment includes: <br/>- SSL verification for URLs <br/>- Threat information <br/>- Providing of URL screenshots | Network Security |






