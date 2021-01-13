---
id: dev-setup
title: Development Setup
---

:::note
This article is brief: please refer to the end-to-end [Tutorial](../tutorials/tut-setup-dev) for more details.
:::

Before you read this make sure you read the [Getting Started Guide](getting-started-guide) and the [Development Requirements](dev-requirements) doc.

## Setting Up a Development Repository

[Fork](https://guides.github.com/activities/forking/) the Cortex XSOAR Content repository and create a branch for your contribution (do not use the `master` or `main` branch).

### Install Python virtualenv

We recommend using [virtualenv](https://github.com/pypa/virtualenv) to create an isolated virtual python development environment. To install virtual env run:
```
pip install virtualenv
```
**Note:** Python 3 includes the `venv` module for creating virtual envs, but it does not permit creating virtual envs with other versions of Python (such as Python 2). If you need to work on older content built with Python 2, you should use the `virtualenv` package.

### Bootstrap

Once `virtualenv` is installed you can run the [`bootstrap`](https://github.com/demisto/content/blob/master/.hooks/bootstrap) script. The script will setup a pre-commit hook which will validate your modified files before committing and setup a python virtual env for development with the package requirements for [python3](https://github.com/demisto/content/blob/master/dev-requirements-py3.txt). Run the script from the root directory of the source tree:
```
.hooks/bootstrap
```
After completing, you can activate the newly created virtual env by running:
```
. ./venv/bin/activate
```

:::note
To ease setup, by default for **forked** repositories we don't setup **Python 2** as part of the virtual env setup. If you require **Python 2** for your automations/integrations (i.e. if you need to modify existing content built with python2) run the `.hooks/bootstrap` script with the environment variable set: `SETUP_PY2=yes`. When run with `SETUP_PY2=yes` set, the virtualenv built contains both Python 2 and 3. `python` and `python2` will point to Python 2 and `python3` to Python 3.
:::

### demisto-sdk 
This is our help tool that will make your lives easier during the contribution process, it will help you generate a 
[Pack](packs-format). And will help you maintain your files and validate them before committing to the branch. It is installed via our `Boostrap` process. If you prefer to install the `demisto-sdk` manually see instructions [here](https://github.com/demisto/demisto-sdk).

To check the you have the latest version of the sdk run:
```
demisto-sdk --version
```

**Congratulations!** You now have a fully configured virtual env, where you can run our different validation and utility scripts. 

If you want more details, please refer to the end-to-end [Tutorial](../tutorials/tut-setup-dev).

## IDE

Cortex XSOAR offers two IDEs for developing: 
* [Built-in Platform Cortex XSOAR IDE](../concepts/xsoar-ide) (not recommended for most use cases. Do not use it if you are planning to [contribute](getting-started-guide#are-you-planning-to-contribute).)
* [PyCharm IDE Plugin](../concepts/pycharm-plugin)

You can also use your IDE of choice along with `demisto-sdk`, for example Visual Studio Code.
