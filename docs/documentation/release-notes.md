---
id: release-notes
title: Pack Release Notes
---

Release notes files help users keep track of changes made for specific content entities, such as integrations or playbooks.

To generate a release notes markdown file, first commit the changes to your branch and then run the following command provided by the **demisto-sdk**:

```bash
demisto-sdk update-release-notes -i [Changed pack path] -u [major|minor|revision]
```

**Please note:** Changes that have not been committed are not detected automatically by the ***update-release-notes*** command.

This command automatically updates the *currentVersion* found in the *pack_metadata.json* file according to the update version (as denoted by the *-u* flag).

In most cases, you run the command when you are ready to merge and expect no further changes. If you need to make additional 
changes after running the command, remove the `-u` argument. This updates the release notes file for you to fill out.

```bash
demisto-sdk update-release-notes -i [Changed pack path]
```

For more information regarding the ***update-release-notes*** command in the **demisto-sdk**, please refer to the 
[command documentation](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/update_release_notes/README.md).

## Naming
The release notes file is generated for you and is found in the *ReleaseNotes* folder within each pack. If this folder does not already exist, it is created for you.

Do not change the names of the files that are automatically generated, as this can cause potential issues later in the development process. 

## Format
After running the ***demisto-sdk*** command, the release notes file contains a section for each entity changed in the pack as well as a placeholder (`%%UPDATE_RN%%`).
This placeholder should be replaced with a line describing what was changed for that specific entity.

For example, if changes are detected in the Cortex XDR pack for the items *IncidentFields*, *Integrations*, and *Playbooks*; the following is created:
```markdown
#### Incident Fields
##### XDR Alerts
  - %%UPDATE_RN%%

#### Integrations
##### Cortex XDR - IR
  - %%UPDATE_RN%%

#### Playbooks
##### Cortex XDR - Isolate Endpoints
  - %%UPDATE_RN%%

##### Cortex XDR - Port Scan
  - %%UPDATE_RN%%

```

## MD Formatting
For single line RNs, follow this format:
```markdown
#### Integrations
##### Cortex XDR - IR
Release note here.
```

For single line RNs with a nested list, follow this format:
```markdown
#### Integrations
##### Cortex XDR - IR
Release note here.
  - List item 1
  - List item 2
```

For multiline RNs, follow this format:
```markdown
#### Integrations
##### Cortex XDR - IR
  - Release note 1 here.
  - Release note 2 here.
  - Release note 2 here.
```

For multiline RNs with nested content, follow this format:
```markdown
#### Integrations
##### Cortex XDR - IR
  - Release note 1 here.
    - List item 1
    - List item 2
  - Release note 2 here.
    - List item 1
    - List item 2
  - Release note 2 here.
```

## Examples and Best Practices

### What Should Be Logged
Specify in the corresponding release notes file:
  - Any change(s) made
  - New command(s)
  - New or udpated parameters
  - New or updated arguments
  - Updated outputs
  - Bug fixes

### General
- Release notes should be simple, informative, and clearly written. Consider the impact of changes on the user and what they need to know about this version. A poorly written release note with inadequate information can lead to a Customer Support ticket.
    - Bad example: `Added the timeout parameter.`  
    - Good example: `Added the timeout parameter, which enables you to define the amount of time (in minutes) that the integration will try to execute commands before it throws an error.`

- Single line release notes do not need a bullet point.
- Release notes must start with one of the following prefixes:

```
'Added support for '
'Added the '
'Fixed an issue '
'Improved implementation '
'Updated the Docker image to '
'You can now '
'Deprecated. '
'Deprecated the' 
```

Release notes not using one of these prefixes will generate an error when running `demisto-sdk doc-review`:

```
Line is not using one of our templates, consider changing it to fit our standard.
```

### Entity Styling  
- Command names: - should be wrapped with three stars - ***command_name***
- Packs/integrations/scripts/playbooks and other content entities (incident fields, dashboards. etc.) - should be wrapped with two stars - **entity_name**
- Parameters/arguments/functions/outputs names - should be wrapped with one star - *parameter_name*


### Examples  

