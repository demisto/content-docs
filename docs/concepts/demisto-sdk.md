---
id: demisto-sdk
title: Demisto SDK
---
The [Demisto SDK](https://github.com/demisto/demisto-sdk) is a Python library designed to aid the development process, both to validate  entities being developed and to assist in the interaction between your development setup and Cortex XSOAR.
This guide will help you get acquainted with the Demisto SDK, including installation and set up and will provide some 
basic information about key commands to aid you in the development process. For additional information, please see our full [Demisto SDK documentation](https://github.com/demisto/demisto-sdk#demisto-sdk).

## Installation and Setup

The Demisto SDK library supports Python 3.7 and up. Prior to installation please make sure you have a compatible Python version installed.  

If you have followed our development setup [`bootstrap` process](dev-setup.md#bootstrap) you don't need to install the SDK manually as it is installed for you on your `venv`.

These installation steps are only required if you are not working with the `bootstrap` or if you are working on a repository which is not part of the Content repository.
To manually install the Demisto-SDK, enter your terminal and run the command:
```buildoutcfg
pip3 install demisto-sdk
```
After running the command the library should install - as a first step, check what version of the SDK you are using, by running:
```buildoutcfg
demsito-sdk -v
```
This command should print the version you are using. You can check the latest released version [here](https://pypi.org/project/demisto-sdk/#history).

If you already have the SDK installed and you wish to upgrade the version, run the following command:
```buildoutcfg
pip3 install --upgrade demisto-sdk
```

### Environment Variable Setup 

Some SDK commands require you to have an interaction with the Cortex XSOAR server. Examples of such interactions 
include uploading and downloading entities to or from XSOAR and running commands in XSOAR's CLI.

To use these functions set up the base URL and API key:
 1. Get your API key by going to the Cortex XSOAR server -> `Settings` -> `Integrations` -> `API Keys` -> `Get Your Key` -> Give your key a name and press `Generate Key`.
 2. Copy the given key.
 3. Add the following parameters to `~/.zshrc` and `~/.bash_profile`:
    ```buildoutcfg
    export DEMISTO_BASE_URL=<http or https>://<demisto-server url or ip>:<port>
    export DEMISTO_API_KEY=<API key>
    ```
    For example:
    ```buildoutcfg
    export DEMISTO_BASE_URL=http://127.0.0.1:8080
    export DEMISTO_API_KEY=XXXXXXXXXXXXXXXXXXXXXX
    ```
    
### Using the SDK in Private Repositories

Finally, if you are using a private GitHub repository, some SDK functions require an interaction with Git. To use the SDK you should setup your GitHub token.
To generate your token on GitHub use [the following guide](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) and then run:
```buildoutcfg
export GITHUB_TOKEN=<token>
```

## General CLI Usage

Run SDK commands from the CLI by following this basic structure:
```buildoutcfg
demisto-sdk <command_name> <command_arguments>
``` 
If you are not sure of the available commands, run:
```buildoutcfg
demisto-sdk -h
```
This command gives you a full list of available commands as well as a short description of each command's purpose.
If you need the list of arguments available for a command, run:
```buildoutcfg
demisto-sdk <command_name> -h
```
This gives you a full list of the command's arguments and their descriptions. We add new arguments and features regularly, so please feel free to approach us with new ideas and suggestions!

## Commands

This guide will give you a short tutorial about the basic SDK commands. While there are additional commands and use cases found in the SDK, these are the main commands you should know to begin:

### init

Use this command to create a new pack, integration or a script.

#### Examples and Use Cases:
 - Create a new pack:
    ```buildoutcfg
    demisto-sdk init -n myNewPackName
    ```
   This creates a new pack under the `Packs` directory with the name `myNewPackName`. 
   After the pack initialization ends the command gives you the option to create a new integration in the pack.


 - Create a new integration in a specified directory:
    ```buildoutcfg
    demisto-sdk init --integration -n myIntegration -o Packs/myNewPack/Integrations
    ```
  This creates a new integration with the name `myIntegration` under the directory `Packs/myNewPack/Integrations`.


 - Create a new *feed* integration:
    ```buildoutcfg
    demisto-sdk init --integration -n myFeed -t FeedHelloWorld
    ```
  This creates a new integration named `myFeed` which will be based on the `FeedHelloWorld` integration. The `init` command has several preset templates that you can choose as the basis for your integration or script.
  By default the template is the `BaseIntegration` and `BaseScript` but you can also use `HelloWorld`, `HelloIAMWorld`, or `FeedHelloWorld` for integrations and `HelloWorldScript` for scripts.
  These templates have more robust integration information and examples. Additionally, some templates are used to create the basic structure for feed and IAM integrations.
  
  
 - Create a new script:
    ```buildoutcfg
    demisto-sdk init --script -n myScript
    ``` 
  This command creates a new script named `myScript`.
  
For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md#init).

### validate
Use this command to make sure your `.yml`, `.json` and `.md` files are up to Cortex XSOAR standards.

#### Examples and Use Cases:
 - Validate all committed files:
    ```buildoutcfg
    demisto-sdk validate
    ```
   This command identifies all the files that were **committed** via `git` in your current branch and  runs validations on them.
  Note that this is the variation of the command that runs in our build process, in case of a build failure run this to recreate it locally.
 
 
 - Validate all committed and staged files:
    ```buildoutcfg
    demisto-sdk validate -g
    ```
   This command identifies all the files that were **committed and staged** via `git` in your current branch and runs validations on them.
 
 
 - Validate a specific file:
    ```buildoutcfg
    demisto-sdk validate -i Packs/myPack/Integrations/myIntegration/myIntegration.yml
    ```
   This runs validation only on the file `Packs/myPack/Integrations/myIntegration/myIntegration.yml`. This variation does not detect the file status via `git` and thus will not check for backwards compatibility changes.
  
  
 - Validate all committed and staged files, print ignored files and errors and debug git:
    ```buildoutcfg
    demisto-sdk validate -g --print-ignored-errors --print-ignored-files --debug-git
    ```
   This command validates all committed and staged files and prints out additional information which is hidden by default: 
    - Which files were ignored.
    - Error codes that were ignored.
    - A report on which files were identified and in what status via `git`.
   This additional information might be helpful in debugging SDK commands or figuring out why a file did not validate.

#### Validate Error Structure and Ignoring Errors
Each one of our validation errors follows a basic structure:
```buildoutcfg
File_Path: [Error_Code] - Error Message
```

For example:
```buildoutcfg
Packs/CortexXDR/Integrations/CortexXDRIR/CortexXDRIR.yml: [BA100] - The version for our files should always be -1, please update the file.
```

At the end of the validation a summary appears with the file paths and error codes.

The error codes serve two main functions:
1. The first two letters are used to identify the type of  error encountered. For example, `DO` is a Docker related error, `BC` is backwards compatibility related and `ST` is a yml/json structure error.
    A full list of abbreviations can be found in the [full validation documentation](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/validate/README.md#validate).
2. The error code can be used to ignore specific error types. To ignore an error go to the file `.pack-ignore` file and input the following structure:
   ```buildoutcfg
    [file:file_name]
    ignore=<error_code_to_ignore>
    ```
   For example:
   ```buildoutcfg
    [file:CortexXDRIR.yml]
    ignore=IN126,IN135
    ```
   * Note: **Not all error codes can be ignored! It is  preferable to fix errors rather than ignore them.** 
   Please consult with a Cortex XSOAR team member before ignoring an error.  

For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/validate/README.md#validate).

### lint
Use this command to make sure your `.py` and `.ps1` files are up to Cortex XSOAR standards.
This command runs several libraries to validate your code,  including:
 - [Flake8](https://pypi.org/project/flake8/) - Makes sure your code is up to PEP8 standards.
 - [MyPy](https://pypi.org/project/mypy/) - Validates type annotations, assignments and additional Python checks.
 - [Vulture](https://pypi.org/project/vulture/) - Finds unused code.
 - [Bandit](https://pypi.org/project/bandit/) - Finds security issues.
 - XSOAR Linter - An internal linter used to identify XSOAR specific restrictions and provide best practice advice for your code.
 - Pylint and Pytest - Used to run your attached unit test (in the `_test.py`) file on the integration/script's Docker.
 - PowerShell test and analyze - Code linters for PowerShell.

At the end of the command a short report appears with all of the error and warnings found, as well as failed and passed unit tests.

For additional information please see our documentation about [linting](../integrations/linting.md) and [unit testing](../integrations/unit-testing.md).

#### Examples and Use Cases:
 - Run lint on all committed and changed files:
    ```buildoutcfg
    demisto-sdk lint -g
    ```
   This command identifies all the files that were **committed and staged** via `git` in your current branch and runs `lint` on them.
  Note that this is the variation of the command that runs in our build process, in case of a build failure run this to recreate it locally.
 
 
 - Run lint without flake8 on a specific file:
   ```buildoutcfg
   demisto-sdk lint -i Packs/myPack/Integrations/myIntegration/ --no-flake8
    ```
   This runs the lint command on the integration found in `Packs/myPack/Integrations/myIntegration/` - please note that the path requested is **to the directory not to the file itself**.
   Also, it should be noted that there are additional flags used to turn off any specific linter such as `--no-mypy` and `--no-xsoar-linter`, etc.
 
For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/lint/README.md#lint).

### secrets
Use this command to find secrets such as emails and IP addresses in your files.
Cortex XSOAR is an open source product, its code can be found on a public repository on GitHub and thus is very visible.
You have a responsibility to identify and eliminate any secrets before they get to our repository or even to our pull requests.

> Please note: **this command is not fool proof and a manual review of the files is still highly recommended**.

#### Examples and Use Cases:
 - Detect secrets in your files:
    ```buildoutcfg
    demsito-sdk secrets
    ```
   This detects secrets in all your changed files. Please note that this command can have some false positives. You can make the command less sensitive by adding the `-ie` flag.

#### Ignoring secrets
At times there is information that might be flagged incorrectly by the command as a secret. Or it may be "secret" but we wish to share it publicly (for example the support email address).
To ignore a specific secret, enter it to the packs's `.secrets-ignore` file.

For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/secrets/README.md#secrets).
 
### format
Use this command to format an XSOAR entity in accordance with Cortex XSOAR standards.
In some cases, when a file is downloaded from the XSOAR server, it might contain additional fields that are 
not required when entering the entity to the `content` repository. The `format` command will remove the unnecessary fields and make any fixes needed to the existing fields.

#### Examples and Use Cases:
 - Format a specific file:
    ```buildoutcfg
    demisto-sdk format -i Packs/myPack/Integrations/myIntegration/myIntegration.yml
    ```
   This formats the file `Packs/myPack/Integrations/myIntegration/myIntegration.yml` in accordance with Cortex XSOAR standards.
 
 
 - Format a pack and update script and integration Docker images:
    ```buildoutcfg
    demisto-sdk format -i Packs/myPack -ud
    ```
   This formats all files in `myPack`. It also updates any Docker images in integrations and scripts in the pack.

For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/format/README.md#format).

### upload
Use this command to upload an XSOAR entity to a Cortex XSOAR server. Be sure to set up the `DEMISTO_BASE_URL` 
and the `DEMISTO_API_KEY` prior to running this command in order to establish a connection between `demisto-sdk` and the XSOAR server.

#### Examples and Use Cases:
 - Upload an integration to the server:
    ```buildoutcfg
    demisto-sdk upload -i Packs/myPack/Integrations/myIntegration
    ```
   This uploads the integration found in `Packs/myPack/Integrations/myIntegration` to the preset XSOAR server.
 
 
 - Upload a pack to the server without certificate validation:
    ```buildoutcfg
    demisto-sdk -i Pack/myPack --insecure
    ```
   This iterates over all the content entities in the pack `myPack` and uploads them to the preset XSOAR server 
   without checking the certification. Note that this command does not upload the entities as a whole pack but instead uploads them individually.

For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/upload/README.md#upload).

### download
Use this command to download entities from a Cortex XSOAR server to your local repository. Be sure to set up the `DEMISTO_BASE_URL` 
and the `DEMISTO_API_KEY` prior to running this command in order to establish a connection between `demisto-sdk` and the XSOAR server.

This command can be useful when developing within the Cortex XSOAR server itself and downloading the new entities to your 
local environment in order to continue with the contribution process.

#### Notes and Limitations
- `JavaScript` integrations and scripts are not downloadable using this command.
- If there are files that exist both in the output directory and are specified in the input, they will be ignored. To override this behavior so that existing files will be merged with their newer version, use the `--force`/`-f` flag.
- For consistency, it is assumed that for each integration or script the folder containing it will have the same name as the integration/script name with no separators. For example the integration `Test Integration_Full-Name`, will be under `~/.../Packs/TestPack/Integrations/TestIntegrationFullName/`.

#### Examples and Use Cases:
 - See which files are downloadable:
    ```buildoutcfg
    demisto-sdk download -lf
    ```
   This lists all the files which are downloadable using this command from the preset XSOAR server. 
   Note: Do not run the `-lf` flag with `-i` or `-o`.
 
 
 - Download a file to a given pack:
    ```buildoutcfg
    demsito-sdk download -i "My Integration" -o Packs/myPack
    ```
   This downloads the entity named `My Integration` and places it in the appropriate directory within `myPack`.
  Note that if `My Integration` exists in the pack, it will not be downloaded.
  
  
 - Download several files to a given pack and overwrite any file which already exists:
    ```buildoutcfg
    demsito-sdk download -i "My Integration" -i myScript -o Packs/myPack -f
    ```
   This downloads both the `My Integration` and `myScript` entities to `myPack`. If any of the files already exist in the pack they are overwritten.
 
 
 - Download all available custom files to a given pack:
    ```buildoutcfg
    demisto-sdk download -a -o Packs/myPack
    ```
   This downloads all accessible files (listed with the `-lf` flag) to the appropriate directories in `myPack`.
  
For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/download/README.md#download).

### update-release-notes
Use this command to automatically generate release notes for a given pack and update the `pack_metadata.json` version.

Running this command creates a new release notes file under the `ReleaseNotes` directory in the given pack in the form of `X_Y_Z.md` where X_Y_Z is the new pack version.
After running this command, add the newly created release notes file to `GitHub` and add your notes under their respective headlines. For example:
```buildoutcfg

#### Integrations
##### Cortex XDR - IOC
- Fixed an issue where searching more than 10K indicators failed when using ElasticSearch.
- Updated the Docker image to: *demisto/python3:3.9.4.18682*.

#### Incident Fields
- **XDR Similar Incidents** - New incident field.

#### Playbooks
##### Cortex XDR incident handling v3
- Added a new machine learning script to search for similar incidents by shared incident fields and indicators.

#### Layouts
##### Cortex XDR Incident
- Updated layout with a new section for similar incidents.

```
Further information about how to run this command can be found  [here](../documentation/release-notes.md).

### generate-docs
Use this command to generate a readme file for your integration, script or playbook.

Running this command creates a new `README.md` file in the same directory as the entity on which it ran, unless otherwise specified using the `-o` flag.
To generate command examples, set up the `DEMISTO_BASE_URL` and the `DEMISTO_API_KEY` prior to running this command 
in order to establish a connection between `demisto-sdk` and the XSOAR server, as well as create a file containing some command examples to be run for the documentation.

Further information about how to run this command can be found [here](../documentation/readme_file.md#creating-documentation).

## Setting a Preset Custom Command Configuration
You can create your own configuration for the `demisto-sdk` commands by creating a file named `.demisto-sdk-conf` 
within the directory from which you run the commands. This file will enable you to set a default value to the existing command flags that will take effect whenever the command is run. This can be done by entering the following structure in the file:

```buildoutcfg
[command_name]
flag_name=flag_default_value
```

Note: Be sure to use the flag's full name and use `_` instead of a `-` if it exists in the flag name 
(e.g. instead of `no-docker-checks` use `no_docker_checks`).

Here are a few examples:
 - As a user, I would like to not use the `MyPy` linter in my environment when using the `lint` command. 
 In the `.demisto-sdk-conf` file I'll enter:
    ```buildoutcfg
    [lint]
    no_mypy=true
    ```
 
 - As a user, I would like to include untracked git files in my validation when running the `validate` command. 
 In the `.demisto-sdk-conf` file I'll enter:
    ```buildoutcfg
    [validate]
    include_untracked=true
    ```
  
 - As a user, I would like to automatically use minor version changes when running the `update-release-notes` command. 
 In the `.demisto-sdk-conf` file I'll enter:
    ```buildoutcfg
    [update-release-notes]
    update_type=minor
    ```
