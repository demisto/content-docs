---
id: packs-format
title: Content Packs Structure
---

As part of the content contribution process we are using a structure called `Content Packs`.  
This content artifact will behave like a mini content repo. we will have all the relevant content items relevant 
fot that pack located within it.
<br/>
For instance a pack for CortexXDR will look as can be seen in the Content Repository: [Packs/CortexXDR](https://github.com/demisto/content/tree/master/Packs/CortexXDR)

### Directories  
All the directories within the pack are the representation of all the possible entities possible in Content. And the pack will be located in the Content repo under `Packs/<Pack Name>`
```angular2
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

### Pack files
The pack will have few files for its' configuration. And will give you a place to add your documentation for the 
pack, and some metadata regarding the pack itself.
Please note that all of the following files will be created using the `demisto-sdk init --pack`, and some of them 
will have to be filled by you. An explanation for each of them will be provided below.

#### .secrets-ignore
This file will be used while running the `demisto-sdk secrets`([explanation](https://github.com/demisto/demisto-sdk/blob/master/docs/secrets.md)), we will determine the file and will
 use it as a  white list of approved words for your PR.
##### Note: We check that you don't have secrets in the PR so you don't leak any potential secrets to a public repository.
 
#### pack_metadata.json
This file will contain all the relevant metadata about the pack and will be maintained in the future using the demisto-sdk.
Information that you can find there is: the author name(you), pack id, etc...  
This file will generate the structure of the file based on our need but the contents should be filled
 by you. This data will be fields like the support details, in order to contact you about the pack you've just wrote,
  or the pack name.

#### changelog.md
This file will contain the version history for the pack. Each entry of the file will direct to the pack version and 
release notes for that specific version. This file will have to be filled by you when changing an integration, and it will specify the work that was done with that change.
It helps us maintain the version history of your pack.

#### README.md
This file will be the general explanation for the pack and will contain any information you want to put there.