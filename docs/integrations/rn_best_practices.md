---
id: rn_best_practices
title: Release Notes - Best Practice
---

## General 
- The release notes needs to be in simple language and informative.  
    - Bad example: `Added the timeout parameter.`  
    - Good example: `Added the timeout parameter, which enables you to define the amount of time (in minutes) that the integration will try to execute commands before it throws an error.`

- If this is a single line release note, there is no need for the bullet point, just a regular sentence. 

Pretend you need this release note to do your work. A bad RN can easily lead to a CS ticket.
## Entities marks in the RN:  

- Command names - should be wrapped with three stars - \*\*\*command_name***
- Packs/Integrations/scripts/playbooks and other content entities (incident fields, dashboards...) - should be wrapped with two stars - \*\*entity_name**
- Parameters/arguments/functions/outputs names - should be wrapped with one stars - \*entity_name*


## Improved Integrations/bug fixes examples  

### Enhancements examples:

- **MISP V2**
You can now filter an event by attribute data fields.

- **WhatIsMyBrowser**
Added support for the *extend-context* argument in the ***ua-parse*** command.

- **Microsoft Graph Mail**  
Added 3 commands.
    - ***msgraph-mail-list-folders***
    - ***msgraph-mail-list-child-folders***
    - ***msgraph-mail-create-folder***


### Bug fixes examples:
- **Slack v2**
    - Fixed an issue where mirrored investigations contained mismatched user names.
    - Added the **reporter** and **reporter email** labels to incidents that are created by direct messages.

- **CrowdStrike Falcon**  
Fixed an issue with ***fetch incidents***, which caused incident duplication.

- **IBM QRadar**  
Fixed an issue in which the ***qradar-delete-reference-set-value*** command failed to delete reference sets with the "\" character in their names.

- **GitHub**  
Improved implementation of the default value for the *fetch_time* parameter.


