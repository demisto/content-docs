---
id: dev-setup
title: Development Setup
---

*Note*: this article is brief, please refer to the end-to-end [Tutorial](../tutorials/tut-setup-dev) for more details.

## Prerequisites

### Development OS
Our recommended OS for development is either macOS or Linux, as we use bash and docker in some of our validation/testing flows.

#### Windows Users
If you are working on Windows, you can either work with a Linux VM or utilize [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10). 

**Note:** When using WSL2 you may experience performance issues if working on the Windows mounted file system (for example `/mnt/c/`). See the following [WSL issue](https://github.com/microsoft/WSL/issues/4197) for more info. In such cases we recommend using the Linux file system (`ext4` partition) WSL2 provides. Meaning that the local demisto content and the SDK will all be located on the WSL file system and using an editor which supports remote WSL. Editors supporting remote WSL include:
* VS Code: https://code.visualstudio.com/docs/remote/wsl
* PyCharm Professional Edition: https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html 


### Git
We use GitHub (as you can see). See: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git for git client install instructions.

### Python
Our repository utilizes mostly Python 3 (3.7 and up).

We recommend managing python versions via [pyenv](https://github.com/pyenv/pyenv)

Optionally, macOS users can install via [homebrew](https://docs.brew.sh/Homebrew-and-Python).

### Docker
If you would like to write [unit tests](unit-testing) and run them, as we do in our CI process (within docker), you must install docker. See: https://docs.docker.com/install/ for install options.

### Node.js and NPM
Optional. We use Node.js for validating README documentation files for Integrations, Automations and Playbooks. If you are creating README documentation files, we recommend installing Node.js to be able to validate the files locally. Node.js installation instructions for your target platform are available at: https://nodejs.org/en/download/package-manager/.

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
[Pack](packs-format). And will help you maintain your files and validate them before committing to the branch. It is installed via our `Boostrap` process. If for prefer to install the `demisto-sdk` manually see instructions [here](https://github.com/demisto/demisto-sdk).

To check the you have the latest version of the sdk run:
```
demisto-sdk --version
```

**Congratulations!** You now have a fully configured virtual env, where you can run our different validation and utility scripts. 

If you want more details, please refer to the end-to-end [Tutorial](../tutorials/tut-setup-dev).

## IDE

Cortex XSOAR offers two IDEs for developing: 
* [Built-in Platform Cortex XSOAR IDE](../integrations/xsoar-ide) (not recommended for most use cases)
* [PyCharm IDE Plugin](../integrations/pycharm-plugin)

You can also use your IDE of choice along with `demisto-sdk`.
