---
id: Digital-Forensics-Content
title: Digital Forensics Content Roundup
description: Article listing all Cortex XSOAR content that is currently available to support digital forensic analysis and investigations.

---
This page aggregates Cortex XSOAR content that is currently available to support forensic analysis and investigations.

## Endpoint Response/Analysis/Triage Packs
#### Currently compatible with the [Malware Investigation and Response](https://xsoar.pan.dev/docs/reference/packs/malware-investigation-and-response) pack:
| Pack Name | Available Functionality |
| --- | --- |
| [Palo Alto Networks Cortex XDR - Investigation and Response](https://xsoar.pan.dev/docs/reference/packs/palo-alto-networks-cortex-xdr---investigation-and-response) | <ul><li>Retrieve files from endpoint based on path with command `xdr-file-retrieve`</li><li>Execute Python script on endpoint with command `xdr-script-run`</li><li>Execute snippet of Python code on endpoint with command `xdr-snippet-code-script-execute`; then get results with command `xdr-get-script-execution-results`</li><li>Run OS shell (i.e., Windows Command or Unix bash) command on endpoint with command `xdr-script-commands-execute`; then get results with command `xdr-get-script-execution-results`</li><li>Execute XQL query with commands `xdr-xql-*-query`</li></ul> |
| [CrowdStrike Falcon](https://cortex.marketplace.pan.dev/marketplace/details/CrowdStrikeFalcon/) | <ul><li>Perform CrowdStrike Real Time Response (RTR) operations on endpoint (retrieve files, list network/process/scheduled tasks information, read registry data, etc.) with commands `cs-falcon-rtr-*`</li><li>Run any RTR command on endpoint (list files, get file hashes, dump memory, etc.) with command `cs-falcon-run-command`</li><li>Retrieve files across hosts with command `cs-falcon-run-get-command`</li><li>Execute PowerShell script on endpoint with command `cs-falcon-run-script`</li></ul> |
| [Microsoft Defender for Endpoint](https://cortex.marketplace.pan.dev/marketplace/details/MicrosoftDefenderAdvancedThreatProtection/) | <ul><li>Retrieve files associated with alert with command `microsoft-atp-get-alert-related-files`</li><li>Execute script on endpoint with command `microsoft-atp-live-response-run-script`</li><li>Perform other live response operations on endpoint with commands `microsoft-atp-live-response-*`</li></ul> | 

#### Other response/analysis/triage packs:
| Pack Name | Available Functionality |
| --- | --- |
| [Cyber Triage](https://cortex.marketplace.pan.dev/marketplace/details/CyberTriage/) | <ul><li>Send triage tool to endpoint to acquire and analyze forensic artifacts with command `ct-triage-endpoint`</li></ul> |
| [Illusive Networks](https://cortex.marketplace.pan.dev/marketplace/details/IllusiveNetworks/) | <ul><li>Collect forensic data from endpoint and generate forensic timeline on-demand with command `illusive-run-forensics-on-demand`</li><li>Retrieve forensic artifacts from Illusive with command `illusive-get-forensics-artifacts`</li><li>Retrieve forensic timeline for an incident with command `illusive-get-forensics-timeline`</li></ul> |
| [Infocyte](https://cortex.marketplace.pan.dev/marketplace/details/Infocyte/) | <ul><li>Acquire forensic artifacts and save to S3 bucket with command `infocyte-collect-evidence`</li><li>Run [Infocyte extension](https://github.com/Infocyte/extension-docs) on endpoint with command `infocyte-run-response`</li><li>Initiate Infocyte scan to collect data from endpoint with command `infocyte-scan-host`</li></ul> |
| [Tanium Threat Response](https://cortex.marketplace.pan.dev/marketplace/details/TaniumThreatResponse/) | <ul><li>Download file from endpoint with commands `tanium-tr-create-connection` (to create connection), `tanium-tr-request-file-download` (to initiate download), and then `tanium-tr-get-downloaded-file` (to get file contents)</li><li>Capture evidence from event (process) with command `tanium-tr-create-evidence`; list evidence with command `tanium-tr-event-evidence-list` and return with `tanium-tr-get-evidence-by-id`</li></ul> |

## Packs for Dedicated Forensics Tools
| Pack Name | Available Functionality |
| --- | --- |
| [Exterro/AccessData](https://cortex.marketplace.pan.dev/marketplace/details/Exterro/) | <ul><li>Trigger automation workflow in Exterro FTK Connect with command `exterro-ftk-trigger-workflow`</li></ul> |

## Analysis Tools Packs
| Pack Name | Available Functionality |
| --- | --- |
| [ExifRead](https://cortex.marketplace.pan.dev/marketplace/details/ExifRead/) | <ul><li>Return image file metadata and EXIF tags with automation `ExifRead`</li></ul> |
| [Oletools](https://cortex.marketplace.pan.dev/marketplace/details/Oletools/) | <ul><li>Analyze potentially malicious Microsoft Word, Microsoft Excel, and other Microsoft OLE2 files using the [oletools](https://github.com/decalage2/oletools) analysis tools with automation `Oletools`</li></ul> |
| [PCAP Analysis](https://cortex.marketplace.pan.dev/marketplace/details/PcapAnalysis/) | <ul><li>Analyze packet capture (PCAP) files using automation `PcapMinerV2`</li><li>Extract streams and files, respectively, from PCAP files using automations `PcapFileExtractStreams` and `PcapFileExtractor`</li></ul> |
| [Volatility](https://cortex.marketplace.pan.dev/marketplace/details/Volatility/) | <ul><li>Perform memory forensics analysis by running the [Volatility](https://www.volatilityfoundation.org/) tool on a remote analysis server over SSH (using the [RemoteAccess v2 integration](https://xsoar.pan.dev/docs/reference/integrations/remote-access-v2)) with the automation `AnalyzeMemImage` (which includes some common memory analysis commands) and the other automations in this pack</li></ul> |
| [Windows Forensics](https://xsoar.pan.dev/docs/reference/packs/Windows_Forensics) | <ul><li>Acquire and analyze a few key forensic artifacts from Windows hosts using the [PowerShell Remoting integration](https://xsoar.pan.dev/docs/reference/integrations/power-shell-remoting) with playbook `Acquire And Analyze Host Forensics`:<ul><li>Acquire artifacts (network traffic data, Master File Table (MFT), and registry hives) with subplaybook `PS-Remote Acquire Host Forensics`</li><li>Perform analysis of the artifacts with subplaybook `Forensics Tools Analysis`</li></ul></li><li>Parse out important registry keys with automation `RegistryParse`</li></ul> |

## Data Acquisition Tools Packs
| Pack Name | Available Functionality |
| --- | --- |
| [Binalyze AIR](https://cortex.marketplace.pan.dev/marketplace/details/Binalyze/) | <ul><li>Perform targeted evidence acquisition from endpoint with command `binalyze-air-acquire`</li></ul> |
| [Cado Response](https://cortex.marketplace.pan.dev/marketplace/details/CadoResponse/) | <ul><li>Trigger disk acquisition and processing in Cado Response with commands `cado-trigger-ec2` and `cado-trigger-s3`</li></ul> |

## Cloud Forensics
| Pack Name | Available Functionality |
| --- | --- |
| [Prisma Cloud Compute by Palo Alto Networks](https://cortex.marketplace.pan.dev/marketplace/details/PrismaCloudCompute/) | <ul><li>Get detailed event data for endpoint from Prisma Cloud Forensics with command `prisma-cloud-compute-host-forensic-list`</li><li>Get runtime forensics data for specific container on specific endpoint with command `prisma-cloud-compute-profile-container-forensic-list`</li></ul> |
| [Office 365 and Azure (Audit Log)](https://cortex.marketplace.pan.dev/marketplace/details/Office365AndAzureAuditLog/) | <ul><li>Search the Office 365 unified audit log, which includes events across various Microsoft/Azure products, with command `o365-auditlog-search`</li></ul> |
| [GsuiteAuditor](https://cortex.marketplace.pan.dev/marketplace/details/GsuiteAuditor/) | <ul><li>Search for audit log events across various Google Workspace products with command `gsuite-activity-search`</li></ul> |

## Forensics Case Management
| Pack Name | Available Functionality |
| --- | --- |
| [CaseManagement-Generic](https://cortex.marketplace.pan.dev/marketplace/details/CaseManagementGeneric/) | <ul><li>Use the `Case Management Layout v2` as inspiration or a jumping-off point for a forensics case management layout to keep track of evidence items, indicators of compromise, incident timeline, affected hosts/users, etc.</li></ul> |

## Conclusion

For more digital forensics content ideas, search the Marketplace by keyword or filter by tag "Forensics".

<img width="1207" alt="Screen Shot 2023-01-08 at 12 45 31 PM" src="https://user-images.githubusercontent.com/91506078/211215821-ead5063e-72a0-4833-bfe7-f161c0b0d3f0.png">
