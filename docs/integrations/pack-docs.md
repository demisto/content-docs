---
id: pack-docs
title: Pack Documentation
---

Content Packs displayed in the Cortex XSOAR Marketplace contain 2 main documentation sections: 
* **Description**: displayed in the Content Pack card when browsing the Marketplace and in the top of the *Details* tab.
* **README**: displayed in the main display area of the *Details* tab.

#### Screenshots
* *Description* in Pack display card: <br/>  
<img src="../doc_imgs/integrations/gdpr-card.png" width="250"></img>  
* Details Tab with *Description* and *README*:
![](../doc_imgs/integrations/gdpr-details.png)    


## Pack Description
The Pack Description is maintained in the `pack_metadata.json` file under the description field. Packs should always contain a description, even if a README file is provided with more details. This is to allow users to get a short overview of the Pack when browsing the Marketplace.

### General Description Guidelines
- Short and to the point
- Convey gain/benefit for user
- If possible - what is unique about this pack (e.g. minimal, extended, fast, thorough, streamlined etc.)
- Use active voice (You, yours, do, use, investigate) where possible
- Omit redundancy (Do not repeat the name of the pack, do not start with "Use this…")
- Must respect product capitalization (e.g. Content Pack)
- Constant tense (e.g. if "Engages" than "investigates", not "investigating")
- Up to 150 chars
- Up to 4 lines

#### An example of turning a "fat" description into a "lean" description:
**Before** 300 chars / 44 words:  
Use this content pack to investigate and remediate a potential phishing incident. The playbook simultaneously engages with the user that triggered the incident, while investigating the incident itself and enriching the relevant IOCs.
The final remediation tasks are always decided by a human analyst.

**After** 139 chars / 10 words :  
Streamline Investigation and remediation of Phishing incidents. Playbook engages with users while simultaneously investigates and enriches.

#### An example of turning a "passive" description into a "active" description:
**Before** (passive and impersonal):  
Provides data enrichment for domains and IP addresses.

**After** (active and personal) :  
Enrichment for your domains and IP addresses.

## Pack README
For larger Packs that provide a use case, we recommend creating a README file which will be displayed in the *Details* tab of the Pack. The `README.md` file should be markdown formatted and placed in the Packs root directory. The file should contain a more detailed overview of the Pack compared to the *Description* section. You are free to add any information you see fit to include about the pack. It is recommended to provide an overview of what the Pack does and how to start working with the Pack.  

### Images
Images can provide a great addition to the Pack `README.md` and can help users to get a quick understanding of the Pack. For Packs that contain playbooks which implement a use case, we recommend including at least an image of the main use case playbook.  Images can be included in the same way as documented for integrations. See the [following for instructions](integration-docs#images). 
