---
id: dev-setup
title: Development Setup
---

## Prerequisites

### Development OS
Our recommended OS for development is either macOS or Linux, as we use bash and docker in some of our validation/testing flows.

If you are working on Windows, you can either work with a Linux VM or utilize [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

### Git
We use GitHub (as you can see). See: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git for git client install instructions.

### Python
Our repository utilizes both Python 2 (2.7 and up) and Python 3 (3.7 and up). Make sure to install both versions.

We recommend managing python versions via [pyenv](https://github.com/pyenv/pyenv)

Optionally, macOS users can install via [homebrew](https://docs.brew.sh/Homebrew-and-Python).


### Docker
Docker is an optional, but highly recommended install. If you would like to write [unit tests](unit-testing) and run them, as we do in our CI process (within docker), we recommend installing docker. See: https://docs.docker.com/install/ for install options.

## Setting Up a Development Environment
Clone (Cortex XSOAR users) or [Fork](https://guides.github.com/activities/forking/) (external contributors) the Cortex XSOAR Content repository.
### Install Python virtualenv
We recommend using [virtualenv](https://github.com/pypa/virtualenv) to create an isolated virtual python development environment. To install virtual env run:
```
pip install virtualenv
```
**Note:** Python 3 includes the `venv` module for creating virtual envs, but it does not permit creating virtual envs with other versions of Python (such as Python 2). Thus, we use the `virtualenv` package.

### Bootstrap
Once `virtualenv` is installed you can run the [`bootstrap`](https://github.com/demisto/content/blob/master/.hooks/bootstrap) script. The script will setup a pre-commit hook which will validate your modified files before committing and setup a python virtual env for development with the package requirements for [python2](https://github.com/demisto/content/blob/master/dev-requirements-py2.txt) and [python3](https://github.com/demisto/content/blob/master/dev-requirements-py3.txt). Run the script from the root directory of the source tree:
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
[Pack](packs-format). And will help you maintain your files and validate them before committing to the branch. It is installed via our `Boostrap` process. If for prefer to install the `demisto-sdk` manually see instructions [here](https://github.com/demisto/demisto-sdk).

To check the you have the latest version of the sdk run:
```
demisto-sdk --version
```

**Congratulations!** You now have a fully configured virtual env, where you can run our different validation and utility scripts. For example, to convert an exported yml integration to our [package (directory) format](package-dir), you can use the `demisto-sdk` utility. Try:
```
demisto-sdk split-yml --help
```

## IDE

Cortex XSOAR offers two IDEs for developing: 
* [Built-in Platform Cortex XSOAR IDE](xsoar-ide)
* [PyCharm IDE Plugin](pycharm-plugin) 

