---
id: vscode-extension
title: Visual Studio Code Extension
sidebar_label: VSCode Extension
---

The Cortex XSOAR extension for Visual Studio Code enables you to design and author scripts and integrations for Cortex XSOAR directly from VSCode. The extension adds a set of commands, as a sidebar with Automation and Integration Settings, just like the Settings sidebar in the Cortex XSOAR script editor. When writing code, the plugin provides you with auto-completion of Cortex XSOAR and Python functions.
The extension also provides an easy-to-use set of demisto-sdk commands to format your packs, lint, and validate.
The extension provides an easy virtual environment setup for Cortex XSOAR integrations and scripts.

## Extension Workflow

The extension defines a slightly different workflow than Cortex XSOAR. With the plugin, you can work on your code (whether it is Python, PowerShell or JavaScript).
It utilizes the excellent [demisto-sdk](https://github.com/demisto/demisto-sdk) python package.

## Prerequisites

- Mac, Linux or WSL2 (on Windows)
- Python 3.8 and up.
- Docker (Follow the instructions [here](https://code.visualstudio.com/docs/remote/containers#_installation) to install **Docker** to your operating system.)
- [VSCode](https://code.visualstudio.com/Download)

## Install the Visual Studio Code extension

Install the Visual Studio Code extension directly from the Visual Studio Code marketplace or use this [link](https://marketplace.visualstudio.com/items?itemName=CortexXSOARext.xsoar).
If working on a Windows machine, click `ctrl + shift + P` and choose `Connect to WSL`.

## Configurations

Cortex XSOAR recommends configuring **_xsoar.autoFindProblems.readProblems_**.

This configuration will auto-run _demisto-sdk lint_ and _demisto-sdk validate_ when saving your file if the configuration is set to _true_.

The default is _false_, and for now, it is recommended not to enable this configuration for performance.

## Commands

All of the commands in the extension start with the easy-to-find pattern _XSOAR_.  
Notable commands:

- **_XSOAR: Demisto-SDK Pre-Commit/Validate/Update Release Notes..._**: Will run the [demisto-sdk](https://docs-cortex.paloaltonetworks.com/r/1/Demisto-SDK-Guide/Demisto-SDK-commands) commands.

- **_XSOAR: Configure XSOAR unit tests_**: Will configure the integration unit tests.

- **_XSOAR: Configure Demisto-SDK for XSOAR_**: Will configure XSOAR environnement variables for _demisto-sdk_.

## Environment setup

### Remote development (Any OS)

To develop in a fully configured remote development environment, follow the instructions in this [guide](./../tutorials/tut-setup-dev-remote.md).

### Local development (Linux, MacOS, WSL2)

The VScode extension supports setting up your development environment automatically.

#### Usage

Execute the command **_XSOAR: install local development environment_**, either from [VSCode Command Pallete](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette), or by right-clicking a file.

If you want to install the dependencies manually, follow the instructions in this [guide](./dev-setup.md#option-3-manual-setup) until the `Bootstrap` step.

## Setup integrations and scripts environment

Each integration or script in `Cortex XSOAR` runs on a different environment, and has different dependencies.
This feature will configure the integration or script, and will allow you to debug it easily and run unit tests.

In addition, you will be able to open the integration environment in a new workspace with a virtual environment, for autocompletion.

### Usage

- Go to the integration or a script.
- Right-click it, and select **Setup integration/script environment**
- There will be a popup asking you if you want to use the current workspace or open a new one with a virtual environment.
  - Using the current workspace is quicker, but you may will not have autocompletion for some integrations.
  - Opening a new workspace will take longer, but you will have autocompletion for all integrations.
- With both options, you will be able to debug your integration/script easily, run unit tests, and see problems in the IDE.

## Debugging

- First, [Setup integrations and scripts environment](#setup-integrations-and-scripts-environment)
- Then, read the [Debugging using your IDE](../integrations/debugging#Debugging%20using%20your%20IDE) section.
- Go to the Run and Debug (⇧⌘D), and make sure that `Docker: debug (<integration>)` is selected.
- Click on the green arrow or F5 to start debugging.

## Run and Debug tests

- First, [Setup integrations and scripts environment](#setup-integrations-and-scripts-environment)
- Go to the [Run and Debug](https://code.visualstudio.com/docs/editor/debugging#_run-and-debug-view) (⇧⌘D), and make sure that `Docker: debug tests (<integration>)` is selected.
- Click on the green arrow or F5 to start debugging.

## Notes

If during the installation one or more Python packages fail to install, the installation will proceed and create the virtual environment with the packages that were installed.

## Python 2 support

VSCode dropped support for **Python 2**.
In order to debug **Python 2** code, it is necessary to install an older python extension.

- Go to VSCode extensions.
- Select **Python**.
  ![Python](https://github.com/demisto/vscode-extension/raw/master/documentation/changelog/0.2.0/python2_1.png)
- Select **Install Another version**.
- Select the version `2022.2.1924087327`.
  ![Version](https://github.com/demisto/vscode-extension/raw/master/documentation/changelog/0.2.0/python2_2.png)

## Troubleshooting

### **Setup integration/script environment** fails

* Make sure **Docker** is running.
* Make sure that `Allow the default Docker socket to be used (requires password)` is enabled in **Docker** advanced settings.
* If _Docker_ is running try to [clean up Docker](https://docs.docker.com/config/pruning/) or [sign in to Docker](https://www.docker.com/blog/seamless-sign-in-with-docker-desktop-4-4-2/) to avoid the [Docker pull rate limit](https://docs.docker.com/docker-hub/download-rate-limit/#:~:text=Pull%20rates%20limits%20are%20based,to%205000%20pulls%20per%20day.).
