---
id: dev-setup
title: Development Setup
---

:::info Important Note
This article is focused on setting up a development environment to create and contribute supported new content. If you are not planning to contribute or your contribution will be only community supported, the content in this article is not required. For more details, refer to the [Getting Started Guide](../concepts/getting-started-guide#using-the-right-tools).
:::

**For details, the [Setup Tutorial](../tutorials/tut-setup-dev) summarizes the end-to-end steps that are required.**

Before you read the following information, make sure you read the [Getting Started Guide](../concepts/getting-started-guide) and the [Contribution Requirements](../contributing/contrib-requirements) documentation.

## Setting Up a Development Repository

[Fork](https://guides.github.com/activities/forking/) the Cortex XSOAR Content repository and create a branch for your contribution. Do not work on the `master` or `main` branch.

## Set up environment

### Option 1: Use remote development environment (Any operating system)

Follow [this](./../tutorials/tut-setup-dev-remote.md) guide to set up a fully configured remote development environment.

### Option 2: Let VSCode extension set up a local environment (Linux, MacOS, WSL2)

Follow [this](./vscode-extension.md#local-development-linux-macos-wsl2) guide to set up a fully configured local environment.

### Option 3: Manual setup

#### Install Python

You will need `python3` installed on your system. We recommend using `pyenv`. At the time of this writing, the latest version of Python 3.10 is *3.10.5*.

Make sure `pyenv` is installed first and that the `eval "$(pyenv init -)"` expression is placed in your shell configuration (`~/.bashrc` or `~/.zshrc`). For additional information see [this guide](https://github.com/pyenv/pyenv#installation).

After installing `pyenv`, you can install `Python`:
```bash
pyenv install 3.10.5
pyenv global 3.10.5
```

#### Install Poetry

We recommend using [poetry](https://python-poetry.org/) to create an isolated virtual python development environment. To install poetry, follow the instructions in this [installation guide](https://python-poetry.org/docs/master/#installing-with-the-official-installer) .

#### Install Docker

**Demisto-sdk** uses **Docker** to run certain commands. Follow the instructions in the [Docker Getting Started](https://www.docker.com/get-started/) guide to install **Docker** in your host.

*Note:* If you are using Windows with WSL2, you can still use Docker Desktop from WSL. Follow the instructions in this [tutorial](https://docs.docker.com/desktop/windows/wsl/#enabling-docker-support-in-wsl-2-distros)  for details.

#### Install Node

To install the `nvm` package manager, follow the instructions in [this](https://github.com/nvm-sh/nvm#install--update-script) nvm guide.

After installing, run:
```bash
nvm install node
```

#### Install pipx

`Pipx` is a package that enables you to install and run the Python application globally in an isolated Python environment.

Installation:
  ```bash
  pip install --user pipx
  pipx ensurepath
  ```

#### Install demisto-sdk

This is our help tool that will ease the contribution process. It will help you to generate a [Pack](../packs/packs-format), maintain your files, and validate them before committing to the branch.

To install **demisto-sdk** using `pipx`
```bash
pipx install demisto-sdk --force
```

To check the you have the latest version of the SDK, run:

```bash
demisto-sdk --version
```

#### Bootstrap

Run the [`bootstrap`](https://github.com/demisto/content/blob/master/.hooks/bootstrap) script. The script will set up a pre-commit hook that will validate your modified files before committing. It will also set up a python virtual environment for development with the package requirements for [Python3](https://github.com/demisto/content/blob/master/pyproject.toml). Run the script from the root directory of the source tree:

```bash
.hooks/bootstrap
```

After the script completes, you can activate the newly created virtual environment by running:

```bash
poetry shell
```

**Congratulations!** You now have a fully configured virtual environment, where you can run our different validation and utility scripts.

For more details, refer to the end-to-end [Tutorial](../tutorials/tut-setup-dev).

## IDE

Cortex XSOAR offers two IDEs for developing:

* [Built-in Platform Cortex XSOAR IDE](../concepts/xsoar-ide) (not recommended for complex/advanced use cases. More details [here](getting-started-guide#using-the-right-tools).)
* [Visual Studio Code Extension](vscode-extension)

You can also use your IDE of choice along with `demisto-sdk`, for example, Visual Studio Code.
