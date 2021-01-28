---
id: Windows_Forensics
title: Windows Forensics
description: This Windows Forensics pack enables gathering Forensics data from windows hosts and analyzing the provided artifacts. The pack utilizes the Powershell Remoting integration to collect the artifacts and other tools such as the PCAP Miner or Registry Parse in order to analyze and parse the data.
---

## Pack Workflow
The uses provides in the Acquire And Analyze Host Forensics playbook inputs which hosts should we gather the forensic data from.

The playbook PS-Remote Acquire Host Forensics executes 3 subplaybooks

**PS-Remote Get Network Traffic** Which handles recording and acquiring network traffic from hosts. In addition it also converts the ETL file that was recorded on the host to a PCAP file.
**PS-Remote Get Registry** Which handles acquiring the entire registry or a specific hive from hosts.
**PS-Remote Get MFT** Which handles acquiring the MFT (Master File Table) from hosts.

Once the forensic data was uploaded to XSOAR, The Forensics Tools Analysis playbook will analyze the acquired network traffic and the registry to extract relevant information.

The playbook Forensics Tools Analysis executes 2 playbooks

**Registry Parse Data Analysis** Which parses the data in the registry file according to the default or custom settings.
**PCAP Search** Which shows all TCP/UDP detected traffic in the PCAP file.

You can view the extracted PCAP and registry data in the War Room or in the incident layout.

## In This Pack
The Windows Forensics content pack includes several content items.

### Automations
There are 2 Automations in this pack.

* [Etl2Pcap](https://xsoar.pan.dev/docs/reference/scripts/etl2pcap): Converts an ETL file to a PCAP format file.

* [RegistryParse](https://xsoar.pan.dev/docs/reference/scripts/registryparse): Parses registry file for common registry keys of interest or user defined registry paths.

### Incident Types
There is 1 incident type - **Forensic Acquisition And Analysis**. The default playbook for this incident type is Acquire And Analyze Host Forensics.

### Layout
There is 1 layout - **Forensic Acquisition And Analysis** 
The Forensics Acquisition tab displayed the acquired forensic artifacts. The Analysis tabs displays the data extracted from the PCAP and the registry file.

## Before You Start
This pack requires that you have an active instance of the Powershell Remoting integration enabled for the Forensic acquisition pack. Make sure to configure the Powershell Remoting env as described in the relevant article.
https://xsoar.pan.dev/docs/reference/articles/powershell_remoting

## Testing the Pack
Once you have configured the Powershell Remoting integration as explained in the relevant article. Provide in the Acquire And Analyze Host Forensics playbook inputs which hosts should we gather the forensic data from. Create a new incident of type Forensic Acquisition And Analysis and review the work plan and layout.


## Integrations
Although this integration are not included in the pack, the Powershell Remoting integration is required in order to gather the forensic data from hosts although You can use the automations and the analysis playbooks without the configuring the integration.
