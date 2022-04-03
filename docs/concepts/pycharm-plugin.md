---
id: pycharm-plugin
title: PyCharm IDE Plugin
---
> Starting 1st October, 2021, Cortex XSOAR will no longer be developing nor updating the Pycharm plugin. After this date, the Pycharm plugin only be supported by the community with no official help or resources from Cortex XSOAR.
>
> Use the new [Cortex XSOAR extension for VSCode](./vscode-extension). It feature-full, quicker and easy to use!

The Cortex XSOAR plugin for the PyCharm IDE enables you to design and author scripts and integrations for Cortex XSOAR directly from PyCharm. The plugin adds a sidebar with Automation and Integration Settings, just like the Settings sidebar in the Cortex XSOAR script editor. When writing code, the plugin provides you with auto-complete of Cortex XSOAR and Python functions.

<iframe width="560" height="315" src="https://www.youtube.com/embed/i7n9q5R919A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="true"></iframe>

## Plugin Workflow

The plugin defines a slightly different workflow than Cortex XSOAR. With the plugin, you can work on your Python code, and use the **Cortex XSOAR Settings** side toolbar to define all of the automation and integration parameters under the **Automation Settings** or **Integration Settings** tab, respectively.

You can run the script locally in PyCharm, or run it in Cortex XSOAR and have the results display in PyCharm.

## Prerequisites

* Server v4.1 or later
* PyCharm, or IntelliJ with Python Community Edition (Python plugin for IntelliJ) v2018.5 and later.
* Cortex XSOAR server
* Cortex XSOAR API key: To generate Cortex XSOAR API key follow these steps:
    1. Log in to your Cortex XSOAR instance.
    2. Go to **Settings > Integrations > API Keys**.
    3. Click **Get Your Key**.
    4. Enter a name for the API key, and click **Generate key**.

## Install the PyCharm Plugin

There are specific installation instructions depending on your PyCharm version.

### PyCharm 18.2.x

1. From the top menu, click **PyCharm > Preferences**.
2. Select **Plugins > Browse Repositories**.
3. Search for "_Demisto_".
4. When "_Demisto Add-on for PyCharm"_ is located, click **Install**.

### PyCharm 18.3 (and later)

1. From the top menu, click **PyCharm > Preferences**.
2. Select **Plugins > Marketplace**.
3. Search for "_Demisto_".
4. When "_Demisto Add-on for PyCharm"_ is located, click **Install**.

## Configure Cortex XSOAR on PyCharm

To interact with Cortex XSOAR while working in PyCharm, you need to enter several Cortex XSOAR instance parameters.

