---
id: sdk
title: Contributing to Demisto SDK
slug: sdk
authors: [kgal-pan]
tags: [sdk,python,dev_env,contributing,pr]
---

# Contributing to Demisto SDK

Contributions to [`demisto-sdk`](https://github.com/demisto/demisto-sdk) are welcome and appreciated. 

Some common ways to contribute are:

- Create new commands.
- Improve existing implementation.
- Fix bugs.
- Improve documentation. 

### Prerequesites

Verify you have the following requirements:

* An active GitHub account.
* A [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of the [`demisto-sdk`](https://github.com/demisto/demisto-sdk) repository. 
* The forked repository cloned in your local machine or a codespace.
* Python 3 and [`poetry`](https://python-poetry.org/docs/#installation) installed.
* [Docker](https://docs.docker.com/engine/install/) installed.

## How to Contribute

Before contributing, you must set up a development environment. The development process includes adding or modifying code, adding unit tests and documenting the changes. Upon completion, a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) should be opened to push your changes into the next release of the Demisto SDK. 

### 1. Set Up a Development Environment

Run the following commands from the repository root directory:

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

4. Run the following command to see where the new virtual environment is saved in the filesystem:

```bash
❯ poetry env info

Virtualenv
Python:         3.10.8
Implementation: CPython
Path:           /path/to/pypoetry/virtualenvs/demisto-sdk-zRo7lI35-py3.10
Executable:     /path/to/pypoetry/virtualenvs/demisto-sdk-zRo7lI35-py3.10/bin/python
Valid:          True
```

This output will be useful when selecting the Python interpreter in [Visual Studio Code](https://code.visualstudio.com/docs/python/environments) and [PyCharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter).

You should now have a working development environment. Open your IDE and then open the repository.

### 2. Add Your Proposed Changes

Add new features, fix bugs, etc., commit and push them.

To get you started, here's some useful information about the Demisto SDK project structure, important modules and how to create new commands. 

#### Directory Structure

The package that holds the source code for the commands, utilities and unit tests is `demisto_sdk`.

The main module is located in `demisto_sdk/__main__.py` and it holds the business logic for initializing the SDK and parsing the commands/arguments. So to run the `demisto-sdk -h`, run the following command from within your virtual environment:

```bash
❯ python demisto_sdk/__main__.py -h
```

Each command has its own package under `demisto_sdk/commands`.

#### Example Contribution: Create a New Command

To create a new command, follow the steps below:

1. Create a package for your command in the `demisto_sdk/commands/$NEW_COMMAND` directory.
2. Create the `click` command and arguments in the `__main__.py` module. See [Basic Concepts - Creating a Command](https://click.palletsprojects.com/en/8.1.x/quickstart/#basic-concepts-creating-a-command) for more information.
3. Create a module in `demisto_sdk/commands/$NEW_COMMAND/$NEW_MODULE.py`.
   **Note:** Modules should return `0` on success or `1` on failure. 


#### Tests

There are two types of tests in the SDK:

* **Unit Tests** - These test individual modules/functions and should be placed in the same directory as the code being tested. For example, unit tests for a new command should be in `demisto_sdk/commands/$NEW_COMMAND/tests/$NEW_COMMAND_test.py`.
* **Integration Tests** - These test the command execution end-to-end and are located in `demisto_sdk/tests/integration_tests`. They usually include permutations of arguments, inputs, expected outputs, etc.  For example, to test the `demisto-sdk download` command, which includes different flags such as `--force` and `--list-files`, create integration tests with those variations, `demisto_sdk/tests/integration_tests/download_integrations_test.py::test_integration_download_force`, `demisto_sdk/tests/integration_tests/download_integrations_test.py::test_integration_download_list_files`, respectively.

To run the unit tests from within your virtual environment:

```bash
❯ pytest -v demisto_sdk/commands/$NEW_COMMAND/tests
```

To run a specific unit test or integration test, specify the file and test name separated by `::`. For example, to run only the `test_integration_download_list_files` test:
```bash
❯ pytest -v demisto_sdk/tests/integration_tests/download_integrations_test.py::test_integration_download_list_files
```

You can also run and debug unit tests in the IDE. Follow the instructions to set up `pytest` unit test discovery in [Visual Studio Code](https://code.visualstudio.com/docs/python/testing) and [PyCharm](https://www.jetbrains.com/help/pycharm/pytest.html#create-pytest-test).

### 3. Open Pull Request

After finishing the development process, push the changes to your SDK fork on GitHub and [open a pull request from the forked repo](https://help.github.com/articles/creating-a-pull-request-from-a-fork/) to the [`demisto-sdk`](https://github.com/demisto/demisto-sdk) `master` branch.

After opening the pull request, run the following command to generate a changelog entry:

```bash
poetry run sdk-changelog --init
```

This will create a YML in the `.changelog` directory with the PR number (e.g. `.changelog/123.yml`). Open the file with a text editor and fill out the `changes.description` and `changes.type` fields. 

The possible values for `changes.type` are:

* `breaking`
* `feature`
* `fix`
* `internal`

### 4. Pull Request Review

Once the pull request is open, it is assigned to a member of the Demisto SDK team to review. 

In addition, you will see the following [GitHub Status Checks](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-status-checks) running:

* **CI - On Push** : We use GitHub Actions to run a full build on each commit of your pull request. The build runs our validation hooks, linting and unit tests. We require that the build pass (green build). Follow the *details* link of the check to see the full log.
* **guardrails/scan**: We use [GuardRails](https://www.guardrails.io/) to review the contributed code and find potential security vulnerabilities.
* **license/cla**: Status check that all contributors have signed our Contributor License Agreement. Before merging any PRs, all contributors must sign a Contributor License Agreement. By signing this agreement, you enable the community to use your contributions.

These jobs are run in order to validate that the pull request meets our standards. Review failed jobs and address any issues found before requesting a review from the SDK team. If you have any questions, reach out to the assigned PR reviewer.

Once the pull request is approved and merged, the changes are available in the next [SDK release](https://github.com/demisto/demisto-sdk/releases/).
