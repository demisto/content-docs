---
id: checklist
title: Contribution Checklist
---

This document includes a checklist that summarizes the list of files that you need in order to contribute to the Cortex XSOAR content repository. Please make sure you have everything before you open a Pull Request (unless stated otherwise).

Keep in mind that content packs can contain multiple types of entities, such as Integrations, Automations, Playbooks, Incident Types, Incident Fields, and so on.

Depending on whether your content pack is aiming to be *certified* or not, there will be different requirements.

This article also includes a Pull Request checklist, that summarized everything you must do before and after opening a Pull Request on GitHub to contribute your pack.

# Content pack checklist

No matter you include in your content pack or whether it's going to be certified, the pack must include the following:

- [ ] Pack Metadata file (i.e. `Packs/YourPackName/pack_metadata.json`) : the information about your content pack. It should be compiled with all the required information
- [ ] Pack README (i.e. `Packs/YourPackName/README.md`): the readme of the pack file
- [ ] Release Notes (i.e. `Packs/YourPackName/ReleaseNotes/1_0_1.md`): these are required only if you are updating an existing Content pack, not for the first

Skeleton files are created by `demisto-sdk init`. Check out [here](pack-docs) and [here](release-notes) to find information on how to modify these files.

**Note**: Please use PascalCase (YourPackName) for the names of the directories and files that include your company, integration and playbook names (see the examples below).

Please follow the [directory structure](TK add link here) for all the directory information.

##  Integrations

If your pack contains at least an Integration, the integration directory should contain the following:

- [ ] Code file (i.e. `Packs/YourPackName/YourIntegrationName/Integrations/YourIntegrationName.py`)
- [ ] Metadata file (i.e. `Packs/YourPackName/Integrations/YourIntegrationName/YourIntegrationName.yml`)
- [ ] Description file (i.e. `Packs/YourPackName/Integrations/YourIntegrationName/YourIntegrationName_description.md`)
- [ ] Image file (i.e. `Packs/YourPackName/Integrations/YourIntegrationName/YourIntegrationName_image.png`)
- [ ] README file (i.e. `Packs/YourPackName/Integrations/YourIntegrationName/README.md`)
- [ ] Command examples file (i.e. `Packs/YourPackName/Integrations/YourIntegrationName/command_examples`)
- [ ] Unit tests file (i.e. `Packs/YourPackName/Integrations/YourIntegrationName/YourIntegrationName_test.py`)
- [ ] Unit tests data (i.e. `Packs/YourPackName/Integrations/YourIntegrationName/test_data/*.json`)

**Note**: if you use PowerShell and not Python, the extension of the code files will be `.ps1` instead of `.py`.

### Additional requirements Certified packs

If your integration is going to be *certified*, you also have the following requirements (that are optional for non-certified):

- [ ] Test Playbook (i.e. `Packs/YourPackName/TestPlaybooks/playbook-YourIntegrationName_Test.yml`)
- [ ] Custom Incident Types, Fields, Classifiers, Mappers and Layouts: *if* your integration the ability to (fetch incidents*)[fetching-incidents], most likely you will need to provide custom Incident Types and the related entifies: This is usually covered during the Design phase. Work with your Palo Alto Networks alliance contact if in doubt.

... and of course your adherence to our best practices and [code conventions](code-conventions) will be evaluated in a stricter way.

## Playbooks

If your pack contains at least a playbook, the playbook directory must contain the following files:

- [ ] Playbook file (i.e. `Packs/YourPackName/Playbooks/playbook-YourPlaybookName.yml`)
- [ ] README file (i.e. `Packs/YourPackName/Playbooks/playbook-YourPlaybookName.md`)
- [ ] Image file (i.e. `Packs/YourPackName/doc_files/YourPlaybookName.png`)

