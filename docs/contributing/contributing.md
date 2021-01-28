---
id: contributing
title: Contributing 
---

Thanks for being interested in contributing to Cortex XSOAR. This document describes the Contribution process. If you are not sure whether you should read this, more details can be found [here](getting-started-guide#creating-new-content).

Contributing allows you to make the content that you build on Cortex XSOAR available to every client through the  [Marketplace](../partners/marketplace). Content can be either Partner or Community supported, [Free or Paid](../partners/marketplace#pricing).

All the free content (i.e. everything excluding Paid Content Packs) is open source and lives in the Cortex XSOAR [GitHub Repository](https://github.com/demisto/content), with a MIT license.

In order to setup a developing environment that will help you create your content, you can use the [Set Up Your Dev Environment](https://xsoar.pan.dev/docs/tutorials/tut-setup-dev#the-tutorial-starts-here) tutorial. The tutorial contains several parts including an elaborated process, you don't have to complete the entire tutorial you can just use it as a guide and to get real examples.

After you have created your content, you must submit your content for our team to review and approve.

There are three ways to submit your work:
 1. Starting from version 6.0, Cortex XSOAR supports a [simplified flow](../contributing/marketplace) to Contribute directly from the product UI: use this flow only if you are an individual contributor and your Content Pack is going to be community supported.
 1. If you want to provide a Content Pack that you want to support (i.e. if you are a Technology Partner), you must open a GitHub Pull Request.
 1. Only if you are providing a Premium (aka Paid) Content Pack, the GitHub process is slightly different and is described [here](../integrations/premium_packs).

 This document describes the main flow that covers cases 2 and 3 and summarizes everything you must do before and after opening a Pull Request on GitHub to contribute your pack.

## Contributor Guidelines

Please read the following guidelines carefully: following them will maximize the chances for a fast, easy, and effective review process for everyone involved. If something is not clear, please don't hesitate to reach out to us via [Slack](http://go.demisto.com/join-our-slack-community) on the `#demisto-developers` channel.

1. Begin by designing your contribution: we recommend to follow the [Design](../concepts/design) guidelines to identify what you want to build and make sure it is aligned with our best practices. Also check out the [Design Tutorial](../tutorials/tut-design).
1. Make sure you have all the [Contributing Requirements](../contributing/contrib-requirements) satisfied.
1. Setup a development environment by following the brief [Dev Setup Guide](dev-setup) or the more detailed [Tutorial](../tutorials/tut-setup-dev).
1. Review the [Contribution](../contributing/contributing) process and [Checklist](../contributing/checklist).
1. Follow the [Content Pack format](packs-format) to build your contribution. [demisto-sdk init](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md) will help you create it.
1. Depending on the content entities you need to build, navigate to the specific section of this website for details. If you are creating Integrations and/or Automations, make sure that you:
    * Use the proper  [Directory Structure](../integrations/package-dir). [demisto-sdk init](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md) will help you create it. If working on existing code, beyond trivial changes, we require converting to this structure as it allows running linting and unit tests and provides a clearer review process.
    * Understand the [YAML file](../integrations/yaml-file) structure and the [Parameter Types](../integrations/parameter-types).
    * Make sure your integration follows our [Logo Guidelines](../integrations/integration-logo).
    * Read and follow [Python code conventions](../integrations/code-conventions) (recommended) or [Powershell code conventions](../integrations/powershell-code) (advanced users only).
    * If your integration generates Incidents, follow the [Fetch Incidents](../fetching-incidents) guidelines.
    * Make sure your commands make proper use of the [Context](../integrations/context-and-outputs), including [Context Standards](../integrations/context-standards-about) and [DBotScore](../integrations/dbot).
    * Run and verify that the various linters we support pass as detailed [here](../integrations/linting).
    * Make sure to create unit tests as documented [here](../integrations/unit-testing)
    * Document your integration and automation as detailed [here](../documentation/readme_file) and [here](../documentation/documentation_tips).
1. Make sure your Content Pack is properly [documented](../documentation/pack-docs) and read the [documentation best practices](../documentation/documentation_tips).
1. Validate your content: the validation hook should run automatically every time you `git commit`. You can also run the validation manually by using [demisto-sdk validate](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/validate/README.md). 
1. As you build newer versions of your Content Pack, document your changes in a relevant release notes file as detailed [here](../documentation/release-notes).

At this point you should be ready to submit a Pull Request! Check out again our [Contributing Checklist](../contributing/checklist), and for more details on the review process, refer to our [PR Conventions](../contributing/conventions) document.

**Note**: if you are a technology partner, make sure you have reviewed the use cases with your [Cortex XSOAR Alliances Team](mailto:soar.alliances@paloaltonetworks.com) and that you have a *Partner ID* to associate your Pull Request to.

A good working example that summarizes all of the above is the [Hello World Content Pack](https://github.com/demisto/content/tree/master/Packs/HelloWorld) that you can use as a reference. Also check out the [Hello World Design Document](https://docs.google.com/document/d/1wETtBEKg37PHNU8tYeB56M1LE314ux086z3HFeF_cX0).

This guide doesn't cover all the topics: please browse the left sidebar and use the search bar to find what you need, and reach out for help over [Slack](https://start.paloaltonetworks.com/join-our-slack-community) on the `#demisto-developers` channel when in doubt.


## Before opening a Pull Request

In order to be able to submit a Pull Request to the Cortex XSOAR [GitHub Repository](https://github.com/demisto/content), you need to:

- Make sure to check the content contribution [checklist](../contributing/checklist) to make sure you have created everything you need.
- Make sure you follow the general [prerequisites](getting-started-guide#before-you-start), satisfy the [requirements](../contributing/contrib-requirements) and set up the [development environment](../concepts/dev-setup) ([tutorial](../tutorials/tut-setup-dev)).
- Make sure you are working on a GitHub **fork** of the XSOAR content repository, and **create a branch** for your contribution (do **NOT** work on *master*).
- If you're an XSOAR partner, have your `partner-id` (this should have been communicated to you over the onboarding emails from the Alliance team).
- Design Document: we encourage you to prepare a Design Document that describes the capabilities of your Pack. Usually it's a Google Doc shared with you by the Alliances team. Click [here](https://docs.google.com/document/d/1wETtBEKg37PHNU8tYeB56M1LE314ux086z3HFeF_cX0) to see a compiled example of a Design Document.
- Create a short video to demo your product and your pack, and link it: this will be used by our reviewers to understand what your product does and how the content pack work.
- Pass the linters `demisto-sdk lint`: if you have an Integration or Script, your code must pass the [tests](../tutorials/tut-setup-dev#step-5-run-the-linter-and-unit-tests).
- Pass the validation `demisto-sdk validate`: make sure you run `demisto-sdk validate -i Packs/YourPackName` and all the checks are passed before opening the Pull Request. If unsure, ask for help on the `#demisto-developers` channel on our [Slack DFIR Community](https://www.demisto.com/community/).

## Open a Pull Request

After you have completed all the requirements and ready to open your Pull Request commit and push your work to the a branch you have created in your forked repo. 

Now you can go ahead an open your Pull Request, you can use [this article](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) to do so.
When creating the pull request make sure to fill in the different section in the pull request template.

:::note Important Note
As part of the Pull Request template, you will be asked to fill in the [contribution registration form](https://forms.gle/XDfxU4E61ZwEESSMA), make sure to do so, without it we cannot review your contribution.
:::


## After opening a Pull Request

After opening the Pull Request, make sure that you:

- Sign the [CLA](https://github.com/demisto/content/blob/master/docs/cla.pdf): every contributor must sign our Contributor License Agreement in order for their contribution to be added to our content. In case of CLA issues check out our [FAQs](../concepts/faq#cla-is-pending-even-though-i-signed-the-agreement).
- Monitor your Pull Request on GitHub and be ready for a demo: our Content team will add comments to the Pull Request, asking questions and requesting changes. At some point, we'll ask you to schedule a meeting to see an interactive demo, make sure you have a working installation of Cortex XSOAR with your pack fully configured.

For more details on how to handle the Pull Request, check out our [Pull Request Conventions](../contributing/conventions).

