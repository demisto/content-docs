---
id: content-management
title: Content Management (Alpha)
description: This process encapsulates what you need in order to control your XSOAR machines in an automated manner, while providing the ability to manage your own content, in your artifacts server of choice, with your version control system of choice.
---

### Purpose
This process encapsulates what you need in order to control your XSOAR machines in an automated manner, while providing the ability to manage your own content, in your artifacts server of choice, with your version control system of choice.

---

### The `xsoar_config.json` File
The configuration file that defines what will be set up on the machine.<br /> 
Consists of the following sections:
- `custom_packs` - Your own internal packs to be installed through the build process.
- `marketplace_packs` - Marketplace packs to be installed on the machine.
- `lists` - Lists to be created in the machine.
- `jobs` - Jobs to be created in the machine.

[Example file](https://raw.githubusercontent.com/demisto/content/master/Packs/XSOARbuild/docs-files/xsoar_config.json)

---

### The `Configuration Setup` Incident type
#### Custom Fields:
- `Configuration File Source` - The source of the configuration file.
- `Custom Packs Source` - The source of the custom packs.
- `Configuration File Path` - The relative path within the repository to the `xsoar_config.json` file. (Optional)
- `Branch Name` - The branch from which to fetch the file. Default is the main branch. (Optional)

#### Layout:
![layout.png](https://raw.githubusercontent.com/demisto/content/master/Packs/XSOARbuild/docs-files/layout.png)

---

### The `Configuration Setup` Playbook
This playbook will manage the entire configuration process and needs to run through a `Configuration Setup` incident type.<br />
It consists of five stages:
1. Fetching the configuration file and loading its content to the machine.
2. Downloading and installing the custom packs.
3. Installing Marketplace packs.
4. Configuring lists.
5. Configuring jobs.

![playbook.png](https://raw.githubusercontent.com/demisto/content/master/Packs/XSOARbuild/docs-files/playbook.png)

---

### How to use the pack
#### You can choose either to use the pack manually, or set it up to work as a scheduled job:
-To run the pack manually, you will need to create a new `Configurtaion Setup` type incident.
- To run the pack as a scheduled job, you will need to set up a new job for a `Configurtaion Setup` type incident.

#### How to configure the incident/job:
1. Choose the source of the configuration file for the playbook run:
   - Attachment - The file is already attached to the incident, and its information is located under the `File` context path.
   - GitHub - Will use the `GitHub` integration to fetch the configuration file.
2. Choose the source of the custom packs files for the playbook run:
   - Attachments - The files are already attached to the incident, and their information is located under the `File` context path.
   - Google Cloud Storage - Will use the `Google Cloud Storage` integration to download the files.
   - HTTP request - Will use the `http` script to download the files.
3. If you choose the option to use the `GitHub` integration to fetch the configuration file, you will also need to enter the information regarding its location and branch in the repo by completing the `Configuration File Path` and `Branch Name` fields.

---

### Recommendations for creating custom packs ready for installation
1. Validate the packs' files using the [demisto-sdk validate](https://xsoar.pan.dev/docs/concepts/demisto-sdk#validate) command.
2. Run unit tests and linters on the packs using the [demisto-sdk lint](https://xsoar.pan.dev/docs/concepts/demisto-sdk#lint) command.
3. Create uploadable pack zips using the [demisto-sdk create-content-artifacts](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/create_artifacts/README.md) command.

### Limitations
Currently, the pack does not support the following features:
1. Integration instances.
2. Server configuration keys.
