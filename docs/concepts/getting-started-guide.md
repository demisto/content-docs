---
id: getting-started-guide
title: Getting Started Guide
---

This guide will provide you with some pointers to jumpstart your development journey. After reading it, you’ll have a great background for creating content for the Cortex XSOAR platform.

If you have trouble with any of these items, please reach out for help over [Slack](https://start.paloaltonetworks.com/join-our-slack-community) on the `#demisto-developers` channel or, if you are/want to be a technology partner, also via [email](mailto:soar.alliances@paloaltonetworks.com).
 
## Before you start

Cortex XSOAR is a powerful platform that comes with a rich set of features and functionality that allow for a high degree of customization: we therefore recommend that you start by familiarizing yourself with the different aspects of the product:

1. Read and understand Cortex XSOAR [Concepts](../concepts/concepts).
1. Register to the [Learning Center](http://education.paloaltonetworks.com/learningcenter) and go through the [Product Training](../partners/become-a-tech-partner#3-take-required-training).
1. If you plan to publish your content to the [XSOAR Marketplace](../partners/marketplace) for other customers to use, read about the [Contribution](../contributing/contributing) process and the different tiers and support levels (partner vs community support, etc.).
1. Bookmark the links to the [Cortex XSOAR Developer Hub](https://xsoar.pan.dev/docs/) (this site) and the [Cortex XSOAR Product Documentation Page](https://docs.paloaltonetworks.com/cortex/cortex-xsoar.html).
1. Access the Palo Alto Networks [DFIR Slack Community](https://start.paloaltonetworks.com/join-our-slack-community) and join the *#demisto-developers* channel.
1. Sign up to the [Developer Newsletter](https://start.paloaltonetworks.com/cortex-xsoar-developer-newsletter.html) to receive technical updates on developing and contributing.
1. Obtain and install a copy of Cortex XSOAR. If you are not a Partner, you can obtain the Community Edition [here](https://start.paloaltonetworks.com/sign-up-for-demisto-free-edition). Installation instructions are available [here](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/installation.html).

### Other prerequisites (for Integrations and Automations)

If you want to develop Integrations and Automations, some coding is required. You will need:
1. Python (3.7 and above) or Powershell programming experience.
1. (for Integrations) API or SDK access to your product or solution you want to integrate with.

### Technology Partners

If you are or want to become a Technology Partner, make sure that you also:

1. Read the [Become a Technology Partner](../partners/become-a-tech-partner) page and follow the steps to sign up and sign the agreements.
1. Work with the [Cortex XSOAR Alliances Team](mailto:soar.alliances@paloaltonetworks.com) to make sure your use cases have been validated.

## Are you planning to contribute?

This site describes how to create content meant to be published on the XSOAR Marketplace and used by several customers. You must following proper design, development and documentation guidelines to make sure that the content can used in production in large SOCs. While it's always recommended to follow all these guidelines,  some steps, such as the dev environment setup, are mandatory only if you are planning to contribute your content.

The following summarizes some common developer profiles and recommendations on what tools to use to develop and contribute. If you are not creating Integrations and Automations, no coding is required and you can do most of the work just through the XSOAR UI.

|Who|Contributing?|Integrations/Scripts?|Write Code With|Contribute With|
|--:|------------:|--------------------:|-----------------|---------------|
|End customer<br/>Individual contributor|No|No|N/A|N/A|
|End customer<br/>Individual contributor|No|Yes|[XSOAR IDE](../concepts/xsoar-ide)|N/A|
|End customer<br/>Individual contributor|Yes|No|[XSOAR IDE](../concepts/xsoar-ide)|[Cortex XSOAR UI](../contributing/marketplace)|
|End customer<br/>Individual contributor|Yes|Yes|demisto-sdk + IDE (Pycharm, VSCode, etc.)|GitHub|
|Technology Partner<br/>Palo Alto Networks Employee|Yes|Either way|demisto-sdk + IDE (Pycharm, VSCode, etc.)|GitHub|

:::note Important Note
In general, even if you are not contributing, you are never wrong if you develop following the detailed guidelines below, including setting up the development environment and designing and documenting your content properly.
:::

If, based on the assumptions above,  you are contributing via GitHub and developing with `demisto-sdk` and an IDE, keep reading through the next sectiobn.

If you are not planning to contribute and you plan to do everything thorugh the XSOAR UI, feel free to skip to the [XSOAR IDE](xsoar-ide) document and the relevant sections in the lest menu (i.e. Playbooks)

## Contributor Guidelines

Please read the following guidelines carefully: following them will maximize the chances for a fast, easy, and effective review process for everyone involved. If something is not clear, please don't hesitate to reach out to us via [Slack](http://go.demisto.com/join-our-slack-community) on the `#demisto-developers` channel.

1. Begin by designing your contribution: we recommend to follow the [Design](../concepts/design) guidelines to identify what you want to build and make sure it is aligned with our best practices. Also check out the [Design Tutorial](../tutorials/tut-design).
1. Make sure you have all the [Development Requirements](dev-requirements) satisfied.
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
    * Document your integration and automation as detailed [here](integration-docs).
1. Make sure your Content Pack is properly [documented](../integrations/pack-docs).
1. Validate your content: the validation hook should run automatically every time you `git commit`. You can also run the validation manually by using [demisto-sdk validate](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/validate/README.md). 
1. As you build newer versions of your Content Pack, document your changes in a relevant release notes file as detailed [here](../integrations/release-notes).

At this point you should be ready to submit a Pull Request! Check out again our [Contributing Checklist](../contributing/checklist), and for more details on the review process, refer to our [PR Conventions](../contributing/conventions) document.

**Note**: if you are a technology partner, make sure you have reviewed the use cases with your [Cortex XSOAR Alliances Team](mailto:soar.alliances@paloaltonetworks.com) and that you have a *Partner ID* to associate your Pull Request to.

A good working example that summarizes all of the above is the [Hello World Content Pack](https://github.com/demisto/content/tree/master/Packs/HelloWorld) that you can use as a reference. Also check out the [Hello World Design Document](https://docs.google.com/document/d/1wETtBEKg37PHNU8tYeB56M1LE314ux086z3HFeF_cX0).

This guide doesn't cover all the topics: please browse the left sidebar and use the search bar to find what you need, and reach out for help over [Slack](https://start.paloaltonetworks.com/join-our-slack-community) on the `#demisto-developers` channel when in doubt.
