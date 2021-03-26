---
id: adopt 
title: Adopt-a-Pack 
---

The Cortex XSOAR Adopt-a-Pack program provides our technical partners a way to ‘take over’ a pack that was originally written by Demisto or Cortex XSOAR developers. The partner becomes the maintainer and supporter of the pack and receives several benefits as outlined below.

## Benefits for our Partner
Adopting a pack has several advantages for the partner:
- Differentiation: deliver unique solutions, commands, use cases, etc. in the pack.
- Control: Directly set the pack’s roadmap, features and release timing.
- Feedback: Receive direct input from actual users in the form of defects and enhancement requests.
- Visibility: See and review all community updates to that pack as a GitHub Reviewer.

### Marketing with Palo Alto Networks
- Opportunity to place company name and logo on the pack.
- Add detailed description and marketing to the pack (see yellow box, below) including links, images, company overview, etc. 
- Engage in marketing activities with Palo Alto Networks (e.g. joint solution blog).

![pack example cyren](../doc_imgs/partners/packexample_cyren.png)

## Process
The process to Adopt-a-Pack is simple:
1. Partner signs the Palo Alto Networks Technology Partnership Agreement. If you've already signed our agreement, you will not have to sign again. We may need to send you a statement via email but there is no additional paperwork to Adopt. 
1. Partner notifies Palo Alto Networks that they wish to adopt the pack. *Important:* you must notify us so we can work with you. 
1. Partner opens a PR on the pack. The PR must update the pack readme and elevant release note both containing the text below, and increment the version number. To increment the version and adjust the release note it is recommended to run `demisto-sdk update-release-notes -i Packs/<MyPack>` which will generate a new release note file and will bump the pack version. More information can be found [here](..docs/documentation/release-notes). This starts the 90 day transition period. 
1. Once that PR is merged, the Partner is able to make changes and updates to the pack via PR(s), but the primary support will remain with Palo Alto Networks. (If the existing pack is not in use, the transition time can be shortened.) 
1. After the 90 day transition period has elapsed, the Partner submits a pull request updating the readme (per text below), support information, and increments the version number and officially takes over the pack!

### Text for the Pack
For partners who received permission for the adoption process, please add the following text to the **top** of the pack readme.md file and the relevant release note.
- At the start of the adoption process: `Note: Support for this pack will be moving to the partner around <<Month>>, <<Day>>, <<Year>>.` (Be sure to update the date to 90 days in the future.)
- At the end of the 90 day period: `Note: Support for this pack moved to the partner on <<Month>>, <<Day>>, <<Year>>. Please contact the partner directly via the support link on the right.` (Be sure to update the date.)
