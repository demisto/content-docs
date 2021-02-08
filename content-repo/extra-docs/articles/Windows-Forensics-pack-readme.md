---
id: Windows_Forensics
title: Windows Forensics
description: This Windows Forensics pack enables gathering Forensics data from Windows hosts and analyzing the provided artifacts. The pack uses the Powershell Remoting integration to collect the artifacts and other tools such as the PCAP Miner and Registry Parse to analyze and parse the data.
---

## Pack Workflow
In the **Acquire And Analyze Host Forensics** playbook, you configure from which hosts the forensic data should come.

The **PS-Remote Acquire Host Forensics** executes the following 3 sub-playbooks to acquire the hosts' artifacts:
   - **PS-Remote Get Network Traffic**
   - **PS-Remote Get Registry**
   - **PS-Remote Get MFT**

Once the forensic data is uploaded to XSOAR, the Forensics Tools Analysis playbook analyzes the acquired network traffic and the registry to extract relevant information.

The **Forensics Tools Analysis** playbook executes the following 2 sub-playbooks:
- **Registry Parse Data Analysis** - Parses the data in the registry file according to the default or custom settings.
- **PCAP Search** - Displays all TCP/UDP detected traffic in the PCAP file. Note: This playbook is included in the PCAP ANALYSIS pack. 

You can view the extracted PCAP and registry data in the War Room or in the incident layout.

## In This Pack
The Windows Forensics content pack includes several content items.

### Playbooks
There are 8 playbooks in this pack.

- **Acquire And Analyze Host Forensics** - This is the main playbook in which you configure from which hosts the forensic data should come.
- **PS-Remote Acquire Host Forensics** - Executes sub-playbooks to acquire the hosts' artifacts.
- **PS-Remote Get Network Traffic** - Records and acquires network traffic from the hosts. In addition, it also converts the ETL file that was recorded on the host to a PCAP file.
- **PS-Remote Get Registry** - Acquires the entire registry or a specific hive from hosts.
- **PS-Remote Get MFT** - Acquires the MFT (Master File Table) from hosts.
- **Forensics Tools Analysis**  - Executes sub-playbooks to parse the registry data and display the TCP/UDP traffic.
- **Registry Parse Data Analysis** - Parses the data in the registry file according to the default or custom settings.
- **PS Remote Get File Sample From Path** - Acquires a specified file from a path provided in the playbook inputs.



### Automations
There are 2 Automations in this pack.

* [Etl2Pcap](https://xsoar.pan.dev/docs/reference/scripts/etl2pcap) - Converts an ETL file to a PCAP format file.

* [RegistryParse](https://xsoar.pan.dev/docs/reference/scripts/registryparse) - Parses a registry file for common registry keys of interest or user defined registry paths.

### Incident Types
There is 1 incident type.
**Forensic Acquisition And Analysis**. The default playbook for this incident type is **Acquire And Analyze Host Forensics**.

### Layout
There is 1 layout - **Forensic Acquisition And Analysis** 
- The **Forensics Acquisition** tab displays the acquired forensic artifacts. 
- The **Analysis** tab displays the data extracted from the PCAP and registry file.
 !["Forensics Acquisition"](https://raw.githubusercontent.com/demisto/content-docs/57b5d0a866f90e378da89625489fe220503b3901/docs/doc_imgs/reference/WindowsForensics/Forensic_acquisition.JPG "Forensics Acquisition")
 !["Analysis"](https://raw.githubusercontent.com/demisto/content-docs/57b5d0a866f90e378da89625489fe220503b3901/docs/doc_imgs/reference/WindowsForensics/analysis.JPG "Analysis")

## Before You Start
This pack requires that you have an active instance of the PowerShell Remoting integration enabled for the Forensic acquisition pack. Make sure to configure the PowerShell Remoting environment as described in the [PowerShell Remoting](https://xsoar.pan.dev/docs/reference/articles/powershell_remoting) article.


## Testing the Pack
Once you have configured the Powershell Remoting integration, in the Acquire And Analyze Host Forensics playbook provide as inputs from which hosts the forensic data should be gathered. Create a new incident of type Forensic Acquisition And Analysis and review the workflow and layout.

## Integrations
Although the Powershell Remoting integration is not included in the pack, the integration is required in order to gather the forensic data from hosts. Note that you can use the automations and the analysis playbooks without configuring the integration.

