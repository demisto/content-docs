---
id: sdk
title: Contributing to XSOAR SDK
slug: sdk
authors: [kgal-pan]
tags: [sdk,python,dev_env,contributing,pr]
---

# Contributing to XSOAR SDK

Contributions to [`demisto-sdk`](https://github.com/demisto/demisto-sdk) are welcome and appreciated. 

Some common ways to contribute are:

- Create new commands.
- Improve existing implementation.
- Fix bugs.
- Improve documentation. 

### Prerequesites

Make sure you already have the following requirements:

* An active GitHub account.
* A [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of the [`demisto-sdk`](https://github.com/demisto/demisto-sdk) repository. 
* The forked repository cloned in your local machine or a codespace.
* Have Python 3 and [`poetry`](https://python-poetry.org/docs/#installation) installed.
* [Docker](https://docs.docker.com/engine/install/) installed.

## How to Contribute

Before contributing, it is required set up a development environment. Once that is ready, the development process can begin. The development process includes adding or modifying code, adding unit tests and documenting the changes. Upon completion, a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) should be opened to push those changes into the next release of the SDK. 

### 1. Set Up Development Environment

Run the following command from the repository root directory:

1. Install all required dependencies:

```bash
❯ poetry install
```

2. Create a new branch to hold contributed work:

```bash
❯ git checkout -b $BRANCH_NAME
```

3. Activate the virtual environment:

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

### 2. Add Work

This is the step where you add new features, fix bugs, etc., commit and push them.

To get you started, here's some useful information about the SDK project structure, important modules and how to create new commands. 
#### Directory Structure

The package that holds the source code for the commands, utilities and unit tests is `demisto_sdk`.

The main module is located in `demisto_sdk/__main__.py` and it holds the business logic for initializing the SDK and parsing the commands/arguments. So to run the `demisto-sdk -h`, you could run the following command from within virtual environment:

```bash
❯ python demisto_sdk/__main__.py -h
```

Each command has it's own package under `demisto_sdk/commands`.

#### Example Contribution: Create a New Command

To create a new command, follow the steps below:

1. Create package for your command in the `demisto_sdk/commands/$NEW_COMMAND` directory.
2. Create the `click` command and arguments in the `__main__.py` module. See [Basic Concepts - Creating a Command](https://click.palletsprojects.com/en/8.1.x/quickstart/#basic-concepts-creating-a-command) for more information.
3. Create a module in `demisto_sdk/commands/$NEW_COMMAND/$NEW_MODULE.py`.
   **Note:** Modules are supposed to return `0` on success or `1` on failure. 


#### Tests

We have two types of tests in the SDK:

* **Unit Tests** - These test individual modules/functions and should be placed in the same directory as the code being tested. For example, unit tests for a new command would live in `demisto_sdk/commands/$NEW_COMMAND/tests/$NEW_COMMAND_test.py`.
* **Integration Tests** - These test the command execution end-to-end and are located in `demisto_sdk/tests/integration_tests`. They will usually include permutations of arguments, inputs, expected outputs etc.  For example, to test the `demisto-sdk download` command, which includes different flags such as `--force` and `--list-files`, we would create integration tests with those variations, `demisto_sdk/tests/integration_tests/download_integrations_test.py::test_integration_download_force`, `demisto_sdk/tests/integration_tests/download_integrations_test.py::test_integration_download_list_files`, respectively.

   
   To run the unit tests from within your virtual environment:

   ```bash
   ❯ pytest -v demisto_sdk/commands/$NEW_COMMAND/tests
   ```

   You can also run and debug unit tests in the IDE. Follow the instructions on how to set up `pytest` unit test discovery in [Visual Studio Code](https://code.visualstudio.com/docs/python/testing) and [PyCharm](https://www.jetbrains.com/help/pycharm/pytest.html#create-pytest-test).


### 3. Add Release Notes

Open `CHANGELOG.md`. Under the **Unreleased** section, add a new bullet with the description of the work done.

### 4. Open Pull Request

After finishing the development process, push the changes to your SDK fork on GitHub and [open a Pull Request from the forked repo](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) to the [`demisto-sdk`](https://github.com/demisto/demisto-sdk) `master` branch.

Once the Pull Request is open, it will be assigned to a member of the XSOAR SDK team to review. 

In addition, you will see the following [GitHub Status Checks](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-status-checks) running:

* `ci/circleci` : We use [CircleCI](https://circleci.com/gh/demisto/demisto-sdk) to run a full build on each commit of your pull request. The build will run our content validation hooks, linting and unit test. We require that the build pass (green build). Follow the `details` link of the status to see the full build UI of CircleCI.
* **guardrails/scan**: We use [GuardRails](https://www.guardrails.io/) to review the contributed code and find potential security vulnerabilities.
* **license/cla**: Status check that all contributors have signed our Contributor License Agreement. Before merging any PRs, we need all contributors to sign a Contributor License Agreement. By signing a this agreement, we ensure that the community is free to use your contributions.

These jobs are run in order validate that the Pull Request meets our standards. Make sure to review failed jobs and address any issues found before requesting a review from the SDK team. If you have any other questions, feel free to reach out to the assigned PR reviewer!

Once the Pull Request is approved and merged, the changes will be available in the next [SDK release](https://github.com/demisto/demisto-sdk/releases/).
