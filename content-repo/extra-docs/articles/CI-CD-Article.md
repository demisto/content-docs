CI/CD in Cortex XSOAR

In Cortex XSOAR you can develop and test your content on other machines, before using it in a  production environment. You can do this by using one of the following options:
 
 - [Remote Repositories via the UI](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-admin/remote-repository/remote-repositories-overview.html): 
Enables you to work in separate repositories for development and production environments, which is set up in Cortex XSOAR. Cortex XSOAR content updates are only delivered to the development environment. When content is ready, push the content to the production environment via a Git repository. In your production environment, you pull the content as you would all other content updates.   
You should use this remote repository feature for non-complex and minimal content (such as one developer building on a local machine). 
 - CI/CD:  
Use CI/CD to develop and maintain your own custom content for more complex content development. Instead of building and maintaining your code on the Cortex XSOAR development environment, you can build from your own repository and utilize third party tools (like Gitlab, Jenkins, etc), build servers, artifact servers, etc. You can also add to your development and testing process version control, code review, distributed developing environments, automatic testing, etc. 
Essentially CI/CD has 2 major advantages over using remote repositories via the UI.
Control your code base with a multi-branch approach. Multiple developers can work on different branches. You can have code reviews, issue pull requests, etc.
Use CI/CD solutions (like Gitlab, Jenkins, etc) as part of your testing and deployment. You also have the ability to run automatic testing.  

NOTE: To use this process you need to have a Git repository. Github, Gitlab and Bitbucket are currently supported.

The CI/CD process