1. Open the project you want to work on in PyCharm. For example, `Cortex XSOAR Content` repository.
2. In PyCharm, click **Preferences > Tools > Demisto Plugin Setup**.
3. (MacOS users) When prompted for access to your keychain, select **Allow Always**. This will avoid issues later on.
4. Enter your Cortex XSOAR server URL and port, if necessary.  
    If you are working on a dev instance on localhost, use HTTP (not HTTPS), for example: ([http://localhost:8080](http://localhost:8080/)).
5. Enter your Cortex XSOAR API key.
6. Optional: To test the configuration, click **Test**.
7. Click **Apply**.

After you successfully configure the plugin, several files are automatically downloaded from your Cortex XSOAR instance and saved in your project's root directory. These files enable you to use the functions you defined in Cortex XSOAR and run the scripts locally in PyCharm.

* `CommonServerPython`
* `CommonServerUserPython`
* `demistomock` (enables you to run the scripts locally in PyCharm)

![PyCharm_-_General.png](/doc_imgs/integrations/pycharm-general.png)

## Create a New Cortex XSOAR File

1. In the IDE project view, select the folder in which to save the new file.
2. In the top navigation bar, click **File**, and select the file type to create.  
    * New Cortex XSOAR Automation
    * New Cortex XSOAR Integration
3. Enter a name for the file.

New Python and YML files are created. By default, the editor opens the new Python file. You're ready to start writing code.

## Python Files

You can create new Python files, or open existing Python files.

### Create a Python file

1. Under the **Cortex XSOAR Settings** toolbar, you’ll have two buttons named `Create Cortex XSOAR Automation Configuration` and `Create Cortex XSOAR Integration Configuration`
2. Click the appropriate button. A new Cortex XSOAR YML file is created for this script, and you can now define arguments and other settings.

### Edit an Existing Cortex XSOAR File

You can't directly edit system integrations. To edit a system integration, change the `id` and `name` parameters in the YML file.

1. In the top menu bar, click File > `Open Cortex XSOAR Configuration`.
1. Select the file you want. (It should be a Cortex XSOAR YML)
1. A Python script file would open, and you can edit the code and use `Cortex XSOAR Settings` to edit arguments etc.
1. Go to a Cortex XSOAR YML file (open it in through the IDE project view)
1. Click the **Create Cortex XSOAR Python** button in the top actions toolbar.
.  A Python script file would open, and you can edit the code and use `Cortex XSOAR Settings` to edit arguments etc.

### Export a File to Cortex XSOAR

When you run a script in PyCharm, the file is automatically exported to Cortex XSOAR. To manually export a file to Cortex XSOAR, click the **Export to Cortex XSOAR** button in the top actions toolbar.

## Run an Integration or Automation in Cortex XSOAR

From PyCharm, you can run an integration or automation in Cortex XSOAR. When you want to run the script in Cortex XSOAR. The script will be uploaded to, and run in Cortex XSOAR, and the results will be displayed in the `Cortex XSOAR Results` toolbar in PyCharm.

To run an integration from PyCharm, you need an active Playground in Cortex XSOAR, otherwise an error is thrown in PyCharm. To create a Playground, from the Cortex XSOAR CLI run the `/playground_create` command.

1. From the **Cortex XSOAR Settings** toolbar, select what to run.  
    * Run Automation
    * Run Integration
2. Enter the necessary arguments.
3. Click **Export and run in Cortex XSOAR**.

![PyCharm_-_Export_and_Run.png](/doc_imgs/integrations/pycharm-export.png)

## Update Cortex XSOAR Mock Files

In general, you do not need to update Cortex XSOAR mock files. When there is an important update to the mock files, we will announce it in the plugin release notes.

You might want to manually update the mock files after content updates, in which `CommonPythonServer` and `CommonServerUserPython` files are changed or updated. Manually updating the mock files updates the files in your local environment.

To update the Cortex XSOAR mock files, select **Tools > Demisto Plugin Setup**, and click Update **Demisto Mocks**.

![](/doc_imgs/integrations/pycharm-mceclip0.png)

## Local Run/Local Debug (Advanced)

Instead of running commands in Cortex XSOAR, you can run them locally in PyCharm. Every demisto action `(demisto.___)` is executed by mock files, and the code runs as a regular Python script.

Since the script is run as a regular Python file, you can debug the code by adding the relevant parameters in the \`demistomock.py\` file, which is located in your project's root. In most cases, you need to edit the return value for several functions.

|Function|Description|Example|
|--- |--- |--- |
|command|Called for `demisto.command()`|return `"my_command_name"`|
|args|Called for `demisto.args()`|return `{ "myArg": "example"}`|
|parameters|Called for `demisto.params()`|return `{ "api_key": "example"}`|

## Logs

The logs include default PyCharm logs and plugin-specific logs. Logs are located under the `idea.log` file.

### MacOS

`~/Library/Logs/`  
For example: `~/Library/Logs/PyCharmCE2018.2/idea.log Linux and Other Unix systems: ~/`

### Windows

* Windows Vista, 7, 8, 10: `\Users<USER ACCOUNT NAME>`
* Windows XP: `\Documents and Settings<USER ACCOUNT NAME>`  
    For example: `c:\Users\John.PyCharm45\`
