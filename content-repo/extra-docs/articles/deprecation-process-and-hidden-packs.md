---
id: deprecation-process-and-hidden-packs
title: Deprecating content items and hide packs processes
description: Review content items deprecation and hidden packs processes.
---
## What Deprecated Content Item Means
Deprecated content items are no longer supported, and **should not be used**. The feature may no longer be considered efficient or safe.

The **only** content items that can be deprecated are **integrations, scripts and playbooks**.

A pack is considered deprecated when all of its integrations, scripts and playbooks are deprecated.

## How to Deprecate an Integration
1) Add the following key to the integration yaml file: 
   ```deprecated: true```

2) Add the following sentence to the integration yaml's description: 
  
   ```description: Deprecated. {reason why it is deprecated} either {use integration v2 instead} or {No available replacement}```

Example: No available replacement integration:
<img src="../../../docs/doc_imgs/integrations/deprecated-integration-1.png" width="400" align="middle"></img>

Example: Use other integration example:
<img src="../../../docs/doc_imgs/integrations/deprecated-integration-2.png" width="400" align="middle"></img>

## How to Deprecate a Script
1) Add the following key to the script yaml file: 
```deprecated: true```

2) Add the following sentence to the script yaml's comment: 
   ```description: Deprecated. {reason why it is deprecated} or {Use other script instead} or {No available replacement}```
   
Example: No available replacement script:
<img src="../../../docs/doc_imgs/scripts/deprecated-script-1.png" width="400" align="middle"></img>  

Example: Use other script:
<img src="../../../docs/doc_imgs/scripts/deprecated-script-2.png" width="400" align="middle"></img>

## How to Deprecate a Playbook
1) Add the following key to the playbook yaml file:
   ```deprecated: true```

2) Add the following sentence to the playbook yaml's description:
   ```Deprecated. {reason why it is deprecated} or {use other playbook instead} or {No available replacement}```

Example: No available replacement playbook:
<img src="../../../docs/doc_imgs/playbooks/deprecated-playbook-1.png" width="400" align="middle"></img>

Example: Use other playbook:
<img src="../../../docs/doc_imgs/playbooks/deprecated-playbook-2.png" width="400" align="middle"></img>

## Hidden Packs
A hidden pack will no longer be shown in Marketplace.

A pack should be hidden from Marketplace when all of its integrations, scripts, and playbooks are deprecated.

There is a validation in the demisto-sdk that checks that such packs are marked as hidden.

## How to Make a Pack Hidden
There are two options to make a pack hidden:
- Manually add the following key to the `pack_metadata.json` file.
   ```"hidden": true```
   
- Run the following command to automatically add the `"hidden"` key to the `pack_metadata.json` file.
  ```demisto-sdk format -i Packs/<pack-name>/pack_metadata.json```

<img src="../../../docs/doc_imgs/packs/hidden-pack.png" width="400" align="middle"></img>