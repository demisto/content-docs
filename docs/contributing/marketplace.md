---
id: marketplace
title: Contributing From Cortex XSOAR Marketplace
---

Cortex XSOAR v6.0 introduces a Marketplace which is the central location for installing, exchanging, contributing, and managing all of your content, including playbooks, integrations, automations, fields, layouts, and more. For more information, you can read all about the [Marketplace](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/marketplace/marketplace-overview.html).

This article walks you through the process of contributing content from the Marketplace.

1. Contribute your content pack from Cortex XSOAR. For more information, see [Contribute a Content Pack](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/marketplace/content-pack-contributions.html).

2. After you contribute the content pack a message displays explainingi that your contribution is ready for review, and includes a link to a form you need to fill in to complete your contribution. You will receive an email with a link to the form.

3. In the form, complete the following steps.
     - Fill in additional details, such as, pack name, author, and description.
     - Log in to your GitHub account so you can participate in the review process of the pull request that will be opened for your content pack.
     - Sign the [Palo Alto Networks Contributor License Agreement](https://github.com/demisto/content/blob/master/docs/cla.pdf).
     
4. After you submit the form you will be redirected to a page that informs you that pack was received and is being processed.  
5. A GitHub branch will be created in the [xsoar-contrib Content repository fork](https://github.com/xsoar-contrib/content) based on the pull request that will be opened.
6. You will receive an invitation to join the **xsoar-contrib** organization, so the **xsoar-bot** will be able to invite you to a GitHub team and grant you write permissions to the created branch.
(Each contributor can only modify files in content packs that they contributed).
7. The pull request is created and a reviewer is assigned.
8. You can now modify the files changed in the pull request as part of the review process.

:::note
In order to update the content pack that you contributed, you will need to modify the files in the pull request created in GitHub or close the pull request and create a new contribution.
:::
 
