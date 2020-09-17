---
id: integration-cache
title: Integration Cache
---

## Overview

Occasionally, you might need to store data between integration commands runs.

A common use-case would be storing API tokens which have expiration time (i.e. JWT). 

Very often JWTs (a.k.a. JSON Web Tokens) are generated through an API call and have a validity of several minutes or hours: in order to avoid re-generating tokens every time a command is executed in Cortex XSOAR, you can cache them using `integrationContext` and retrieve them until they expire.

For that, Cortex XSOAR introduces the cached object `integrationContext`.

The object is stored in the database per integration instance.

Note: the `integrationContext` object cannot be retrieved or set in the `test-module` command.

## Implementation

The `integrationContext` supports two methods: getter and setter.

Both methods are provided by the `demisto` class.

If no object is stored, the method will return an empty dictionary.

### The `getIntegrationContext()` Method
This is the getter the cached object, which returns a key-value dictionary.

### The `setIntegrationContext()` Method
This is the setter the cached object.

This method takes only one argument - the object to store, which its keys and values must be strings.

Note that this method overrides the existing object which is stored, so in order to update a stored object, one should first get it, make the requested changes and then set it.


## Examples

### General usage
```python
integration_context: Dict = demisto.getIntegrationContext()
demisto.results(integration_context)
>>> {}
integration_context_to_set = {'token': 'TOKEN'}
demisto.setIntegrationContext(integration_context_to_set)
integration_context = demisto.getIntegrationContext()
demisto.results(integration_context['token'])
>>> "TOKEN"
integration_context_to_set = {'token': 'NEW-TOKEN'}
demisto.setIntegrationContext(integration_context_to_set)
integration_context = demisto.getIntegrationContext()
demisto.results(integration_context['token'])
>>> "NEW-TOKEN"
```

### Storing token with expiration time
```python
integration_context = demisto.getIntegrationContext()
token = integration_context.get('token')
valid_until = integration_context.get('valid_until')
time_now = int(time.time())
if token and valid_until:
    if time_now < valid_until:
        # Token is still valid - did not expire yet
        return token
# get_token() should be the implementation of retrieving the token from the API 
token = get_token()
integration_context = {
    'access_token': token,
    'valid_until': time_now + 3600  # Assuming the expiration time is 1 hour
}
demisto.setIntegrationContext(integration_context)
```

### For more examples, refer to following integrations:
 - [Microsoft Graph](https://github.com/demisto/content/blob/master/Packs/ApiModules/Scripts/MicrosoftApiModule/MicrosoftApiModule.py)
 - [EWS v2](https://github.com/demisto/content/blob/master/Packs/EWS/Integrations/EWSv2/EWSv2.py) 