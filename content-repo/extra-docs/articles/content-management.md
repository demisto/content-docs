## Content Management (Alpha)
### Purpose
This process encapsulates what you need in order to control your XSOAR machines in an automated manner, while providing the ability to manage your own content, in your artifacts server of choice, with your version control system of choice.

---

### The `xsoar_config.json` File
The configuration file that defines what will be set up on the machine.<br /> 
Consists of the following sections:
1. `custom_packs` - Your own internal packs to be installed through the build process.
2. `marketplace_packs` - Marketplace packs to be installed on the machine.
3. `lists` - Lists to be created in the machine.
4. `jobs` - Jobs to be created in the machine.

[Example file](https://raw.githubusercontent.com/demisto/content/aace565faff531f09a42268b897d629981e69b08/Packs/XSOARbuild/docs-files/xsoar_config.json)

---

### The `Configuration Setup` Incident type
#### Custom Fields:
1. `Configuration File Source` - The source of the configuration file.
2. `Custom Packs Source` - The source of the custom packs.
3. `Configuration File Path` - The relative path within the repository to the `xsoar_config.json` file. (Optional)
4. `Branch Name` - The branch from which to fetch the file. Default is the main branch. (Optional)

#### Layout:
![layout.png](https://raw.githubusercontent.com/demisto/content/aace565faff531f09a42268b897d629981e69b08/Packs/XSOARbuild/docs-files/layout.png)

---

### The `Configuration Setup` Playbook
This playbook will manage the entire configuration process and needs to run through a `Configuration Setup` incident type.<br />
It consists of five stages:
1. Fetching the configuration file and loading its content to the machine.
2. Downloading and installing the custom packs.
3. Installing marketplace packs.
4. Configuring lists.
5. Configuring jobs.

![playbook.png](https://raw.githubusercontent.com/demisto/content/aace565faff531f09a42268b897d629981e69b08/Packs/XSOARbuild/docs-files/playbook.png)

---

### How to use the pack
#### You can choose either to use the pack manually, or set it up to work as a scheduled job:
1. In order to run it manually, you will need to create a new `Configurtaion Setup` type incident.
2. In order to run it as a scheduled job, you will need to set up a new job for a `Configurtaion Setup` type incident.

#### How to configure the incident/job:
1. Choose what is the source of the configuration file for the playbook run:
   1. Attachment - The file is already attached to the incident, and its information located under the `File` context path.
   2. GitHub - Will use the `GitHub` integration to fetch the configuration file.
2. Choose what is the source of the custom packs files for the playbook run:
   1. Attachments - The files are already attached to the incident, and their information located under the `File` context path.
   2. Google Cloud Storage - Will use the `Google Cloud Storage` integration to download the files.
   3. HTTP request - Will use the `http` script to download the files.
3. If you chose the option to use the `GitHub` integration to fetch the configuration file, you will also need to enter the information regarding the location and branch of it in the repo by filling the `Configuration File Path` and `Branch Name` fields.

---

### Recommendations for creating custom packs ready for installation
1. Validate the packs' files using the [demisto-sdk validate](https://xsoar.pan.dev/docs/concepts/demisto-sdk#validate) command.
2. Run unit tests and linters on the packs using the [demisto-sdk lint](https://xsoar.pan.dev/docs/concepts/demisto-sdk#lint) command.
3. Create uploadable packs zips using the [demisto-sdk create-content-artifacts](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/create_artifacts/README.md) command.

### Limitations
Currently, the pack does not support the following features:
1. Integrations instances.
2. Server configuration keys.
