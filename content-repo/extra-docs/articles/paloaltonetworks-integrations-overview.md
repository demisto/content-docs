---
id: PaloAltoNetworks_Integrations
title: Palo Alto Networks Integrations Overview  
description: The following maps the Palo Alto Networks Integrations and their use cases.
---


# Palo Alto Networks Integrations Overview
Palo Alto Networks is a portfolio company with many different products and functionalities.
Moreover, the APIs behind them are vast and do not fit under one integration.

Review this document to determine the Palo Alto Networks integrations you need for your use cases.


## [Palo Alto Networks PAN-OS](https://xsoar.pan.dev/marketplace/details/PANOS)

### Use Cases
- Create and manage custom security rules in Palo Alto Networks PAN-OS.
- Create and manage address objects, address-groups, custom URL categories, URL filtering objects.
- Use the URL Filtering category information to enrich URLs.
- Commit configurations to Palo Alto Firewall and to Panorama, and push configurations from Panorama to Pre-Defined Device-Groups of Firewalls.
- Upgrade the version and content of the firewall.
- Query the following PAN-OS log types: traffic, threat, url, data-filtering, and Wildfire.
- Manage External Dynamic Lists (EDLs).

### Playbooks
- [PAN-OS Query Logs For Indicators](https://xsoar.pan.dev/docs/reference/playbooks/pan-os-query-logs-for-indicators)
- [PAN-OS Commit Configuration](https://xsoar.pan.dev/docs/reference/playbooks/pan-os-commit-configuration)

## [Palo Alto Networks BPA](https://xsoar.pan.dev/marketplace/details/BPA)

### Use Cases
Analyzes NGFW and Panorama configurations and compares them to the best practices.

### Playbooks
[Run Panorama Best Practice Assessment](https://xsoar.pan.dev/docs/reference/playbooks/run-panorama-best-practice-assessment)


## [AutoFocus](https://xsoar.pan.dev/marketplace/details/AutoFocus)

### Use Cases
- Query samples, sessions.
- Get sample analysis.
- Get session details.
- Get tag details.

### Playbooks
[Autofocus Query Samples, Sessions and Tags](https://xsoar.pan.dev/docs/reference/playbooks/autofocus-query-samples-sessions-and-tags)


## [Palo Alto Networks WildFire](https://xsoar.pan.dev/marketplace/details/Palo_Alto_Networks_WildFire)

### Use Cases
- Send a file sample to WildFire.
- Upload a file hosted on a website to WildFire.
- Submit a webpage to WildFire.
- Get a report regarding the sent samples using the file hash.
- Get a sample file from WildFire.
- Get the verdict regarding multiple hashes (up to 500) using the ***wildfire-get-verdicts*** command.


## [Palo Alto Networks Threat Vault](https://xsoar.pan.dev/marketplace/details/PaloAltoNetworks_Threat_Vault)

### Use Cases
Use the Palo Alto Networks Threat Vault to research the latest threats (vulnerabilities/exploits, viruses, and spyware) that Palo Alto Networks next-generation firewalls can detect and prevent.


## [Cortex Xpanse](https://xsoar.pan.dev/marketplace/details/ExpanseV2)

### Use Cases
- Automate Attack Surface Management to identify internet assets and quickly remediate misconfigurations.
- Collect Expanse issues and bi-directionally mirror them.


## [Cortex XDR](https://xsoar.pan.dev/marketplace/details/CortexXDR)

### Use Cases
- Syncs and updates Cortex XDR incidents.
- Triggers a sub-playbook to handle each alert by type.
- Extracts and enriches all relevant indicators from the source alert.
- Hunts for related IOCs.
- Calculates the severity of the incident.
- Interacts with the analyst to choose a remediation path or close the incident as a false positive based on the gathered information and incident severity.
- Remediates the incident by blocking malicious indicators and isolating infected endpoints.

### Playbooks
- [Cortex XDR - Port Scan](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---port-scan)
- [Cortex XDR incident handling v3](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-incident-handling-v3)
- [Cortex XDR - Execute snippet code script](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr---execute-snippet-code-script)


## [Cortex Data Lake](https://xsoar.pan.dev/marketplace/details/CortexDataLake)

### Use cases
Provides cloud-based, centralized log storage and aggregation for your on-premise, virtual (private cloud and public cloud) firewalls, for Prisma Access and for cloud-delivered services such as Cortex XDR.


## [Prisma Access](https://xsoar.pan.dev/marketplace/details/PrismaAccess)

### Use Cases
- Force logout of a specific user from Prisma Access.
- List currently active users.
- Run a Prisma Access query (e.g., getGPaaSLast90DaysUniqueUsers).
- Run a custom CLI command.


### Playbooks
- [Prisma Access - Logout User](https://xsoar.pan.dev/docs/reference/playbooks/prisma-access----logout-user)
- [Prisma Access Whitelist Egress IPs on SaaS Services](https://xsoar.pan.dev/docs/reference/playbooks/prisma-access-whitelist-egress-i-ps-on-saa-s-services)
- [Prisma Access - Connection Health Check](https://xsoar.pan.dev/docs/reference/playbooks/prisma-access---connection-health-check)


## Feeds

### Use Cases:
Fetch indicators from Palo Alto Networks services.

### [Unit42 ATOMs Feed](https://xsoar.pan.dev/docs/reference/integrations/unit42v2-feed)
Unit42 feed of published IOCs, which contains known malicious indicators.

### [Unit 42 Intel Objects Feed](https://xsoar.pan.dev/marketplace/details/Unit42Intel)
Fetch a list of threat intel objects, including Campaigns, Threat Actors, Malware and Attack Patterns, provided by Palo Alto Network's Unit 42 threat researchers.

### [Prisma Access Egress IP feed](https://xsoar.pan.dev/docs/reference/integrations/prisma-access-egress-ip-feed)
Dynamically retrieve and allow IPs Prisma Access uses to egress traffic to the internet and SaaS apps.

### [Expanse Expander Feed](https://xsoar.pan.dev/docs/reference/integrations/feed-expanse)
Use this feed to retrieve the discovered IPs/Domains/Certificates from the Expanse Expander asset database.

### [AutoFocus Feed](https://xsoar.pan.dev/docs/reference/integrations/auto-focus-feed)
Use the AutoFocus Feeds integration to fetch indicators from AutoFocus. This feed supports the AutoFocus Custom Feed and the AutoFocus Samples Feed.

### [AutoFocus Daily Feed](https://xsoar.pan.dev/docs/reference/integrations/auto-focus-daily-feed)
Use the AutoFocus Daily feed to export threat intelligence data produced by AutoFocus and connected services.

### [AutoFocus Tags Feed](https://xsoar.pan.dev/docs/reference/integrations/auto-focus-tags-feed)
Use the AutoFocus Tags Feed integration to fetch indicators from AutoFocus Tags.
