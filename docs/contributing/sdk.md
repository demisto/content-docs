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


