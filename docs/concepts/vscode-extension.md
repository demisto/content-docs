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
It utilizes the excellent [demisto-sdk](./demisto-sdk) python package.

## Prerequisites

- Python 3.8 and up.
- [VSCode](https://code.visualstudio.com/Download)
- Set up the [content repository](../concepts/dev-setup)

## Install the Visual Studio Code extension

Install the Visual Studio Code extension directly from the Visual Studio Code marketplace or use this [link](https://marketplace.visualstudio.com/items?itemName=CortexXSOARext.xsoar).

## Configurations

Cortex XSOAR recommends configuring **_xsoar.autoFindProblems.readProblems_**.

This configuration will auto-run _demisto-sdk lint_ and _demisto-sdk validate_ when saving your file if the configuration is set to _true_.

The default is _false_, and for now, it is recommended not to enable this configuration for performance.

## Commands

All of the commands in the extension start with the easy-to-find pattern _XSOAR_.  
Notable commands:

- **_XSOAR: Load Script/Integration_**: Opens a side-panel to easily modify the integration configuration, inputs, and outputs.

* ***XSOAR: Demisto-SDK Lint/Validate/Update Release Notes...***: Will run the [demisto-sdk](https://github.com/demisto/demisto-sdk/) commands.

## Debugging

Read the [Debugging using your IDE](../integrations/debugging#Debugging%20using%20your%20IDE) section.

### launch.json configuration

The launch (*.vscode/launch.json*) configuration for running an integration should be as follows:

```json title=".vscode/launch.json"
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",  // File example: Packs/Pasta/Integrations/Pasta/Pasta.py
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}" // workspaceFolder is the content repository
        }
    ]
}
```

You can use Run and Debug (⇧⌘D) in VSCode (or click F5 on the python file).

## Advanced debugging

If you are developing an integration that relies on packages other than the base packages, Cortex XSOAR recommends that you create a separate environment for that.

In addition, you will need the *CommonServerPython.py*, *CommonServerUserPython.py*, *demistomock.py* files alongside your integration.

### Example

Let's say you are developing an integration in *Packs/Pasta/Integrations/Pasta* and your integration requires the *pasta* package.
You would need to create a pipenv in that root:

```bash
cd "${CONTENTDIR}/Packs/Pasta/Integrations/Pasta"
pipenv install -r "${CONTENTDIR}/dev-requirements-py3.txt pasta"
#                   ^^                                     ^^
#             requirements location              new package to install
```

The command will create a new environment along with *Pipfile* and *Pipfile.lock*.

> If you need to deactivate your current pipenv, run ***exit***.

Activate that pipenv in your VSCode (Command Pallete (⇧⌘P) -> Python: Select Interpreter).

### Link or Copy Required Files

You need the following three files in your directory:

* [CommonServerPython.py](https://github.com/demisto/content/tree/master/Packs/Base/Scripts/CommonServerPython)  
Can be found in *Packs/Base/Scripts/CommonServerPython*.
* Create an empty file with the name [CommonServerUserPython.py](https://xsoar.pan.dev/docs/reference/scripts/common-server-user-python).
* [demistomock.py](https://github.com/demisto/content/tree/master/Tests/demistomock)  
Can be found in *Tests/demistomock*.

The files will be auto-copied to your integration folder when running ***XSOAR: Demisto-SDK Lint***. You can run the command by right-clicking on the file from the command pallet.

## Troubleshooting

### **Open integration/script in a Dev Container** or **Open integration/script in a virtual environment** fails

### Launch Configuration

- ### **demisto-sdk** is not available when using **MacOS** and **zsh** terminal

```json title=".vscode/launch.json"
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Run Custom Integration",
            "type": "python",
            "request": "launch",
            "program": "${file}",  // File example: Packs/Pasta/Integrations/Pasta/Pasta.py
            "console": "integratedTerminal",
            "cwd": "${fileDirname}" // The directory name of the Pasta integration (Packs/Pasta/Integrations/Pasta/).
        }
    }
  ```
