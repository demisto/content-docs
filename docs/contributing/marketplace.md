---
id: marketplace
title: Contributing From Cortex XSOAR Marketplace
---

Cortex XSOAR v6.0 introduces a marketplace to share content, for more details refer to the [Marketplace Overview](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/marketplace/marketplace-overview.html).

This article walks you through the flow of contributing content from the marketplace.

1. On Cortex XSOAR, contribute as described in [this article](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/marketplace/content-pack-contributions.html).

2. You will then be promoted with a toast saying that your contribution is ready for review, with a link to a form you need to fill to complete your contribution.
In addition, you will receive an email with the link to the form.

3. In the form you will be asked for the following:
     - Fill in additional details, such as: pack name, author and description.
     - Log in to your GitHub account, so you can later participate in the review process as part of the pull request that will be opened.
     - Sign the [Palo Alto Networks Contributor License Agreement](https://github.com/demisto/content/blob/master/docs/cla.pdf).
     
4. After submitting the form, you will be redirected to a page in which it will say that pack was accepted and is being processed.  
5. A GitHub branch will be created in the [xsoar-contrib Content repository fork](https://github.com/xsoar-contrib/content), based on the pull request will be opened.
6. An invitation to join the **xsoar-contrib** organization will be sent to you, so xsoar-bot will be able to invite you to a GitHub team to give you write permissions to the branch created.
(Each contributor can modify only files in content packs he contributed).
7. The pull request will then be created, and a reviewer will be assigned to it.
8. You can now modify the files changed in the pull request as part of the review.

:::note
In order to update the content pack you contributed, you will need modify the files in the GitHub pull request created, or close the pull request and create a new contribution.
:::
 