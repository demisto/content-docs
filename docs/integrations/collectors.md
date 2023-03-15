---
id: event-collectors
title: Event Collection Integrations
tags: [xsiam, integration, collector]
---
Server version 6.8.0 adds support for Event Collection integrations for Cortex XSIAM. Collection integrations allow fetching events and logs from external products, for example OKTA,
Jira and so on.

An example Collection integration can be seen [here](https://github.com/demisto/content/tree/master/Packs/Jira/Integrations/JiraEventCollector).

Collection integrations are developed the same as other integrations. They provide a few extra configuration parameters and APIs.


## Naming Convention
Collection Integration names (`id`, `name` and `display` fields) should end with the words **Event Collector**. This consistent naming convention ensures that users can easily understand what the integration is used for.

## Required Keys
- Every Event Collection integration should have the `isfetchevents` key in the integration YAML file, to indicate that this integration is a Collection integration.
- A Collection integration's YAML file must have the `fromversion: 6.8.0` field. This is because Collection integrations are only supported from server version 6.8.0 and onwards.
- Since Collection integrations are only supported in XSIAM make sure that your YML file includes the `marketplaces` key with the `-marketplacev2` value.

Example:
```yml
script:
  isfetchevents: true
fromversion: 6.8.0
marketplaces:
- marketplacev2
```

## Commands
Every Collection integration will at minimum support these three commands:
- `test-module` - this is the command that is run when the `Test` button in the configuration panel of an integration is clicked.
- `<product-prefix>-get-events` - where `<product-prefix>` is replaced by the name of the Product or Vendor source providing the events. So for example, if you were developing a Collection integration for Microsoft Intune, this command might be called `msintune-get-events`. This command should fetch a limited number of events from the external source and display them in the war room.
- `fetch-events` - this command will initiate a request to the external product chosen endpoint(s) using the relevant chosen params, and send the fetched events to the XSIAM database. If the integration instance is configured to `Fetch events`, then this is the command that will be executed at the specified `Events Fetch Interval`.

## API Command: `send_events_to_xsiam()`
Call the `send_events_to_xsiam()` function from `CommonServerPython` when the `fetch-events` command is executed. The function expects the following arguments:
- `events` - The events to send to the XSIAM server. Should be of the following:
  1. `List[str]` or `List[Dict[str, Any]]` where each string or `Dict` represents an event.
  2. `str` containing raw events separated by new lines.
- `vendor` - The vendor represented by Collection integration.
- `product` - The specific product integrated in the given Collection integration.
- `data_format` - Should only be filled in case the `events` parameter contains a string in the format of `leef` or `cef`. In other cases the `data_format` will be set automatically.

Let's look at an example `main()` function from a Collection integration:
```python
def main():
    params = demisto.params()

    client = Client(params.get('insecure'),
                    params.get('proxy'))

    command = demisto.command()
    demisto.info(f'Command being called is {command}')
    # Switch case
    try:
        if demisto.command() == 'fetch-events':
            events, last_run = fetch_events_command(client)
            # we submit the indicators in batches
            send_events_to_xsiam(events=events, vendor='MyVendor', product='MyProduct')
        else:
            results = get_events_command(client)
            return_results(results)
    except Exception as e:
        raise Exception(f'Error in {SOURCE_NAME} Integration [{e}]')
```
Notice: 
- You should always pass the `events` to the `send_events_to_xsiam()` function, also in cases when no events were fetched. This is important as the `send_events_to_xsiam()` function also updates the UI for the number of events fetched which could also be 0. Don't be troubled, in such cases the empty data will not be sent forward to the Dataset.
- In the given example we assume the events are **not** in a `cef` or `leef` formats and therefore the `data_format` argument is not used.
- In cases where `events` consist of multiple types with differing structures, i.e. within `fetch-events` we're calling two different API endponts, we call `send_events_to_xsiam()` with an aggregated list of events from both endpoints. For example, if we have `detections: List[Dict[str, Any]]` and `audits: List[Dict[str, Any]]`, we would send them as so:
 
  ```python
  audits, detections, last_run = fetch_events_command(client)
  send_events_to_xsiam(events=audits + detections, vendor='MyVendor', product='MyProduct')
  ```

For more info on the `send_events_to_xsiam()` function visit the [API reference](https://xsoar.pan.dev/docs/reference/api/common-server-python#send_events_to_xsiam).


## Creating Parsing Rules

When developing an event collector, we need to set the [Parsing Rules](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Administrator-Guide/Create-Parsing-Rules) within the collector code.

The most common parsing rule is the `_time` system property which indicates the event time from the remote system. For example, if we use the following events as an example:


```json
 {
    "id": "1234",
    "message": "New user added 'root2'",
    "type": "audit",
    "op": "add",
    "result": "success",
    "host_info": {
      "host": "prod-01",
      "os": "Windows"
    },
    "created": "1676764803"
  }
```

 We see that the `created` event property is a `str` representation of a timestamp (without milliseconds). However, The `_time` system property expects the result to be an `str` in format `%Y-%m-%dT%H:%M:%S.000Z`. So we can can transform it using the [`timestamp_to_datestring`](https://xsoar.pan.dev/docs/reference/api/common-server-python#timestamp_to_datestring) function from `CommonServerPython`.


```python
from datetime import datetime
from CommonServerPython import *

#  ...
  events: List[Dict[str, Any]] = get_events()

  for event in events:
    event["_time"] = timestamp_to_datestring(float(event.get("created")) * 1000)

# ...
```

## Seeing the Events

After the events are received by XSIAM, they will be stored in a Dataset in the structure of `<vendor>_<product>_raw`. In case it's the first time we fetch events, this Dataset will be created. To manage the Datasets, you can visit the [Dataset Management](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Administrator-Guide/Dataset-Management).


In order to see the events, visit the [Query Builder](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Administrator-Guide/Query-Builder).

In our example, to view all events, we would use the following [XQL search](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Administrator-Guide/XQL-Search):
```xql
dataset = MyVendor_MyProduct_raw
```

If all was done correctly you should be seeing the events sent by your integration in the table of results, like this:

![debug test](/doc_imgs/integrations/XSIAM_XQL_query.png)


## Creating Data Modeling Rules

Now that we see the events in the Dataset, we need to create Data Modeling rules and to add them to the Content Pack.

Creating Data Modeling rules entails 2 steps that should be done sequentially:

### 1. Mapping Event to Data Modeling Rules

At this point, we have a Dataset of raw events. We will use the Dataset to [create Data Modeling rules](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Administrator-Guide/Create-Data-Model-Rules). 

The Data Model definition begins with:

```
[MODEL: dataset="MyVendor_MyProduct_raw"]
```

Next, we want to map the raw event JSON to XSIAM system fields. Completion of this mapping of the XDM (XSIAM Data Model) system fields adds out-of-the-box enrichment.

In our example, let's say that we have the following events we sent to XSIAM and are currently in the Dataset `MyVendor_MyProduct_raw`:

```json
[
  {
    "id": "1234",
    "message": "New user added 'root2'",
    "type": "audit",
    "op": "add",
    "result": "success",
    "host_info": {
      "host": "prod-01",
      "os": "Windows"
    },
    "created": "1676764803"
  },
  {
    "id": "1235",
    "message": "User 'root2' delete failed, permission denied",
    "type": "audit",
    "op": "delete",
    "result": "failed",
    "host_info": {
      "host": "prod-01",
      "os": "Windows"
    },
    "created": "1676764823"
  },
  {
    "id": "1236",
    "message": "User 'root2' logged in",
    "type": "authentication",
    "op": "login",
    "result": "success",
    "host_info": {
      "host": "prod-01",
      "os": "Windows"
    },
    "created": "1676764834"
  },
  {
    "id": "1237",
    "message": "User 'root2' sent async request",
    "type": "request",
    "op": "request",
    "result": "pending",
    "host_info": {
      "host": "prod-01",
      "os": "Windows"
    },
    "created": "1676764903"
  }
]
```

We would like to map each one of these JSON keys to XDM system fields. To find the relevant XDM system fields (which are prefixed with `XDM_CONST`), we can either use the auto-completion offered by the Data Rules Editor or we can search for the fields in the [XDM field reference](https://docs-cortex.paloaltonetworks.com/r/XSIAM-Data-Model).

In our example, the Data Modeling rules will look like this:

```sql
[MODEL: dataset="MyVendor_MyProduct_raw"]
ALTER
  xdm.event.id = id,
  xdm.event.description = message,
  xdm.event.type = type,
  xdm.event.operation = if(
    op = "add", XDM_CONST.OPERATION_TYPE_CREATE,
    op = "delete", XDM_CONST.OPERATION_TYPE_MODIFY,
    op = "login", XDM_CONST.OPERATION_TYPE_LOGIN,
    op = null, null, to_string(op)
  ),
  xdm.event.outcome = if(
    result = "success", XDM_CONST.OUTCOME_SUCCESS,
    result = "failed", XDM_CONST.OUTCOME_FAILED,
    result = null, null, to_string(result)
  ),
  xdm.event.is_completed = if(result != pending),
  xdm.source.hostname = json_extract_scalar(host_info, "$.host"),
  xdm.source.os_family = if(
    json_extract_scalar(host_info, "$.os") = "Windows", XDM_CONST.OS_FAMILY_WINDOWS,
    -- rest of conditions for operating systems
    json_extract_scalar(host_info, "$.os") = null, null, to_string(json_extract_scalar(host_info, "$.os"))
  )
```

A few things are worth reviewing from the above rules:

- To map the `op` field to the appropriate XDM system field, in this case the `OPERATION_TYPE`, we use the [XQL `if` function](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-XQL-Language-Reference/if). We're basically setting the `xdm.event.operation` field to `XDM_CONST.OPERATION_TYPE_CREATE` if the value of the `op` field in the raw response is `add`.
- When we use an `if` function, the best practice is to have an additional argument which will be used as default which has the `field_name = null, null, to_string(field_name)` structure. We can see an example of this when defining the `op`, `result` and `os_family` fields.
- When we want to access nested fields from within the JSON, we use the [`json_extract_scalar` function](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-XQL-Language-Reference/json_extract_scalar).
- See [XQL Functions Reference](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-XQL-Language-Reference/XQL-Functions-Reference) for more information about other functions.

If at any time the XDM rules are incorrect, the editor will notify you of the error.

After we finish creating the XDM rules, we can construct a new [XQL query](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM/Cortex-XSIAM-Administrator-Guide/XQL-Search) with the XDM rules we specified:

```sql
datamodel dataset in("MyVendor_MyProduct_raw") |
FIELDS
  xdm.event.id,
  xdm.event.description,
  xdm.event.type,
  xdm.event.outcome,
  xdm.event.is_completed,
  xdm.source.hostname,
  xdm.source.os_family
```

### 2. Adding Data Modeling Rules to Content Pack

After we finished creating the XDM rules and verifying that our XQL query provides us with the expected result set, we need to export the XDM rules to our Content Pack.

We need to first create a new directory named `ModelingRules/MyVendorEventCollector` inside our Content Pack, e.g. `content/Packs/MyVendor/ModelingRules/MyVendorEventCollector`. This folder will hold 3 files within it:

- `MyVendorEventCollector_1_3.xif`: This file will hold the actual XDM rule we created in the Data Model Editor. We can copy and paste it directly into this file.
- `MyVendorEventCollector_1_3.yml`: This file contains some additional information about the Event Collector. It will have the following structure:

  ```yaml
  fromversion: 6.10.0
  id: MyVendor_Event_Collector
  name: MyVendor Event Collector
  rules: ''
  schema: ''
  tags: MyVendor, Events
  ```

- `MyVendorEventCollector_1_3_schema.json`: This file contains the fields that came directly from the raw response and were used in the development of the XDM rules. The file has the following structure:

  ```json
  {
    "MyVendor_MyProduct_raw": {
      "field_1": {
        "type": "string|int|datetime", // Specify whether the field is a string, an integer or a datetime
        "is_array": true|false // Specify whether the field is an array/list of types.
      },
      "field_2": {
        "type": "string|int",
        "is_array": true|false
      }
      // ...
    }
  }
  ```
