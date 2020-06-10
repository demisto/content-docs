---
id: changelog
title: Change Log
---

A change log file helps to keep track on the changes made for a specific content entity like an integration or a playbook.

To generate a change log, run the following command provided by the `demisto-sdk`:

```bash
demisto-sdk update-release-notes -p [Changed Pack Name] -u [major|minor|revision]
```

This command will bump the `currentVersion` found in `pack_metadata.json` file automatically according to the update version (as denoted by the `-u` flag) for you.

Generally, you will use the command when you are ready to merge and expect no other changes. If you need to make additional 
changes *after* running the command, you will need to remove the `-u` argument. This will generate a new release notes 
file for you to fill out.

```bash
demisto-sdk update-release-notes -p [Changed Pack Name]
```

## Naming
The change log file will be generated for you and is found under the `ReleaseNotes` folder within each pack. If this folder does not already exist, one will be created for you.

The names for the files generated should not be changed as this will cause potential issues in the future. 


## Format
After running the `demisto-sdk` command mentioned above, the change log which was generated will contain a section for each entity changed in the pack as well as a placeholder (`%%UPDATE_RN%%`).
This placeholder should be replaced with a line describing what was changed for that specific entity.

For example, if changes were detected in the Cortex XDR pack for the items IncidentFields, Integrations, and Playbooks; the following would be created:
```markdown
#### IncidentFields
- __XDR Alerts__
%%UPDATE_RN%%

#### Integrations
- __Cortex XDR - IR__
%%UPDATE_RN%%

#### Playbooks
- __Cortex XDR - Isolate Endpoints__
%%UPDATE_RN%%

- __Cortex XDR - Port Scan__
%%UPDATE_RN%%

```

## MD Formatting
For single line RNs, follow this format:
```markdown
#### Integrations
- __Cortex XDR - IR__
  - Release note here.
```

For single line RNs with a nested list, follow this format:
```markdown
#### Integrations
- __Cortex XDR - IR__
  - Release note here.
    - List item 1
    - List item 2
```

For multiline RNs, follow this format:
```markdown
#### Integrations
- __Cortex XDR - IR__
  - Release note 1 here.
  - Release note 2 here.
  - Release note 2 here.
```

For multiline RNs with nested content, follow this format:
```markdown
#### Integrations
- __Cortex XDR - IR__
  - Release note 1 here.
    - List item 1
    - List item 2
  - Release note 2 here.
    - List item 1
    - List item 2
  - Release note 2 here.
```

## What Should Be Logged
One should specify in the corresponding change log file the following changes:
  - Any change made
  - Creation of a new command
  - Adding/updating parameters
  - Adding/updating arguments
  - Updating outputs
  - Fixes for customer bugs
  
  
## Excluding Items
Release notes are required to contain all items which have been changed included in the generated file. As such, validation will fail if detected items are removed from the generated release notes file.

However, you may encounter a scenario where certain changes are not necessary to document in the release notes. To solve this, you may comment out the entries by using the following syntax:

```markdown
<!--
#### Integrations
- __Cortex XDR - IR__
  - Renamed an item. Not necessary to document in release notes.
-->
```

## Common Troubleshooting Tips

<details>
<summary>I excluded an item from the changelog file, but it won't pass validation.</summary>
<br>
Make sure to remove the `%%%UPDATE_RN%%` from the generated file.
</details>
<details>
<summary>When I run the **update-release-notes** command, it does not find any of my changes.</summary>
<br>
First make sure you have committed your files. Next check to see that the type of file you changed requires a release notes entry. TestPlaybooks, Images, README's and TestData don't require release notes.
</details>

To view the previous format for release notes, you may find them [here.](../integrations/changelog-old-format)
