---
id: content-update-notification
title: XSOAR Content Update Notifications
description: Use this pack to automate your content update process for marketplace packs.
---

Use this pack to automate your content update process for marketplace packs.
The playbooks in this pack will check for any available content updates for existing packs and send an e-mail, or Slack message, to inform users of the updates. Then, users will be able to choose whether to automatically update the chosen content packs.
 
# What does this pack do?
Automate your content update process for marketplace packs.

- Check if there are any content updates available for chosen installed content packs, or for all installed packs.
- Notify users via e-mail or Slack.
- The playbook contains an auto-update flow that allows users to decide whether they want to install all updates that were found.

# In this Pack

## Automations
**_ListInstalledContentPacks_** - This script will show all installed content packs and whether there is an update available.

**_FormatContentData_** - This script formats the value given input from a JSON list into a table.

**_CollectPacksData_** - This script will collect the pack data that is needed to update the pack.

Scripts from other packs that are used in the process:

**_GetServerURL_** - From the “Get Server URL” pack.

**_MarketplacePackInstaller_** - From the “Content Installation” pack.

## Playbooks
**Content Update Manager** - Use this playbook to check if there are any content updates available for chosen installed content packs, and notify users via e-mail or Slack. The playbook contains an auto-update flow that allows users to decide whether they want to install all updates that were found. See more about the playbook [here](https://xsoar.pan.dev/docs/reference/playbooks/content-update-manager).

## Incident types
**Content Update Manager** - The incident type that triggers the `Content Update Manager` playbook. Creating this incident will let you choose the preferred notification method (Slack or email), and the packs you want to check using the playbook.

## Layouts
**Content Update Manager Layout** - The main layout for the **Content Update Manager** incident type.

The Content Update Manager incident layout contains the following tabs:

**_New Content Available**_ tab - This tab will show the trigger information of the incident, chosen packs to check, and the available updates.

![image](https://user-images.githubusercontent.com/43776787/145987422-d080f2a8-52f9-4919-a2ab-11b70217d963.png)

# Pack Workflow and Configuration
To run the use-cases in this pack, you need to:

1) Create an incident and choose the type “Content Update Manager”.

2) In the incident creation form, choose the preferred notification method.
 
3) In the incident creation form, choose the packs for the playbooks to check (You can specify ‘All’ for all existing packs, or specific pack names.)

4) After the incident is created, the playbook is triggered, and you will receive all of the packs’ update information.
You can then decide whether to automatically, or manually, update the packs.

**You can use the use-case in this pack as a:**
- **Incident** - Manually create an incident as described above.
- **Job** - Configure the “Content Update Manager” to run as a job, managing your content update process on a regular basis.

## Before You Start

You can configure the auto_update input in the “Content Update Manager” playbook to “Yes”, if you always want to automatically update the content packs without asking via communication task. Otherwise, you will be asked to approve the update every time the playbook is triggered.
