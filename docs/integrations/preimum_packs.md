---
id: premium_packs
title: Premium Packs setup
---

First of all, we would like to thank you for trusting us with your content. We hope to make this process as smooth and easy for you as possible.

In this document we will go over the entire process for developing paid content for XSOAR’s marketplace, step by step.
If anything is confusing or unclear,  please feel free to reach out - we would love to hear your feedback and improve this documentation with it.

1. Duplicate the demisto/content-external-template repository by clicking on the “Use this template”, then choose to create it as a private repository under your user.
2. Setup your development environment using [this](https://xsoar.pan.dev/docs/integrations/dev-setup).
3. Create your new pack under the Packs folder in the repository and use the documentation we have under the following [guide](https://xsoar.pan.dev/docs/integrations/getting-started-guide) to get you started.
4. Under your pack you will need to update your pack_metadata.json file using the description provided in [the following guide](https://xsoar.pan.dev/docs/integrations/packs-format#pack_metadatajson).
5. Once you have completed the work on the pack you should invite the “xsoar-bot” user as a collaborator to your repository so that we will be able to review your contribution and add it into our build system.
This can be done using this [guide](https://help.github.jp/enterprise/2.11/user/articles/inviting-collaborators-to-a-personal-repository/).
6. Send the details of the pack to the person you are in contact with and he will link your contribution to our system.
7. Now the review phase begins, so as a regular review we will leave comments and will ask you to fix the comments we leave there, once we approve we move to the next step.
8. When your build passes and we give you the ok you can merge the PR. When you do, our build will pull your changes once again and upload your pack to the XSOAR marketplace.
