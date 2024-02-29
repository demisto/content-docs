---
id: packs-format
title: Content Packs Structure
---

For better separation between Content artifacts from different use cases and Partners we use a directory structure called `Content Packs`. Each `Content Pack` behaves like a mini content repo. It contains all relevant content items within its directory.

For instance a pack for CortexXDR will look as can be seen in the Content Repository
[Packs/CortexXDR](https://github.com/demisto/content/tree/master/Packs/CortexXDR).

To generate a new pack make sure to use: `demisto-sdk init --pack`. Detailed command instructions are available [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md).

**Note**: The Content repo is going through a transition phase to move all content into packs. During this phase you will see some Content artifacts are still not maintained within Packs. All new Content should be maintained via Packs.

## Directories  

All the directories within the pack are the representation of all the possible entities possible in Content. And the pack will be located in the Content repo under `Packs/<Pack Name>`
```
- Integrations        
- Scripts
- Playbooks
- Reports
- Dashboards
- IncidentTypes
- IncidentFields
- Layouts
- Classifiers
- IndicatorTypes
- IndicatorFields
- Connections
- TestPlaybooks
```

## Pack files

The pack directory contains numerous configuration files used for metadata and documentation.

Please note that all of the following files will be created using the `demisto-sdk init --pack`, and some of them
will have to be filled by you. An explanation for each of them will be provided below.

### pack_metadata.json

This file contains all the relevant metadata about the pack.

The following fields are populated in the pack metadata:

| Field Name | Field Type | Field Description |
| ---- | ---- |  ---- |
| name | String | The pack name. Usually it's the name of the integration the pack contains (e.g. CortexXDR) or the use-case implemented in it. |
| description | String | A short overview of the pack. |
| support | String | Should be one of the following:<br />1.  xsoar - Supported by Cortex XSOAR.<br />2.  partner - Supported by a Cortex XSOAR partner.<br />3.  developer - Supported by an independent developer/organization.<br />4.  community - Not officialy supported, but available for the community to use.<br /> For `partner` and `developer`, either email address or URL fields must be filled out.  |
| currentVersion | String | The pack version, in the format of `x.x.x`. On the initial release this should be set to "1.0.0". See [here](#content-packs-versioning)|
| author | String | The name of the organization (for partners) or developer (for individual contributions) which developed the integration. |
| url | String | The URL to which users should refer to in case of support needed regarding the pack. Usually is the organization support URL or the developer GitHub repository. If left empty the default support site presented to users will be the [Live Community](https://live.paloaltonetworks.com/t5/cortex-xsoar-discussions/bd-p/Cortex_XSOAR_Discussions) site.|
| videos | String | The Youtube video link of the pack.|
| email | String | The email address to which users should reach out to in case of support needed regarding the pack. |
| categories | List | The use-case categories which are implemented in the pack. Usually set by the integration, which included in the pack category. Should be one of the following:<br />1. Analytics & SIEM<br />2. Utilities<br />3. Messaging<br />4. Endpoint<br />5. Network Security<br />6. Vulnerability Management<br />7. Case Management<br />8. Forensics & Malware Analysis<br />9. IT Services<br />10. Data Enrichment & Threat Intelligence<br />11. Authentication<br />12. Database<br />13. Deception<br />14. Email Gateway|
| tags | List | Tags to be attached to the pack on Cortex XSOAR marketplace. |
| created | String | Pack creation time in ISO 8601 format - YYYY-MM-DDTHH:mm:ssZ, e.g. 2020-01-25T10:00:00Z |
| useCases | List | Use-cases implemented by the pack. |
| keywords | List | List of strings by which the pack can be found in Cortex XSOAR marketplace. |
| marketplaces    | List | List of marketplaces in which the pack can be found (XSOAR XSIAM). |
| hidden | Boolean | (Optional) Whether to hide the pack from Marketplace. Updates to this pack will not be published to Marketplace and the pack cannot be installed. |
| dependencies | Dictionary | (Optional) An object that describes the content packs that the pack is dependant on. Should be kept empty on pack creation, as it is calculated by Cortex XSOAR content infrastructure. |
| displayedImages | List | (Optional) Images to be displayed in Cortex XSOAR marketplace. Should be kept empty on pack creation, as it is calculated by Cortex XSOAR content infrastructure. |
| githubUser | List | (Optional) List of Github usernames to receive notification in the PR in case pack files were modified. |
| devEmail | List | (Optional) List of emails to receive notification in case contributed pack files were modified. |
| certification | String | (Optional) If the pack is certified the value of this fields should be "certified". The allowed values are "certified" and "verified". |
| itemPrefix | String | (Optional) String to overwrite pack fields prefix. You can specify an alternative string instead of the default pack name enforced by the validation process. |

Pack metadata contents for example:

```json
{
    "name": "Palo Alto Networks Cortex XDR - Investigation and Response",
    "description": "Cortex XDR is the world's first detection and response app that natively integrates network, endpoint and cloud data to stop sophisticated attacks.",
    "support": "xsoar",
    "currentVersion": "1.0.0",
    "author": "Cortex XSOAR",
    "url": "https://www.paloaltonetworks.com/cortex",
    "videos": "https://www.youtube.com/watch?v=ium2969zgn8",
    "email": "",
    "categories": [
        "Endpoint"
    ],
    "tags": [
        "Recommended by Cortex XSOAR",
        "xdr"
    ],
    "created": "2020-03-11T13:16:53Z",
    "useCases": [
        "Malware"
    ],
    "keywords": [
        "adaptive cyber protection",
        "apt"
    ],
    "dependencies": {
        "Base": {
            "mandatory": true,
            "name": "Base"
        },
        "CortexXDR": {
            "mandatory": false,
            "name": "Palo Alto Networks - Cortex XDR"
        }
    },
    "displayedImages": [
        "CortexXDR"
    ]
}
```

A supported partner pack metadata contents for example:

```json
{
    "name": "Product name",
    "description": "Pack description",
    "support": "partner",
    "currentVersion": "1.1.0",
    "author": "Partner name",
    "url": "https://support.<partner>.com",
    "email": "support@<partner>.com",
    "devEmail": "dev@<partner>.com",
    "categories": [
        "Deception"
    ],
    "tags": [],
    "created": "2020-03-19T09:39:30Z",
    "useCases": [],
    "keywords": [],
    "dependencies": {},
    "githubUser": [
        "<partner Github username>"
    ]    
}
```

### Content Packs Versioning

Pack versions have the following format MAJOR.MINOR.REVISION:

   1. **Revision** when you make backwards compatible bug fixes.
   2. **Minor** when you add functionality in a backwards compatible manner.
   3. **Major** when you make incompatible API changes or revamping the pack by adding to it a lot of new backwards compatible functionality.

### README.md

The file contains a general explanation for the pack and you are free to add any information relevant for the pack. For more details refer to the [Pack Documentation](../documentation/pack-docs) page.

### .secrets-ignore

This file will be used while running the `demisto-sdk secrets`([explanation](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/secrets/README.md)), we will determine the file and will
 use it as an allow list of approved words for your PR.

**Note**: We use `demisto-sdk secrets` as part of our pre-commit hook to check that possible secrets in the PR aren't exposed to a public repository.

### .pack-ignore

1) This file allows ignoring linter errors while lint checking and ignoring tests in the test collection.

   To add ignored tests/linter errors in a file, first, add the file name to the **.pack-ignore** in this format
```
[file:integration-to-ignore.yml]
```

On the following line add `ignore=` flag, with one or more comma-separated values:
* `auto-test` - ignore test file in the build test collection.
* `linter code` e.g., IN126 - ignore linter error codes.

2) By default, unit-tests of scripts/integrations are running without a docker network.

   In case one of the integrations/scripts inside a pack needs a network during the unit-tests run, this can be done in this format

```
[tests_require_network]
integration-id-1
script-id-1
```

#### Example .pack-ignore
```
[file:playbook-Special-Test-Not-To-Run-Directly.yml]
ignore=auto-test

[file:integration-to-ignore.yml]
ignore=IN126,PA116

[tests_require_network]
integration-id-1
script-id-1
```

### Author_image.png

It's possible to add an author image - a logo of the contributing company, which will be displayed on the marketplace page of the pack, under the "PUBLISHER" section.  
The image should be saved in the root directory of the pack (e.g., `content/packs/MyPackName`), be named `Author_image.png`, and have a size of up to 4 KB, at a resolution of 120x50.

:::info Partner Contributions
For partner contributions, this file is mandatory, and will be validated as part of the build process.  
If the file is missing, the build will fail with the following validation error:

```bash
- Issues with unique files in pack: $PACK_NAME
  Packs/$PACK_NAME/Author_image.png: [IM109] - Partners must provide a non-empty author image under the path Packs/$PACK_NAME/Author_image.png
```
:::
 
:::note
If the `Author_image.png` file does not exist, the name of the author will be displayed under the "PUBLISHER" section instead.
:::

### CONTRIBUTORS.json

If you are contributing to an existing pack, you can add a **CONTRIBUTORS.json** file to the root of the pack in the event that one does not already exist. The file should contain a list of strings including your name.

#### Example of a CONTRIBUTORS.json file:
```json
[
    "Jane Doe",
    "John Smith"
]
```

#### Once your contribution is merged, pack details will show the following:

![image](https://user-images.githubusercontent.com/44666568/176713193-8a0857bf-a5ed-45cd-98e4-3c575752c0ff.png)
