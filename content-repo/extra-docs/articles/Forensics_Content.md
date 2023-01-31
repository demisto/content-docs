---
id: Digital-Forensics-Content
title: Digital Forensics Content Roundup
description: Article listing all Cortex XSOAR content that is currently available to support digital forensic analysis and investigations.
---
This page aggregates Cortex XSOAR content that is currently available to support forensic analysis and investigations.

## Endpoint Response/Analysis/Triage Packs
####  The following packs are compatible with the [Malware Investigation and Response](https://xsoar.pan.dev/docs/reference/packs/malware-investigation-and-response) pack:
| Pack Name | Available Functionality |
| --- | --- |
| [Palo Alto Networks Cortex XDR - Investigation and Response](https://xsoar.pan.dev/docs/reference/packs/palo-alto-networks-cortex-xdr---investigation-and-response) | <ul><li>Retrieve files from an endpoint based on the path with the  `xdr-file-retrieve` command.</li><li>Execute a Python script on an endpoint with the `xdr-script-run` command.</li><li>Execute a snippet of Python code on an endpoint with the  `xdr-snippet-code-script-execute` command. Then get results with the `xdr-get-script-execution-results` command. </li><li>Run an OS shell (i.e., Windows Command or Unix bash) command on an endpoint with the `xdr-script-commands-execute` command. Then get the results with the `xdr-get-script-execution-results` command.</li><li>Execute an XQL query with the `xdr-xql-*-query` commands.</li></ul> |
| [CrowdStrike Falcon](https://cortex.marketplace.pan.dev/marketplace/details/CrowdStrikeFalcon/) | <ul><li>Perform CrowdStrike Real Time Response (RTR) operations on an endpoint (retrieve files, list network/process/scheduled tasks information, read registry data, etc.) with the  `cs-falcon-rtr-*` commands.</li><li>Run any RTR command on an endpoint (list files, get file hashes, dump memory, etc.) with the `cs-falcon-run-command` command.</li><li>Retrieve files across hosts with the  `cs-falcon-run-get-command` command. </li><li>Execute a PowerShell script on an endpoint with the `cs-falcon-run-script` command.</li></ul> |
| [Microsoft Defender for Endpoint](https://cortex.marketplace.pan.dev/marketplace/details/MicrosoftDefenderAdvancedThreatProtection/) | <ul><li>Retrieve files associated with an alert with the `microsoft-atp-get-alert-related-files` command.</li><li>Execute a script on an endpoint with the `microsoft-atp-live-response-run-script` command.</li><li>Perform other live response operations on an endpoint with the `microsoft-atp-live-response-*` commands.</li></ul> | 

#### Other response/analysis/triage packs:
| Pack Name | Available Functionality |
| --- | --- |
| [Cyber Triage](https://cortex.marketplace.pan.dev/marketplace/details/CyberTriage/) | Send a triage tool to an endpoint to acquire and analyze forensic artifacts with the `ct-triage-endpoint` command. |
| [FireEye HX](https://cortex.marketplace.pan.dev/marketplace/details/FireEyeHX/) (integration [FireEye Endpoint Security (HX) v2](https://xsoar.pan.dev/docs/reference/integrations/fire-eye-hx-v2)) | <ul><li>Perform triage data acquisition from an endpoint and fetch the data as a MANS file with the following commands: <ul><li>`fireeye-hx-data-acquisition`</li> <li>`fireeye-hx-initiate-data-acquisition`</li><li>`fireeye-hx-get-data-acquisition`</li></ul></li><li>The MANS file can then be passed into FireEye HX apps like [Redline](https://fireeye.market/apps/211364) for further analysis.</li></ul> |
| [Illusive Networks](https://cortex.marketplace.pan.dev/marketplace/details/IllusiveNetworks/) | <ul><li>Collect forensic data from an endpoint and generate a forensic timeline on-demand with the `illusive-run-forensics-on-demand` command.</li><li>Retrieve forensic artifacts from Illusive with the `illusive-get-forensics-artifacts` command.</li><li>Retrieve a forensic timeline for an incident with the  `illusive-get-forensics-timeline` command.</li></ul> |
| [Infocyte](https://cortex.marketplace.pan.dev/marketplace/details/Infocyte/) | <ul><li>Acquire forensic artifacts and save to an S3 bucket with the `infocyte-collect-evidence` command.</li><li>Run [Infocyte extension](https://github.com/Infocyte/extension-docs) on an endpoint with the `infocyte-run-response` command.</li><li>Initiate an Infocyte scan to collect data from an endpoint with the `infocyte-scan-host` command.</li></ul> |
| [Tanium Threat Response](https://cortex.marketplace.pan.dev/marketplace/details/TaniumThreatResponse/) | <ul><li>Download a file from an endpoint with the `tanium-tr-create-connection` command (to create connection) and the `tanium-tr-request-file-download` command (to initiate download), and then run the  `tanium-tr-get-downloaded-file` command (to get file contents).</li><li>Capture evidence from an event (process) with the `tanium-tr-create-evidence` command. List evidence with the `tanium-tr-event-evidence-list` command and return with the`tanium-tr-get-evidence-by-id` command.</li></ul> |

## Packs for Dedicated Forensics Tools
| Pack Name | Available Functionality |
| --- | --- |
| [Exterro/AccessData](https://cortex.marketplace.pan.dev/marketplace/details/Exterro/) | Trigger an automation workflow in Exterro FTK Connect with the `exterro-ftk-trigger-workflow` command. |

## Analysis Tools Packs
| Pack Name | Available Functionality |
| --- | --- |
| [ExifRead](https://cortex.marketplace.pan.dev/marketplace/details/ExifRead/) | Return an image file metadata and EXIF tags with the `ExifRead` automation.</li></ul> |
| [Oletools](https://cortex.marketplace.pan.dev/marketplace/details/Oletools/) | Analyze potentially malicious Microsoft Word, Microsoft Excel, and other Microsoft OLE2 files using the [oletools](https://github.com/decalage2/oletools) analysis tools with the `Oletools` automation. |
| [PCAP Analysis](https://cortex.marketplace.pan.dev/marketplace/details/PcapAnalysis/) | <ul><li>Analyze packet capture (PCAP) files using the `PcapMinerV2` automation.</li><li>Extract streams and files, respectively, from PCAP files using the `PcapFileExtractStreams` and `PcapFileExtractor` automations.</li></ul> |
| [Volatility](https://cortex.marketplace.pan.dev/marketplace/details/Volatility/) | Perform memory forensics analysis by running the [Volatility](https://www.volatilityfoundation.org/) tool on a remote analysis server over SSH (using the [RemoteAccess v2 integration](https://xsoar.pan.dev/docs/reference/integrations/remote-access-v2)) with the `AnalyzeMemImage` automation (which includes some common memory analysis commands) and the other automations in this pack. |
| [Windows Forensics](https://xsoar.pan.dev/docs/reference/packs/Windows_Forensics) | <ul><li>Acquire and analyze a few key forensic artifacts from Windows hosts using the [PowerShell Remoting integration](https://xsoar.pan.dev/docs/reference/integrations/power-shell-remoting) with the `Acquire And Analyze Host Forensics` playbook:<ul><li>Acquire artifacts (network traffic data, Master File Table (MFT), and registry hives) with the  `PS-Remote Acquire Host Forensics` sub-playbook.</li><li>Perform an analysis of the artifacts with the `Forensics Tools Analysis` sub-playbook.</li></ul></li><li>Parse out important registry keys with the `RegistryParse` automation.</li></ul> |

## Data Acquisition Tools Packs
| Pack Name | Available Functionality |
| --- | --- |
| [Binalyze AIR](https://cortex.marketplace.pan.dev/marketplace/details/Binalyze/) | Perform targeted evidence acquisition from an endpoint with the `binalyze-air-acquire` command. |
| [Cado Response](https://cortex.marketplace.pan.dev/marketplace/details/CadoResponse/) | Trigger disk acquisition and processing in Cado Response with the `cado-trigger-ec2` and `cado-trigger-s3` commands. |

## Cloud Forensics
| Pack Name | Available Functionality |
| --- | --- |
| [Prisma Cloud Compute by Palo Alto Networks](https://cortex.marketplace.pan.dev/marketplace/details/PrismaCloudCompute/) | <ul><li>Get detailed event data for an endpoint from Prisma Cloud Forensics with the `prisma-cloud-compute-host-forensic-list` command.</li><li>Get runtime forensics data for a specific container on a specific endpoint with the `prisma-cloud-compute-profile-container-forensic-list` command.</li></ul> |
| [Office 365 and Azure (Audit Log)](https://cortex.marketplace.pan.dev/marketplace/details/Office365AndAzureAuditLog/) | Search the Office 365 unified audit log, which includes events across various Microsoft/Azure products, with the `o365-auditlog-search` command. |
| [GsuiteAuditor](https://cortex.marketplace.pan.dev/marketplace/details/GsuiteAuditor/) | Search for audit log events across various Google Workspace products with the `gsuite-activity-search` command. |

## Forensics Case Management
| Pack Name | Available Functionality |
| --- | --- |
| [CaseManagement-Generic](https://cortex.marketplace.pan.dev/marketplace/details/CaseManagementGeneric/) | Use `Case Management Layout v2` as inspiration or a jumping-off point for a forensics case management layout to keep track of evidence items, indicators of compromise, incident timeline, affected hosts/users, etc. |

## Conclusion

For more digital forensics content ideas, search Marketplace by keyword or filter using the  "Forensics" tag.

<img width="1207" alt="Screen Shot 2023-01-08 at 12 45 31 PM" src="https://user-images.githubusercontent.com/91506078/211215821-ead5063e-72a0-4833-bfe7-f161c0b0d3f0.png">
