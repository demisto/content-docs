---
id: powershell-code
title: PowerShell
---
Starting with Server 5.5, PowerShell is supported for developing Automations and Integrations. PowerShell Integrations and Automations are executed using [PowerShell Core](https://github.com/PowerShell/PowerShell). Version 6.2 and higher of PowerShell Core is supported.

**Note for Partners/Contributors:** As support for PowerShell is available from Server version 5.5+ (released April 2020), for the widest audience we recommend to develop your Integrations in Python until adoption by customers of Server 5.5 increases. Additionally, most of our customers have a better understanding of Python compared to PowerShell, thus developing in Python will allow them to easily contribute back fixes and improvements. You should choose to develop your integration in PowerShell only if you've invested extensively already in PowerShell (for example you have a product SDK written in PowerShell), your Integration requires technologies available only in PowerShell (for example Microsoft based SDKs available only in PowerShell), or your development capabilities are significantly greater in PowerShell versus Python. 

## PowerShell supported Docker Images
Similar to Python, PowerShell Integrations and Automations run in a Docker container. All of the Demisto Docker images that support PowerShell are named with a prefix of either `demisto/powershell` or `demisto/pwsh`. If you need to create a new image follow the instructions at the `demisto/dockerfiles` project: https://github.com/demisto/dockerfiles. 

## Directory Structure
Similar to Python, PowerShell Integrations/Automations should follow the [Directory Structure](package-dir). With a slight difference that unit test files should be named: `<IntegrationFileName>.Tests.ps1` (Pester Unit Testing naming convention). You can use `demisto-sdk split` to convert an exported PowerShell Integration/Automation to the Directory Structure (more info [here](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/split/README.md)).

## Linting
We use [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer) for linting and static code analysis of PowerShell Integrations/Automations. If you receive a false positive from the Analyzer, you can suppress the rule by decorating the function/script with `SuppressMessageAttribute`. Make sure to specify a `Justification` in the attribute why the suppression was necessary. An example usage of suppression can be seen [here](https://github.com/demisto/content/blob/master/Packs/Base/Scripts/CommonServerPowerShell/CommonServerPowerShell.ps1#L3). PSScriptAnalyzer suppression documentation is available [here](https://github.com/PowerShell/PSScriptAnalyzer#suppressing-rules).

## Unit Testing
Follow the same guidelines for writing unit tests as recommended for Python. Unit tests should avoid performing communication with external APIs and should prefer to use mocking. Testing actual interaction with external APIs should be performed via [Test Playbooks](test-playbooks).

For running the unit tests we use [Pester](https://pester.dev/).

### Import `CommonServerPowerShell.ps1`
Make sure your code imports `CommonServerPowerShell.ps1`. The import should be done by adding the following line to the start of the file:
```powershell
. $PSScriptRoot\CommonServerPowerShell.ps1
```
When the Integration/Automation code is unified by `demisto-sdk` for deployment to the Server the import line is automatically removed.

### Use `Main` in Integration/Automation Code

When writing unit tests you will import the Integration/Automation file from the `*.Tests.ps1` file. Thus, there is need to make sure that the file is written in such a way that when importing, it will not execute. This can be done with a simple `Main` function which is called depending on how the file was executed. When the Integration/Automation script is imported by the unit test file we will not execute the `Main` function. Adding the following code will ensure the script is not run when imported by the unit tests:

```powershell
# Execute Main when not in Tests
if ($MyInvocation.ScriptName -notlike "*.Tests.ps1") {
    Main
}
``` 

### Write Your Unit Tests
All unit tests should be written in a separate PowerShell file named: `<IntegrationFileName>.Tests.ps1` (Pester Unit Testing naming convention). The unit test file should import the Integration/Automation code file by adding the following line at the start of the file:

```powershell
. $PSScriptRoot\<IntegrationFileName>.ps1
```  
Group related unit tests using the `Describe` block. Use `Context` for grouping tests that use the same mock logic. Write your tests using the `It` command. For more details see the [Pester Docs](https://pester.dev/docs/quick-start). Example unit tests can be seen at: [VerifyJSON](https://github.com/demisto/content/tree/master/Packs/CommonScripts/Scripts/VerifyJSON).

### Mocking
Pester supports mocking PowerShell functions. You can mock any function defined in CommonServerPowerShell.ps1 and functions included in standard PowerShell and imported modules. Pester doesn't support mocking object methods. This includes methods of the `$demisto` object. You can however modify the `$demisto` object properties in a test. For example you can set the `ContextArgs` property to control the return of `$demisto.Args()` method. Example code:
```powershell
$demisto.ContextArgs = @{arg1 = 'val1' }
``` 
Additionally, you can mock functions called by the `$demisto` object. For example you can mock `DemistoServerLog` which is called by the `$demisto` object methods: `Info, Debug, Error`. Example of using mocking can be seen at: [VerifyJSON](https://github.com/demisto/content/tree/master/Packs/CommonScripts/Scripts/VerifyJSON). More info about Pester Mocking is available [here](https://pester.dev/docs/usage/mocking).

## Run Lint and Test

### Run with Docker (demisto-sdk)
CircleCI build will run the unit tests within the docker image the Integration/Automation will run with. It is recommended to use this method to run linting and tests as it uses exactly the same environment (docker container) with all modules and OS dependencies that are used by the Integration/Automation. To run both linting and testing run:

```bash
demisto-sdk lint -i <path to code directory>
```
For example:
```bash
demisto-sdk lint -i Packs/Legacy/Scripts/VerifyJSON
```
**Tip:** Use the command line params `--no-pwsh-analyze` and `--no-pwsh-test` to skip either the PSScriptAnalyzer or unit testing.

Sample output:
![lint output](/doc_imgs/integrations/lint-powershell-output.png)

### PowerShell Command Line
Make sure to install [Pester](https://pester.dev/docs/introduction/installation), [PSScriptAnalyzer](https://github.com/PowerShell/PSScriptAnalyzer#installation) and all dependent modules. Run `demisto-sdk lint -i ...` to copy `CommonServerPowerShell.ps1` and `demistomock.ps1` to the Integration/Automation directory. Enter the pwsh console and change into the Integration/Automation directory. 

To run unit tests use Pester:
```
Invoke-Pester
```
To run PSScriptAnalyzer:
```
Invoke-ScriptAnalyzer -Path <code file>
```
Check the command help on how to specify specific tests to run.

Sample output:
![](/doc_imgs/integrations/pwsh-lint-cmd-output.png)

### VSCode IDE
We recommend using VSCode as a PowerShell editor. The [PowerShell Extension](https://code.visualstudio.com/docs/languages/powershell) developed by Microsoft comes with built-in support for PSScriptAnalyzer and Pester unit testing (including Debugging).

Sample output of PSScriptAnalyzer in VS Code alerting about an unused variable:
![VS Code PSScriptAnalyzer](/doc_imgs/integrations/vs-code-pwsh-analyazer.png)

Sample debug session using VS Code:
![VS Code Debug](/doc_imgs/integrations/vscode-pwsh-debug.gif)