*Note*: the playbook README file must be updated with the correct image link after the Pull Request is opened, as explained in the documentation [here](integration-docs#images)

## Incident or Indicator Fields

If your pack contains at least a custom Incident or Indicator field, you'll need:

- [ ] Incident or Indicator field JSON file (i.e. `Packs/YourPackName/IncidentFields/YourIncidentFieldName.json` or `Packs/YourPackName/IndicatorFields/YourIndicatorFieldName.json`)

## Incident or Indicator Types

If your pack contains at least a custom Incident or Indicator type, you'll need:

- [ ] Incident or Indicator type JSON file (i.e. `Packs/YourPackName/IncidentTypes/YourIncidentTypeName.json` or `Packs/YourPackName/IndicatorType/YourIndicatorTypeName.json`)

If you have a custom Incident or Indicator type, most probably you'll also have to include corresponding *Classifiers*, *Mappers* and *Layouts*:

## Classifiers and Mappers

- [ ] Classifier JSON file (i.e. `Packs/YourPackName/Classifiers/classifier-YourIntegrationName.json`)
- [ ] Mapper JSON file (i.e. `Packs/YourPackName/Classifiers/classifier-mapper-incoming-YourIntegrationName.json`)

If you want your pack to be also compatible with version 5.x of Cortex XSOAR (5.0 and 5.5), you'll also need:

- [ ] 5.x Classifier & Mapper JSON file (i.e. `Packs/YourPackName/Classifiers/classifier-YourIntegrationName_5_9_9.json`)

## Incidents or Indicator Layouts

- [ ] Layout JSON file (i.e. `Packs/YourPackName/Layouts/layoutscontainer-YourIncidentTypeName.json`)

If you want your pack to be also compatible with version 5.x of Cortex XSOAR (5.0 and 5.5), you'll also need:

- [ ] 5.x Layout JSON File (one file for each Layout type, i.e. `Packs/YourPackName/Layouts/layouts-details-YourIncidentTypeName.json`)

##  Scripts (Automations)

If your pack contains at least an automation script, the automation directory should contain the following:

- [ ] Code file (i.e. `Packs/YourPackName/YourScriptName/Scripts/YourScriptName.py`)
- [ ] YML metadata file (i.e. `Packs/YourPackName/Scripts/YourScriptName/YourScriptName.yml`)
- [ ] README markdown file (`Packs/YourPackName/Scripts/YourScriptName/README.md`)
- [ ] Unit tests file (i.e. `Packs/YourPackName/Scripts/YourScriptName/YourScriptName_test.py`)
- [ ] Unit tests data files (i.e. `Packs/YourPackName/Scripts/YourScriptName/test_data/*.json`)

**Note**: if you use PowerShell and not Python, the extension of the code files will be `.ps1` instead of `.py`.

### Additional requirements Certified packs

If your integration is going to be *certified*, you also have the following requirements (that are optional for non-certified):

- [ ] Test Playbook (i.e. `Packs/YourPackName/TestPlaybooks/playbook-YourScriptName_Test.yml`)

... and of course your adherence to our best practices and [code conventions](code-conventions) will be evaluated in a stricter way.

**Note**: if your pack contains both integrations and scripts, you can use a single Test Playbook to test both.

## Widgets

If your pack contains at least a custom widget, you'll need:

- [ ] Widget JSON file (i.e. `Packs/YourPackName/Widgets/widget-YourWidgetName.json`)

## Dashboards

If your pack contains at least a custom dashboard, you'll need:

- [ ] Dashboard JSON file (i.e. `Packs/YourPackName/Dashboard/dashboard-YourDashboardName.json`)


# Pack Requirements Table

The requirements above are also summarized in the following table:

|               Entity Type |                                                                          Non-certified and certified                                                                          | Certified only  |
|--------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|---------------------------------|
| Pack                      | <ul><li>Pack metadata</li><li>Pack readme</li><li>Release Notes</li></ul>                                                                                                                       | <ul><li>Test Playbook</li></ul> |
| Integration               | <ul><li>Code file</li><li>Metadata file</li><li>Description file</li><li>Image file</li><li>README file</li><li>Command examples file</li><li>Unit tests file</li><li>Unit tests data</li></ul> |                                 |
| Playbook                  | <ul><li>Playbook file</li><li>README file</li><li>Image file</li></ul>                                                                                                                                          |                                 |
| Incident/Indicator Field  | <ul><li>Incident/Indicator field JSON file</li></ul>                                                                                                                                                             |                                 |
| Incident/Indicator Type   | <ul><li>Incident/Indicator type JSON file</li></ul>                                                                                                                                                              |                                 |
| Classifier and Mapper     | <ul><li>Classifier JSON file (for XSOAR 6.0 and above)</li><li>Mapper JSON file (for XSOAR 6.0 and above)</li><li>5.x Classifier JSON file (for XSOAR 5.x)</li></ul>                                                           |                                 |
| Incident/Indicator Layout | <ul><li>Layout JSON files (for XSOAR 6.0 and above)</li><li>5.x Layout JSON file(for XSOAR 5.x)</li>                                                                                                              </ul>|                                 |
| Script                    | <ul><li>Code file</li><li>Metadata file</li><li>README file</li><li>Unit tests file</li><li>Unit tests data</li></ul>                                                                                               | <ul><li>Test Playbook</li></ul>             |
| Widget                    | <ul><li>Widget JSON file</li></ul>                                                                                                                                                                               |                                 |
| Dashboard                 | <ul><li>Dashboard JSON file</li></ul>                                                                                                                                                                            |                                 |

# Pull Request Checklist

Before opening the Pull Request on the Cortex XSOAR [GitHub Repository](https://github.com/demisto/content), you need to:

- [ ] Have a [GitHub](https://github.com) account
- [ ] If you're an XSOAR partner, have your `partner-id` (this should have been communicated to you over the onboarding emails from the Alliances team)
- [ ] Design
- [ ] Create a short demo video of your Product and your Contribution and have a link ready
- [ ] Pass the linters `demisto-sdk lint`
- [ ] Pass the validation `demisto-sdk validate`

After opening the Pull Request, make sure that you:

- [ ] Sign the CLA
- [ ] Are ready for a demo
- [ ] Provide us credentials: you'll need to provide us some credentials to access a test/demo environment so that we will run our nightly build. Please work with your Palo Alto Networks alliance team contact to provide these to us securely.
