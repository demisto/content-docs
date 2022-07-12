---
id: vscode-extension
title: Visual Studio Code Extension
sidebar_label: VSCode Extension
---
The Cortex XSOAR extension for Visual Studio Code enables you to design and author scripts and integrations for Cortex XSOAR directly from VSCode. The extension adds a set of commands, as a sidebar with Automation and Integration Settings, just like the Settings sidebar in the Cortex XSOAR script editor. When writing code, the plugin provides you with auto-completion of Cortex XSOAR and Python functions.
The extension also provides an easy-to-use set of demisto-sdk commands to format your packs, lint, and validate.

## Extension Workflow

The extension defines a slightly different workflow than Cortex XSOAR. With the plugin, you can work on your code (whether it is Python, PowerShell or JavaScript).
It utilizes the excellent [demisto-sdk](./demisto-sdk) python package.

## Prerequisites

* Python 3.8 and up.
* [Python for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
* Setup the [content repository](../concepts/dev-setup)
* Install [demisto-sdk](../concepts/demisto-sdk#installation-and-setup). Don't forget to [setup the required environment variables](../concepts/demisto-sdk#environment-variable-setup). 

## Install the Visual Studio Code extension

Install the Visual Studio Code extension directly from the Visual Studio Code marketplace or use this [link](https://marketplace.visualstudio.com/items?itemName=CortexXSOARext.xsoar).

## Configurations

Cortex XSOAR recommends configuring the following:

### xsoar.autoFindProblems.readProblems

Will auto-run *demisto-sdk lint* and *demisto-sdk validate* when saving your file if this configuration is set to *true*.
It is recommended to change this configuration to *false* for performance.

## Commands

All of the commands in the extension start the easy-to-find pattern *XSOAR*.  
Notable commands:

* ***XSOAR: Load Script/Integration***: Opens a side-panel to easily modify the integration configuration, inputs, and outputs.

* ***XSOAR: Demisto-SDK Lint/Validate/Update Release Notes...***: Will run the [demisto-sdk](https://github.com/demisto/demisto-sdk/) commands.

* ***XSOAR: Configure XSOAR unit tests***: Will configure the integration unit tests. 

## Open integrations and scripts in python virtual environment.

Each integration or a script in `XSOAR` runs on a different environnement, and has different dependencies.
With the VSCode extension, you are able to open a workspace of the integration or a script with it's dedicated virtual environment.

### Usage

* Go to the integration or a script.
* Right click on it, and select ***Open integration/script in virtual environnement***

### Features

When using it, those actions will be performed automatically:

* Initializes a python virtual environment based on the integration docker image with all dependencies and test dependencies installed.
* Copies the dependent files to the directory (`CommonServerPython.py` , `demistomock.py` and ApiModules if necessary).
* Opens a new VSCode workspace which is configured with **pytest** and linting with **mypy** and **flake8** enabled. Run the tests with the `Test Explorer`, See the linting errors in the `Problems` tab.
* Switches to the new created virtual environment as the selected python interpeter in this workspace.
* Creates a configured `launch.json` in the workspace, to debug the integration easily with demistomock.
* If the virtual environment already exists, a popup will be triggered to ask you if open the existing env or create a new one.

## Debugging

Read the [Debugging using your IDE](../integrations/debugging#Debugging%20using%20your%20IDE) section.
[Open integrations and scripts in python virtual environment](#open-integrations-and-scripts-in-python-virtual-environment)

You can use Run and Debug (⇧⌘D) in VSCode (or click F5 on the python file).

## Notes

* If during the installation one or more python packages fail to install, it will proceed and create the virtual environment with the packages that were installed.
  It is your responsibility to figure out why it’s failed (probably due to missing non python dependencies in your host), and install manually or recreate the virtual environnement afterwards.
  If you face this issue, you might want to try [Open integration/script in Dev Container](#open-integrations-and-scripts-in-dev-container-advanced) option.
* To use [demisto-sdk](./demisto-sdk) in this workspace it has do be installed globally in your system, with `pip install demisto-sdk` in the system interpreter.
* You can use this feature together with the content Dev Container.

## Open integrations and scripts in Dev Container (Advanced)

The `XSOAR` integrations and scripts actually runs on a dedicated docker image.
In some integrations, the python environment is not enough, and it's not easy to install the system dependencies.

With this feature, you are able to develop inside the integration or a script docker image, with **all** dependencies preinstalled.
This will use the docker image which is in the `YAML` file.

### System requirements

**Windows**: Docker Desktop 2.0+ on Windows 10 Pro/Enterprise. Windows 10 Home (2004+) requires Docker Desktop 2.3+ and the WSL 2 back-end.
**macOS**: Docker Desktop 2.0+.
**Linux**: Docker CE/EE 18.06+ and Docker Compose 1.21+.

### Installation

Follow the [VSCode documentation](https://code.visualstudio.com/docs/remote/containers#_installation).

### Usage

* Go to the integration or a script.
* Right click on it, and select ***Open integration/script in a Dev Container***

### Features

The same features of [virtual env](#open-integrations-and-scripts-in-python-virtual-environment) feature is available here. 