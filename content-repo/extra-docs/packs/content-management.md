---
id: content-management
title: XSOAR CI/CD
description: This process encapsulates what you need in order to control your XSOAR machines in an automated manner, while providing the ability to manage your own content, in your artifacts server of choice, with your version control system of choice.
---
​
The XSOAR CI/CD content pack is intended to help security engineers develop, test, review, implement, and maintain their content in a smooth and secure process. It allows you to create your content alongside other members of your security team, and merge that content to ensure you have not overwritten work done by someone else, or vice versa. In addition, you can manage your content in a single, yet separate, repository with the out-of-the-box content provided by Cortex XSOAR. Also, you can track the versioning of your content to support rolling back, if necessary.
​
For example, you can implement unit tests, make sure that the content that you have created is compatible with your integrations, etc.
​
The pack is used to make sure that content that is developed is implemented in your environment while making certain that changes you make to your content does not break existing flows. This enables you to develop and implement with confidence that and security.
​
The CI/CD process works as follows:
​
* create your own repository in which to create your content. The examples provided in the pack are based on GitHub, however, you can use any git-supported platform.
​
* set up the repository using the hierarchy provided in the content pack. For example, Packs -> Entities -> etc.
​
* configure your CI/CD - the pack provides a template to execute your CI/CD process.
​
* content is saved in a bucket in your cloud provider. The examples in the pack are based on Google Cloud Storage, but the pack can be configured to work with other vendors, too.
​
* run a playbook that reads from a configuration file that determines which content to install in your environment. The configuration file contains a list of content to install from your bucket.
​
​
## What's in this Content Pack
The XSOAR CI/CD pack includes several content items.
​
### Automations
There are 5 automations in this pack.
- **ConfigurationSetup** - 
Configuration loader for the XSOAR CI/CD pack.
- **CustomPackInstaller** - 
Custom Pack Installer for the XSOAR CI/CD pack.
- **JobCreator** - Job creator for the XSOAR CI/CD pack.
- **ListCreator** - List creator for the XSOAR CI/CD pack
- **MarketplacePackInstaller** - Marketplace pack installer for the XSOAR CI/CD pack.
​
### Incident Fields
There are 8 incident fields.
- **Branch Name** - The branch from which to fetch the file. Default is the main branch. (Optional)
- **Configuration File Path** - The relative path within the repository to the *xsoar_config.json* file. (Optional)
- **Configuration File Source** - The source of the configuration file.
- **Custom Packs Installed** - Custom packs that were installed.
- **Custom Packs Source** - The source of the custom packs.
- **Jobs Created** - Jobs that were created.
- **Lists Created** - Lists that were created.
- **Marketplace Packs Installed** - Content packs that were installed.
​
### Incident Type
There is 1 incident type - **Configuration Setup**.
​
### Layout
There is 1 layout - **configuration setup**
![layout.png](https://raw.githubusercontent.com/demisto/content/master/Packs/ContentManagement/doc_files/layout.png)
​
### Playbook
There is 1 playbook - **Configuration Setup**
This playbook will manage the entire configuration process and needs to run through a `Configuration Setup` incident type.<br />
It consists of five stages:
1. Fetching the configuration file and loading its content to the machine.
2. Downloading and installing the custom packs.
3. Installing Marketplace packs.
4. Configuring lists.
5. Configuring jobs.
![playbook.png](https://raw.githubusercontent.com/demisto/content/master/Packs/ContentManagement/doc_files/playbook.png)
​
## Prerequisites
​
The following are the prerequisites for using this pack:
- [Create the Repository](#create-the-repository)
- [Create the CI/CD process](#create-the-cicd-process)
- [Create the Structure for the Artifacts Server](#create-the-structure-for-the-artifacts-server)
​
### Create the Repository
​
The repository is used to organize your custom content packs and your configuration files.  
​
You should clone our [example repository](https://github.com/demisto/content-ci-cd-template) to use as a baseline.
​
The structure of the repository is as follows:
​
```
├── .hooks
│   ├── <your-hooks-here>
├── Packs
│   ├── Pack1
│   │   ├── IncidentFields
│   │   │   ├── <your-incident-field.json>
│   │   │   ├── ...
│   │   ├── IncidentTypes
│   │   │   ├── <your-incident-type.json>
│   │   │   ├── ...
│   │   ├── Layouts
│   │   │   ├── <your-layout.json>
│   │   │   ├── ...
│   │   ├── Playbooks
│   │   │   ├── <your-playbook.yml>
│   │   │   ├── ...
│   │   ├── Scripts
│   │   │   ├── <your-script>
│   │   │   │   ├── <your-script.py>
│   │   │   │   ├── <your-script.yml>
│   │   │   ├── ...
│   │   ├── Integrations
│   │   │   ├── <your-integration>
│   │   │   │   ├── <your-integration.py>
│   │   │   │   ├── <your-integration.yml>
│   │   │   ├── ...
│   │   ├── ReleaseNotes
│   │   │   ├── <1_0_1.md>
│   │   │   ├── <1_0_2.md>
│   │   │   ├── ...
│   ├── ...
├── README.md
├── xsoar_config.json
├── .private-repo-settings
├── .demisto-sdk-conf
├── requirements.txt
├── tox.ini
├── demistomock.py                    # Can be copied from the Content repo
├── demistomock.ps1                   # Can be copied from the Content repo
├── CommonServerPython.py             # Can be copied from the Content repo
├── CommonServerPowerShell.ps1        # Can be copied from the Content repo
├── dev_envs
│   ├── pytest
│   │   ├── conftest.py               # Can be copied from the Content repo
```
​

| Content of repo | Description |
| --- | ---|
| .hooks | --- |
| Packs | Your customized packs that contain your incident fields, incident types, layouts, playbooks, scripts, integrations, and release notes. You can define multiple packs. |
| README.md | A markdown file that provides a description of the pack. |
| xsoar_config.json<br/>[Example file](https://raw.githubusercontent.com/demisto/content/master/Packs/ContentManagement/doc_files/xsoar_config.json) | The configuration file that defines what packs lists, and jobs will be set up on the machine.<br/> It consists of the following sections:<br/>- *custom_packs* - Your own internal packs to be installed through the build process.<br/>- *marketplace_packs* - Marketplace packs to be installed on the machine.<br/>- *lists* - Lists to be created in the machine.<br/>- *jobs* - Jobs to be created in the machine. |
| .private-repo-settings | --- |
| .demisto-sdk-conf | Your custom configuration file for the demisto-sdk commands. For details, click [here](https://xsoar.pan.dev/docs/concepts/demisto-sdk#setting-a-preset-custom-command-configuration). |
| requirements.txt | Contains a list of all the project’s dependencies. |
| tox.ini | The command-line driven automated testing tool for Python. |
| demistomock.py | You can copy this file from the Content repo (content/Tests/demistomock/). |
| demistomock.ps1 | You can copy this file from the Content repo (/content/Tests/demistomock/).  |
| CommonServerPython.py | You can copy this file from the Content repo (/content/Packs/Base/Scripts/CommonServerPython/). |
| CommonServerPowerShell.ps1 | You can copy this file from the Content repo (/content/Packs/Base/Scripts/CommonServerPowerShell/). |              
| conftest.py | You can copy this file from the Content repo (/content/Tests/scripts/dev_envs/pytest/). |
​
### Create the CI/CD Process
​
Create a yml file for the CI/CD process. The [Example File](https://raw.githubusercontent.com/demisto/content/master/Packs/ContentManagement/doc_files/ci-cd.yml) is a GitHub actions YML file that can be used as a template for creating your CI/CD process.
​
​
1. Prepare the environment and the virtual environment on which to run the demisto-sdk. 
2. Create an ID set for the private repository using the [demisto-sdk create-id-set](https://github.com/demisto/demisto-sdk/tree/master/demisto_sdk/commands/create_id_set) command.
3. Merge the ID set with the Content repository's ID set using the following command: ***demisto-sdk merge-id-sets -i1 <path_to_private_repo_id__set> -i2 <path_to_content_repo_id_set> -o <path_to_output>***.
4. Validate the packs' files using the [demisto-sdk validate](https://xsoar.pan.dev/docs/concepts/demisto-sdk#validate) command.
5. Run unit tests and linters on the packs using the [demisto-sdk lint](https://xsoar.pan.dev/docs/concepts/demisto-sdk#lint) command.
6. Create uploadable pack zips using the [demisto-sdk zip-packs](https://github.com/demisto/demisto-sdk/tree/master/demisto_sdk/commands/zip_packs) command.
​
   Or 
​
   Upload zipped packs directly to your machine using the [demisto-sdk upload](https://xsoar.pan.dev/docs/concepts/demisto-sdk#upload) command.
7. Upload the artifacts to your artifact repository.
​
​
​
### Create the Structure for the Artifacts Server
This artifacts server structure enables you to keep track of your work. Your versions are saved in the *production* folder. The *builds* folder saves your test packs before your deploy them.
```
├── builds
│   ├── <branch-name>
│   │   ├── packs
│   │   │   ├── <pack1>
│   │   │   │   ├── 1.0.0
│   │   │   │   │   ├── pack1.zip
│   │   │   ├── <pack2>
│   │   │   │   ├── 1.0.1
│   │   │   │   │   ├── pack2.zip
│   │   │   ├── ...
│   ├── ...
├── production
│   ├── packs
│   │   ├── <pack1>
│   │   │   ├── 1.0.0
│   │   │   │   │   ├── pack1.zip
│   │   │   ├── 1.0.1
│   │   │   │   │   ├── pack1.zip
│   │   │   ├── 1.1.0
│   │   │   │   │   ├── pack1.zip
│   │   │   ├── ...
│   │   ├── <pack2>
│   │   │   ├── 1.0.0
│   │   │   │   │   ├── pack2.zip
│   │   │   ├── 1.0.1
│   │   │   │   │   ├── pack2.zip
│   │   │   ├── 1.0.2
│   │   │   │   │   ├── pack2.zip
│   │   │   ├── ...
│   │   ├── ...
```
​
## How to Use the Pack
- [Run the playbook manually](#run-the-playbook-manually)
- [Run the playbook as a scheduled job](#run-the-playbook-as-a-scheduled-job)
​
### Run the Pack Manually
1. Navigate to **Incidents**.
2. Click **New Incident**.
3. Enter a name for the incident.
4. From the Type drop down list, choose *Configuration Setup*.
5. (Optional) From the Configuration File Source field in the Configurations section, select the source of the configuration file for the playbook run. If left empty, the master configuration will be used.
   - Attachment - Attach the file to the incident. It's information is located under the *File* context path.
   - GitHub - Use the **GitHub** integration will fetch the configuration file. If you select this option, you will also need to enter relative location in the *Configuration File Path* field and the Git branch in the repository to fetch the file from in the *Branch Name* field.
6. (Optional) From the the Custom Packs Source field in the Configurations section, select the source of the custom packs files for the playbook run.
   - Attachments - Attach the file to the incident. It's information is located under the *File* context path. 
   - Google Cloud Storage - Use the *Google Cloud Storage(*) integration to download the files.
   - HTTP request - Use the *http* script to download the files.
The playbook will now run automatically.
​
​
### Run the Pack as a Scheduled Job
1. Navigate to **Jobs**.
2. Click **New Job**.
2. Select if the job is time-triggered or feed-triggered.
   - Time-triggered jobs run at pre-determined times. You can schedule the job to run at a recurring time or one time at a specific time or date.
   - Feed-triggered jobs run when a feed has completed an operation.
3. Enter a name for the job.
4. From the Type drop down list, choose *Configuration Setup*.
5. (Optional) From the Configuration File Source field in the Configurations section, select the source of the configuration file for the playbook run. If left empty, the master configuration will be used.
   - Attachment - Attach the file to the incident. It's information is located under the *File* context path.
   - GitHub - Use the **GitHub** integration will fetch the configuration file. If you select this option, you will also need to enter relative location in the *Configuration File Path* field and the Git branch in the repository to fetch the file from in the *Branch Name* field.
6. (Optional) From the the Custom Packs Source field in the Configurations section, select the source of the custom packs files for the playbook run.
   - Attachments - Attach the file to the incident. It's information is located under the *File* context path. 
   - Google Cloud Storage - Use the *Google Cloud Storage(*) integration to download the files.
   - HTTP request - Use the *http* script to download the files.
The playbook will now run automatically.
To run the pack as a scheduled job, you will need to set up a new job for a `Configuration Setup` type incident.
​
​
---
​
### Limitations
Currently, the pack does not support the following features:
1. Integration instances.
2. Server configuration keys.


### Demo Video
<video controls>
    <source src="https://github.com/demisto/content-assets/raw/c332ede923f40990749a1498c6501fcacbf58bfd/Assets/ContentManagement/content_management_demo.mp4"
            type="video/mp4"/>
    Sorry, your browser doesn't support embedded videos. You can download the video at: https://github.com/demisto/content-assets/blob/master/Assets/ContentManagement/content_management_demo.mp4 
</video>


### CI/CD Pull Request Creation
<video controls>
    <source src="https://github.com/demisto/content-assets/raw/master/Assets/ContentManagement/CICD-Pull-Request.mp4"
            type="video/mp4"/>
    Sorry, your browser doesn't support embedded videos. You can download the video at: https://github.com/demisto/content-assets/raw/master/Assets/ContentManagement/CICD-Pull-Request.mp4
</video>


https://github.com/demisto/content-assets/blob/master/Assets/ContentManagement/CICD-Pull-Request.mp4
