---
id: contributing
title: Contributing 
---

Thanks for being interested in contributing to Cortex XSOAR. This document describes the Contribution process.

Contributing allows you to make the content that you build on Cortex XSOAR available to every client through the  [Marketplace](../partners/marketplace). Content can be either Partner or Community supported, [Free or Paid](../partners/marketplace#pricing).

All the free content (i.e. everything excluding Paid Content Packs) is open source and lives in the Cortex XSOAR [GitHub Repository](https://github.com/demisto/content), with a MIT license.

In order to setup a developing environment that will help you create your content, you can use the [Set Up Your Dev Environment](..tutorials/tut-setup-dev#the-tutorial-starts-here) tutorial. The tutorial contains several parts including an elaborated process, you don't have to complete the entire tutorial you can just use it as a guide and to get real examples.

After you have created your content, you must submit your content for our team to review and approve.

There are three ways to submit your work:
 - In the majority of the cases and you want to provide a Content Pack that you want to support, you must open a GitHub Pull Request.
 - Starting from version 6.0, Cortex XSOAR supports a [simplified flow](../contributing/marketplace) to Contribute directly from the product UI: use this flow only if you are an individual contributor and your Content Pack is going to be community supported.
 - Only if you are providing a Premium (aka Paid) Content Pack, the GitHub process is slightly different and is described [here](../integrations/premium_packs).

 This document describes the main flow that covers most of the cases and summarizes everything you must do before and after opening a Pull Request on GitHub to contribute your pack.

Before proceeding, sure to check the content contribution [checklist](../contributing/checklist) to make sure you have created everything you need.

## Before opening a Pull Request

In order to be able to submit a Pull Request to the Cortex XSOAR [GitHub Repository](https://github.com/demisto/content), you need to:

- Have a [GitHub](https://github.com) account that you'll use to create the fork and open the Pull Request.
- Create a fork of the repo in your own Github account. You can follow the instruction described [GitHub docs](https://guides.github.com/activities/forking/) or follow this steps in the [following tutorial](https://xsoar.pan.dev/docs/tutorials/tut-setup-dev#step-2-fork-the-github-repo).
- If you're an XSOAR partner, have your `partner-id` (this should have been communicated to you over the onboarding emails from the Alliance team).
- Join our our [Slack DFIR Community](https://www.demisto.com/community/), this is the place to ask questions, consult about use-case and raise issues regarding the Cortex XSOAR platform (use the `#demisto-developers` channel).
- Design Document: we encourage you to prepare a Design Document that describes the capabilities of your Pack. Usually it's a Google Doc shared with you by the Alliances team. Click [here](https://docs.google.com/document/d/1wETtBEKg37PHNU8tYeB56M1LE314ux086z3HFeF_cX0) to see a compiled example of a Design Document.
- Create a short video to demo your product and your pack, and link it: this will be used by our reviewers to understand what your product does and how the content pack work.
- Pass the linters `demisto-sdk lint`: if you have an Integration or Script, your code must pass the [tests](../tutorials/tut-setup-dev#step-5-run-the-linter-and-unit-tests).
- Pass the validation `demisto-sdk validate`: make sure you run `demisto-sdk validate -i Packs/YourPackName` and all the checks are passed before opening the Pull Request. If unsure, ask for help on the `#demisto-developers` channel on our [Slack DFIR Community](https://www.demisto.com/community/).

## Open a Pull Request

After you have completed all the requirements and ready to open your Pull Request commit and push your work to the a branch you have created in your forked repo. 

Now you can go ahead an open your Pull Request, you can use [this article](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) to do so.
When creating the pull request make sure to fill in the different section in the pull request template.

:::note Important Note
As part of the Pull Request template, you will be asked to fill in the [contribution registration form](https://forms.gle/XDfxU4E61ZwEESSMA), make sure to do so, without it we cannot revirew your contribution.
:::


## After opening a Pull Request

After opening the Pull Request, make sure that you:

- Sign the [CLA](https://github.com/demisto/content/blob/master/docs/cla.pdf): every contributor must sign our Contributor License Agreement in order for their contribution to be added to our content.
- Monitor your Pull Request on GitHub and be ready for a demo: our Content team will add comments to the Pull Request, asking questions and requesting changes. At some point, we'll ask you to schedule a meeting to see an interactive demo, make sure you have a working installation of Cortex XSOAR with your pack fully configured.

