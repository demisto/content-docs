---
id: contributing
title: Contributing XSOAR Content
---

This article describes the Contribution process for XSOAR Content.  
Contributing allows clients / partners who made custom content, enhancements to existing content, and bugfixes, to share them with the community by making them publicly available on the [Marketplace](/marketplace).
Content can be either partner or community supported, and can be either [free or paid](../partners/premium-packs#pricing).

All content (except for paid content packs) is open source, and is hosted on the [Cortex XSOAR Content GitHub Repository](https://github.com/demisto/content) licensed under the [MIT license](https://github.com/demisto/content/blob/master/LICENSE).  

**If you have any questions, please feel free to reach out to us on the `#demisto-developers` channel on our [Slack DFIR Community](https://www.demisto.com/community/).**  
:::note
This article is only for content contributions.  
For contributions to the documentation (like the current article for example), please refer to [Documentation Contributions](docs-contrib).  
:::

## Content Support Types
Contributions can be either officially supported (by Palo Alto Networks, a Technology Partner, or an individual), or *community* supported.  

### Officially Supported Packs
Officially supported packs include an email address or a website of the contributor for customers to contact for support (that they will be referred to in case of an issue), and have a more strict quality-control process.

### Community Supported Packs
Community supported packs on the other hand, do not have a support contact (customers will be able to ask questions on our [Live Community Forum](https://live.paloaltonetworks.com/t5/cortex-xsoar-discussions/bd-p/Cortex_XSOAR_Discussions)), and will have a less strict quality-control process.

:::info
Contributed content for Palo Alto Networks products (e.g. PAN-OS, XDR, etc.) will be required to be officially supported.  
Because of that, the contributed content might be adopted at some point be officially supported and maintained by the XSOAR Content team.
:::

## Contribution Methods
After creating new content to contribute, you must submit your content to Palo Alto Networks. the Cortex XSOAR Content Team will review and approve it before it becomes available to customers.
Before starting to work on a contribution, it is recommended to go over the [Contribution SLA](../contributing/sla) article.

There are several ways to submit contributions:

### Cortex XSOAR Content GitHub Repository (Pull Request)
Contribute by creating a fork and opening a pull request on the [Cortex XSOAR Content GitHub repository](https://github.com/demisto/content).  
Use this method in the following scenarios:
    - You are a Technology Partner contributing with *partner* supported new content.
    - Your contribution is big and contains lots of different parts (Integrations, Scripts, Playbooks, Layouts, etc) that is likely to lead to a complex review process.
    - You are proficient with GitHub.

:::tip
For contributing through GitHub, we recommend to use a GitHub Codespace, which will provide you with a pre-configured ready-to-use development environment.  
This method is still experimental, but will make the contribution, development, and review processes much easier.  
For more information and a step-by-step guide, see the dedicated [GitHub Codespace Setup tutorial](../tutorials/tut-setup-dev-codespace.md).
:::

### Cortex XSOAR Marketplace
Contribute from within Cortex XSOAR's UI using the [Marketplace](../contributing/marketplace). This method is simpler and doesn't require to set up a development environment or be familiar with git. However, it is recommended **only** in the following scenarios:
    - You are an individual contributor, contributing **new** content that is *community* supported.
    - You are making small changes to **existing** content, even if it's *XSOAR* or *partner* supported (usually a bug fix or adding a new command to an Integration).

:::caution
Contributing from the marketplace has several limitations:
* The built-in editor is very limited and does not support features full-fledged IDEs have.
* Documentation files (README, instance configuration help, etc.) cannot be created or edited.
* Unit tests cannot be created or updated.
* Private content packs cannot be contributed this way.

Because of these limitations, we do not recommend to use this method for large contributions.
:::

### A Private GitHub Repository (Premium Packs)
Contributing from a private GitHub repository is required when the contribution is for a **Premium** (paid) content pack, to make sure the content is not publicly available.  
The requirements are the same as supported packs, and the contribution process of premium packs is described in [the following dedicated article](../packs/premium_packs).

This document describes the main method that covers *supported* and free contributions(i.e. item *2.* in the above list) and summarizes everything you must do before and after opening a Pull Request on GitHub to contribute your pack.

---

:::note
The following sections are necessary only for *officially supported* contributions,
but we still recommended to read them even if you are contributing *community supported* content to be aware of the best practices are.  
(The *Pull Request Process* section is not relevant for contributions that were created from the Marketplace).
:::

## Guidelines
Please carefully review the following guidelines, as they will greatly enhance the likelihood of a swift, streamlined, and efficient review process for all parties involved. If you have any questions or require clarification, please feel free to contact us through the Slack platform using the #demisto-developers channel.

1. Begin by designing your contribution. we recommend to follow the [Design](../concepts/design) guidelines to identify what you want to build and make sure it is aligned with our best practices. Also check out the [Design Tutorial](../tutorials/tut-design).
2. Make sure you have all the [Contributing Requirements](../contributing/contrib-requirements) satisfied.
3. Setup a development environment by following the brief [Dev Setup Guide](../concepts/dev-setup) or the more detailed [Tutorial](../tutorials/tut-setup-dev).
4. Follow the [Content Pack Structure](../packs/packs-format) to build your contribution. [demisto-sdk init](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md) will help you create it.
5. If you are updating an **existing** content pack, make sure it is updated with the latest version available in the marketplace before proceeding.
6. Depending on the content entities you need to build, navigate to the specific section of this website for details. If you are creating Integrations and/or Scripts (aka Automations), make sure that you:
    * Use the proper  [Integration/Script Directory Structure](../integrations/package-dir). [demisto-sdk init](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md) will help you create it. If working on existing code, beyond trivial changes, we require converting to this structure as it allows running linting and unit tests and provides a clearer review process.
    * Understand the [YAML file](../integrations/yaml-file) structure and the [Parameter Types](../integrations/parameter-types).
    * Make sure your integration follows our [Logo Guidelines](../integrations/integration-logo).
    * Read and follow [Python code conventions](../integrations/code-conventions) (recommended) or [Powershell code conventions](../integrations/powershell-code) (advanced users only).
    * If your integration generates Incidents, follow the [Fetch Incidents](../integrations/fetching-incidents) guidelines.
    * Make sure your commands make proper use of the [Context](../integrations/context-and-outputs), including [Context Standards](../integrations/context-standards-about) and [DBotScore](../integrations/dbot).
    * Make sure to create unit tests as documented [here](../integrations/unit-testing) and that the various linters we support pass as detailed [here](../integrations/linting).
    * Document your integration and automation by generating the [README File](../documentation/readme_file).
7. Create the appropriate [Content Pack Documentation](../documentation/pack-docs).
8. Make sure you follow the [Documentation Best Practices](../documentation/documentation_tips).
9. As you build newer versions of your Content Pack, document your changes in a relevant release notes file as detailed [here](../documentation/release-notes).

At this point you should be ready to submit a Pull Request!  
Check out our [Contributing Checklist](../contributing/checklist) to make sure you have all the parts you need.

:::tip
A good working example that implements all of the above guidelines is the [Hello World Content Pack](https://github.com/demisto/content/tree/master/Packs/HelloWorld), which can be useful as a reference (alongside the [Hello World Design Document](https://docs.google.com/document/d/1wETtBEKg37PHNU8tYeB56M1LE314ux086z3HFeF_cX0)).
:::

:::note
If you are an XSOAR Technology Partner, make sure you have reviewed the use-cases with your [Cortex XSOAR Alliances Team](mailto:soar.alliances@paloaltonetworks.com) and that you have a *Partner ID* to associate your Pull Request to.
:::

## Pull Request Submission Process
### Prerequisites
Before submitting a Pull Request to the [Cortex XSOAR GitHub Repository](https://github.com/demisto/content), the following requirements must be met:
- Make sure to check the content contribution [checklist](../contributing/checklist), and assure that all the required files exist and are properly formatted.
- Create and upload your contribution to a GitHub **fork** of the XSOAR Content repository, and submit your changes **on a new branch** (do **NOT** push your changes to the *master* branch).
- Validate your content: the validation hook should run automatically every time you run `git commit`. You can also run the validation manually by using [demisto-sdk validate](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/validate/README.md): `demisto-sdk validate -i Packs/YourPackName`.
- If your contribution has Integrations or Scripts, run linting (which also runs [unit tests](../tutorials/tut-setup-dev#step-5-run-the-linter-and-unit-tests)) by running `demisto-sdk lint -i Packs/YourPakName`.
- Create a short demo video presenting the product and your pack, and link it. This will help our reviewers to better understand what the product is used for, and the newly contributed content integrates with it.

![Creating a fork](../doc_imgs/contributing/create-a-new-fork.gif)

### Pull Request Creation
After all the prerequisites are met, and you are ready to create your Pull Request, commit and push your work to the branch you have created in your forked repository (if you haven't already done so).
Then on the main page of your forked repository, click on the **Compare & pull request** button to open a new Pull Request (on the original Cortex XSOAR Content repository).  
Make sure to fill in the description template, and click on **Create pull request**.

For additional information on how to create a Pull Request from a fork, you can refer to [official GitHub documentation](https://help.github.com/articles/creating-a-pull-request-from-a-fork).

### Post-Submission
After submitting your Pull Request sign our [Contributor License Agreement (CLA)](https://github.com/demisto/content/blob/master/docs/cla.pdf), and monitor your Pull Request on GitHub.  
Our Content team will add comments to the Pull Request, asking questions and requesting changes.  
In order to establish a proper release timeframe for your contribution, you are required to respond and apply the requested changes within 14 days.  
Stale Pull Requests will be closed.

At some point, when the review process is complete (or close to completion), we'll ask to schedule a meeting for an interactive demo.  
Prepare for it, and make sure you have a working installation of Cortex XSOAR with your contributed pack fully configured. Check out our [Contribution Demo Page](../contributing/demo-prep) for additional information.

:::caution
As part of the Pull Request template, you will be asked to fill in the [contribution registration form](https://forms.gle/XDfxU4E61ZwEESSMA).  
Make sure to do so, as without it, your contribution we will not be able to review your contribution.
:::

:::info
If after signing the CLA it still shows as unsigned, refer to the [FAQ](../concepts/faq#cla-is-pending-even-though-i-signed-the-agreement) for possible solutions.
:::

For more details on how properly create and manage your Pull Request, check out the dedicated [Pull Request Conventions](../contributing/conventions) article.