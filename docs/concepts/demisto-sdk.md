---
id: demisto-sdk
title: Demisto-SDK
---
The Demisto-SDK is a python library designed with the purpose of aiding the development process both in 
validating the entities being developed and in assisting in the interaction between your development setup and Cortex XSOAR.
This guide will help you get acquainted with the package, how can you install it, set it up and some 
basic information about key commands to aid you in the development process. For additional information please see our full [Demisto-SDK documentation](https://github.com/demisto/demisto-sdk#demisto-sdk).

## Installation and Setup

Demisto-SDK library supports python version 3.7 and up, prior to installation please make sure you have a compatible python version installed.  

To install the Demisto-SDK enter your terminal and run the command:
```buildoutcfg
pip3 install demisto-sdk
```
After running the command the library should install - as a first step we should make sure what version of the SDK we are using, to do that simply run:
```buildoutcfg
demsito-sdk -v
```
This command should print the version that is currently in use. You can check what is the latest released version [here](https://pypi.org/project/demisto-sdk/).

In you already have the SDK installed and you wish to upgrade the version, run the following command:
```buildoutcfg
pip3 install --upgrade demisto-sdk
```

#### Environment Variable Setup 

Some SDK commands require you to have an interaction with the Cortex XSOAR server. Examples of such interactions 
include uploading and downloading entities to or from XSOAR, running commands in XSOAR's CLI.

To use these functions please setup the base URL and API key environment setup like so:
 1. Get your API key by entering Cortex XSOAR server -> `Settings` -> `Integrations` -> `API Keys` -> `Get Your Key` -> Give your key a name and press `Generate Key`.
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
    
#### Using the SDK in Private Repositories

Finally, if you are using a private GitHub repository, some SDK functions require an interaction with Git. To use the SDK you should setup your GitHub token.
To generate your token on GitHub use [the following guide](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) and then run:
```buildoutcfg
export GITHUB_TOKEN=<token>
```

## General CLI Usage

Running SDK commands from the CLI by following this basic structure:
```buildoutcfg
demisto-sdk <command_name> <command_arguments>
``` 
If you are not sure what are the available commands simply run:
```buildoutcfg
demisto-sdk -h
```
This command will give you a full list of available commands as well as a short description of each command's purpose.
If you are unsure about which arguments are available for the command you can run:
```buildoutcfg
demisto-sdk <command_name> -h
```
This will give you a full list of the command's arguments and their descriptions. Do note that we add new arguments and features all the time so feel free to approach us with new ideas and suggestions!

## Commands

This guide will give you a short tutorial about the basic SDK commands. Should be noted that there are additional commands and use cases found in the SDK, yet these are the main commands you should know:

#### init

Use this command to ease the initial creation of a pack, integration or a script.

Here are some examples of how to run the command for some use cases:
 - Create a new pack:
    ```buildoutcfg
    demisto-sdk init -n myNewPackName
    ```
   This will create a new pack under the `Packs` directory with the name `myNewPackName`. 
   After the pack initialization ends the command will give you the option to create a new integration in the pack.

 - Create a new integration in a specified directory:
    ```buildoutcfg
    demisto-sdk init --integration -n myIntegration -o Packs/myNewPack/Integrations
    ```
  This will create a new integration with the name `myIntegration` under the directory `Packs/myNewPack/Integrations`.

 - Create a new *feed* integration:
    ```buildoutcfg
    demisto-sdk init --integration -n myFeed -t FeedHelloWorld
    ```
  This will create a new integration named `myFeed` which will be based on the `FeedHelloWorld` integration. The command has several pre-set templates which you can choose as the basis for your integration or script.
  By default the template is the `BaseIntegration` and `BaseScript` but you can also use `HelloWorld`, `HelloIAMWorld`, `FeedHelloWorld` for integrations and `HelloWorldScript` for scripts.
  These templates have a more robust integration information and examples additionally some are used to create the basic structure for feed and IAM integrations.
  
 - Create a new script:
    ```buildoutcfg
    demisto-sdk init --script -n myScript
    ``` 
  This command will create a new script named `myScript`.
  
For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/init/README.md#init).

#### validate
Use this command to make sure your `.yml` and `.json` files are up to Cortex XSOAR standards.

Here are some examples of how to run the command for some use cases:
 - Validate all committed files:
    ```buildoutcfg
    demisto-sdk validate
    ```
   This command will identify all the files that were **committed** via `git` in your current branch and will run validations on them.
   Do note that this is the variation of the command that runs in our build process, in case of a build failure run this to recreate it locally.
 
 - Validate all committed and staged files:
    ```buildoutcfg
    demisto-sdk validate -g
    ```
   This command will identify all the files that were **committed and staged** via `git` in your current branch and will run validations on them.
 
 - Validate a specific file:
    ```buildoutcfg
    demisto-sdk validate -i Packs/myPack/Integrations/myIntegration/myIntegration.yml
    ```
   This will run validation only on the file `Packs/myPack/Integrations/myIntegration/myIntegration.yml`. This variation does not detect the file status via `git` and thus will not check for backwards comparability changes.
  
 - Validate all committed and staged files, print ignored files and errors and debug git:
    ```buildoutcfg
    demisto-sdk validate -g --print-ignored-errors --print-ignored-files --debug-git
    ```
   This command will validate all committed and staged files and will print out some additional information which is hidden by default: 
    - Which files were ignored.
    - Error codes that were ignored.
    - A report on which files where identified and in what status via `git`.
   This additional information might be helpful in debugging SDK commands or trying to figure out why a file was not validate of some reason.

##### Validate Error Structure and Ignoring Errors
Each one of our validation errors follows a basic structure to ease it's readability:
```buildoutcfg
File_Path: [Error_Code] - Error Message
```

For example:
```buildoutcfg
Packs/CortexXDR/Integrations/CortexXDRIR/CortexXDRIR.yml: [BA100] - The version for our files should always be -1, please update the file.
```

At the end of the validation a summery would appear with all the file paths and error codes that were encountered.
The error codes serve two main functions:
1. The first two letters are used to identify the type of the error encountered for example: `DO` is a Docker related error, `BC` is backwards compatibility related and `ST` is a yml/json structure error.
    A full list of abbreviations can be found in the full validate documentation liked below.
2. The error code is used to ignore errors. To ignore an error go to the file's `.pack-ignore` file and input the following structure:
   ```buildoutcfg
    [file:file_name]
    ignore=<error_code_to_ignore>
    ```
   For example:
   ```buildoutcfg
    [file:CortexXDRIR.yml]
    ignore=IN126,IN135
    ```
   * Note: **not all error codes are ignorable! Also, it is always preferable to fix the error rather than trying to ignore it!** 
   Please consult with a Cortex XSOAR team before ignoring an error.  

For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/validate/README.md#validate).

#### lint
Use this command to make sure your `.py` and `.ps1` files are up to Cortex XSOAR standards.
This command runs several libraries to validate your code these include:
 - [Flake8](https://pypi.org/project/flake8/) - Making sure your code is up to PEP8 standards.
 - [MyPy](https://pypi.org/project/mypy/) - Validating type annotations, assignments and additional python checks.
 - [Vulture](https://pypi.org/project/vulture/) - Finds unused code.
 - [Bandit](https://pypi.org/project/bandit/) - Finds security issues.
 - XSOAR Linter - An internal linter used to identify XSOAR specific restrictions and provide best practice advice for your code.
 - Pylint and Pytest - Used to run your attached unit test (in the `_test.py`) file on the integration/script's Docker.
 - PowerShell test and analyze - Code linters for PowerShell.

At the end of the command a short report will appear with all the error and warnings found, as well as failed and passed unit tests.

Here are some examples of how to run the command for some use cases:
 - Run lint on all committed and changed files:
    ```buildoutcfg
    demisto-sdk lint -g
    ```
   This command will identify all the files that were **committed and staged** via `git` in your current branch and run `lint` on them.
   Do note that this is the variation of the command that runs in our build process, in case of a build failure run this to recreate it locally.
 
 - Run lint without flake8 on a specific file:
   ```buildoutcfg
   demisto-sdk lint -i Packs/myPack/Integrations/myIntegration/ --no-flake8
    ```
   This will run the lint command on the integration found in `Packs/myPack/Integrations/myIntegration/` - please not that the path requested is **to the directory not to the file itself**.
   Also, it should be noted that there are additional flags used to turn off any specific linter like `--no-mypy` and `--no-xsoar-linter`.
 
For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/lint/README.md#lint).

#### secrets
Use this command to find secrets such as emails and IP addresses in your files.
Cortex XSOAR is an open source product, it's code can be found on a public repository on GitHub and thus it very visible.
With that there comes a responsibility to identify and eliminate any secrets before they find their way to our repository and even our pull requests.

* Please note **this command is not fool proof and a manual review of the files is still highly recommended**.

Here are some examples of how to run the command for some use cases:
 - Detect secrets in your files:
    ```buildoutcfg
    demsito-sdk secrets
    ```
   This will detect secrets in all your changed files. Please do note that this command can have some false positives 
   and can be made a bit less sensitive by also using the `-ie` flag.

##### Ignoring secrets
At times there is information that might be flagged by the command as a secret and it might be incorrect or that it is a "secret" but we do wish to share it publicly (for example the support email address).
To ignore a specific secret simply enter it to the packs's `.secrets-ignore` file.

For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/secrets/README.md#secrets).
 
#### format
Use this command to format an XSOAR entity in accordance to Cortex XSOAR standards.
At times when a file is downloaded from the XSOAR server, it might contain some additional fields which are 
not required when entering the entity to the `content` repository. The `format` command will remove the unnecessary fields 
and make any additional fixes needed to the existing fields.

Here are some examples of how to run the command for some use cases:
 - Format a specific file:
    ```buildoutcfg
    demisto-sdk format -i Packs/myPack/Integrations/myIntegration/myIntegration.yml
    ```
   This will format the file `Packs/myPack/Integrations/myIntegration/myIntegration.yml` in accordance to Cortex XSOAR standards.
 
 - Format a pack and update script and integration docker images:
    ```buildoutcfg
    demisto-sdk format -i Packs/myPack -ud
    ```
   This will format all files in `myPack`. It will also update any docker images in integrations and scripts in the pack.

For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/format/README.md#format).

#### upload
Use this command to upload an XSOAR entity to a Cortex XSOAR server. Be sure to setup the `DEMISTO_BASE_URL` 
and `DEMISTO_API_KEY` prior to running this command in order to establish a connection between `demisto-sdk` and the XSOAR server.

Here are some examples of how to run the command for some use cases:
 - Upload an integration to the server:
    ```buildoutcfg
    demisto-sdk upload -i Packs/myPack/Integrations/myIntegration
    ```
   This will upload the integration found in `Packs/myPack/Integrations/myIntegration` to my preset XSOAR server.
 
 - Upload a pack to the server without certificate validation:
    ```buildoutcfg
    demisto-sdk -i Pack/myPack --insecure
    ```
   This will iterate over all the content entities in the pack `myPack` and will upload then to the preset XSOAR server 
   without checking the certification. Note this does not upload the entities as a whole pack but does upload them individually.

For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/upload/README.md#upload).

#### download
Use this command to download entities from a Cortex XSOAR server to your local repository. Be sure to setup the `DEMISTO_BASE_URL` 
and `DEMISTO_API_KEY` prior to running this command in order to establish a connection between `demisto-sdk` and the XSOAR server.

This command can become useful when developing within the Cortex XSOAR server itself and downloading the new entities to your 
local environment to continue with the contribution process.

##### Notes and Limitations
-  `JavaScript` integrations and scripts are not downloadable using this command.
- If there are files that exist both in the output directory and are specified in the input, they will be ignored. To override this behavior such that existing files will be merged with their newer version, use the `--force`/`-f` flag.
- For consistency, it is assumed that for each integration or script the folder containing it will have the same name as the integration/script name with no separators. For example the integration `Test Integration_Full-Name`, will be under `~/.../Packs/TestPack/Integrations/TestIntegrationFullName/`.

Here are some examples of how to run the command for some use cases:
 - See which files are accessible for download through the command:
    ```buildoutcfg
    demisto-sdk download -lf
    ```
   This will list all the files which are downloadable using this command from the preset XSOAR server. 
   Note: do not run the `-lf` flag alongside `-i` or `-o`.
 
 - Download a file to a given pack:
    ```buildoutcfg
    demsito-sdk download -i "My Integration" -o Packs/myPack
    ```
   This will download the entity named `My Integration` and will place it in the appropriate directory within `myPack`.
   Do note that if `My Integration` exists in the pack, it will not be downloaded!
  
 - Download several files to a given pack and overwrite any file which already exists:
    ```buildoutcfg
    demsito-sdk download -i "My Integration" -i myScript -o Packs/myPack -f
    ```
   This will download both the `My Integration` and `myScript` entities to `myPack`. If any of the files already exists in the pack it will be overwritten.
 
 - Download all available custom files to a given pack:
    ```buildoutcfg
    demisto-sdk download -a -o Packs/myPack
    ```
   This will download all accessible files (listed with the `-lf` flag) to the appropriate directories in `myPack`.
  
For additional information see [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/download/README.md#download).

#### update-release-notes
Use this command to automatically generate release notes for a given pack and update the `pack_metadata.json` version.

Running this command will create a new release notes file under the `ReleaseNotes` directory in the given pack in the form of `X_Y_Z.md` where X_Y_Z is the new pack version.
After running this command please add the newly created release notes file to `GitHub` and add your notes under their respective headlines. For example:
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
Further information about how to run this command can be found in [here](../documentation/release-notes.md).

#### generate-docs
Use this command to generate a readme file for your integration, script or playbook.

Running this command will create a new `README.md` file at the same directory as the entity on which it ran, unless otherwise specified using the `-o` flag.
To generate command examples be sure to setup the `DEMISTO_BASE_URL` and `DEMISTO_API_KEY` prior to running this command 
in order to establish a connection between `demisto-sdk` and the XSOAR server as well as create a file containing some command examples to be ran for the documentation.

Further information about how to run this command can be found in [here](../documentation/readme_file.md#creating-documentation).


