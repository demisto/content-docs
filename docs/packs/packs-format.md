---
id: packs-format
title: Content Packs Structure
---

For better separation between Content artifacts from different use cases and Partners we use a directory structure called Content Packs. Each Content Pack behaves like a mini content repo. It contains all relevant content items within its directory.

For example, the Cortex XDR pack can be seen in the content repository.
[Packs/CortexXDR](https://github.com/demisto/content/tree/master/Packs/CortexXDR).

To generate a new pack, use: `demisto-sdk init --pack`. Read more information about the `demisto-sdk init` command in the [Demisto SDK Guide](https://docs-cortex.paloaltonetworks.com/r/1/Demisto-SDK-Guide/init).


## Directories  

The directories within the pack represent all the possible content entities. Each pack is located in the Content repo under `Packs/<Pack Name>`
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

## Pack Files

The pack directory contains numerous configuration files used for metadata and documentation.

All of the following files are created using the `demisto-sdk init --pack`, and some of them
need to be manually populated. 

### `pack_metadata.json`

This file contains all the relevant metadata about the pack.

The following fields are populated in the pack metadata:

| Field Name | Field Type | Field Description |
| ---- | ---- |  ---- |
| `name` | `String` | The pack name. Usually it's the name of the integration the pack contains (for example, Cortex XDR) or the use case implemented in it. |
| `description` | `String` | A short overview of the pack. |
| `support` | `String` | Should be one of the following:<br />1.  `xsoar` - Supported by Cortex XSOAR.<br />2.  `partner` - Supported by a Cortex XSOAR partner.<br />3.  `developer` - Supported by an independent developer/organization.<br />4.  `community` - Not officially supported, but available for the community to use.<br /> For `partner` and `developer`, either email address or URL fields must be filled out.  |
| `currentVersion` | `String` | The pack version, in the format of `x.x.x`. On the initial release this should be set to "1.0.0". See [here](#content-packs-versioning).|
| `author` | `String` | The name of the organization (for partners) or developer (for individual contributions) which developed the integration. |
| `url` | `String` | The URL to which users should refer to in case of support needed regarding the pack. Usually is the organization support URL or the developer GitHub repository. If left empty the default support site presented to users will be the [Live Community](https://live.paloaltonetworks.com/t5/cortex-xsoar-discussions/bd-p/Cortex_XSOAR_Discussions) site.|
| `videos` | `String` | The Youtube video link of the pack.|
| `email` | `String` | The email address to which users should reach out to for support regarding the pack. |
| `categories` | `List` | The use case categories which are implemented in the pack, usually set by the integration. The list of approved categories can be found [here](https://github.com/demisto/content/blob/master/Config/approved_categories.json).|
| `tags` | `List` | Tags to be attached to the pack on Cortex XSOAR marketplace. The list of approved tags can be found [here](https://github.com/demisto/content/blob/master/Config/approved_tags.json). |
| `created` | `String` | Pack creation time in ISO 8601 format - YYYY-MM-DDTHH:mm:ssZ, e.g. 2020-01-25T10:00:00Z |
| `useCases` | `List` | Use cases implemented by the pack. The list of approved use cases can be found [here](https://github.com/demisto/content/blob/master/Config/approved_usecases.json). |
| `keywords` | `List` | List of strings by which the pack can be found in Cortex XSOAR marketplace. |
| `marketplaces`    | `List` | List of marketplaces in which the pack can be found. Possible values are `xsoar` (XSOAR 6 and XSOAR 8), `xsoar_on_prem` (XSOAR 6), `xsoar_saas` (XSOAR 8), `marketplacev2` (XSIAM) and `xpanse` (XPANSE). |
| `hidden` | `Boolean` | (Optional) Whether to hide the pack from Marketplace. Updates to this pack will not be published to Marketplace and the pack cannot be installed. |
| `dependencies` | `Dictionary` | (Optional) An object that describes the content packs that the pack is dependant on. Should be kept empty on pack creation, as it is calculated by Cortex XSOAR content infrastructure. |
| `displayedImages` | `List` | (Optional) Images to be displayed in Cortex XSOAR Marketplace. Should be kept empty on pack creation, as it is calculated by Cortex XSOAR content infrastructure. |
| `githubUser` | `List` | (Optional) List of GitHub usernames to receive notification in the PR in case pack files were modified. |
| `devEmail` | `List` | (Optional) List of emails to receive notification in case contributed pack files were modified. |
| `certification` | `String` | (Optional) If the pack is certified the value of this fields should be `certified`. The allowed values are `certified` and `verified`. |
| `itemPrefix` | `String` | (Optional) String to overwrite pack fields prefix. You can specify an alternative string instead of the default pack name enforced by the validation process. |
| `defaultDataSource` | `String` | (Optional) The default data source integration in XSIAM, for packs that have more then one fetching integration. When a default data source needs to be selected, the event collector and the most used integration is preferred if available. |

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

Pack versions have the following format `MAJOR.MINOR.REVISION`:

   1. **Revision** when you make backwards compatible bug fixes.
   2. **Minor** when you add functionality in a backwards compatible manner.
   3. **Major** when you make incompatible API changes or revamping the pack by adding to it a lot of new backwards compatible functionality.

### `README.md`

The file contains a general explanation for the pack and you are free to add any information relevant for the pack. For more details refer to the [Pack Documentation](../documentation/pack-docs) page.

### `.secrets-ignore`

This file will be used while running the `demisto-sdk secrets`([explanation](https://docs-cortex.paloaltonetworks.com/r/1/Demisto-SDK-Guide/secrets)), we will determine the file and will
 use it as an allow list of approved words for your PR.

**Note**: We use `demisto-sdk secrets` as part of our pre-commit hook to check that possible secrets in the PR aren't exposed to a public repository.

### `.pack-ignore`

1) This file allows ignoring linter errors while lint checking and ignoring tests in the test collection.

   To add ignored tests/linter errors in a file, first, add the file name to the `.pack-ignore` in this format:

    ```ini title=".pack-ignore"
    [file:integration-to-ignore.yml]
    ```

On the following line add `ignore=` flag, with one or more comma-separated values:
* `auto-test` - ignore test file in the build test collection.
* `linter code` e.g., IN126 - ignore linter error codes.

2) By default, unit-tests of scripts/integrations are running without a docker network.

   In case one of the integrations/scripts inside a pack needs a network during the unit-tests run, this can be done in this format

    ```ini title=".pack-ignore"
    [tests_require_network]
    integration-id-1
    script-id-1
    ```

#### Example `.pack-ignore`
```ini title=".pack-ignore"
[file:playbook-Special-Test-Not-To-Run-Directly.yml]
ignore=auto-test

[file:integration-to-ignore.yml]
ignore=IN126,PA116

[tests_require_network]
integration-id-1
script-id-1
```

### `Author_image.png`

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

### `CONTRIBUTORS.json`

If you are contributing to an existing pack, you can add a `CONTRIBUTORS.json` file to the root of the pack in the event that one does not already exist. The file should contain a list of strings including your name.

#### Example of a `CONTRIBUTORS.json` file:
```json
[
    "Jane Doe",
    "John Smith"
]
```

#### Once your contribution is merged, pack details will show the following:

![image](https://user-images.githubusercontent.com/44666568/176713193-8a0857bf-a5ed-45cd-98e4-3c575752c0ff.png)
