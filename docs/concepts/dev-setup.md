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

## Set up environment

### Option 1: Use remote development environment (Any OS)

Follow [this](./../tutorials/tut-setup-dev-remote.md) guide to setup a fully configured remote development environment.

### Option 2: Let VSCode extension setup a local environment (Linux, MacOS, WSL2)

* Follow [this](./vscode-extension.md#local-development-linux-macos-wsl2) guide.

### Option 3: Manual setup

#### Install Python

You will need `python3` installed on your system. We recommend using `pyenv`. At the time of writing, the latest version of Python 3.10 is *3.10.5*.

Make sure `pyenv` in installed and that the `eval "$(pyenv init -)"` expression is placed in your shell configuration (`~/.bashrc` or `~/.zshrc`) - [more information about this](https://github.com/pyenv/pyenv#installation).

After installing `pyenv`, you can install `Python`:
```bash
pyenv install 3.10.5
pyenv global 3.10.5
```

#### Install Poetry

We recommend using [poetry](https://python-poetry.org/) to create an isolated virtual python development environment. To install poetry follow [this](https://python-poetry.org/docs/master/#installing-with-the-official-installer) installation guide.

#### Install Docker

**Demisto-sdk** uses **docker** to run certain commands. Follow [this](https://www.docker.com/get-started/) to install **docker** in your host.

*Note:* if you're using Windows with WSL2, you can still use Docker Desktop from WSL. Follow [this](https://docs.docker.com/desktop/windows/wsl/#enabling-docker-support-in-wsl-2-distros) tutorial for details.

#### Install Node

Follow [this](https://github.com/nvm-sh/nvm#install--update-script) instructions to install `nvm` package manager.
After installing, run:
```bash
nvm install node
```

#### Install pipx

`Pipx` is a package to install and run python application globally in an isolated python environment.

Installation:
  ```bash
  pip install --user pipx
  pipx ensurepath
  ```

#### Install demisto-sdk

This is our help tool that will make your lives easier during the contribution process, it will help you generate a [Pack](../packs/packs-format). And will help you maintain your files and validate them before committing to the branch.

To install **demisto-sdk** using `pipx`
```bash
pipx install demisto-sdk --force
```

To check the you have the latest version of the sdk run:

```bash
demisto-sdk --version
```

#### Bootstrap

Run the [`bootstrap`](https://github.com/demisto/content/blob/master/.hooks/bootstrap) script. The script will setup a pre-commit hook which will validate your modified files before committing and setup a python virtual env for development with the package requirements for [python3](https://github.com/demisto/content/blob/master/pyproject.toml). Run the script from the root directory of the source tree:

```bash
.hooks/bootstrap
```

After completing, you can activate the newly created virtual env by running:

```bash
poetry shell
```

**Congratulations!** You now have a fully configured virtual env, where you can run our different validation and utility scripts.

If you want more details, please refer to the end-to-end [Tutorial](../tutorials/tut-setup-dev).

## IDE

Cortex XSOAR offers two IDEs for developing:

* [Built-in Platform Cortex XSOAR IDE](../concepts/xsoar-ide) (not recommended for complex/advanced use cases. More details [here](getting-started-guide#using-the-right-tools).)
* [Visual Studio Code Extension](vscode-extension)

You can also use your IDE of choice along with `demisto-sdk`, for example Visual Studio Code.