The CI/CD process involves the following stages:
 - Development: Includes creating a repository, configuration steps, how to deploy, etc.
 - Deployment:  Enables you to push content either directly to the server or via an artifact server, such as Google Cloud Storage. 

    If using an artifact server, you need to download and install the [XSOAR CI/CD](https://xsoar.pan.dev/docs/reference/packs/content-management) Content Pack, which enables you to monitor, install content packs via a Playbook, incident type, etc. If not using an artifact server, users can directly install content packs in the  Marketplace. 

    The CI/CD process uses demisto-sdk to download, upload, validate, and create content, etc.

demisto-sdk

The [demisto-sdk](https://xsoar.pan.dev/docs/concepts/demisto-sdk) aids the development process to validate entities being developed and to assist in the interaction between your development setup and Cortex XSOAR. It is required to develop and deploy custom content packs and enables you to do the following:
 - Creates Content Packs
 - Uploads and downloads custom content packs
 - Generates documents
 - Validates the content
 - Generates zipped Content Packs
 - Generates outputs (JSON)
 - Generates a test playbook
 - Runs and test integration
For a full list of the commands and arguments, see [demisto-sdk-commands](https://github.com/demisto/demisto-sdk#commands). 

Migration

If you currently use the existing remote repository feature in the UI  and now want to use the CI/CD process, you can download the content from your development machine using the `demisto-sdk download` command. 

To add content from your test environment, type the following command to add to the content pack:
`demisto-sdk download -o <address of the pack folder> -i <name of the content>`
NOTE: Ensure that the `DEMISTO_BASE_URL` and `DEMISTO_API_KEY` are set to the server environment that you want to download.

If there is a lot of content, downloading can take a substantial amount of time, as it creates separate folders for each pack. It is recommended to create one folder with a general name and then separate them in branch repositories.



Development
Before you start using CI/CD, consider the following:

 - Whether you are going to use an artifact server to deploy your content (which includes content versioning, rollback, etc).
 - Whether you will deploy the content directly to a server.
 - When you want to deploy, etc. By default deploy occurs when content is pushed from a branch repository to a master repository.

Artifact Server
You can choose your own artifact repository (such as AWS, GCP, Git, FTP server, etc). It enables you to maintain and control version deployment and rollbacks so you can keep track of your work. The versions are saved in the artifact server.

<img src="../../../docs/doc_imgs/reference/XSOAR-CICD/artifacts_server.png" width="700"></img>

By default the CI/CD process uses Google Cloud Storage. You need to install the Google Cloud Storage Content Pack and configure the integration. If using another storage provider, such as AWS you need to install the relevant Content Pack and set up the integrations as necessary.

Without an Artifact Server
You can deploy your content without the need for an artifact server. If you do not use an artifact server, the `demisto-sdk upload` command, uploads the content pack directly to the Marketplace. When content is pushed to master, the content will automatically be pushed to the server.

<img src="../../../docs/doc_imgs/reference/XSOAR-CICD/without_artifacts_server.png" width="700"></img>

By default the CI/CD process uses an artifact server. You can change this in the config.yml file, as referred

Set up the CI/CD Process
After installing the demisto-sdk, you need to set up a repository. You can then create branches to work on the content packs. When validated, deploy the content.  
 1. Download and install the demisto-sdk.
    Download, install and configure the demisto-sdk on your machine. 
    Ensure that the DEMISTO_BASE_URL and DEMISTO_API_KEY are set to the server environment that you want to use. For example, if you want to upload content directly to the server without using an artifact server you need to point the server to this environment. When working on a branch and you want to download/upload to a development environment, the demisto-sdk should point to the development server.
 2. Set Up the CI/CD Repository.

    After you have installed the demisto-sdk you need to create or clone a Git repository (such as Github, Gitlab, bitbucket,etc) in accordance with the hierarchical structure set out in this [repository](https://github.com/demisto/content-ci-cd-template) to use as your base. The demisto-sdk connects to this Git repository or a general repository and then automatically connects to Cortex XSOAR servers with the API, to ensure that it validates Cortex XSOAR content.
    The repository contains the following content:
    
        | Content | Description |
        | ------- | ----------- |
        | config.yml | The CI/CD file (in the .github\workflows folder), which validates the Content Pack, creates an ID set, runs tests, etc. You need to update the file with your repository and whether you want to use an artifact server.  For more information, see step 5. |
        | Pre-commit | Within the Hooks folder, the pre-commit file uses the Git rebase interactive tool for manual control of your history revision process. |
        | .vsc code | Used when using VSC as your IDE. |
        | Build_related_scripts | Contains the CI/CD scripts (Update build_related_scripts/bucket_upload.py). The bucket_upload.py script enables you to upload to Google Cloud Storage (artifact server).  You will need to update the name of the bucket list when uploading the Google Cloud Storage. NOTE: If using another storage application such AWS, you need to change this. Contact Customer Support to assist with this. The get_modified_packs script enables you to get the latest version of the content pack before merging. |
        | dev_envs/Pytest| A folder that contains the conftest.py, which validates python files. |
        | .demisto-sdk-conf| Your custom configuration file for the demisto-sdk commands. For more information, see [Setting a preset custom command configuration](https://xsoar.pan.dev/docs/concepts/demisto-sdk#setting-a-preset-custom-command-configuration). |
        | .gitignore | Specifies intentionally untracked files that Git should ignore. |
        | .private-repo-settings | Set who can view your repository. For more information, see [Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility). |
        | CommonServerPowerShell.ps1 | Required when using Powershell. For more information, see [Powershell code](https://xsoar.pan.dev/docs/integrations/powershell-code). |
        | CommonServerPython.py | Required using Python. For more information, see [Common server python](https://xsoar.pan.dev/docs/reference/api/common-server-python). |
        | README.md | A markdown file that provides a description of the pack. |
        | demistomock.ps1 | Enables you to debug Powershell script. |
        | demistomock.py | Enables you to debug Python Script. For more information about the demistomock files see [Debugging using demistomock the demisto-object](https://xsoar.pan.dev/docs/integrations/debugging#using-demistomock-the-demisto-object). |
        | requirements.txt | Contains a list of all the project’s dependencies. |
        | tox.ini | The command-line driven automated testing tool for Python. |
        | xsoar_config.json | The configuration file that defines what packs lists, and jobs will be set up on the machine. Update this when you are ready to deploy. See step 10. |

 3. (Optional) Set up the repository to work with an IDE.
    For example if working with GitHub via VSC, you need to download Git desktop and then  Configure VSC.  Ensure that you enable Git in your IDE tool (Code>Preferences>Settings).
 4. Create branches for content.
    Create content on separate branches for content packs. It makes it easier for separate developers to create content independently, which makes it easier to review content, create pull requests, test the content on a machine, etc. 
 5. Configure the config.yml file.

    When you clone the repository, a [config.yml](https://github.com/demisto/content-ci-cd-template/blob/master/.github/workflows/config.yml) file is included in the repository (github\workflows folder). This file runs various commands and validates the content before you push the content. For example, it  validates Content Packs, runs unit tests and linters and creates and uploads Content Pack zips. 
    
    5.1.  Update the repository details under the steps:
    steps:
    ```
      - name: XSOAR CI/CD master checkout
        uses: actions/checkout@v2
        with:
          repository: your/repository
          path: repository
          fetch-depth: 0
    ```
    For example:
    ```
        repository: demisto/content-ci-cd-template
        path: content-ci-cd-template
    ```
    
    5.2.  If not using an artifact server, change the following section:
    
            # ========= UPLOAD TO ARTIFACTS SERVER OPTION =========
            # TODO: Upload to the artifacts server of your choice.
            # Create a file with the service account data
            # use the bucket_upload script to upload your packs to google cloud storage
            python $GITHUB_WORKSPACE/repository/build_related_scripts/bucket_upload.py --service_account $GITHUB_WORKSPACE/service_account.json --packs_directory $NEW_PACKS_FOLDER --branch_name $BRANCH_NAME
            # Delete the service account file
            rm $GITHUB_WORKSPACE/service_account.json
    
    Change this to:

            # ========= UPLOAD DIRECTLY TO YOUR XSOAR MACHINE (WHEN MERGING TO MAIN REPO) =========
            if [ $BRANCH_NAME != master ]; then
              CONFIG_FILE=$(cat xsoar_config.json)
              MARKETPLACE_PACKS_LIST=$(cat $CONFIG_FILE | jq -r '.marketplace_packs')
              # Upload Custom Packs
              demisto-sdk upload --input-config-file /xsoar_config.json
              # Upload MarketPlace Packs
              python3 build_related_scripts/MarketPlaceInstallerFromCICD.py --marketplace-packs-list $MARKETPLACE_PACKS_LIST

    NOTE: If not using an artifact server, in Cortex XSOAR, ensure that the server configuration (Settings>ABOUT>Troubleshooting)  content.pack.verify is set to false (enables you to import custom Content Packs that are not provided by Cortex XSOAR).
 
 6. Review the lint validations in the demisto-sdk-conf file.

 7. Create Content.
    In a branch that has been created in step 4, create either new content or download content from a development environment.

    7.1 Create New Content.

        Run the `demisto-sdk init` command
    
        The `init` command automatically generates the content pack structure. Follow the on-screen instructions by typing the name of the Content Pack, metadata, description, type of Pack, category, author, email address,tags, integration, etc.
    
        The Pack appears in the repository with the required folders. You can delete those items that are not needed.  In this example, we create a new pack called CICDExample.
        
        <img src="../../../docs/doc_imgs/reference/XSOAR-CICD/pack_example.png" width="700"></img>
    
        The content pack contains the following content:
        
        | Content | Description |
        | ------- | ----------- |
        | Classifiers | Contains the Classifiers in JSON format |
        | Dashboards | Dashboards in JSON format. |
        | GenericDefinitions | Contains Json files that define the generic object that you create. NOTE: Although available from version 6.5, it is currently not supported. You can delete this. |
        | GenericFields | Includes subfolders of custom incidents and custom indicator fields. NOTE: Although available from version 6.5, it is currently not supported. You can delete this. |
        | GenericModules | The context in which the object will be used. Contains the views (pages) displaying the new objects. NOTE: Although available from version 6.5, it is currently not supported. You can delete this. |
        | GenericTypes | Includes subfolders of custom incident and indicator types. Each directory uses the same structure as incident/indicator types. NOTE: Although available from version 6.5, it is currently not supported. You can delete this. |
        | IncidentFields | Incident fields in Json format. |
        | IncidentTypes | Incident types in Json format. |
        | IndicatorTypes | Incident types in JSON format. |
        | Integrations | Contains YML, png, markdown and python files for integrations. |
        | Layouts | Layouts in JSON format |
        | Playbooks | Contains Yml and Md files |
        | README.md | Information about the Content Packs |
        | Reports | Reports in Json format. |
        | Scripts | Contans automations in YML, PY and MD files. |
        | TestPlaybooks | Contains test files |
        | Widgets | Widgets in Json format. |
        | doc_files | Contains images in PNG format. |
        | pack_metadata.json |  Metadata about the Pack eg name, version, description. Every time it changes update the version |

	7.2 Download content.
    
        a. Ensure that the `DEMISTO_BASE_URL` and `DEMISTO_API_KEY` are set to the server environment that you want to download.
    
        b. If you develop custom content via the UI, run the `demisto-sdk download` command to download it to a branch or develop custom content. 
        If you want to add content, such as an integration from your test environment, type the following command to add to an existing content pack in your repository:
        `demisto.sdk download -o <address of the folder> -i <name of the content>`
        For example to add an CICDExample integration to the CICDExample Content Pack, type:
        `demisto-sdk download -o Packs/CICDExample -i CICDExample`
    
        The CICDExample integration file appears in the Integrations folder and it separates the content into PY and YML files together with a README.md. 

        NOTE For Automation's and integrations the content needs to be split. If downloading directly from the development server use the demisto-sdk split command. 

    7.3 Add any additional files that are required. For example, you might want to add a Release Notes folder, secrets-ignore or pack ignore folders. You can see how the Content hierarchy appears in the [Hello World](https://github.com/demisto/content/tree/master/Packs/HelloWorld) Content Pack. See https://xsoar.pan.dev/docs/concepts/demisto-sdk for more information.
    
    7.4 (Optional): While you are developing the content, you can do the following:

        a. Upload content to the testing server by using the following command:
        `Demisto-sdk upload -i Packs/mypack`
        NOTE: Remember to change the base url/key if required.
        b. For example, to upload an integration, type `demisto-sdk upload -i Packs/CICDExample -i CICDExample`
        c. Generate a [README document](https://xsoar.pan.dev/docs/documentation/readme_file#creating-documentation) for your integration, script, or playbook by running the following command:
        `Demisto-sdk generate-docs --insecure -e <directory>`

    7.5 Open a Pull Request for other developers to review.
    CI/CD checks the changes - validations, lints, etc. If it requires approval you have to wait before being able to merge. The validation is done according to the hooks in your repository. When you push the pull request, the CI/CD process runs automatically.

    8. (Artifact Server only) Configure the the bucket_upload.py file
    Update the bucket name, main bucket path and format file before pushing any content from your Git repository. The artifact server is based on Google Cloud Storage. If using a different storage provider, you need to update the bucket_upload.py file. Contact Customer Support if you need to change this.

    9. Configure the xsoar_config.json file.
    The configuration file defines how content packs, lists and jobs are set up on the production machine. It consists of the following sections
     - custom_packs - Your custom content packs, which are installed through the build process.
     - marketplace_packs - Marketplace packs to be installed on the machine.
     - lists - Lists that are created in the machine.
     - jobs - Jobs that are created in the machine.

    Custom Packs
    After you create the branch for each pack in step 4, you need to add the ID and URL for each Content Pack. You need to do one of the following:
     - For a non-artifact server you need to change the URL to the name of the Pack in this format using a local URL. “Url”: “Packs/<name of the pack>/<name.zip”. If you want to change the version you need to change it in the branch repository and not in this file.
     - If using an artifact server you need to update the version in the URL. This enables you to have version control. If there was an error in a Content Pack you can change the version number to an earlier version in your repository. 

    Marketplace Content Packs

    You can also add any Marketplace Content Packs. You can decide which Content Packs to update. You have the option to deploy from here with the latest version. If you have a lot of out of the box content, use the `demisto-sdk xsoar-config-file ---add-all-marketplace-packs`, command which automatically adds all the installed out of the box Content Packs to the configuration file.

    The content is uploaded to the artifacts server or directly to the machine.

    10. When all the changes are validated and successful, merge the changes to the master repository.
    The content is either pushed to the artifact server or to Cortex XSOAR directly. 
    In the Master Repository, ensure that the repository is in a structure similar to this:
        ```
        ├── .github\workflows
        │   ├── config.yml
        ├── .hooks
        │   ├── <your-hooks-here>
        ├── vscode
        │   ├── extensions.json
        ├── build_releated_scripts
        │   ├── bucket_upload.py
        │   ├── get_modified_packs.py
        ├── dev_envs/pytest
        │   ├── conftest.py
        ├── Packs
        │   ├── Pack1
        │   │   ├── IncidentFields
        │   │   │   ├── <your-incident-field.json>
        │   │   │   ├── …
        │   │   ├── IncidentTypes
        │   │   │   ├── <your-incident-type.json>
        │   │   │   ├── …
        │   │   ├── Layouts
        │   │   │   ├── <your-layout.json>
        │   │   │   ├── …
        │   │   ├── Playbooks
        │   │   │   ├── <your-playbook.yml>
        │   │   │   ├── …
        │   │   ├── Scripts
        │   │   │   ├── <your-script>
        │   │   │   │   ├── <your-script.py>
        │   │   │   │   ├── <your-script.yml>
        │   │   │   ├── …
        │   │   ├── Integrations
        │   │   │   ├── <your-integration>
        │   │   │   │   ├── <your-integration.py>
        │   │   │   │   ├── <your-integration.yml>
        │   │   │   ├── …
        │   │   ├── ReleaseNotes
        │   │   │   ├── <1_0_1.md>
        │   │   │   ├── <1_0_2.md>
        │   │   │   ├── …
        │   ├── …
        ├── .demisto-sdk-conf
        ├── .gitignore
        ├── .private-repo-settings
        ├── CommonServerPowerShell.ps1
        ├── CommonServerPython.py 
        ├── demistomock.py
        ├── demistomock.ps1  
        ├── README.md
        ├── requirements.txt
        ├── tox.ini
        ├── xsoar_config.json
        ```
        
    Deployment
    If using an artifact server, open the folder in the artifact server. The hierarchy should appear similar to this:
        
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
        │   │   │   ├── …
        │   ├── …
        ├── production
        │   ├── packs
        │   │   ├── <pack1>
        │   │   │   ├── 1.0.0
        │   │   │   │   │   ├── pack1.zip
        │   │   │   ├── 1.0.1
        │   │   │   │   │   ├── pack1.zip
        │   │   │   ├── 1.1.0
        │   │   │   │   │   ├── pack1.zip
        │   │   │   ├── …
        │   │   ├── <pack2>
        │   │   │   ├── 1.0.0
        │   │   │   │   │   ├── pack2.zip
        │   │   │   ├── 1.0.1
        │   │   │   │   │   ├── pack2.zip
        │   │   │   ├── 1.0.2
        │   │   │   │   │   ├── pack2.zip
        │   │   │   ├── …
        │   │   ├── ...
        ```
        
    1. Add the content to Cortex XSOAR.
         - (Non-artifact server). In the Marketplace, install the custom content packs. 
            NOTE: The content.pack.verify server configuration must be set to false (imports custom Content Packs that are not provided by Cortex XSOAR).

         - (Artifact Server) Do the following:
            a. If using Google Cloud Services, download the Google Cloud Storage Content Pack and set up the integration instance. If using another storage application you need to download the appropriate Content Pack such as AWS. 
            b. Do one of the following:
                Download the XSOAR CI/CD Content Pack. The Content Pack includes the Configuration Setup playbook, the configuration setup layout, incident fields,  automations, etc. The playbook runs via a job every 3 hours.
                The playbook fetches the configuration file and loads the contents to the machine. It downloads, and installs the custom content packs and configures lists and jobs if part of the content packs.
                NOTE: The XSOAR CI/CD Content Pack uses either Google Cloud Storage or HTTP requests to fetch the content packs. If running a different storage provider, you need to download the integration (such as AWS - S3). You need to either create or duplicate the configuration setup incident field and add AWS at the source. You also need to update the Configuration Set_up playbook by adding a task at the same level as Google Cloud Storage.

                Run the Content Manually.
                Run a job - The content automatically appears in Cortex XSOAR without having to install in the Marketplace.


CI/CD FAQs

1. We use Dev/Prod.  Do I still need this feature?  What is the difference?

    This feature is an alternative for the Dev/Prod environment. Instead of building and maintaining your code on a development Cortex XSOAR platform, you can do so from your own chosen git repository and utilize 3rd party tools like CI/CD infrastructures, build servers, artifact servers and more. This adds to your development and testing process. These multiple powerful tools do not exist with the Cortex XSOAR UI feature like Version control, code review, distributed developing environments, automatic testing, etc.

2. Do I need to have Github in order to use this pack?

    You need a Git repository, but the choice is yours. We currently support Github/Gitlab/Bitbucket.

3. How does it work with propagation tags and/or in a multi-tenant environment?

    Once the custom content is pulled to the main account, it will be propagated to the tenants per the propagation labels on the content items.

4. Can I take all the current marketplace packs and turn it into the configuration format?
    
    Yes, that is supported.






 

