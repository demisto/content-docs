---
id: vscode-extension
title: Visual Studio Code Extension
sidebar_label: VSCode Extension
---
The Cortex XSOAR extension for Visual Studio Code enables you to design and author scripts and integrations for Cortex XSOAR directly from VSCode. The extension adds a set of commands, as a sidebar with Automation and Integration Settings, just like the Settings sidebar in the Cortex XSOAR script editor. When writing code, the plugin provides you with auto-completion of Cortex XSOAR and Python functions.
The extension also provides an easy-to-use set of demisto-sdk commands to format your packs, lint, and validate.
In addition, the extension allows to setup a Dev Container environnement of content environnement with `demisto-sdk` and to setup a Dev Container environnement of an integration or script.  

## Extension Workflow

The extension defines a slightly different workflow than Cortex XSOAR. With the plugin, you can work on your code (whether it is Python, PowerShell or JavaScript).
It utilizes the excellent [demisto-sdk](./demisto-sdk) python package.

## Prerequisites

* Python 3.8 and up.
* [Python for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
* [docker](https://www.docker.com/get-started/)
* [Remote-Containers for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
* [setup the required environment variables](../concepts/demisto-sdk#environment-variable-setup).
* Setup the [content repository](../concepts/dev-setup)
* (Optional) Install [demisto-sdk](../concepts/demisto-sdk#installation-and-setup).


## Install the Visual Studio Code extension

Install the Visual Studio Code extension directly from the Visual Studio Code marketplace or use this [link](https://marketplace.visualstudio.com/items?itemName=CortexXSOARext.xsoar).

## Setup content environment with VSCode extension

Right click inside the repo and choose `Open content environment in Dev Container`.
This will create a fully configured development container with `demisto-sdk`, `git` and configured environment variables.

More features:
- [zsh](https://ohmyz.sh/): As default terminal with recommended theme and plugins
- [pyenv](https://github.com/pyenv/pyenv): Easily switch between `python` versions.
- [poetry](https://python-poetry.org/docs/configuration/): Easily configure virtualenvs.

To check the you have the latest version of the sdk run in the terminal inside the VSCode:

```bash
demisto-sdk --version
```
## Commands

All of the commands in the extension start the easy-to-find pattern *XSOAR*.  
Notable commands:

* ***XSOAR: Load Script/Integration***: Opens a side-panel to easily modify the integration configuration, inputs, and outputs.

* ***XSOAR: Demisto-SDK Lint/Validate/Update Release Notes...***: Will run the [demisto-sdk](https://github.com/demisto/demisto-sdk/) commands. If `demisto-sdk` is not installed in your environnement, it is required to run `Open content environment in Dev Container`. This command is available through a right click on the `python` files.

## Development and Debugging

Use Integration/Script Dev Container.
1. **Setup Demisto-SDK**: If `demisto-sdk` is not installed - [setup content environment with Dev Container](vscode-extension.md#setup-content-environment-with-vscode-extension)
2. **Go to Integration/Script**: Browse to the integration or script to develop (or initialize new one using [demisto-sdk init](demisto-sdk.md#init))
3. **Open a Dev Container**: Right click on the VSCode sidebar or on the python file, and select `Open integration/script in Dev Container`

Now, you are ready to start developing.

### Problems

(image to problems)
Here you will see the problems with your file gathered by `pylance`, `flake8`, `mypy`.
Note that `flake8` and `mypy` errors will fail the XSOAR build.

### Testing
(image to unit tests)
You can add [unit-tests](../integrations/unit-testing.md) to test your code.
To run the tests, go to the tests sidebar or to the test file and select the tests to run.

## Debugging

Read the [Debugging using your IDE](../integrations/debugging#Debugging%20using%20your%20IDE) section.

After setting up the `demistomock` file. Enter the main `python` file, go to `Run and Debug`, and hit on the `Play` button.
See [VSCode debugging documentation](https://code.visualstudio.com/docs/editor/debugging).
(image to debug)