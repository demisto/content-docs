---
id: dev-setup
title: Development Setup
---

:::note Important Note
This article is focused on setting up a development environment that you should use to create and contribute supported new content. If you are not planning to contribute or your contribution will be only community supported, this is not a requirement. For more details, refer to the [Getting Started Guide](../concepts/getting-started-guide#using-the-right-tools).
:::

**This article summarize the steps from the end-to-end [Setup Tutorial](../tutorials/tut-setup-dev): for more details please refer to [it](../tutorials/tut-setup-dev).**

Before you read this make sure you read the [Getting Started Guide](../concepts/getting-started-guide) and the [Contribution Requirements](../contributing/contrib-requirements) doc.

## Setting Up a Development Repository

[Fork](https://guides.github.com/activities/forking/) the Cortex XSOAR Content repository and create a branch for your contribution (do not work on the `master` or `main` branch).

### Install VSCode extension

Setup the [Cortex XSOAR VSCode extension](vscode-extension.md).


### demisto-sdk

This is our help tool that will make your lives easier during the contribution process, it will help you generate a [Pack](../packs/packs-format). And will help you maintain your files and validate them before committing to the branch.

#### Setup in content environment Dev Container with XSOAR extension for VSCode
See [Setup with Cortex XSOAR](vscode-extension.md#setup-content-environment-with-vscode-extension)

#### Install demisto-sdk locally (UNIX systems or WSL)
One option is to install
  `demisto-sdk` locally (In Linux or macOS systems) see instructions [here](https://github.com/demisto/demisto-sdk)

To check the you have the latest version of the sdk run:

```bash
demisto-sdk --version
```

If you want more details, please refer to the end-to-end [Tutorial](../tutorials/tut-setup-dev).

## IDE

Cortex XSOAR offers two IDEs for developing:

* [Built-in Platform Cortex XSOAR IDE](../concepts/xsoar-ide) (not recommended for complex/advanced use cases. More details [here](getting-started-guide#using-the-right-tools).)
* [Visual Studio Code Extension](vscode-extension)

You can also use your IDE of choice along with `demisto-sdk`, for example Visual Studio Code.