#### Enhancement Examples
```markdown
- **MISP V2**  
You can now filter an event by attribute data fields.

- **WhatIsMyBrowser**  
Added support for the *extend-context* argument in the ***ua-parse*** command.

- **Microsoft Graph Mail**   
Added 3 commands:
    - ***msgraph-mail-list-folders***
    - ***msgraph-mail-list-child-folders***
    - ***msgraph-mail-create-folder***
```

#### Bug Fix Examples
```markdown
- **Slack v2**  
    - Fixed an issue where mirrored investigations contained mismatched user names.
    - Added the **reporter** and **reporter email** labels to incidents that are created by direct messages.

- **CrowdStrike Falcon**  
Fixed an issue with ***fetch incidents***, which caused incident duplication.

- **IBM QRadar**  
Fixed an issue in which the ***qradar-delete-reference-set-value*** command failed to delete reference sets with the "\" character in their names.

- **GitHub**  
Improved implementation of the default value for the *fetch_time* parameter.
```
#### Docker Updates Example
```markdown
- Updated the Docker image to: *demisto/python3:3.9.1.15759*.
```
#### General Changes

> **Note:** Use these if the change has no visible impact on the user. 

```markdown
- Maintenance and stability enhancements.
- Documentation and metadata improvements.
```
  
## Excluding Items
Release notes must contain all changed items included in the generated file. As such, validation 
fails if detected items are removed from the generated release notes file.

However, you may encounter a scenario where certain changes are not necessary to document in the release notes. In this case, to pass validation, comment out the entries using the following syntax:

```markdown
<!--
#### Integrations
##### Cortex XDR - IR
  - Renamed an item. Not necessary to document in release notes.
-->
```

## demisto-sdk doc-review
**demisto-sdk** includes the ***doc-review*** command to assist with the documentation review process. The ***doc-review*** command checks the spelling of the release notes and provide guidance if you are not using one of our standardized templates. Example usage:

```
demisto-sdk doc-review -i Packs/Base/ReleaseNotes/1_11_10.md
```

More info is available at the ***demisto-sdk doc-review*** command [README](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/doc_reviewer/README.md).

## Breaking Changes Version
In some cases, a new version is introduced which breaks backward compatibility.
From Cortex XSOAR version 6.8 and above, there is support to mark a new version as a **breaking changes version**.

Marking a version as a **breaking changes version** provides the user with an alert before installation:
![image](/doc_imgs/integrations/bc_alert_example.png)


#### Idicate a new version is a breaking changes version
To specify the new introduced version as **breaking changes**, run the demisto-sdk ***update-release-notes*** command with the -bc flag. For example:

```
demisto-sdk update-release-notes -i Packs/<Pack Name> -u revision -bc
```
Adding the *-bc* flag:
- Generates a corresponding configuration JSON file to the new release notes. For example, if the newly created release notes version is 1_1_0.md, a new configuration file 1_1_0.json is created in the corresponding ReleaseNotes directory.
- The configuration JSON file is generated with the following fields:
  -  *breakingChanges*: Indicates whether the version is breaking changes or not, is created with **true** value upon using *-bc* flag.
  -  *breakingChangesNotes*: Contains the text to be displayed to the customer upon installation, as shown in the above image. If *breakingChangesNotes* is not specified, the default is to present the entire release notes text to the user upon installation.


## Common Troubleshooting Tips

#### I excluded an item from the release notes file, but it doesn't pass validation.

Remove the `%%UPDATE_RN%%` from the generated file and leave the other generated items intact.

#### When I run the ***update-release-notes*** command, it does not find any of my changes.

First check you have committed your files. Then verify that the type of file you changed requires a release notes 
entry. TestPlaybooks, Images, README's and TestData don't require release notes.

#### I ran the command and filled out the release notes correctly, but it still fails validation.

On rare occasions, it's possible that the pack you are working on has already had the version updated. To resolve this, delete 
the generated release notes Markdown (*.md) file and restore the *currentVersion* in the *pack_metadata.json* file to its original version. Next, pull from the master branch. Lastly, run the ***update-release-notes*** command again.

#### I added a new pack. Do I need release notes?

New packs do not require release notes. The build process automatically creates the initial release notes.
