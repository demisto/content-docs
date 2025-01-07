---
id: palo-alto-networks-cortex-xdr
title: Cortex XDR by Palo Alto Networks
description: Automates Cortex XDR incident response, and includes custom Cortex XDR incident views and layouts to aid analyst investigations.
---

## Description

Automate Cortex XDR incident response with custom views and layouts designed to streamline analyst investigations. This pack enables organizations to efficiently manage and respond to security incidents, enhancing detection and mitigation capabilities.

## Key Features

- **Incident Synchronization**: Automatically synchronize and update incidents between Cortex XDR and Cortex XSOAR.
- **Alert Enrichment**: Extract and enrich indicators from source alerts to provide actionable intelligence.
- **Remediation Actions**: Automate remediation tasks such as blocking malicious indicators and isolating compromised endpoints.

## Playbooks Highlight

- **Lite Incident Handling** - A streamlined playbook for incident enrichment, investigation, and response.
- **Device Control Violations** - Investigates device control violations by communicating with users to determine the reason for device connections.
- **XDR Incident Handling v3** - Compares and updates incidents across Cortex XDR and Cortex XSOAR.
- **Cloud IAM User Access Investigation** - Responds to alerts involving suspicious use of cloud IAM user access keys.
- **Cortex XDR Cloud Cryptomining** - Addresses cryptomining alerts in cloud environments, supporting AWS, Azure, and GCP.

## Before You Start

### Required Content Packs

This Content Pack may require the following additional Content Packs:

- Active Directory Query
- Base
- Common Playbooks
- Common Types
- Core Alert Fields
- Malware Investigation and Response

### Optional Content Packs

- AutoFocus
- Core REST API
- EWS
- EWS Mail Sender
- Gmail
- Gmail Single User (Beta)
- Mail Sender (New)
- Microsoft Graph Mail Single User
- Microsoft Graph Mail
- PANW Comprehensive Investigation
- Port Scan
- ServiceNow
- Common Scripts
- Active Directory Query
- AWS - IAM
- Atlassian Jira
- Cloud Incident Response

### Pack Configurations

- [Device Control Violations Workflow](#device-control-violations-workflow)
- [Query Disconnected Cortex XDR Endpoints Workflow](#query-disconnected-cortex-xdr-endpoints-workflow)

#### Device Control Violations Workflow

1. Create a job to query for device control violations.  

   1. Click **Jobs**.
   2. Click **New Job**.
   3. Configure the recurring schedule.
   3. Enter a name for the job.
   4. In the Type field, select *XDR Device Control Violations*.
   5. In the Playbook field, select **JOB - Cortex XDR query endpoint device control violations**. 
   6. Click **Create new job**.

   Note: For detailed information about creating jobs, see [Jobs](https://xsoar.pan.dev/docs/incidents/incident-jobs).

2. Define the inputs for the [JOB - Cortex XDR query endpoint device control violations](https://xsoar.pan.dev/docs/reference/playbooks/job---cortex-xdr-query-endpoint-device-control-violations).

   Note: The scheduled run time and the timestamp playbook input must be identical. If the job recurs every 7 days, the timestamp should be 7 days as well.
3. To run the response playbook for the violations found, define the inputs for the [Cortex XDR device control violations](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-device-control-violations).

#### Query Disconnected Cortex XDR Endpoints Workflow

1. Create a job to query the disconnected endpoints.
   1. Click **Jobs**.
   2. Click **New Job**.
   3. Configure the recurring schedule.
   3. Enter a name for the job.
   4. In the Type field, select *Cortex XDR disconnected endpoints*.
   5. In the Playbook field, select **Cortex XDR disconnected endpoints**.
   6. Click **Create new job**.

       Note: For detailed information about creating jobs, see [Jobs](https://xsoar.pan.dev/docs/incidents/incident-jobs).
2. Define the inputs for the [Cortex XDR disconnected endpoints](https://xsoar.pan.dev/docs/reference/playbooks/cortex-xdr-disconnected-endpoints) playbook.

   Note: The scheduled run time and the timestamp playbook input must be identical. If the job recurs every 7 days, the timestamp should be 7 days as well.