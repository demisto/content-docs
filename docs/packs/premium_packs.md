---
id: premium_packs
title: Premium Packs Setup
---

In this document we explain step-by-step how to develop paid content for the XSOAR Marketplace. Learn about [paid packs overview](/docs/partners/premium-packs) and the [business process required](/docs/partners/premium-packs-process).

1. Duplicate the [demisto/content-external-template](https://github.com/demisto/content-external-template) repository by clicking **Use this template** and select to create it as a private repository under your user.  
<img src="/doc_imgs/integrations/demisto_content-external-template.png" width="800"></img>  
2. To get your pack in the template repository, follow the [guidelines](https://github.com/demisto/content-external-template#getting-started) provided in the template repository. Make sure you choose your pricing for the pack.
3. Next you will need to **open your pull request**:
    - Make sure your work is done on a designated branch (not Master). This will help us conduct a proper review of the pack.
    - After you finish the work on your pack you should invite the `xsoar-bot` user as a collaborator to your repository so that we will be able to review your contribution and add it to our build system. For more information, see [how to invite collaborators to a personal repo](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/inviting-collaborators-to-a-personal-repository).
    - In your private repository [open a pull request](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) from the created branch → to the repo's Master/Main branch.
    - When the pull request is ready for review, put `xsoar-bot` as assignee and add the label `ready-for-review`. At this point we might ask you to invite and assign someone from the XSOAR content team members to review the pull request.
4. After we receive your pack, it enters the ***Review Phase***, in which we review your pull request and provide feedback/comments. In parallel to the review, we perform an internal validation process for your pack. In order to approve your pull request, the following criteria must be satisfied:
   - Pull request build must pass.
   - Implement all feedback/comments that we provide in the pull request.
   - Internal validation process must pass. If the validation process fails, we will update you and explain why it failed.
5. After we approve your pull request, you can merge the pull request.
The pack is now officially available to download in Cortex XSOAR Marketplace!
