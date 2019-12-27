---
id: tutorial-setup-dev
title: Tutorial: Setting Up Your Dev Environment for Demisto
---

Thank you for showing interest in contributing to the Demisto content. We hope this experience will be easy and fun.

This tutorial will guide you on how to set up your dev environment to quickly start developing on Demisto. While in Demisto you can write code directly in the UI, which is awesome, you'll also need to set up your development environment outside of Demisto. This is because, in order to build a full fledged integration, you'll need to *lint* your code, run *pytest* for unit testing, create some documentation, submit your changes via *git* and more.

For a quick reference, just jump to the [Development Setup](dev-setup) page, otherwise keep reading for more details.

## Which tools should I use?

As mentioned, you'll need a combination of both the Demisto UI and other tools. 

As a general rule of the thumb, we recommend that you use an external IDE and toolchain when:
- Working on your [integration code](code-conventions) (YourIntegration.py)
- Working on the [unit test script](unit-testing) (YourIntegration_test.py)
- Working on the [CHANGELOG.md](changelog) and README.md documentation files
- Running the [linting](linting) and testing

Instead, you should use the Demisto UI when:
- Creating the [Test Playbooks](testing)
- Auto-generate the [integration documentation](integration-docs)
- Creating [example playbooks](playbooks)
- Working on the properties of your integration (parameters, commands, arguments, outputs, etc.)
- Testing the User Experience

## What IDE should I use?

When it comes to an External IDE, you should stick to what you're comfortable with.

