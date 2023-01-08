---
id: Forensics-Content
title: Forensics Content Roundup
description: Article listing all Cortex XSOAR content that is currently available to support forensic analysis and investigations.

---
This page aggregates Cortex XSOAR content that is currently available to support forensic analysis and investigations.

## Endpoint Response/Analysis/Triage Packs
Currently compatible with the [Malware Investigation and Response](https://xsoar.pan.dev/docs/reference/packs/malware-investigation-and-response) pack:
| Pack Name | Available Functionality |
| --- | --- |
| [Palo Alto Networks Cortex XDR - Investigation and Response](https://xsoar.pan.dev/docs/reference/packs/palo-alto-networks-cortex-xdr---investigation-and-response) | - Retrieve files from endpoint with command `xdr-file-retrieve`<br />- Run script on endpoint with command `xdr-run-script`<br />- Run shell command on endpoint with command `xdr-script-commands-execute` |
| [CrowdStrike Falcon](https://cortex.marketplace.pan.dev/marketplace/details/CrowdStrikeFalcon/) | - Perform CrowdStrike Real Time Response (RTR) operations with commands `cs-falcon-run-command` and `cs-falcon-rtr-*`<br />- Run script on endpoint with command `cs-falcon-run-script` |
| [Microsoft Defender for Endpoint](https://cortex.marketplace.pan.dev/marketplace/details/MicrosoftDefenderAdvancedThreatProtection/) | - Retrieve files associated with alert with command `microsoft-atp-get-alert-related-files`<br />- Perform live response operations with commands `microsoft-atp-live-response-*` | 

Other packs:
| Pack Name | Available Functionality |
| --- | --- |
| [Tanium Threat Response](https://cortex.marketplace.pan.dev/marketplace/details/TaniumThreatResponse/) ||
| [Infocyte](https://cortex.marketplace.pan.dev/marketplace/details/Infocyte/) ||
            
## Packs for Dedicated Forensics Tools
| Pack Name | Available Functionality |
| --- | --- |
| [Exterro/AccessData](https://cortex.marketplace.pan.dev/marketplace/details/Exterro/) ||

## Analysis Tools Packs
| Pack Name | Available Functionality |
| --- | --- |
| [ExifRead](https://cortex.marketplace.pan.dev/marketplace/details/ExifRead/) | |
| [Oletools](https://cortex.marketplace.pan.dev/marketplace/details/Oletools/) | |
| [PCAP Analysis](https://cortex.marketplace.pan.dev/marketplace/details/PcapAnalysis/) | |
| [Volatility](https://cortex.marketplace.pan.dev/marketplace/details/Volatility/) ||
| [Windows Forensics](https://xsoar.pan.dev/docs/reference/packs/Windows_Forensics) | |

## Data Acquisition Tools Packs
| Pack Name | Available Functionality |
| --- | --- |
| [Binalyze AIR](https://cortex.marketplace.pan.dev/marketplace/details/Binalyze/) ||
| [Cado Response](https://cortex.marketplace.pan.dev/marketplace/details/CadoResponse/) ||

## Conclusion

For more ideas, search the Marketplace by keyword or filter by tag "Forensics".

<img width="1207" alt="Screen Shot 2023-01-08 at 12 45 31 PM" src="https://user-images.githubusercontent.com/91506078/211215821-ead5063e-72a0-4833-bfe7-f161c0b0d3f0.png">
