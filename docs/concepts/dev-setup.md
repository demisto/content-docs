---
id: dev-setup
title: Development Setup
---

*Note*: this article is brief, please refer to the end-to-end [Tutorial](../tutorials/tut-setup-dev) for more details.

## Which tools should I use?

As mentioned, you'll need a combination of both the Cortex XSOAR UI and other tools. 

As a general rule of the thumb, we recommend that you use an external IDE and toolchain when:
- Working on your [integration code](../integrations/code-conventions) (YourIntegration.py)
- Working on the [unit test script](../integrations/unit-testing) (YourIntegration_test.py)
- Working on the [release notes](../integrations/release-notes) and README.md documentation files
- Running the [linting](../integrations/linting) and testing

Instead, you should use the Cortex XSOAR UI when:
- Creating the [Test Playbooks](../integrations/test-playbooks)
- Auto-generate the [integration documentation](../integrations/integration-docs)
- Creating [example playbooks](../playbooks/playbooks) to demonstrate your integration
- Working on the properties of your integration (parameters, commands, arguments, outputs, etc.)
- Testing the User Experience

## What IDE should I use?

When it comes to an External IDE, you should stick to what you're comfortable with.

We developed a free [plugin](https://plugins.jetbrains.com/plugin/12093-demisto-add-on-for-pycharm) for [PyCharm](https://www.jetbrains.com/pycharm/) that simplifies/automates a few tasks such as:
- Running unit tests
- Creating a blank integration or automation script
- Uploading/Downloading your integration code to/from Cortex XSOAR
- Running commands directly on Cortex XSOAR

However, if you want to a different IDE (Visual Studio Code, Sublime, vi, emacs, etc.) it's totally fine! It just means that some of those tasks must be performed manually. To automate them, you can use the  [demisto-sdk](https://github.com/demisto/demisto-sdk). In this tutorial, we will be using it for unit tests, but more features will come in the future.

## Setting Up a Development Repository
[Fork](https://guides.github.com/activities/forking/) the Cortex XSOAR Content repository and create a branch for your contribution.

### Install Python virtualenv
We recommend using [virtualenv](https://github.com/pypa/virtualenv) to create an isolated virtual python development environment. To install virtual env run:
```
pip install virtualenv
```
**Note:** Python 3 includes the `venv` module for creating virtual envs, but it does not permit creating virtual envs with other versions of Python (such as Python 2). Thus, we use the `virtualenv` package.

### Bootstrap
Once `virtualenv` is installed you can run the [`bootstrap`](https://github.com/demisto/content/blob/master/.hooks/bootstrap) script. The script will setup a pre-commit hook which will validate your modified files before committing and setup a python virtual env for development with the package requirements for [python3](https://github.com/demisto/content/blob/master/dev-requirements-py3.txt). Run the script from the root directory of the source tree:
```
.hooks/bootstrap
```
After completing, you can activate the newly created virtual env by running:
```
. ./venv/bin/activate
```
**Note:** To ease setup, by default for **forked** repositories we don't setup **Python 2** as part of the virtual env setup. If you require **Python 2** for your automations/integrations run the `.hooks/bootstrap` script with the environment variable set: `SETUP_PY2=yes`. When run with `SETUP_PY2=yes` set, the virtualenv built contains both Python 2 and 3. `python` and `python2` will point to Python 2 and `python3` to Python 3.

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
* [Built-in Platform Cortex XSOAR IDE](../concepts/xsoar-ide) (not recommended for most use cases)
* [PyCharm IDE Plugin](../concepts/pycharm-plugin)

You can also use your IDE of choice along with `demisto-sdk`.
