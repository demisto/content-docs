---
id: package-dir
title: Directory Structure
---

Integrations and Automation Scripts in Cortex XSOAR are stored in YAML files that include all the required information (metadata, code, images, etc.). This is what we call the **Unified YAML** file.

To better handle them in the Content repository, Python/Powershell Automation Scripts and Integrations are stored with a **Directory Structure**, where the [YAML files](../integrations/yaml-file) only contains the metadata, while code and artifacts live in separate files.

This is requirement, among others, for running [linting](linting) and [unit testing](unit-testing) of the code.
When an Integration or Automation Script is exported from Cortex XSOAR using `demisto-sdk download`, the Unified YAML is automatically split in its components.

When an Integration or Automation Script is imported into Cortex XSOAR using `demisto-sdk upload`, the Integration/Automation directory files are automatically assembled in the Unified YAML file that gets uploaded.

As a content developer, most of the times you don't need to worry about the Unified file, and just work with the Directory Structure.

The `Directory Structure` is as follows:
---

```
 .
├── <INTEGRATION-NAME>.py              // Integration / automation script Python code.
├── <INTEGRATION-NAME>_test.py         // Python unit test code.
├── <INTEGRATION-NAME>.yml             // Configuration YAML file.
├── <INTEGRATION-NAME>_image.png       // Integration PNG logo (for integrations only).
├── <INTEGRATION-NAME>_description.md  // Detailed instructions markdown file (for integrations only)
├── README.md                          // Integration / automation script documentation.
├── Pipfile                            // Can be copied from Tests/scripts/dev_envs/default_python3
└── Pipfile.lock                       // Can be copied from Tests/scripts/dev_envs/default_python3    
```
   

For example, the integration [Palo Alto Networks Cortex XDR](https://github.com/demisto/content/tree/master/Packs/CortexXDR/Integrations/PaloAltoNetworks_XDR) is stored under Integrations directory in a sub-directory named `PaloAltoNetworks_XDR` and contain the following files:

```
.Integrations   
│
└─── .PaloAltoNetworks_XDR
│    ├── PaloAltoNetworks_XDR.py
│    ├── PaloAltoNetworks_XDR_test.py
│    ├── PaloAltoNetworks_XDR.yml
│    ├── PaloAltoNetworks_XDR_image.png
│    ├── PaloAltoNetworks_XDR_description.md
│    ├── README.md
│    ├── Pipfile
|    └── Pipfile.lock
```

## Split a YML file to Directory Structure
If you need to split a Unified YAML file (exported via the Cortex XSOAR UI) into the Directory Structure you can use the following options:

- `demisto-sdk split-yml`: This command will also format the code (using autopep8) and setup the proper Pipenv files. See full command documentation [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/split_yml/README.md).
- [Cortex XSOAR IntelliJ Plugin](https://plugins.jetbrains.com/plugin/12093-demisto-add-on-for-pycharm)

## Generate a YML file from Directory Structure

If you need to manually create the Unified YAML file (for example to manually import it in Cortex XSOAR via the UI), you can either use:
-  `demisto-sdk unify`: See full command documentation [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/unify/README.md).
- [Cortex XSOAR IntelliJ Plugin](https://plugins.jetbrains.com/plugin/12093-demisto-add-on-for-pycharm)
