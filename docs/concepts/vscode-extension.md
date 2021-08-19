---
id: vscode-extension
title: Visual Studio Code Extension
sidebar_label: VSCode Extension
---
The Cortex XSOAR extension for the Visual Studio Code enables you to design and author scripts and integrations for Cortex XSOAR directly from VSCode. The extension adds a set of commands, as a sidebar with Automation and Integration Settings, just like the Settings sidebar in the Cortex XSOAR script editor. When writing code, the plugin provides you with auto-complete of Cortex XSOAR and Python functions.
The extension also provides an easy-to-use set of demisto-sdk commands to format your packs, lint and validate.

## Extension Workflow

The extension defines a slightly different workflow than Cortex XSOAR. With the plugin, you can work on your code (whether it is Python, Powershell or Javascript).
It is uses the excellent [demisto-sdk](./demisto-sdk) python package.

## Prerequisites

* Python 3.7 and up.
* [Python for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* Install [demisto-sdk](../concepts/demisto-sdk#installation-and-setup). It is highly recommended to install it on a virtual environment like [pipenv](https://pipenv.pypa.io/en/latest/).

## Install the Visual Studio Code extension

Install it directly from the Visual Studio Code marketplace or use this [link](https://marketplace.visualstudio.com/items?itemName=CortexXSOARext.xsoar).

## Configurations

Those configurations are recommended to set:

### `xsoar.demisto-sdk.pythonPath`

A path to the python interpeter where `demisto-sdk` is installed. If not set, will use default `python.pythonPath` which redirect to `python` by default.

### `xsoar.autoFindProblems.readProblems`

Will auto-run `demisto-sdk lint` and `demisto-sdk validate` on save of file where this configuration is set to `true`.
It is recommended to change this configuration to `false` and enable it only to your [content](https://github.com/demisto/demisto-sdk/) repository.

## Commands

All of the commands in the extension are starts the easy-to-find pattern `XSOAR`.  
Noteable commands:

* `XSOAR: Load Script/Integration`: Will open a side-panel to easily modify the integration configuration, inputs and outputs.

* `XSOAR: Demisto-SDK Lint/Validate/Update Release Notes...`: Will run the [demisto-sdk](https://github.com/demisto/demisto-sdk/) commands.

## Debugging

Read the [Debugging using your IDE](../integrations/debugging#Debugging%20using%20your%20IDE) section.

## launch.json configuration

the launch (`.vscode/launch.json`) configuration for running an integration should be look like that:

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

You can now use the Run and Debug (⇧⌘D) in VSCode (or click F5 on the python file).

## Non-regular debugging

Sometimes we are developing an integration that rely on differrent installed packages than the base packages. it is recommended to create a separate environment for that.

also, you will need the `CommonServerPython.py`, `CommonServerUserPython.py`, `demistomock.py` files alongside your integration.

### Example

let's say were developing a integration in `Packs/Pasta/Integrations/Pasta` and our integration requires the `pasta` package.
We would create a pipenv in that root:

### Create Pipenv

```bash
cd "${CONTENTDIR}/Packs/Pasta/Integrations/Pasta"
pipenv install -r "${CONTENTDIR}/dev-requirements-py3.txt pasta"
#                   ^^                                     ^^
#             requirements location              new package to install
```

The command will create a new environment along with `Pipfile` and `Pipfile.lock`.

> If you need to deactivate your current pipenv, run `exit`.

Activate that pipenv in your VSCode (Command Pallete (⇧⌘P) -> Python: Select Interpeter).

### Link or Copy Required Files

You need 3 files in our directory:

* [CommonServerPython.py](https://github.com/demisto/content/tree/master/Packs/Base/Scripts/CommonServerPython)  
Can be found in `Packs/Base/Scripts/CommonServerPython`.
* CommonServerUserPython.py  
Create empty file with that name.
* [demistomock.py](https://github.com/demisto/content/tree/master/Tests/demistomock)  
Can be found in `Tests/demistomock`.

The files will auto-copied to your integration folder when running `XSOAR: Demisto-SDK Lint`. You can run it with right clicking on the file of from the command pallete.

Alternatily, you can link those files to keep them updated:

```bash title="In your integration directory"
ln CommonServerPython.py "${CONTENTDIR}/Packs/Base/Scripts/CommonServerPython.py"
ln demistomock.py "${CONTENTDIR}/Tests/demistomock/demistomock.py"
ln CommonServerUserPython.py "${CONTENTDIR}/CommonServerUserPython.py"
# ^^ Don't forget to create this file first^^
```

### Launch Configuration

We need need to modify the launch configuration to use our local Pasta's `CommonServerPython` and `demistomock`.

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
    ]
}
```

Now you can run your custom integration with your pipenv!
