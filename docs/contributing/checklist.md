---
id: checklist
title: Contribution Checklist
---


This is a checklist that summarizes the list of files that you need in order to contribute to the Cortex XSOAR content repository. Please make sure you have everything before you open a Pull Request (unless stated otherwise).

Keep in mind that content packs can contain multiple types of entities, such as Integrations, Automations, Playbooks, Incident Types, Incident Fields, and so on.

Depending on whether your content pack is aiming to be *certified* or not, there will be different requirements.

## Pack requirements

No matter what is included in your content pack or whether it's going to be certified, you'll need to provide the following:
- [ ] Pack Metadata file (i.e. `Packs/YourPackName/pack_metadata.json`) : the information about your content pack. It should be compiled with all the required information
- [ ] Pack README (i.e. `Packs/YourPackName/README.md`): the readme of the pack file
- [ ] Release Notes (i.e. `Packs/YourPackName/ReleaseNotes/1_0_1.md`)

Information on how to compile this documentation can be found [here](/integrations/docs/pack-docs)

Please use PascalCase (YourPackName) for the names of the directories and files that include your company, integration and playbook names (see the examples below).

Please follow the [directory structure](TK add link here) for all the directory information.

###  Integration requirements

If your pack contains at least an Integration, the integration directory should contain the following:

- [ ] Integration code file (i.e. `Packs/YourPackName/YourIntegrationName/YourIntegrationName.py`)
- [ ] Integration YML metadata file (i.e. `Packs/YourPackName/YourIntegrationName/YourIntegrationName.yml`)
- [ ] Integration description markdown file (i.e. `Packs/YourPackName/YourIntegrationName/YourIntegrationName_description.md`)
- [ ] Integration README markdown file (`Packs/YourPackName/YourIntegrationName/README.md`)
- [ ] Integration Unit Tests (i.e. `Packs/YourPackName/YourIntegrationName/YourIntegrationName_test.py`)
- [ ] Integration Unit Test data if required by your Unit Tests (i.e. `Packs/YourPackName/YourIntegrationName/test_data/command1.json`)

*Note*: if instead of Python you use PowerShell, the extension of the code files will be `.ps1` instead of `.py`.

#### Additional requirements Certified packs

If your integration is going to be *certified*, you also have the following requirements (that are optional for non-certified):

- [ ] Test Playbook (i.e. `Packs/YourPackName/TestPlaybooks/playbook-YourIntegrationName_Test.yml`)
- [ ] Custom Incident Types, Fields, Classifiers, Mappers and Layouts: *if* your integration the ability to [**fetch incidents**](TK add link), most likely you will need to provide custom Incident Types and the related entifies: This is usually covered during the Design phase. Work with your Palo Alto Networks alliance contact if in doubt.

... and of course your adherence to our [best practices](TK put link here) will be evaluated in a stricter way.

### Playbook requirements

If your pack contains at least a playbook, the playbook directory must contain the following files:

- [ ] Playbook file (i.e. `Packs/YourPackName/Playbooks/playbook-YourPlaybookName.yml`)
- [ ] Playbook README markdown file (i.e. `Packs/YourPackName/Playbooks/playbook-YourPlaybookName.md`)
- [ ] Playbook image file (i.e. `Packs/YourPackName/Playbooks/playbook-YourPlaybookName.md`)

*Note*: the playbook README file must be updated with the correct image link after the Pull Request is opened, as explained in the documentation [here](TK add link)

### Incident or Indicator Fields

If your pack contains at least a custom Incident or Indicator field, you'll need:

- [ ] Incident or Indicator field JSON files (i.e. `Packs/YourPackName/IncidentFields/YourIncidentFieldName.json` or `Packs/YourPackName/IndicatorFields/YourIndicatorFieldName.json`)

### Incident or Indicator Types

If your pack contains at least a custom Incident or Indicator type, you'll need:

- [ ] Incident or Indicator type JSON files (i.e. `Packs/YourPackName/IncidentTypes/YourIncidentTypeName.json` or `Packs/YourPackName/IndicatorType/YourIndicatorTypeName.json`)

If you have a custom Incident or Indicator type, most probably you'll also have to include corresponding *Classifiers*, *Mappers* and *Layouts*:

#### Classification and Mapping

- [ ] Classifier files
- [ ] Mapper files

If you want your pack to be also compatible with version 5.x of Cortex XSOAR (5.0 and 5.5), you'll also need:

- [ ] Classification & Mapping JSON file

#### Incident or Indicator Layouts

- [ ]  Layout Files (one for each type of Layout)

If you want your pack to be also compatible with version 5.x of Cortex XSOAR (5.0 and 5.5), you'll also need:

- [ ] 5.x Layout File (one file only that contains all layout types)

## Pull Request requirements

Before opening the Pull Request:

- [ ] GitHub account
- [ ] Design
- [ ] Pass the linters `demisto-sdk lint`
- [ ] Pass the validation `demisto-sdk validate`

After opening the Pull Request:

- [ ] Sign the CLA
- [ ] Be ready for a demo
- [ ] Credentials: you'll need to provide us some credentials to access a test/demo environment so that we will run our nightly build. Please work with your Palo Alto Networks alliance team contact to provide these to us securely.

