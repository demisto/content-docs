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


* Python 3.8 and up.
* [VSCode](https://code.visualstudio.com/Download)
* Set up the [content repository](../concepts/dev-setup)


## Install the Visual Studio Code extension

Install the Visual Studio Code extension directly from the Visual Studio Code marketplace or use this [link](https://marketplace.visualstudio.com/items?itemName=CortexXSOARext.xsoar).

## Configurations

Cortex XSOAR recommends configuring ***xsoar.autoFindProblems.readProblems***. 

This configuration will auto-run *demisto-sdk lint* and *demisto-sdk validate* when saving your file if the configuration is set to *true*.

The default is *false*, and for now, it is recommended not to enable this configuration for performance.

## Commands

All of the commands in the extension start with the easy-to-find pattern *XSOAR*.  
Notable commands:

* ***XSOAR: Load Script/Integration***: Opens a side-panel to easily modify the integration configuration, inputs, and outputs.

* ***XSOAR: Demisto-SDK Lint/Validate/Update Release Notes...***: Will run the [demisto-sdk](https://github.com/demisto/demisto-sdk/) commands.

* ***XSOAR: Configure XSOAR unit tests***: Will configure the integration unit tests.

* ***XSOAR: Configure Demisto-SDK for XSOAR***: Will configure XSOAR environnement variables for *demisto-sdk*.

## Environment setup

### Remote development (Any OS)

To develop in a fully configured remote development environment, follow the instructions in this [guide](./../tutorials/tut-setup-dev-remote.md).

### Local development (Linux, MacOS, WSL2)

The VScode extension supports setting up your development environment.
This will:
1. Install the dependencies using **Homebrew** (optionally).
2. Install **demisto-sdk** (optionally).
3. Add `code` to `PATH` to open `VSCode` with running `code <path>` from the terminal. 
4. Bootstrap the **Content** repository with `python` and `node` dependencies.
5. Install the **Content** repository recommended extensions.
6. Configure VSCode `settings.json` to lint with `mypy` and `flake8`.
7. Configure **demisto-sdk** settings for `XSOAR`, selecting the Cortex XSOAR server URL, API key and more. 

The first step requires **Homebrew**:

* Install [Homebrew](https://brew.sh/).
* If on **Linux** or **WSL**, make sure to follow the instructions after installing *Homebrew* or follow the instructions in this [guide](https://docs.brew.sh/Homebrew-on-Linux#requirements).

If you want to install the dependencies manually, follow the instructions in this [guide](./dev-setup.md#option-3-manual-setup) until the `Bootstrap` step.

#### Usage

Execute the command ***XSOAR: install local development environment***, either from [VSCode Command Pallete](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette), or by right-clicking a file.


## Open integrations and scripts in Python virtual environment.

Each integration or script in `XSOAR` runs on a different environnement, and has different dependencies.
With the VSCode extension, you are able to open a workspace of the integration or a script with it's dedicated virtual environment.

### Usage

* Go to the integration or a script.
* Right-click it, and select **Open integration/script in virtual environnement**

### Features

When using it, the following actions are automatically performed:

* Initializes a Python virtual environment based on the integration Docker image with all dependencies and test dependencies installed.
* Copies the dependent files to the directory (`CommonServerPython.py` , `demistomock.py` and ApiModules if necessary).
* Opens a new VSCode workspace that is configured with **pytest** and linting with **mypy** and **flake8** enabled. Run the tests with the `Test Explorer`. See the linting errors in the `Problems` tab.
* Switches to the newly created virtual environment as the selected Python interpreter in this workspace.
* Creates a configured `launch.json` in the workspace, to debug the integration easily with demistomock.
* If the virtual environment already exists, a popup will be triggered to ask you whether to open the existing environment or create a new one.

## Debugging

* First, [Open integrations and scripts in the Python virtual environment](#open-integrations-and-scripts-in-python-virtual-environment)
* Then, read the [Debugging using your IDE](../integrations/debugging#Debugging%20using%20your%20IDE) section.

You can use Run and Debug (⇧⌘D) in VSCode (or click F5 on the Python file).

## Notes

* If during the installation one or more Python packages fail to install, the installation will proceed and create the virtual environment with the packages that were installed.

  It is your responsibility to figure out why the installation failed (probably due to missing non-Python dependencies in your host), and manually install or recreate the virtual environnement afterwards.
  If you face this issue, you might want to try [Open integration/script in Dev Container](#open-integrations-and-scripts-in-dev-container-advanced) option.
* To use [demisto-sdk](./demisto-sdk) in this workspace it has do be installed globally in your system, with `pip install demisto-sdk` in the system interpreter.
* You can use this feature together with the content Dev Container.

## Open integrations and scripts in Dev Container (Advanced)

The `XSOAR` integrations and scripts actually run on a dedicated Docker image.
In some integrations, the Python environment is not enough, and it is not easy to install the system dependencies.

With this feature, you are able to develop inside the integration or a script Docker image, with **all** dependencies preinstalled.
This will use the Docker image that is in the `YAML` file.

### System requirements

**Windows**: Docker Desktop 2.0+ on Windows 10 Pro/Enterprise. Windows 10 Home (2004+) requires Docker Desktop 2.3+ and the WSL 2 back-end.
**macOS**: Docker Desktop 2.0+.
**Linux**: Docker CE/EE 18.06+ and Docker Compose 1.21+.

### Installation

Follow the [VSCode documentation](https://code.visualstudio.com/docs/remote/containers#_installation).

### Usage

* Go to the integration or a script.
* Right-click it and select **Open integration/script in a Dev Container**

### Features

The same features of the [virtual environment](#open-integrations-and-scripts-in-python-virtual-environment) feature is available here. 

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

- If **Open integration/script in a Dev Container** or **Open integration/script in a virtual environment** fails, make sure the **Docker** is running. In addition, you can try to [clean up the Docker](https://docs.docker.com/config/pruning/) or [sign in to docker](https://www.docker.com/blog/seamless-sign-in-with-docker-desktop-4-4-2/) to avoid the [docker pull rate limit](https://docs.docker.com/docker-hub/download-rate-limit/#:~:text=Pull%20rates%20limits%20are%20based,to%205000%20pulls%20per%20day.).
- If **demisto-sdk** is not recognized from the extension using **MacOS** and **zsh** terminal, try adding the following to [VSCode settings.json](https://code.visualstudio.com/docs/getstarted/settings#_settingsjson):
  ```json
    "terminal.integrated.profiles.osx": {
        "zsh": {
            "path": "/bin/zsh -l",
            "args": ["-i"]
        }
    }

