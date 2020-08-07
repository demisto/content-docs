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
| currentVersion | String | The pack version, in the format of `x.x.x`. On the initial release this should be set to "1.0.0". |
| author | String | The name of the organization / developer which developed the integration. |
| url | String | The URL to which users should refer to in case of support needed regarding the pack. Usually is the organization support URL or the developer GitHub repository. |
| email | String | The email address to which users should reach out to in case of support needed regarding the pack. |
| categories | List | The use-case categories which are implemented in the pack. Usually set by the integration, which included in the pack category. Should be one of the following:<br />1. Analytics & SIEM<br />2. Utilities<br />3. Messaging<br />4. Endpoint<br />5. Network Security<br />6. Vulnerability Management<br />7. Case Management<br />8. Forensics & Malware Analysis<br />9. IT Services<br />10. Data Enrichment & Threat Intelligence<br />11. Authentication<br />12. Database<br />13. Deception<br />14. Email Gateway|
| tags | List | Tags to be attached to the pack on Cortex XSOAR marketplace. |
| created | String | Pack creation time in ISO 8601 format - YYYY-MM-DDTHH:mm:ssZ, e.g. 2020-01-25T10:00:00Z |
| useCases | List | Use-cases implemented by the pack. |
| keywords | List | List of strings by which the pack can be found in Cortex XSOAR marketplace. |
| dependencies | Dictionary | (Optional) An object that describes the content packs that the pack is dependant on. Should be kept empty on pack creation, as it is calculated by Cortex XSOAR content infrastructure. |
| displayedImages | List | (Optional) Images to be displayed in Cortex XSOAR marketplace. Should be kept empty on pack creation, as it is calculated by Cortex XSOAR content infrastructure. |
| githubUser | List | (Optional) List of Github usernames to receive notification in the PR in case pack files were modified. |
| certification | String | (Optional) If the pack is certifed the value of this fields should be "certified" |


Pack metadata contents for example:

```json
{
    "name": "Palo Alto Networks Cortex XDR - Investigation and Response",
    "description": "Cortex XDR is the world's first detection and response app that natively integrates network, endpoint and cloud data to stop sophisticated attacks.",
    "support": "xsoar",
    "currentVersion": "1.0.0",
    "author": "Cortex XSOAR",
    "url": "https://www.paloaltonetworks.com/cortex",
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
    "url": "https://www.<partner>.com",
    "email": "support@<partner>.com",
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


### README.md
The file contains a general explanation for the pack and you are free to add any information relevant for the pack.

### .secrets-ignore
This file will be used while running the `demisto-sdk secrets`([explanation](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/secrets/README.md)), we will determine the file and will
 use it as a  white list of approved words for your PR.

**Note**: We use `demisto-sdk secrets` as part of our pre-commit hook to check that possible secrets in the PR aren't exposed to a public repository.
