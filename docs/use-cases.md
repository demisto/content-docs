---
id: use-cases
title: Integration Use Cases
---

This section includes common Use Cases for the different categories of Demisto integrations. While this list is not meant to be exhaustive, it's a good starting point for you to understand what use cases could be supported by your integration.

## Analytics and SIEM
Please Note: Will normally include the Fetch Incidents possibility for the instance. Can also include list-incidents or get-incident as integration commands. Important information for an Event/Incident

**Top Use Cases:**
- Fetch Incidents with relevant filters
- Create, close and delete incidents/events/cases
- Update Incidents - Update status, assignees, Severity, SLA, etc.
- Get events related to an incident/case.
- Query SIEM (consider aggregating logs)

Analytics & SIEM Integration Example: [ArcSight ESM](https://support.demisto.com/hc/en-us/articles/115003749113-ArcSight-ESM)

## Authentication

**Top Use Cases:**
- Use credentials from authentication vault in order to configure instances in Demisto (Save credentials in: Settings -> Integrations -> Credentials)
The integration should include the isFetchCredentials Parameter, and other integrations that will use credentials from the vault, should have the ‘Switch to credentials’ option.
- Lock/Delete Account – Give option to lock account (credentials), and unlock/undelete.
- Reset Account - Perform a reset password command for an account.
- List credential names – Do not post the actual credentials. (For example – Credential name: McAfee ePO, do not show actual username and password.)
- Lock Vault – In case of an emergency (if the vault has been compromised), allow the option to lock + unlock the whole vault.

Authentication Integration Example: [CyberArk AIM](https://support.demisto.com/hc/en-us/articles/360015595394-CyberArk-AIM)

## Case Management

**Top Use Cases:**
- Create, get, edit, close a ticket/issue, add + view comments.
- Assign a ticket/issue to a specified user.
- List all tickets, filter by name, date, assignee.
- Get details about a managed object, update, create, delete.
- Add and manage users.
- Case Management/Ticketing Integration Example – ServiceNow
- Data Enrichment & Threat Intelligence
- Important information for an indicator:
- Top Use Cases: Enriching information about different IOC types:
 - upload object for scan and get the scan results. (If there’s a possibility to upload private/public, default should be set to private).
 - search for former scan results about an object (This way you can get information about a sample without uploading it yourself).
 - enrich information and scoring for the object.
- Add/Search for indicators in the system.
- Whitelist/ Blacklist indicators.
- Calculate DBot Score for indicators.

Data Enrichment & Threat Intelligence Integration Example: [VirusTotal](https://support.demisto.com/hc/en-us/articles/360033643594-VirusTotal)

## Email Gateway

**Top Use Cases:**
- Get message – Download the email itself, retrieve metadata, body.
- Download attachments for a given message.
- Manage senders – Block/ Allow specified mail senders.
- Manage URLs – Block/ Allow the sending of specified URLs.
- Encode/ Decode URLs in messages.
- Release a held message (The gateway can place suspicious messages on hold, and sometimes they would need to be released to the receiver).

Email Gateway Integration Example: [MimeCast](https://support.demisto.com/hc/en-us/articles/115004684608-Mimecast)

## Endpoint

**Top Use Cases:**
- Fetch Incidents & Events
- Get event details (from specified incident)
- Quarantine File
- Isolate and contain endpoints
- Update Indicators (Network, hashes, etc.) by policy (can be block, monitor) – Black list
- White list indicators
- Search for indicators in the system (Seen indicators and related incidents/events)
- Download file (based on hash, path)
- Trigger scans on specified hosts
- Update .DAT files for signatures and compare existing .DAT file to the newest one on the server
- Get information for a specified host (OS, users, addresses, hostname)
- Get policy information and assign policies to endpoints
Endpoint Integration Examples: [Cortex XDR](https://support.demisto.com/hc/en-us/articles/360035216393-Palo-Alto-Networks-Cortex-XDR-Demisto-5-0-), [Tanium](https://support.demisto.com/hc/en-us/articles/360039455034-Tanium-v2) and [Carbon Black Protection](https://support.demisto.com/hc/en-us/articles/360022492334-Carbon-Black-Protection-v2)

## Forensics and Malware Analysis

**Top Use Cases:**
- Submit a file and get a report (detonation)
- Submit a URL and get a report (detonation)
- Search for past analysis (input being a hash/url).
- Retrieve a PCAP file
- Retrieve screenshots taken during analysis.
- Sandbox Integration Example: [Cuckoo Sandbox](https://support.demisto.com/hc/en-us/articles/360012792253-Cuckoo-Sandbox)

## Network Security (Firewall)

**Top Use Cases:**
- Create block/accept policies (Source, Destination, Port), for IP addresses and domains.
- Add addresses and ports (services) to predefined groups, create groups, etc.
- Support custom url categories.
- Fetch network logs for a specific address for a configurable time frame.
- URL filtering categorization change request
- Built in blocked rule command for fast-blocking.
- If there is a Management FW, allow the option to manage policy rules through it.

Network Security Firewall Integration Example: [Palo Alto Networks PAN-OS](https://support.demisto.com/hc/en-us/articles/360014816634-Palo-Alto-Networks-PAN-OS)

## Network Security (IDS/IPS)

**Top Use Cases:**
- Get/Fetch alerts.
- Get PCAP file, packet.
- Get network logs filtered by time range, ip addresses, ports, etc.
- Create/manage/delete policies and rules.
- Update signatures from an online source / upload + Get last signature update information.
- Install policy (if existing).

Network Security (IPS/IDS) Integration Example: [Protectwise](https://support.demisto.com/hc/en-us/articles/115001256154-Protectwise)

## Vulnerability Management

**Top Use Cases:**
- Enrich asset – get vulnerability information for an asset (or a group of assets) in the organization.
- Generate/Trigger a scan on specified assets.
- Get a scan report including vulnerability information for a specified scan and export it.
- Get details for a specified vulnerability.
- Scan assets for a specific vulnerability.

Vulnerability Management Integration Example: [Tenable.io](https://support.demisto.com/hc/en-us/articles/360011971614-Tenable-io)
