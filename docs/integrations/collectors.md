---
id: event-collectors
title: Event Collection Integrations
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
- `fetch-events` - this command will initiate a request to the external product chosen endpoint(s) using the relevant chosen params, and send the fetched events to the XSIAM database. If the integration instance is configured to `Fetch evnts`, then this is the command that will be executed at the specified `Events Fetch Interval`.

## API Command: send_events_to_xsiam()
Use the `send_events_to_xsiam()` function when the `fetch-events` command is executed. With the following arguments:
- `events` - The events to send to the XSIAM server. Should be of the following:
  1. List of strings or dicts where each string or dict represents an event.
  2. String containing raw events separated by new lines.
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
- You should always path the `events` to the `send_events_to_xsiam()` function, also in cases when no events were fetched. This is important as the `send_events_to_xsiam()` function also updates the UI for the number of events fetched which could also be 0. Don't be troubled, in such cases the empty data will not be sent forward to the DataBase.
- In the given example we assume the events are **not** in a `cef` or `leef` formats and therefore the `data_format` argument is not used.
- `send_events_to_xsiam()` function will work only if the integration is a system integration. The function will fail if it will be called from a custom integration.

Fore more info on the `send_events_to_xsiam()` function visit the [API reference](https://xsoar.pan.dev/docs/reference/api/common-server-python#send_events_to_xsiam).
   
## Vendor and Product Constants
Define `VENDOR` and `PRODUCT` once as constants at the top of the integration file and reuse them whenever you call `send_events_to_xsiam()` (or any helper that needs them). It keeps the values consistent across the code and makes it trivial to rename the dataset later.

```python
VENDOR = "myvendor"
PRODUCT = "myproduct"
```

## Shaping the Event Dict
Before passing events to `send_events_to_xsiam()`, make sure each event dict carries the fields XSIAM expects:

| Field | Purpose |
|-------|---------|
| `_time` | Event timestamp as an ISO 8601 UTC string. XSIAM uses this as the canonical event time. |
| `source_log_type` | A log-type identifier so XSIAM can categorize events correctly. Add it whenever the collector fetches more than one type of event. |
| The original fields | Keep the raw vendor fields as-is so XSIAM parsing rules and queries have everything to work with. |

## First Fetch for Event Collectors
When there's no `lastRun` yet (the very first fetch), the safest default for an event collector is "now minus one minute":

```python
from datetime import datetime, timedelta, timezone

first_fetch = datetime.now(tz=timezone.utc) - timedelta(minutes=1)
```


## Additional Fetch Best Practices
Event collectors share most of their fetch patterns with `fetch-incidents` — bounded pagination, cross-cycle pagination strategies, what to store in `lastRun`, deduplication, partial-failure recovery, and logging conventions. See [Fetch Best Practices](fetching-incidents#fetch-best-practices) for the full write-up.

## Seeing the data
In order to ses the events sent by the `send_events_to_xsiam()` function, in your XSIAM instance:
1. Go to the left toolbar and navigate to: **Incident response** > **Investigation** > **Query BuilderUnder**. 
2. Click the `XQL Search` button.
3. In the query builder screen type the following:
```xql
dataset = MyVendor_MyProduct_raw
```
If all was done correctly you should be seeing the events sent by your integration in the table of results, like this:
![debug test](/doc_imgs/integrations/XSIAM_XQL_query.png)
