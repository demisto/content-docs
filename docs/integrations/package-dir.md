---
id: package-dir
title: Directory Structure
---

Content code entities in Demisto are presented by [YAML files](yaml-file). For Python/Powershell Automation Scripts and Integrations we support splitting the YML file to separate entities into a **Directory Structure**.

This is requirement for running [linting](linting) and [unit testing](unit-testing) of the code.

The `Directory Structure` is as follows:
---

```
 .
├── <INTEGRATION-NAME>.py              // Integration / automation script Python code.
├── <INTEGRATION-NAME>_test.py         // Python unit test code.
├── <INTEGRATION-NAME>.yml             // Configuration YAML file.
├── <INTEGRATION-NAME>_image.png       // Integration PNG logo (for integrations only).
├── <INTEGRATION-NAME>_description.md  // Detailed instructions markdown file (for integrations only)
├── CHANGELOG.md                       // Markdown file which include the script/integration release notes.
├── README.md                          // Integration / automation script documentation.
├── Pipfile                            // Can be copied from Tests/scripts/dev_envs/default_python3
└── Pipfile.lock                       // Can be copied from Tests/scripts/dev_envs/default_python3    
```
   

For example, a package of the integration [Palo Alto Networks Cortex](https://github.com/demisto/content/tree/master/Integrations/PaloAltoNetworksCortex) is stored under Integrations directory in a sub-directory named `PaloAltoNetworksCortex` and contain the following files:

```
.Integrations   
│
└─── .PaloAltoNetworksCortex
│    ├── PaloAltoNetworksCortex.py
│    ├── PaloAltoNetworksCortex_test.py
│    ├── PaloAltoNetworksCortex.yml
│    ├── PaloAltoNetworksCortex_image.png
│    ├── PaloAltoNetworksCortex_description.md
│    ├── README.md
│    ├── Pipfile
|    └── Pipfile.lock
```

## Split a YML file to Directory Structure
To split a yml file exported from the Demisto Server into the Directory Structure you can use the following:

You can extract a YAML file into Directory Structure by using the following:
 - `demisto-sdk split-yml`: This command will also format the code (using autopep8) and setup the proper Pipenv files. See full command documentation [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/split_yml/README.md).
 - [Demisto IntelliJ Plugin](https://plugins.jetbrains.com/plugin/12093-demisto-add-on-for-pycharm)

## Generate a YML file from Directory Structure

To unify the YAML use:
-  `demisto-sdk unify`: See full command documentation [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/unify/README.md).
- [Demisto IntelliJ Plugin](https://plugins.jetbrains.com/plugin/12093-demisto-add-on-for-pycharm)