We developed a free [plugin](https://plugins.jetbrains.com/plugin/12093-demisto-add-on-for-pycharm) for [PyCharm](https://www.jetbrains.com/pycharm/) that simplifies/automates a few tasks such as:
- Running unit tests
- Creating a blank integration or automation script
- Uploading/Downloading your integration code to/from Demisto
- Running commands directly on Demisto

However, if you want to a different IDE (Visual Studio Code, Sublime, vi, emacs, etc.) it's totally fine! It just means that some of those tasks must be performed manually. To automate them, you can use the  [demisto-sdk](https://github.com/demisto/demisto-sdk). In this tutorial, we will be using it for unit tests, but more features will come in the future.

## Requirements

Here are few requirements to make sure that you an easily build an Demisto Integration without running into issues down the road.

### Demisto

You need an instance of Demisto up and running. You can Sign Up for the [Demisto Free Edition](https://start.paloaltonetworks.com/sign-up-for-demisto-free-edition) or, if you're entitled to, contact your Business Development representative to have a non-production license.

### Operating System

So far we've been using the following Operating Systems:
- MacOS
- Linux
- Windows (only with WSL - [Windows Subsystem For Linux](https://docs.microsoft.com/en-us/windows/wsl/about))

If you successfully manage to get this work on other platforms (native Windows, OpenBSD, etc.) , please let us know and we'll add it to the tutorial! (click on Report an issue at the bottom of this page).

### Python

You will need to build your integration using **Python** and, more specifically, Python 3.6+. While some content is built via Javascript and Python 2, we require Python 3.6+ for contributions.

**Note**: You don't need to be a a Python expert (I'm not!) to write a good integration, although some intermediate level knowledge is preferred.

It is also recommended to have both Python 2 and Python 3 installed on your system: for that purpose, please download and install **[pyenv](https://github.com/pyenv/pyenv)**. It allows to easily manage multiple versions of Python on your system and have them coexist. If you don't use `pyenv` you might have problems when creating a `virtualenv` that contains both Python 2 and Python 3 under MacOS.

### GitHub

You will need a **[GitHub](https://github.com)** account, as the contribution process requires you to submit a Pull Request in the [Demisto Content Repository](https://github.com/demisto/content). To learn more about Pull Requests and contributing , check out the [Collaborating with issue and pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests) tutorial on GitHub, as well as our [Content Contribution Guide](https://github.com/demisto/content/blob/master/CONTRIBUTING.md).

And you will need a `git` client on your system (git, GitHub Desktop, SourceTree, etc). In the examples we'll just use the `git` command line client.

### Docker

In order to be able to run linting and tests, you should have **Docker** installed on your machine. This way you can test your code using the same Python environment as the one that will run inside the Demisto instance.

*Note* if you're using WSL 1, you cannot run Docker natively on WSL, but you can install Docker Desktop on Windows and configure WSL to communicate to it using [this](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly) tutorial.


## The Tutorial Starts Here

Finally! The tutorial will guide you through the following steps:

1. Verify the requirements
2. Fork the GitHub repo
3. Clone the GitHub fork locally
4. Run the bootstrap script
5. Run the linter and unit tests
6. Create a branch
7. Commit

OK, let's begin.

### Step 1: Verify the requirements

Let's go make sure that all the requirements are satisfied, one by one.

#### Demisto

We are assuming that Demisto is already installed. For more information about installing Demisto pleae refer to [this article](https://support.demisto.com/hc/en-us/sections/360001323614-Installing-Demisto) (Support Center credentials are required)

Check if your Demisto License is correctly installed by navigating to *Settings* -> *ABOUT* -> *License* and make sure that everything is green:

![Check Demisto License](doc_imgs/01-checkdemistolicense.gif)

**PRO tip**: you can quickly navigate to different pages within Demisto by hitting *Ctrl-K* and then typing what you want. For the license page, for example, type */settings/license* or just *lic* and select the autocompleted option:

![Jump to Page](doc_imgs/02-jumptopage.png)

#### Operating System

We assume you have an Operating System and that is working :)

*Note:* if you're using **Windows with WSL**, and your code resides to a shared folder on the Windows tree (i.e. `/mnt/c/code/demisto`), please make sure that the folder is set to be [case sensitive](https://devblogs.microsoft.com/commandline/improved-per-directory-case-sensitivity-support-in-wsl/).

#### Python and pyenv

You will need both `python2` and `python3` installed on your system. While there are multiple ways to achieve this, we recommend using `pyenv`. At the time of writing, the latest versions of Python are *2.7.17* and *3.7.5*, so we're going to use these.

Make sure `pyenv` in installed:

```bash
sb@dddd:~/demisto$ pyenv -v
pyenv 1.2.15
sb@dddd:~/demisto$~/demisto$
```

If not, please follow the instructions [here](https://github.com/pyenv/pyenv#installation). Either Homebrew for MacOS or the automatic installer on Linux/WSL work fine.

Make sure that the required versions of Python are available:

```bash
sb@dddd:~/demisto$ pyenv versions
  2.7.17
  3.7.5
sb@dddd:~/demisto$
```

If they're missing, you will need to install them. As `pyenv` compiles CPython, you might need some libraries. Depending on your OS, [this](https://github.com/pyenv/pyenv/wiki/Common-build-problems) article explains how to install the required dependencies and provides useful troubleshooting info.

Also, it's a good time to take a break as installing might take a bit.

Install Python 2.7.17 and 3.7.5:

```bash
sb@dddd:~/demisto$ pyenv install 2.7.17
Downloading Python-2.7.17.tar.xz...
-> https://www.python.org/ftp/python/2.7.17/Python-2.7.17.tar.xz
Installing Python-2.7.17...
Installed Python-2.7.17 to /home/sb/.pyenv/versions/2.7.17

sb@dddd:~/demisto$ pyenv install 3.7.5
Downloading Python-3.7.5.tar.xz...
-> https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tar.xz
Installing Python-3.7.5...
Installed Python-3.7.5 to /home/sb/.pyenv/versions/3.7.5

sb@dddd:~/demisto$ pyenv versions
  2.7.17
  3.7.5
sb@dddd:~/demisto$
```

And that's it! Again, if the installation fails, check out [this](https://github.com/pyenv/pyenv/wiki/Common-build-problems) page.

#### GitHub

Not much to check here, just go to [GitHub](https://github.com) and make sure that you have an account or Sign Up for one:

![GitHub](doc_imgs/03-github.png)

#### Docker

Make sure that `docker` is installed on your system and is working correctly by running the `hello-world` container:

```bash
sb@dddd:~/demisto$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

sb@dddd:~/demisto$
```

*Note:* if you're using Windows with WSL 1, you can still use Docker Desktop from WSL. Follow [this](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly) tutorial for details.

Great, all the prerequisites are set! We can get started.

### Step 2: Fork the GitHub repo

Make sure you're logged on GitHub and navigate to the [Demisto Content Repo](https://github.com/demisto/content) and click on **Fork**:

![Fork Repository](doc_imgs/04-fork.png)

Once the fork is complete, copy the your URL:

![Copy GitHub URL](doc_imgs/05-copygithuburl.png)

This is the fork where you will commit your code and, once ready, create the Pull Request to submit your contribution back to the Demisto Content repository.

### Step 3: Clone the GitHub fork locally

Back to the shell, create a folder (in the tutorial we'll use `~/demisto`) and clone your fork of the content repository using `git clone [your_fork_url]`, where `[your_fork_url]` is the URL you copied from GitHub in the previous step:

```bash
sb@dddd:~$ mkdir demisto
sb@dddd:~$ cd demisto
sb@dddd:~/demisto$ git clone https://github.com/[your_fork_url]/content.git
Cloning into 'content'...
remote: Enumerating objects: 108, done.
remote: Counting objects: 100% (108/108), done.
remote: Compressing objects: 100% (90/90), done.
remote: Total 101143 (delta 50), reused 53 (delta 18), pack-reused 101035
Receiving objects: 100% (101143/101143), 110.65 MiB | 11.04 MiB/s, done.
Resolving deltas: 100% (73634/73634), done.
Checking out files: 100% (4522/4522), done.
sb@dddd:~/demisto$
```

*Note:* you must clone **your fork** of the repository, as you will need to be able to write into it. Do **not** clone `demisto/content`, as you won't be able to commit.

### Step 4: Run the bootstrap script

Before running the `bootstrap` script that creates the virtual environment, let's set up `pyenv` to work correctly in the `content` folder you just cloned.

At the beginning, no local python interpreter has been set via `pyenv`:
```bash
sb@dddd:~/demisto$ cd content
sb@dddd:~/demisto/content$ pyenv local
pyenv: no local version configured for this directory
```

You can tell `pyenv` to use the latest versions of Python 2 and Python 3 you previously installed and verify that everything is set correctly:
```
sb@dddd:~/demisto/content$ pyenv local
3.7.5
2.7.17

sb@dddd:~/demisto/content$ which python2
/home/sb/.pyenv/shims/python2
sb@dddd:~/demisto/content$ which python3
/home/sb/.pyenv/shims/python3

sb@dddd:~/demisto/content$ python2 -V
Python 2.7.17
sb@dddd:~/demisto/content$ python3 -V
Ptyhon 3.7.5
```

Now that Python is set up correctly, also install `pipenv` that will be useful when running Unit Tests

```bash
sb@dddd:~/demisto/content$ pip install pipenv
Collecting pipenv

[... output omitted for brevity ...]

Successfully installed certifi-2019.11.28 pipenv-2018.11.26 virtualenv-16.7.9 virtualenv-clone-0.5.3

sb@dddd:~/demisto/content$ which pipenv
/home/fvigo/.pyenv/shims/pipenv
```

OK, now you can run the `.hooks/bootstrap` script that will install the dependencies and create the `virtualenv`:
```bash
sb@dddd:~/demisto/content$ .hooks/bootstrap
Installing 'pre-commit' hooks
=======================
Initializing virtual env...
Running virtualenv with interpreter /home/sb/.pyenv/shims/python3
Already using interpreter /home/sb/.pyenv/versions/3.7.5/bin/python3
Using base prefix '/home/sb/.pyenv/versions/3.7.5'
New python executable in /home/sb/demisto/content/venv/bin/python3
Also creating executable in /home/sb/demisto/content/venv/bin/python
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter /home/sb/.pyenv/shims/python2
Already using interpreter /home/sb/.pyenv/versions/2.7.17/bin/python2
New python executable in /home/sb/demisto/content/venv/bin/python2

[... output omitted for brevity ...]

Successfully installed GitPython-3.0.5 PyYAML-5.2 atomicwrites-1.3.0 attrs-19.3.0 autopep8-1.4.4 bandit-1.6.2 beautifulsoup4-4.8.1 bs4-0.0.1 certifi-2019.11.28 chardet-3.0.4 demisto-py-2.0.6 demisto-sdk-0.2.6 docopt-0.6.2 entrypoints-0.3 flake8-3.7.8 freezegun-0.3.12 gitdb2-2.0.6 idna-2.8 importlib-metadata-1.3.0 mccabe-0.6.1 more-itertools-8.0.2 mypy-0.730 mypy-extensions-0.4.3 packaging-19.2 pbr-5.4.4 pipenv-2018.11.26 pluggy-0.13.1 py-1.8.0 pycodestyle-2.5.0 pyflakes-2.1.1 pykwalify-1.7.0 pyparsing-2.4.6 pypdf2-1.26.0 pytest-5.2.1 pytest-mock-1.11.1 python-dateutil-2.8.1 pytz-2019.3 requests-2.22.0 requests-mock-1.7.0 ruamel.yaml-0.16.5 ruamel.yaml.clib-0.2.0 six-1.13.0 smmap2-2.0.5 soupsieve-1.9.5 stevedore-1.31.0 typed-ast-1.4.0 typing-extensions-3.7.4.1 tzlocal-2.0.0 urllib3-1.25.7 virtualenv-16.7.9 virtualenv-clone-0.5.3 wcwidth-0.1.7 zipp-0.6.0    ==========================
Done setting up virtualenv at directory 'venv'
Activate the venv by running: . ./venv/bin/activate
Deactivate by running: deactivate
sb@dddd:~/demisto/content$
```

Everything is configured, and you can start developing. When you work on your integration, you can activate the `virtualenv` with the `activate` command:
```bash
sb@dddd:~/demisto/content$ . ./venv/bin/activate
(venv) sb@dddd:~/demisto/content$
```

Note the `(venv)` in front of the prompt. You can always leave the `virtualenv` using the `deactivate` command:

```bash
(venv) sb@dddd:~/demisto/content$ deactivate
sb@dddd:~/demisto/content$
```

### Step 5: Run the linter and unit tests

Our content ships with an `HelloWorld` integration that provides basic functionality and is useful to understand how to create integrations.

It's located in the `Integrations/HelloWorld` folder. We will use `demisto-sdk` to run the *linting* and *unit testing* in order to make sure that everything is fine with the dev environment (python, docker, etc.).

First, make sure you are running inside the `virtualenv`:
```bash
sb@dddd:~/demisto/content$ . ./venv/bin/activate
(venv) sb@dddd:~/demisto/content$
```

Then, make sure that `demisto-sdk` has been installed automatically by the bootstrap script as part of the preqreuisites:
```bash
(venv) sb@dddd:~/demisto/content$ demisto-sdk
Use demisto-sdk -h to see the available commands.
```

Now, run the `demisto-sdk lint` command on the folder `Integrations/HelloWorld` using the `-d` option. It will run both the [linters](linting) and [pytest](unit-testing):

```bash
(venv) sb@dddd:~/demisto/content$ demisto-sdk lint -d Integrations/HelloWorld
Detected python version: [3.7] for docker image: demisto/python3:3.7.4.2245
========= Running flake8 ===============
flake8 completed
========= Running mypy on: /home/fvigo/demisto/content/Integrations/HelloWorld/HelloWorld.py ===============
Success: no issues found in 1 source file
mypy completed
========= Running bandit on: /home/fvigo/demisto/content/Integrations/HelloWorld/HelloWorld.py ===============
bandit completed
2019-12-27 10:27:17.789503: Existing image: devtestdemisto/python3:3.7.4.2245-3e5eff7d0ddbf839419495ab81a26c54 not found will obtain lock file or wait for image
2019-12-27 10:27:17.791519: Obtained lock file: .lock-devtestdemisto-python3:3.7.4.2245-3e5eff7d0ddbf839419495ab81a26c54    2019-12-27 10:27:17.791991: Trying to pull image: devtestdemisto/python3:3.7.4.2245-3e5eff7d0ddbf839419495ab81a26c54        Pull succeeded with output: 3.7.4.2245-3e5eff7d0ddbf839419495ab81a26c54: Pulling from devtestdemisto/python3

[... output omitted for brevity ...]

1158abee0d53: Download complete
1158abee0d53: Pull complete
Digest: sha256:7132d0335cebd6c90d242b30e9fc67cf8edb12bb190b439924906deeba9a7941
Status: Downloaded newer image for devtestdemisto/python3:3.7.4.2245-3e5eff7d0ddbf839419495ab81a26c54
docker.io/devtestdemisto/python3:3.7.4.2245-3e5eff7d0ddbf839419495ab81a26c54



======== Running pylint on files: HelloWorld.py ===========
Pylint completed with status code: 0
========= Running pytest ===============
collecting tests...
============================= test session starts ==============================
platform linux -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.13.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /devwork
plugins: mock-1.11.1, asyncio-0.10.0, xdist-1.30.0, forked-1.1.1, requests-mock-1.7.0
collecting ... collected 2 items

HelloWorld_test.py::test_say_hello PASSED                                [ 50%]
HelloWorld_test.py::test_say_hello_over_http PASSED                      [100%]

=========================== 2 passed in 0.40 seconds ===========================
Pytest completed with status code: 0

(venv) sb@dddd:~/demisto/content$
```

Note that the tests run within a Docker container so, if everything worked well, it means that your development environment is up and running correctly!

### Step 6: Create a branch and integration folder

The [Git Flow](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests) requires to create a *branch* with your new code, that you will later use to submit a *Pull Request*. This tutorial doesn't mean to be an exhaustive guide on how to use `git`: its purpose is just to make sure that you have all the requirements and tools in place to successfully develop a Demisto Integration.

In order to create a branch, use the  `git checkout -b [branch_name]` command, where the name of the branch corresponds to your integration:

```bash
(venv) sb@dddd:~/demisto/content$ git checkout -b my_integration_name
Switched to a new branch 'my_integration_name'
```

Now, create a folder under `Integrations`, named after your integration where you will put all your integration files later, and add it to the staged changes in `git`. 

Make sure you use **PascalCase** in the folder name (i.e. `MyIntegration`):

```bash
(venv) sb@dddd:~/demisto/content$ mkdir Integrations/MyIntegration
(venv) sb@dddd:~/demisto/content$ git add Integrations/MyIntegration
```

### Step 7: Commit and Push

The last step is to `commit` your changes and `push` them to the *origin* in order to make sure that the pre-commit checks work fine.

First, run a `git commit -m '[some commit message]'`, which will automatically run the pre validation checks:


```bash
(venv) sb@dddd:~/demisto/content$ git commit -m 'Initial commit of MyIntegration'
Validating files...
Starting validating files structure
Using git
Running validation on branch my_integration_name
Validates only committed files
Starting validation against origin/master
The files are valid
Starting secrets detection
Finished validating secrets, no secrets were found.

Skipping running dev tasks (flake8, mypy, pylint, pytest). If you want to run this as part of the precommit hook
set CONTENT_PRECOMMIT_RUN_DEV_TASKS=1. You can add the following line to ~/.zshrc:
echo "export CONTENT_PRECOMMIT_RUN_DEV_TASKS=1" >> ~/.zshrc

Or if you want to manually run dev tasks: ./Tests/scripts/pkg_dev_test_tasks.py -d <integration/script dir>
Example: ./Tests/scripts/pkg_dev_test_tasks.py -d Scripts/ParseEmailFiles

On branch my_integration_name
Untracked files:
        .python-version

nothing added to commit but untracked files present
```

Don't worry about the `.python-version` file warning, that is generated by  `pyenv` and shouldn't be added to the repository.

*Note*: since there are no files yet in the directory you have created (`Integrations/MyIntegration` in the example), it will not show up in your branch after the commit. Again, the purpose of this tutorial is just to make sure that all the components are in place.

If everything worked fine so far, now you can *push* to your branch with the command `git push origin [branch_name]`. You will be prompted for your GitHub credentials:

```bash
(venv) sb@dddd:~/demisto/content$ git push origin my_integration_name
Username for 'https://github.com': fvigo
Password for 'https://fvigo@github.com':
Total 0 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'my_integration_name' on GitHub by visiting:
remote:      https://github.com/fvigo/content/pull/new/my_integration_name
remote:
To https://github.com/fvigo/content
 * [new branch]          my_integration_name -> my_integration_name
(venv) sb@dddd:~/demisto/content$
```

You can go back to GitHub and, under **your** work, you should be able to see that there is a new branch with the name you provided (`my_integration_name` in this example):

![GitHub Branch](doc_imgs/06-githubbranch.png)

Congratulations! You completed the set up of the Development Environment for Demisto! Now you can start writing your code. Please have a look at the [Code Conventions](code-conventions).

Thank for your time, we hope you enjoyed this tutorial. Please report issues and suggestions using the link below!