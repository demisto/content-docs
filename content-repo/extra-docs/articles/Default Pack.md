
## Introduction

The Default pack provides a solution for new users who are still early in their Cortex XSOAR journey, or as a solution for use cases that you would like to handle but are yet to create content for.

  

We’ve created a playbook that puts together the core elements of handling any kind of incident. With this playbook there’s also a new layout that gives insight into the data that came with the incident together with any new information collected during the investigation of that incident.

  
  

## Walkthrough

### Playbook

The playbook makes use of existing out-of-the-box, free content in order to investigate the incident.

It has 3 inputs - whether to extract and enrich indicators from the fetched incident (turn on in case you decided to disable [auto-extract](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/6.6/Cortex-XSOAR-Administrator-Guide/Indicator-Extraction)), and two tags used for allowing or blocking indicators using an External Dynamic List.
Extracting and enriching the indicators related to the incident is crucial for the investigation and response process. If you are unsure, we suggest to keep the input value as "True".
The tag inputs are optional names that you would like to use for tagging indicators. For example, you may want to tag malicious indicators as "mal", or benign indicators as "safe". The Default layout then allows you to make use of these tags by using the buttons that correspond to the indicators you want to tag.
Note: tagging the indicators does not automatically allow or block them. Instead, tagging indicators can be used in conjunction with an External Dynamic List and the Generic Export Indicators Service integration. You can read more about it by [installing the pack](https://cortex.marketplace.pan.dev/marketplace/details/EDL/) for the Marketplace and reading the integration documentation..

The playbook begins by de-duplicating any similar incidents. If a file is involved in the incident, it will then run the following steps:

-   Attempt to retrieve the actual file by its hash or file path
    
-   Search for endpoints that have that file on them and display them in the layout
    
-   Extract indicators from the file
    
-   Detonate the file
    

In addition, the playbook will detonate URLs if a supported sandbox integration is enabled.

The playbook then enriches the indicators using the Entity Enrichment - Generic v3 playbook, which can verify SSL certificates, take screenshots of URLs, check for domain-squatting, and more.

After doing so, the playbook calculates a severity for the incident based on various factors.

If the incident is deemed a true positive, the playbook allows the user to remediate the incident.

Finally, the playbook generates an investigation report and closes the incident.

  

### Layout

The layout is built in a way that would fit any type of incident by using a dynamic section that dynamically loads the fields you’ve mapped for that incident type.

If you haven’t mapped any fields - you will see them in the “Unmapped Fields” section.

Additionally, the layout provides buttons for the user to tag indicators as benign or malicious for later use in an EDL.

The layout also provides buttons for checking whether an IP is private or public, and whether a domain is internal or external. Those buttons make use of new scripts that utilize Cortex XSOAR Lists for centralized management of that data. The scripts are easily customizable.

The Default layout aims to make it as easy as possible for an analyst to investigate an incident, so it includes a “Cheat Sheet” page which provides a collection of the most common scripts an analyst may use - from data manipulation scripts and networking tools to Cortex XSOAR debugging utilities.

  
  

## How To Use

In order to make use of the Default layout, do the following:

1.  Go to **Settings & Info** > **Settings**.
    
2.  Under **Object Setup**, click **Incidents**
    
3.  Under the Types tab, find the incident type you would like to use with the Default layout.
    

1.  If the incident type is locked, click **Detach**.
    

5.  Click on the name of the incident type
    
6.  Under **Layout**, select the **Default** layout.
    
7. To use the Default playbook for your incident type - under **Default playbook** - select the **Default** playbook.
    

![](https://github.com/demisto/content-docs/blob/master/docs/doc_imgs/reference/unclassified%20edit.png?raw=true)
