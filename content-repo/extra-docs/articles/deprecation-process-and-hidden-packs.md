---
id: deprecation-process-and-hidden-packs
title: Deprecating content items and hide packs processes
description: Review content items deprecation and hidden packs processes.
---

## What Deprecated Content Item Means
Deprecated content items are no longer supported, and **should not be used**. The feature may no longer be considered efficient or safe.

## Supported Content Items
The **only** content items that can be deprecated are **integrations, scripts and playbooks**.

A pack is considered deprecated when all of its integrations, scripts and playbooks are deprecated.

## Deprecating integration process

Deprecating integration is a very simple process. 

1) Add the following key to the integration yaml file ```deprecated: true```.

2) Add the following sentence to the integration yml's description : Deprecated. {reason why it is deprecated} either {use integration v2 instead} or {No available replacement}

no available replacement integration example:
<img src="../../../docs/doc_imgs/integrations/deprecated-integration-1.png" width="400" align="middle"></img>

use other integration example:
<img src="../../../docs/doc_imgs/integrations/deprecated-integration-2.png" width="400" align="middle"></img>

## Deprecating script process

Deprecating script is a very simple process.

1) define in the script yml file the following key: ```deprecated: true```.

2) Add to the script yml comment the sentence: Deprecated. "reason why it is deprecated" or "use other script instead" or "No available replacement"

no available replacement script example:
<img src="../../../docs/doc_imgs/scripts/deprecated-script-1.png" width="400" align="middle"></img>  

use other script example:
<img src="../../../docs/doc_imgs/scripts/deprecated-script-2.png" width="400" align="middle"></img>

## Deprecating playbook process

Deprecating playbook is a very simple process.

1) define in the playbook yml file the following key: ```deprecated: true```.

2) Add to the playbook yml comment the sentence: Deprecated. "reason why it is deprecated" or "use other playbook instead" or "No available replacement"

no available replacement playbook example:
<img src="../../../docs/doc_imgs/playbooks/deprecated-playbook-1.png" width="400" align="middle"></img>

use other playbook example:
<img src="../../../docs/doc_imgs/playbooks/deprecated-playbook-2.png" width="400" align="middle"></img>

## Hidden Packs
Hidden pack means that customers will not see that pack in the marketplace anymore.

A pack should be hidden from the marketplace when all of its integrations, scripts and playbooks are deprecated.

Right now there is a validation in our content build which checks whether all the integrations, scripts and playbooks are deprecated for every pack.

In case all integrations, scripts and playbooks of a single pack are deprecated the validation will alert to make the pack hidden from the marketplace.

## Making Pack Hidden Process
There are two options to make a pack hidden:

1) by adding manually to the `pack_metadata.json` the key ```"hidden": true```

2) by running ```demisto-sdk format -i Packs/<pack-name>/pack_metadata.json``` it will automatically hide the pack as seen below.

<img src="../../../docs/doc_imgs/packs/hidden-pack.png" width="400" align="middle"></img>