---
id: contributing
title: Contributing 
---

:::note
This article is focused on contributing Cortex XSOAR Content. If you want to contribute fixes/suggestions to our development and reference Content docs (the site you are currently browsing) go to: [Documentation Contributions](docs-contrib).
:::

Thanks for being interested in contributing to Cortex XSOAR. This document describes the Contribution process. If you are not sure whether you should read this, make sure you read the [Getting Started Guide](../concepts/getting-started-guide) first.

Contributing allows you to make the content that you build on Cortex XSOAR available to every client through the  [Marketplace](../partners/paid-packs). Content can be either Partner or Community supported, [Free or Paid](../partners/paid-packs#pricing).

All the free content (i.e. everything excluding Paid Content Packs) is open source and lives in the Cortex XSOAR [GitHub Repository](https://github.com/demisto/content), with a MIT license.

## Support and requirements

Contributions can be either officially supported (by Palo Alto Networks, a Technology Partner, or an individual developer), or *community* supported: the former means that when a customer has a problem with the content, they will have an email address or web site to reach out to, and they will expect an answer. When the contribution is *community* supported, it's not required to provide support (customers will ask questions on our [Live Community Forum](https://live.paloaltonetworks.com/t5/cortex-xsoar-discussions/bd-p/Cortex_XSOAR_Discussions)) and the quality requirements for the contribution to be accepted will be lower.

For more information about the different support levels, check the [official documentation](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/marketplace/marketplace-overview/content-packs-support-types.html).

## How to contribute

After you have created your content, you must submit your content to Palo Alto Networks: the Cortex XSOAR Content Team will review and approve it before it becomes available to customers.

There are three ways to submit your work:
 1. Contribute from the Cortex XSOAR UI [Marketplace](../contributing/marketplace). This flow is simpler and doesn't require to set up a development environment or be familiar with git. However, it is recommended **only** in the following scenarios:
    - You are an individual contributor, contributing **new** content that is *community* supported.
    - You are making small changes to **existing** content, even if it's *xsoar* or *partner* supported (usually a bug fix or adding a new command to an Integration).
 1. Contribute through a GitHub Pull Request on the public [XSOAR Content Repository](https://github.com/demisto/content). Use this flow in the following scenarios:
     - You are a Technology Partner contributing with *partner* supported new content.
     - Your contribution is big and contains lots of different parts (Integrations, Scripts, Playbooks, Layouts, etc) that is likely to lead to a complex review process.
     - You are proficient with GitHub.
 1. Contribute through a private GitHub repository: this is required if you are providing a **Premium** (aka Paid) Content Pack. The requirements are the same of supported Packs, and the contribution process is described [here](../packs/premium_packs).

This document describes the main flow that covers *supported* and free contributions(i.e. item *2.* in the above list) and summarizes everything you must do before and after opening a Pull Request on GitHub to contribute your pack.

If you are contributing *community* supported content, feel free to skip the rest of this document (although it's still recommended to read it to be aware of the best practices).

## Contributor Guidelines

Please read the following guidelines carefully: following them will maximize the chances for a fast, easy, and effective review process for everyone involved. If something is not clear, please don't hesitate to reach out to us via [Slack](http://go.demisto.com/join-our-slack-community) on the `#demisto-developers` channel.

1. Begin by designing your contribution: we recommend to follow the [Design](../concepts/design) guidelines to identify what you want to build and make sure it is aligned with our best practices. Also check out the [Design Tutorial](../tutorials/tut-design).
1. Make sure you have all the [Contributing Requirements](../contributing/contrib-requirements) satisfied.
1. Setup a development environment by following the brief [Dev Setup Guide](../concepts/dev-setup) or the more detailed [Tutorial](../tutorials/tut-setup-dev).
1. Follow the [Content Pack Structure](../packs/packs-format) to build your contribution. [demisto-sdk init](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md) will help you create it.
1. Depending on the content entities you need to build, navigate to the specific section of this website for details. If you are creating Integrations and/or Scripts (aka Automations), make sure that you:
    * Use the proper  [Integration/Script Directory Structure](../integrations/package-dir). [demisto-sdk init](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md) will help you create it. If working on existing code, beyond trivial changes, we require converting to this structure as it allows running linting and unit tests and provides a clearer review process.
    * Understand the [YAML file](../integrations/yaml-file) structure and the [Parameter Types](../integrations/parameter-types).
    * Make sure your integration follows our [Logo Guidelines](../integrations/integration-logo).
    * Read and follow [Python code conventions](../integrations/code-conventions) (recommended) or [Powershell code conventions](../integrations/powershell-code) (advanced users only).
    * If your integration generates Incidents, follow the [Fetch Incidents](../fetching-incidents) guidelines.
    * Make sure your commands make proper use of the [Context](../integrations/context-and-outputs), including [Context Standards](../integrations/context-standards-about) and [DBotScore](../integrations/dbot).
    * Make sure to create unit tests as documented [here](../integrations/unit-testing) and that the various linters we support pass as detailed [here](../integrations/linting).
    * Document your integration and automation by generating the [README File](../documentation/readme_file).
1. Create the appropriate [Content Pack Documentation](../documentation/pack-docs).
1. Make sure you follow the [Documentation Best Practices](../documentation/documentation_tips).
1. As you build newer versions of your Content Pack, document your changes in a relevant release notes file as detailed [here](../documentation/release-notes).

At this point you should be ready to submit a Pull Request! Check out our [Contributing Checklist](../contributing/checklist) to make sure you have all the parts you need.

:::note XSOAR Technology Partners
If you are an XSOAR Technology Partner, make sure you have reviewed the use cases with your [Cortex XSOAR Alliances Team](mailto:soar.alliances@paloaltonetworks.com) and that you have a *Partner ID* to associate your Pull Request to.
:::

A good working example that summarizes all of the above is the [Hello World Content Pack](https://github.com/demisto/content/tree/master/Packs/HelloWorld) that you can use as a reference. Also check out the [Hello World Design Document](https://docs.google.com/document/d/1wETtBEKg37PHNU8tYeB56M1LE314ux086z3HFeF_cX0).

This guide doesn't cover all the topics: please browse the left sidebar and use the search bar to find what you need, and reach out for help over [Slack](https://start.paloaltonetworks.com/join-our-slack-community) on the `#demisto-developers` channel when in doubt.


## Before opening a Pull Request

In order to be able to submit a Pull Request to the Cortex XSOAR [GitHub Repository](https://github.com/demisto/content), you need to:

- Make sure to check the content contribution [checklist](../contributing/checklist) to make sure you have created everything you need.
- Make sure you are working on a GitHub **fork** of the XSOAR content repository, and **create a branch** for your contribution (do **NOT** work on *master*).
- Validate your content: the validation hook should run automatically every time you run `git commit`. You can also run the validation manually by using [demisto-sdk validate](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/validate/README.md): `demisto-sdk validate -i Packs/YourPackName`.  If you get an error that is unclear, ask for help on the `#demisto-developers` channel on our [Slack DFIR Community](https://www.demisto.com/community/).
- (*Only if your contribution has Integrations or Scripts*): Pass lint checks and [unit tests](../tutorials/tut-setup-dev#step-5-run-the-linter-and-unit-tests) with `demisto-sdk lint -i Packs/YourPakName`.
- Create a short video to demo your product and your pack, and link it: this will be used by our reviewers to understand what your product does and how the content pack work.


## Open a Pull Request

After you have completed all the requirements and are ready to open your Pull Request, commit and push your work to the branch you have created in your forked repo. 

Now you can go ahead an open your Pull Request, you can use [this article](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) to do so.
When creating the pull request make sure to fill in the different section in the pull request template.

## After opening a Pull Request

After opening the Pull Request, make sure that you:

- Sign the [CLA](https://github.com/demisto/content/blob/master/docs/cla.pdf): every contributor must sign our Contributor License Agreement in order for their contribution to be added to our content. In case of CLA issues check out our [FAQs](../concepts/faq#cla-is-pending-even-though-i-signed-the-agreement).
- Monitor your Pull Request on GitHub and be ready for a demo: our Content team will add comments to the Pull Request, asking questions and requesting changes. At some point, we'll ask you to schedule a meeting to see an interactive demo, make sure you have a working installation of Cortex XSOAR with your pack fully configured.

:::note Important Note
As part of the Pull Request template, you will be asked to fill in the [contribution registration form](https://forms.gle/XDfxU4E61ZwEESSMA), make sure to do so, without it we cannot review your contribution.
:::

For more details on how to handle the Pull Request, check out our [Pull Request Conventions](../contributing/conventions).
