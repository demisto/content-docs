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

### Install Python virtualenv

We recommend using [virtualenv](https://github.com/pypa/virtualenv) to create an isolated virtual python development environment. To install virtual env run:

```bash
pip install virtualenv
```

**Note:** Python 3 includes the `venv` module for creating virtual envs, but it does not permit creating virtual envs with other versions of Python (such as Python 2). If you need to work on older content built with Python 2, you should use the `virtualenv` package.

### Bootstrap

Once `virtualenv` is installed you can run the [`bootstrap`](https://github.com/demisto/content/blob/master/.hooks/bootstrap) script. The script will setup a pre-commit hook which will validate your modified files before committing and setup a python virtual env for development with the package requirements for [python3](https://github.com/demisto/content/blob/master/dev-requirements-py3.txt). Run the script from the root directory of the source tree:

```bash
.hooks/bootstrap
```

After completing, you can activate the newly created virtual env by running:

```bash
. ./venv/bin/activate
```

:::note
To ease setup, by default for **forked** repositories we don't setup **Python 2** as part of the virtual env setup. If you require **Python 2** for your automations/integrations (i.e. only if you need to modify existing content written in python2), run the .hooks/bootstrap script with the environment variable set: SETUP_PY2=yes. When run with SETUP_PY2=yes set, the virtualenv built contains both Python 2 and 3. python and python2 will point to Python 2, while python3 to Python 3.
:::

### demisto-sdk

This is our help tool that will make your lives easier during the contribution process, it will help you generate a [Pack](../packs/packs-format). And will help you maintain your files and validate them before committing to the branch. It is installed via our `Boostrap` process. If you prefer to install the `demisto-sdk` manually see instructions [here](https://github.com/demisto/demisto-sdk).

To check the you have the latest version of the sdk run:

```bash
demisto-sdk --version
```

**Congratulations!** You now have a fully configured virtual env, where you can run our different validation and utility scripts.

If you want more details, please refer to the end-to-end [Tutorial](../tutorials/tut-setup-dev).

## IDE

Cortex XSOAR offers two IDEs for developing:

* [Built-in Platform Cortex XSOAR IDE](../concepts/xsoar-ide) (not recommended for complex/advanced use cases. More details [here](getting-started-guide#using-the-right-tools).)
* [Visual Studio Code Extension](vscode-extension)

You can also use your IDE of choice along with `demisto-sdk`, for example Visual Studio Code.
