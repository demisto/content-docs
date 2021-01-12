---
id: dev-requirements
title: Development Requirements
---

This article summarizes all the requirements you need to satisfy in order to be able to develop content (including code parts, such as Integrations and Automations) and contribute it to Cortex XSOAR.

Before you read this part, make sure you follow the general [preqreuisites](getting-started-guide#before-you-start).

If you are not sure whether you should read this, more details can be found [here](getting-started-guide#are-you-planning-to-contribute).

## Requirements

### Cortex XSOAR

You need an instance of Cortex XSOAR up and running. You can Sign Up for the [Cortex XSOAR Free Edition](https://start.paloaltonetworks.com/sign-up-for-demisto-free-edition) or, if you're entitled to, contact the XSOAR Alliances team to have a non-production license.

### Development OS

Our recommended OS for development is either macOS or Linux, as we use bash and docker in some of our validation/testing flows. We also support Windows through WSL.

#### Windows Users

If you are working on Windows, you can either work with a Linux VM or utilize [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). 

**Note:** When using WSL2 you may experience performance issues if working on the Windows mounted file system (for example `/mnt/c/`). See the following [WSL issue](https://github.com/microsoft/WSL/issues/4197) for more info. In such cases we recommend using the Linux file system (`ext4` partition) WSL2 provides. Meaning that the local demisto content and the SDK will all be located on the WSL file system and using an editor which supports remote WSL. Editors supporting remote WSL include:
* VS Code: https://code.visualstudio.com/docs/remote/wsl
* PyCharm Professional Edition: https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html 

#### Other Operating Systems

If you successfully manage to develop and contribute on other platforms (native Windows, OpenBSD, etc.), please let us know and we'll add it to the tutorial! (click on Report an issue at the bottom of this page).

### GitHub

You will need a **[GitHub](https://github.com)** account, as the contribution process requires you to submit a Pull Request in the [Cortex XSOAR Content Repository](https://github.com/demisto/content). To learn more about Pull Requests and contributing , check out the [Collaborating with issue and pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests) tutorial on GitHub.


And you will need a `git` client on your system (git, GitHub Desktop, SourceTree, etc). In the examples we'll just use the `git` command line client. See: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git for git client install instructions.

### Python

You will need to build your integration using **Python** and, more specifically, Python 3.7+. While some content is built via Javascript and Python 2, we require Python 3.7+ for contributions.

:::note
Note
You don't need to be a a Python expert to write a good integration, although some intermediate level knowledge is preferred. Just make sure you adhere to our [Code Conventions](../integrations/code-conventions).
:::

It is also recommended to have a dedicated Python 3 installed on your system: for that purpose, please download and install **[pyenv](https://github.com/pyenv/pyenv)**. It allows to easily manage multiple versions of Python on your system.

Optionally, macOS users can install via [homebrew](https://docs.brew.sh/Homebrew-and-Python).

#### PowerShell

Starting from version 5.5 of Cortex XSOAR, we also support [PowerShell](../integrations/powershell-code). However, we recommend to use it only for advanced users as the amount of content examples is limited at the moment.

### Docker

If you are writing code (i.e. Integrations and Scripts), you will need to run several linters and [unit tests](unit-testing) to validate your code, as we do in our build process. In this case you must install docker. See: https://docs.docker.com/install/ for install options.

:::note
If you're using WSL, you cannot run Docker natively on WSL, but you can install Docker Desktop on Windows and configure WSL to communicate to it using [this](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly) tutorial.
:::

### Node.js and NPM
Optional. We use Node.js for validating README documentation files for Integrations, Automations and Playbooks. If you are creating README documentation files, we recommend installing Node.js to be able to validate the files locally. Node.js installation instructions for your target platform are available at: https://nodejs.org/en/download/package-manager/.
