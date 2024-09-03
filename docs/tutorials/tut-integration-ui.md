---
id: tut-integration-ui
title: Create an Integration
---

## Welcome

This tutorial guides you through creating an integration for Cortex XSOAR/Cortex XSIAM. You should have a working instance of Cortex XSOAR/XSIAM and programming experience with Python. <br/><br/>**NOTE**: As an introductory guide, not all code in the tutorial strictly follows our code conventions. See 
[Code Conventions](../integrations/code-conventions) to learn more about our coding standards.

The complete code for the integration is available at the end of the tutorial.

Although this tutorial is based on Cortex XSOAR, it can be used with the following platforms:
- Cortex XSOAR 6 and 8
- Cortex XSIAM

## The Cortex XSOAR IDE

You have the option to develop integrations using the Cortex XSOAR/XSIAM IDE or a standalone IDE such as Visual Studio Code (if you use Visual Studio, see the [Extension for Visual Studio Code](../concepts/vscode-extension)). For this tutorial, use the Cortex XSOAR/XSIAM IDE, which includes access to the Script Helper (a library of many common server functions within Cortex XSOAR/XSIAM), and a graphical user interface for editing integration settings, commands, and arguments.  

## CommonServerPython &  CommonServerUserPython
The [CommonServerPython (CSP)](../reference/api/common-server-python) and [CommonServerUserPython (CSUP)](https://xsoar.pan.dev/docs/reference/scripts/common-server-user-python) scripts are implicitly imported at the beginning of every Python script in Cortex XSOAR/XSIAM. CSP is imported first, enabling you to create common CSUP methods to use across scripts and integrations. 

**NOTE**: CSP and CSUP scripts can’t be attached to integrations you create, so any changes you implement are not available for other users. 


## Script Helper

![scripthelper](/doc_imgs/tutorials/tut-integration-ui/cortex-xsoar-ide-8.png)

In many cases, there is an existing script for common server functions. With the **Script Helper**, you can easily find tools to format a table, manipulate data, post to the War Room, etc. If a function can be used in many different scripts, there’s a good chance it already exists in the **Script Helper**. If you create a new function that would be useful across many scripts, we encourage you to contribute that function to [CommonServerPython](https://github.com/demisto/content/blob/master/Packs/Base/Scripts/CommonServerPython/CommonServerPython.py) scripts.

## Navigate to BYOI (Bring Your Own Integration)

In this example, you are going to create an English-to-Yoda translator, which translates normal English into Yoda (the Star Wars character) language. This is a simple integration that lets you explore important aspects of integration development. You can try calling an API, parsing data, and posting it to the War Room.  You will use the Yoda-Speak translate API available at https://funtranslations.com/api/yoda.

1. Navigate to one of the following:
    - Cortex XSOAR 8: Settings & Info > Settings > Integrations > Instances
    - Cortex XSOAR 6: Settings > Integrations
    - Cortex XSIAM: Settings > Configurations > Automation & Feed Integrations
2. Click **BYOI** in the top right corner.

    ![byoi](/doc_imgs/tutorials/tut-integration-ui/byoi-8.png)


    
    You enter the Cortex XSOAR/XSIAM IDE. 

    If you don’t see this button, it means you don’t have the correct permissions required for creating new integrations. Ask your admin for assistance. 


## Define Integration Settings

When clicking **BYOI**, the HelloWorld integration template is loaded by default. You will replace the existing **HelloWorld** integration settings with the new **Yoda Speak** settings and delete any unused parameters or arguments. 
    
The new settings are saved in a YAML file, which you can export and import. To learn more about integration YAML files, see [Integrations and Scripts Metadata YAML File](../integrations/yaml-file).


### Basic Integration Settings

In the **BASIC** section, add the following: 

| Parameter | Description |
| ----------------- | ---------------------|
| Integration Name | This integration will be called **Yoda Speak**. |
| Description | The description usually includes basic information about the integration, common troubleshooting steps, and any required setup instructions. For the purposes of this tutorial, however, let's enter ***Creating an Integration***, we are.|
| Category | Select **Utilties**. For the full list of available categories, see [Design Best Practices](../concepts/design-best-practices). |
| Drag and Drop a file | (**Logo** in Cortex XSOAR 6) Add a logo, which should be no larger than 10KB, have a transparent background, and be in the PNG format. You can drag and drop the logo here or click the box to find the file for upload. |

![integration-settings](/doc_imgs/tutorials/tut-integration-ui/integration-settings-image-8.png)

**NOTE**: 
- For Cortex XSOAR, the **Fetches incidents** checkbox enables the integration to run periodically to ingest events and create incidents. 
- For Cortex XSIAM, the **Fetches Alerts** checkbox enables the integration to run periodically to ingest event and create alerts.
- The **Yoda Speak** integration doesn't need to fetch incidents/alerts, so ensure this checkbox is empty. While you don’t need this feature for this **Yoda Speak** integration, [fetching incidents/alerts](../integrations/fetching-incidents) is an essential part of many integrations. There are additional options available, but these are less commonly used:
    - [External schema support](../incidents/incident-classification-mapping#classify-using-a-classification-key)
    - [Can sync mirror in](../integrations/mirroring_integration)
    - [Can sync mirror out](../integrations/mirroring_integration)
    - [Long running integration](../integrations/long-running)

    **NOTE**: Mirroring is not supported in Cortex XSIAM. 


### Parameters

These parameters can be used across all commands in the integration. Some common parameters include the API key used for communicating with the product, your username, whether to use proxy, etc.

For the **Yoda Speak** integration, you want to include the API key and proxy settings, and to allow for insecure requests. You will also include a URL parameter, which tells the integration where to send requests. For each parameter, include a display name that tells the user why the value is used.

***API Key***

Add the following values for the apikey parameter:

| API Key Parameter Settings  |  |
| ------------- |-------------|
| Parameter name    |apikey     |
| Type dropdown      |Authentication     |
| Mandatory      | not selected     |
| Display password      |API Key

In this integration, the free service does not require an API key, and allows up to 60 API calls a day with up to 5 calls an hour. If you require more API calls, [FunTranslations](https://funtranslations.com/) offers a paid service that you can access with an API key.  In this case, you provide the option for users with a paid subscription to enter their API key, but you don’t make it mandatory.  The Authentication parameter type enables you to use Cortex XSOAR/XSIAM’s built-in credential management system to save and use the API key, and ensures that the API key is not displayed to the user and not stored in logs. 

**NOTE:** Many integrations that connect to third party services require an API key for authentication, which is sent with every request to the third party service. Since it’s used by every command that performs an API call, you add it as a global parameter and not an argument. 

![apikey](/doc_imgs/tutorials/tut-integration-ui/apikey_param.png) 
 
***URL***

Add the following values for the url parameter:

| URL Parameter Settings  |  |
| ------------- |-------------|
| Parameter name    |url     |
| Type dropdown      |Short Text      |
| Mandatory      | selected ✓     |
| Initial value      |https://api.funtranslations.com/translate/     |
| Display name     | API URL     |

**NOTE:** In some cases, the URL parameter may be used for third party services that allow you to connect to more than one server, such as servers in different geographic regions, for example https://login.example.de or https://login.example.com.

![url](/doc_imgs/tutorials/tut-integration-ui/url.png)

***Insecure***

Add the following values for the insecure parameter:

| Insecure Parameter Settings  |  |
| ------------- |-------------|
| Parameter name|insecure     |
| Type dropdown |Boolean     |
| Initial value |false    |
| Display name  | Trust any certificate (not secure)    |- 

When **Trust any certificate** is set to **True**, the integration ignores TLS/SSL certificate validation errors. Use this to test connection issues or connect to a service while ignoring SSL certificate validity. We do not recommend setting this option to true in a production environment. 

![insecure](/doc_imgs/tutorials/tut-integration-ui/insecure.png)

***Proxy***

Add the following values for the proxy parameter:


| Proxy Parameter Settings  |  |
| ------------- |-------------|
| Parameter name|proxy     |
| Type dropdown |Boolean     |
| Initial value |false    |
| Display name  | Use system proxy settings |

When **Use system proxy settings** is set to **True**, the integration runs using the proxy server (HTTP or HTTPS)  defined in the server configuration. In most cases, a proxy is not required.

![proxy](/doc_imgs/tutorials/tut-integration-ui/proxy.png)

### Commands 

Before you start coding, add commands in the **Commands** section.
1. Click **+Add command.**
2. For the Command name, enter ***yoda-speak-translate***. 
3. For the description, enter **Translates a text from English to Yoda**. 

![command-name](/doc_imgs/tutorials/tut-integration-ui/command-name.png )

**NOTE:** Command names should follow “brand-function” name formatting convention. For example, VirusTotal uses the ***vt-comments-add*** command that adds a comment to a scan. An exception to this rule is that when creating commands that enrich indicators, the commands should be named according to the indicator: ***!ip***, ***!domain***, etc. This naming convention allows commands from multiple integrations to be run together to enrich an indicator. For example, running ***!ip ip=8.8.8.8*** can trigger multiple integrations that gather information about the IP address. For more information, see [Generic Reputation Commands](../integrations/generic-commands-reputation).

***Arguments***

You want to translate English text to Yoda-style text, so you need to add an argument called *text*. Users can provide a different text string on every call. The argument is mandatory, since the command can’t run if there’s nothing to translate.

![argument](/doc_imgs/tutorials/tut-integration-ui/argument-text-8.png)

**NOTE:** Unlike parameters, arguments are specific to each command. 

***Outputs***

In Cortex XSOAR/XSIAM, the [context](../integrations/context-and-outputs) is a JSON object that is created for each incident and stores results from integration commands and automation scripts. Context is important because it enables you to add information to an incident and run playbooks and integrations utilizing that information. 

To write the translation to context, you can add an output to the ***yoda-speak-translate*** command. The naming convention for the context path is *Brandname.Object.Property*, so you will add *YodaSpeak.Phrase.Translation* as the context path. For a description, enter **Translation text, in Yodish**. Select type *String*.

![outputs](/doc_imgs/tutorials/tut-integration-ui/outputs-new.png)


## Integration Code

Once you have finished adding your parameters, command, argument, and outputs, you can write the integration code.

**NOTE:** The sample code uses standard Python error handling mechanisms, such as *try*. For more information about errors and exceptions in Python, see the [Python documentation](https://docs.python.org/3/tutorial/errors.html).
In this integration code, you want to raise exceptions when errors occur. The convention is to have a main *try*/*except* block on *main()*, that catches errors and calls *return_error*.

The *return_error* function ensures that playbooks calling these functions will fail and stop, alerting the user to a problem. In integrations and automations, you refrain from calling *return_error* in other places in the code.

### Import

At the beginning of the code, you can import Python libraries, so that its commands are available for our integration. Every integration runs inside a Docker image, and our standard Docker image includes most of the common packages, such as JSON and collections. In our **Yoda Speak** integration, you don’t need to import any libraries, as it only uses the *BaseClient* class, implicitly imported from *CommonServerPython*.

**NOTE:** When working within a traditional IDE, such as PyCharm, or Visual Studio Code, we recommend [importing the following](../integrations/debugging#debugging-using-your-ide) at the top of your code for debugging purposes.

```python
import demistomock as demisto
from CommonServerPython import * 
from CommonServerUserPython import * 
```

For Cortex XSOAR, if you want to use Python libraries that are not included in the standard Cortex XSOAR Docker image, you can [create a customized Docker image](../integrations/docker). For Cortex XSOAR 8, see [Change the Docker Image](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Cloud-Documentation/Change-the-Docker-image-in-an-integration-or-script).

### Disable Secure Warnings

Next you want prevent Python from raising a warning when accessing resources insecurely.

```python
requests.packages.urllib3.disable_warnings() # pylint: disable=no-member
```
 Since you created the insecure parameter that allows the integration to ignore TLS/SSL certificate validation errors, you also need to disable the warning.

### Create the Class Client

```python
class Client(BaseClient):
    def __init__(self, api_key: str, base_url: str, proxy: bool, verify: bool):
       super().__init__(base_url=base_url, proxy=proxy, verify=verify)
       
       self.api_key = api_key
       
       if self.api_key:
            self._headers = {'X-Funtranslations-Api-Secret': self.api_key}
 
    def translate(self, text: str):
        return self._http_request(method='POST', url_suffix='yoda', data={'text': text}, resp_type='json',  ok_codes=(200,))
```

The Client is an object that communicates with the API. You create a class called *Client*.
When a Client object is created, it instantiates a parent *BaseClient* using the params you have set up (whether to use proxy, whether to allow insecure connections, and the base URL). If the user provides values to the *api_key* parameter, the Client sets the headers it will use accordingly. 

**NOTE:** When using the [Yoda Speak API](https://funtranslations.com/api/yoda) with an API key, the API key is passed as a header.

The number of methods our [Client class](../integrations/code-conventions#client-class) has usually matches the number of commands in our integration. The **Yoda Speak** integration only has the translation command, so our Client object should have a matching method to the API request which returns its result.	

### Create the test_module 

```python
def test_module(client: Client) -> str:
    """
    Tests API connectivity and authentication'
    Returning 'ok' indicates that connection to the service is successful.
    Raises exceptions if something goes wrong.
    """

    try:
        response = client.translate('I have the high ground!')

        success = demisto.get(response, 'success.total')  # Safe access to response['success']['total']
        if success != 1:
            return f'Unexpected result from the service: success={success} (expected success=1)'

        return 'ok'

    except Exception as e:
        exception_text = str(e).lower()
        if 'forbidden' in exception_text or 'authorization' in exception_text:
            return 'Authorization Error: make sure API Key is correctly set'
        else:
            raise e
```

The *test_module* function is run whenever the **Test** integration button is clicked in the integration instance settings. The *test_module* function sends a hardcoded preset string (here, it’s **I have the high ground**) to the Yoda-Speak translate API to test API connectivity and authentication. There are three possible results:

- HTTP response code is 200, which means the request is successful. You return the string **ok** per the convention for a successful test. 
- The request is not successful and the problem is related to authorization: **Authorization Error: make sure API Key is correctly set**.
- The request is not successful for any other reason: The error text is displayed. 

### Create the Translate Command

```python
def translate_command(client: Client, text: str) -> CommandResults:
    if not text:
        raise DemistoException('the text argument cannot be empty.')

    response = client.translate(text)
    translated = demisto.get(response, 'contents.translated')

    if translated is None:
        raise DemistoException('Translation failed: the response from server did not include `translated`.',
                               res=response)

    outputs = {Phrase: {'Original': text,
                            'Translation': translated}}

    return CommandResults(outputs_prefix='YodaSpeak',
                          outputs_key_field=’Phrase.Original',
                          outputs=outputs,
                          raw_response=response,
                          readable_output=tableToMarkdown(name='Yoda Says...', t=outputs))

```

The *translate_command* function uses the client that is provided as an argument for the function and it calls translate using the text provided. The client is created outside of the function (in *main()*). The function performs several steps.

1. Confirms that there is a non-empty string to translate. If the string input is empty, it raises an exception. 
2. Tells the Client to send the appropriate API call. If the translation fails (due to an API rate limit, authentication or connection error, etc.), an exception is raised. 
3. If the translation succeeds, you want to return it to Cortex XSOAR/XSIAM. To do this, use a class called *CommandResult* (which is declared in CSP). You supply it with the following arguments: 
    - *outputs*: You create a dictionary called *outputs* where both the original text and the translation are stored. 
    - *outputs_prefix*:  The first level of the output in the context data. It usually matches the name of the integration or service. 
    - *raw_response*: The argument used to attach the raw response received from the service, which can be useful when debugging unexpected behaviors. 
    - *outputs_key_field*: Since you can run the translation command multiple times, and possibly receive different results for the same string of text, the system needs to know where to update or append each result. In this example you tell the system that *Phrase.Original* is the key that represents the original text you translated, so that the next time the command is run on the same string of text, the translated values will update. Learn more about storing results as [context data](../concepts/concepts#context-data).
    - *readable_output*: This is what users see in their War Room when calling the command, so it should be formatted. You can use the *tableToMarkdown* function (from CSP) to turn the JSON into a user-friendly table. You provide *tableToMarkdown* with both the JSON values and a title for the table. 
    
        **NOTE:** The Script Helper provides an easy way to insert common functions into your code. If you click on the **Script Helper** button and search for the *tableToMarkdown* command, you have the option to insert it directly into the code with placeholders for its *name* (title) and *t* (JSON) arguments.

### Create the Main Function

Everything actually runs within Main. You pull in the integration parameters, arguments, and the translate command. The parameters are assigned to variables. Notice that the parameters are the same ones you set up in the integration settings earlier. 

```python
def main() -> None:
    params = demisto.params()
    args = demisto.args()
    command = demisto.command()

    api_key = params.get('api_key',{}).get('password')
    base_url = params.get('url')
    verify = not params.get('insecure', False)
    proxy = params.get('proxy', False)
```

When the function runs, the command will be logged for debugging purposes. 

```python
demisto.debug(f'Command being called is {command}')
```

You now create a Client using the given parameters. The Client is defined.

```python
try:
    client = Client(api_key=api_key, base_url=base_url, verify=verify, proxy=proxy)
```

There are two possible commands that can be passed to the *main* function in our integration.  

```python
if command == 'test-module':
    # This is the call made when clicking the integration Test button.
    return_results(test_module(client))

elif command == 'yoda-speak-translate':
    return_results(translate_command(client, **args))

else:
    raise NotImplementedError(f"command {command} is not implemented.")
```

- ***test-module***
If the command name is ***test-module***, it means the user has clicked the integration test button while setting up or editing an integration instance. **NOTE:** You did not explicitly create a command called ***test-module***. It is a built-in command.
<br /><br />When returning **ok**, the user is shown a green **Success** message. If any value other than **ok** is returned, an error is displayed. Ensure you return errors that help the user understand what to change in the integration settings to fix connection issues. 

- ***yoda-speak-translate***
This is the primary command for our integration and lets us translate strings of text.


There is also an *else* option. This returns an error if someone tries to run a command that was created in the YAML  file but does not exist in the Python (PY) file. For example, if you added a command ***yoda-interpret*** in the integration settings, but did not add it to this file, and then tried to run that command, you would see **Yoda-interpret is not implemented**.

### Log Errors

```python
# Log exceptions and return errors
except Exception as e:
    demisto.error(traceback.format_exc())  # print the traceback
    return_error("\n".join(("Failed to execute {command} command.",
                            "Error:",
                            str(e))))
```
If any errors occur during the execution of our code, show those errors to the user and also return an error.

### Start at Main
```python
if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
```
This line tells the system where to start running our code. By convention, you call the main function *main*.


## Test the Integration

| Platform | Navigation |
| -------------| --------------|
| Cortex XSOAR 8 | Settings & Info > Settings > Integrations > Instances > Yoda > Add Instance |
| Cortex XSOAR 6 | Settings > Integrations > Yoda > Add Instance |
| Cortex XSIAM | Settings > Configurations > Automations and Feed Integrations > Yoda > Add Instance


![yoda-utility](/doc_imgs/tutorials/tut-integration-ui/yoda-utility.png)

You don't need to enter an API key, but will instead use the free option with a limited number of API calls. To test connectivity, click **Test**. If the connection is successful, you will see **Success** and the date/time displayed. Click **Save & Exit**.  

![yoda-instance](/doc_imgs/tutorials/tut-integration-ui/yoda-instance.png)

**NOTE:** If you have an integration open in two different tabs, you may encounter an error where your changes aren’t saved. In this case, take a screenshot of your changes, close both tabs, and then reopen one tab. Enter your changes again and save.

To test the integration, in the CLI, enter ***!yoda-speak-translate*** and the text argument with the value *Hello, my name is John Smith. We are learning about integrations.*

**NOTE**: In Cortex XSIAM, to access the CLI, select **Incident Response** > **Automation** > **Playground** 

In the Playground, you can see the table you created with the *tableToMarkdown* function, with the results. 

![yoda-results](/doc_imgs/tutorials/tut-integration-ui/translation-results.png)

View the same translation in the context.

*YodaSpeak* is the root for *Phrase*. If the translation changes the next time you run the command, the translation field will be updated. 

![yoda-context](/doc_imgs/tutorials/tut-integration-ui/translationcontext-new-8.png)

## Create a Playbook

You can see the real power of integrations when you include them in a playbook. Go to the **Playbooks** page and click **New Playbook**. 

**NOTE:** In Cortex XSIAM, go to **Incident Response** > **Automation** > **Playbooks**.

1. Name the playbook **Yoda Speak**. 

    The playbook translates the **Details** field in an incident into Yoda Speak. 
2. In the task library, search for **yoda** and click **Add**. 
    
    You can see there is a field for *text*, which is a required argument. While you could type text here, instead you want to pull the string from the incident **Details** field. 
3. Do one of the following:
    - For Cortex XSOAR, click the curly brackets, **Incident details**, **Details**, and click **OK**.
    - For Cortex XSIAM, click the curly brackets, **Alert details**, **Details**, and click **OK**. 

    For Cortex XSOAR 8:

    ![yoda-source](/doc_imgs/tutorials/tut-integration-ui/xsoar-yoda-task.png)

    For Cortex XSIAM:

    ![yoda-source-xsiam](/doc_imgs/tutorials/tut-integration-ui/xsiam-yoda-task.png)

4. To print the translation to the War Room, add a print task. 

    1. In the task library, search for **print** and under utilities, add the *Print* task.  
    2. In the **value** field, as you want to pull our text from the incident, click the curly brackets. 
        
        Our options now include yoda-speak-translate. 
    3. Under ***yoda-speak-translate***, select *Translation* and click **OK**.

        ![yoda-print](/doc_imgs/tutorials/tut-integration-ui/print-task-xsoar-8.png)

5. Connect the tasks in our playbook. Use your cursor to create lines between all tasks.

    ![connect-tasks](/doc_imgs/tutorials/tut-integration-ui/connect-tasks-8.png)

6. Go back to the Playbook Settings > Advanced, and deselect **Quiet Mode**.
    
    This ensures that you see that results are printed to the War Room.
 
    ![playbook-quiet](/doc_imgs/tutorials/tut-integration-ui/playbook-quiet.png)

7. Save the playbook.

## Create an Incident

To test our new playbook, go to the **Incidents** page and create a new incident. In the **Details** field, enter the text for translation: *The prequel movies are more entertaining than the new Disney movies*. Assign the **Yoda Speak** playbook, and click **Create new incident**.

For Cortex XSOAR:

![new-incident](/doc_imgs/tutorials/tut-integration-ui/new-incident.png)

For Cortex XSIAM:

![xsiam-incident](/doc_imgs/tutorials/tut-integration-ui/xsiam-incident.png)

Select the incident you just created. Go to the **Work Plan** page and you can see that your playbook executed successfully. Go to the **War Room** and view the translation.

![playbook-complete](/doc_imgs/tutorials/tut-integration-ui/war-room-entry.png)

## We’re Done!	

Your example integration is now complete, and you can use it throughout Cortex XSOAR/XSIAM.

Real world integrations are usually more complex than our example. Like any code, integrations require maintenance and can be extended over time with new features, commands etc.

To ensure integrations perform as expected, packs can have [unit tests](../integrations/unit-testing), and [test playbooks](../integrations/test-playbooks). Learn more about [contributing content](../contributing/contributing). 


## Resources

The [YodaSpeak](https://github.com/demisto/content/tree/master/docs/tutorial-integration/YodaSpeak) content pack is available on GitHub. The pack contains the standard pack file structure and can be viewed as a resource when creating new integrations. 

Go to **Settings > Integrations**. Click the blue button **BYOI** in the top right corner, and the built-in Cortex XSOAR IDE will open. If you don’t see this button, it means you don’t have the correct permissions required for creating new integrations. Please reach out to your admin for assistance. 
