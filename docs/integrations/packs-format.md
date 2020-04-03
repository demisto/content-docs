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
- Misc
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
Information that you can find there is: the author name(you), pack id, etc...  
This file will generate the structure of the file based on our need but the contents should be filled
 by you. This data will be fields like the support details, in order to contact you about the pack you've just wrote,
  or the pack name.

### README.md
The file contains a general explanation for the pack and you are free to add any information relevant for the pack.

### .secrets-ignore
This file will be used while running the `demisto-sdk secrets`([explanation](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/secrets/README.md)), we will determine the file and will
 use it as a  white list of approved words for your PR.

**Note**: We use `demisto-sdk secrets` as part of our pre-commit hook to check that possible secrets in the PR aren't exposed to a public repository.
