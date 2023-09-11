---
id: sdk
title: Contributing to XSOAR SDK
slug: sdk
---

# Contributing to XSOAR SDK

Contributions to [`demisto-sdk`](https://github.com/demisto/demisto-sdk) are welcome and appreciated.

### Prerequesites

Make sure you already have the following requirements:

* An active GitHub account.
* A [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of the [`demisto-sdk`](https://github.com/demisto/demisto-sdk) repository. 
* The forked repository cloned in your local machine or a codespace.
* Have Python 3 and [`poetry`](https://python-poetry.org/docs/#installation) installed.
* [Docker](https://docs.docker.com/engine/install/) installed.

## How to Contribute

### Set Up Development Environment

Run the following command from the repository root directory:

1. Create a new branch to hold contributed work:

```bash
❯ git checkout -b $BRANCH_NAME
```

1. Install all required dependencies:

```bash
❯ poetry install
```

1. Activate the virtual environment:

```bash
❯ poetry shell 
```

Run the following command to see where the new virtual environment is saved in the filesystem:

```bash
❯ poetry env info

Virtualenv
Python:         3.10.8
Implementation: CPython
Path:           /path/to/pypoetry/virtualenvs/demisto-sdk-zRo7lI35-py3.10
Executable:     /path/to/pypoetry/virtualenvs/demisto-sdk-zRo7lI35-py3.10/bin/python
Valid:          True
```

This output will be helpful when selecting the Python interpreter in [Visual Studio Code](https://code.visualstudio.com/docs/python/environments) and [PyCharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter).

You should now have a working development environment. Feel free to jump into your favorite IDE and open the repository.

### Directory Structure

The package that holds the source code for the commands, utilities and unit tests is `demisto_sdk`.

The main module is located in `demisto_sdk/__main__.py` and it holds the business logic for initializing the SDK and parsing the commands/arguments. So to run the `demisto-sdk -h`, you could run the following command from within virtual environment:

```bash
❯ python demisto_sdk/__main__.py -h
```

Each command has it's own package under `demisto_sdk/commands`.

### Create a New Command

1. Create package for your command in the following path: `demisto_sdk/commands/$NEW_COMMAND`.
1. Create the `click` command and arguments in the main module.
1. Create a module in `demisto_sdk/commands/$NEW_COMMAND/$NEW_MODULE.py`
**Note:** Modules are supposed to return `0` on success or `1` on failure. 
1. Create unit tests. Unit tests should be saved in `demisto_sdk/commands/$NEW_COMMAND/tests`. Test files for all commands which located are located in 
`demisto_sdk/tests/test_files`.
   
   To run the unit tests from within your virtual environment:

   ```bash
   ❯ pytest -v demisto_sdk/commands/$NEW_COMMAND/tests
   ```


### # TODO Open a Pull Request


### Further Reading

The SDK uses the [`click`](https://click.palletsprojects.com/en/8.1.x/) and [`typer`](https://typer.tiangolo.com/) libraries to expose the commands, arguments and create the command line interface. The `click`/`typer` implementations are found in the `demisto_sdk/__main__.py` module.

# TODO
- neo4j
