---
id: debugging
title: Debugging
---

During the development phase of Integrations and Scripts, debugging plays a very important role to understand what is happening behind the scenes when your code exhibits unexpected behavior. There are a few strategies that you can implement to debug code in Cortex XSOAR, described in the folowing sections.

## Printing to the War Room

Let's face it, a mountain of `print` statements are often useful in figuring out what the issue is. To do this, simply add the following:

```python
error_msg = "Here's your completely broken code"
demisto.results(error_msg)
```

This will print the statement in the War Room, where you will be able to see it. Just remember to remove these statements so you can maintain the illusion of your bug never happening.

Keep in mind that this may not appear in the War Room depending on how close the ```demisto.results()``` statement is to the failure. To display the results before an error, you can add ```sys.exit(2)```, which will end the process before the error is returned.

>Note:
Both ```demisto.results()``` and ```sys.exit()``` should not be part of your final code. Make sure you follow the [Code Conventions](../integrations/code-conventions).


## The *Logs*

When necessary, you can look in to the server logs to determine the issue. You can use the following in your code to print information to the logs.

```python
demisto.info("I am ashamed of my code")
```

Will print to the logs at the "Info" level.

```python
demisto.debug("I shouldn't have gone into STEM")
```

This will print to the logs at the "Debug" level.

And lastly:

```python
demisto.error("I could open an Italian restaurant with all this spaghetti I am writing.")
```

Will print to the logs at the "Error" level. It also may or may not notify your co-workers of your short comings.

## Debugging using your IDE

Sometimes when printing or using the logs is too confusing or messy you want to just use the debugger and go through the code line-by-line or breakpoint-by-breakpoint.

> It is recommended to use the [Cortex XSOAR Visual Studio Code Extension](../concepts/vscode-extension.md) when you are developing content.

### Python Environment  

* You need to prepare a Python environment with all the base dependencies. Follow the instructions in the [Development setup](../concepts/dev-setup.md).
* After the Python environment is prepared, [open the integration in a virtual environment](../concepts/vscode-extension.md#open-integrations-and-scripts-in-python-virtual-environment) using the `Cortex XSOAR Visual Studio Code Extension` in `VSCode`.
### Using Demistomock (the demisto object)

Ever noticed that all integrations in your IDE start with:

```python
import demistomock as demisto
from CommonServerPython import *
from CommonServerUserPython import *
```

This is the part where you start to understand what they are (well, at least one of them and that's good enough for now).

Cortex XSOAR is a sophisticated platform with tons of amazing features but sometimes, especially when debugging, you only want one simple command to work. `demisto` as a python library has a lot of functions that are integrated with the server some examples you can see above but for our debugging we usually want to use 2 or 3 of these functions:

1. We want the `demisto.params()` function to return the connection details we insert into the create instance in the UI.
1. We want `demisto.command()` to return the name of the command we want to run.
1. We want `demisto.args()` to return the arguments for that command.

There could be more but the following applies to those as well.
In the `demistomock` file we can see a `params` function defined:

```python
def params():
    return {}
```

This is what is returned if we run the Python file.
We can instead fill it with the connection credentials needed to connect to our instance.

```python
def params():
    return {
        "credentials":{
            "identifier": "demisto",
            "password": "password"
        },
        "server": "https://1.2.3.4/",
        "insecure": True
    }
```

and now commands such as:

```python
    params: dict = demisto.params()
    username = params.get('credentials').get('identifier')  # demisto
    password = params.get('credentials').get('password')  # password
    verify_certificate = not params.get('insecure', False)
```

will take their information from there.

This is called mocking demisto.

We need to make sure that all Cortex XSOAR functions that are used in the functions we are testing are mocked correctly.
Now we can use the debugger from the IDE or ipdb to debug the code as we would any other simple Python file!
