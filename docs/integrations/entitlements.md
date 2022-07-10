---
id: entitlements
title: Understanding Entitlements
---

Entitlements are the medium by which integrations can trigger a playbook task to complete when given a response by a user.

## Entitlement Structure
Entitlements are composed of three main parts. The GUID, which is an identifier used by XSOAR to determine that the response
is unique. The Incident ID, which ties the entitlement to a specific incident. And lastly, the Task ID which is used to 
close a specific playbook task with the response given.

The following is an example of an entitlement string where `e95cb5a1-e394-4bc5-8ce0-508973aaf298` is the GUID, `22` is the Incident ID, and `43` is the Task ID.
```text
e95cb5a1-e394-4bc5-8ce0-508973aaf298@22|43
```

The basic format for an entitlement is always `GUID`@`IncidentID`|`TaskID`.

## Creating an Entitlement
Within a script, creating an entitlement is fairly simple.
```python
res = demisto.executeCommand('addEntitlement',
     {
         'persistent': demisto.get(demisto.args(), 'persistent'),
         'replyEntriesTag': demisto.get(demisto.args(), 'replyEntriesTag')
     })
```

The response received will provide you with the GUID. which can be extracted with the following:
```python
guid = demisto.get(res[0], 'Contents')
```

Now that we have a GUID, we need to add the Incident ID and Task ID (which is optional, but recommended).
```python
entitlement_string = guid + '@' + demisto.investigation()['id']
entitlement_string += '|' + demisto.get(demisto.args(), 'task')
```

This formatted entitlement can now be used by an end user.


## Consuming an Entitlement
To consume an entitlement, the process is fairly simple. The service returning the entitlement string should also provide 
some basic information about the user replying and what the response was.

Consider the following response from a service:

```json
{
  "entitlement": "8e8798e0-5f49-4dcd-85de-cf2c2b13bc3a@2200|57",
  "reply": "Yes",
  "user_email": "user@company.com"
}
```

Our integration should handle the response by calling the `demisto.handleEntitlementForUser()` function.

Typically, it is necessary to parse the required information out of the entitlement string.

You may use a function similar to the following to do so.
```python
def extract_entitlement(entitlement: str) -> Tuple[str, str, str]:
    """
    Extracts entitlement components from an entitlement string
    Args:
        entitlement: The entitlement itself

    Returns:
        Entitlement components
    """
    parts = entitlement.split('@')
    guid = parts[0]
    id_and_task = parts[1].split('|')
    incident_id = id_and_task[0]
    task_id = ''

    if len(id_and_task) > 1:
        task_id = id_and_task[1]

    return guid, incident_id, task_id
```

After we have the parts extracted from our entitlement, we will call the `demisto.handleEntitlementForUser()` method as shown below.
```python
demisto.handleEntitlementForUser(incidentID=incident_id, guid=guid, email=user_email, response=reply, taskID=task_id)
```

When the `demisto.handleEntitlementForUser()` function is called, the XSOAR server will close the given task in the given incident with the response which was provided.