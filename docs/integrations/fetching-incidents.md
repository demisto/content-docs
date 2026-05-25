---
id: fetching-incidents
title: Fetching Incidents
---

Cortex XSOAR pulls events from third party tools and converts them into incidents using the ***fetch-incidents*** command.  

This topic provides:  
- A description of the fetching command and parameters
- A description of creating fetched incidents in Cortex XSOAR
- An explanation of how missing incidents are fetched with generic lookback methods
- Troubleshooting tips

## fetch-incidents Command
The ***fetch-incidents*** command is the function that Cortex XSOAR calls to import new incidents. It is triggered by the *Fetches incidents* parameter in the integration configuration. It is not necessary to configure the ***fetch-incidents*** command in the integration settings.

When you select the *Fetch incidents* parameter in the integration configuration, you should also configure the *incidentFetchInterval* parameter (displayed as *Incidents Fetch Interval* in the integration configuration window). This controls how often the integration will perform a ***fetch_incidents*** command. The default is 1 minute.

![screen shot 2023-09-20](/doc_imgs/integrations/fetch-incidents.png)

Open the ***fetch-incidents*** command. Make sure the command is also referenced in the execution block.

```python
def fetch_incidents():
      # your implementation here


if demisto.command() == 'fetch-incidents':
      fetch_incidents()

```




## Last Run
The *demisto.getLastRun()* function retrieves the last previous run time.  
This helps avoid duplicate incidents by fetching only events that occurred since the last time the function was run.

```python
    # demisto.getLastRun() will returns an obj with the previous run in it.
    last_run = str(demisto.getLastRun())
```

**Note:**  
The value of *demisto.getLastRun()* is not stored between CLI command runs; it is only stored in the incident fetch flow on the server side. Therefore, if you print out the value of *demisto.getLastRun()* in the integration code, its value will appear as {}.

For debugging, you can save the value of *demisto.getLastRun()* to integration context, which does persist between CLI command runs. Alternatively, you can run the ***fetch_incidents()*** command twice within the same command run.

## First Run
When an integration runs for the first time, the last run time is not in the integration context.  
To set up the first run properly, use an ```if``` statement with a time that is specified in the integration settings.

It is best practice to specify how far back in time to fetch incidents on the first run. This is a configurable parameter in the integration settings.

Make sure that first_fetch parameter exist in the integration yml file.

## Query and Parameters

Queries and parameters enable filtering events.  
For example, you may want to import only certain event types into Cortex XSOAR. To do this, you need to query the API for only that specific event type. These are configurable parameters in the integration settings.

#### Example
The following example uses the **First Run** ```if``` statement and **query**.
```python
    # usually there will be some kind of query based on event creation date, 
    # or get all the events with id greater than X id and their status is New
    query = 'status=New'

    day_ago = datetime.now() - timedelta(days=1) 
    start_time = day_ago.time()
    if last_run and 'start_time' in last_run:
        start_time = last_run.get('start_time')

    # execute the query and get the events
    events = query_events(query, start_time)
```

### Fetch Limit 
The *Fetch Limit* parameter sets the maximum number of incidents to get per fetch command. To maintain an optimal load on Cortex XSOAR we recommend setting a limit of 200 incidents per fetch.  
**Note:**
Make sure that the max_fetch parameter exist in the integration yml file and it has a default value.
If you enter a larger number or leave *Fetch Limit* blank, the **Test** button will fail.

## Create an Incident
Incidents are created by building an array of incident objects. These objects must contain:
- The ```name``` of the incident
- When the incident ```occurred``` 
- The ```rawJSON``` key for the incident

Recommended to include:
- ```details``` - a brief description of the incident.
- ```dbotMirrorId``` - the ID of the incident in the third-party product (see [Fetch History](https://xsoar.pan.dev/docs/integrations/fetching-incidents#fetch-history)).

#### Example

```python
# convert the events to Cortex XSOAR incident 
events = [
  {
      'name': 'event_1',
      'create_time': '2019-10-23T10:11:00Z',
      'event_id': 100
  }
]
    
incidents = []
for event in events:
    incident = {
        'name': event['name'],        # name is required field, must be set
        'occurred': event['create_time'], # must be string of a format ISO8601
        'dbotMirrorId': str(event['event_id']),  # must be a string
        'rawJSON': json.dumps(event)  # the original event, this will allow mapping of the event in the mapping stage. Don't forget to `json.dumps`
    }
    incidents.append(incident)
```

### rawJSON
The ```rawJSON``` key in the incident field enables event mapping. Mapping is how an event gets imported into Cortex XSOAR and enables you to choose which data from the event is to be mapped to Cortex XSOAR fields.

#### Example

```python
incident = {
    'name': event['name'],        # name is required field, must be set
    'occurred': '2019-10-23T10:00:00Z', # occurred is optional date - must be string of a format ISO8601
    'rawJSON': json.dumps(event)  # set the original event to rawJSON, this will allow mapping of the event. Don't forget to `json.dumps`
}
```

### Set Last Run
When the last events are retrieved, you need to save the new last run time to the integration context. This timestamp will be used the next time the ***fetch-incidents*** function runs.  
**Notes:**
- When setting *demisto.setLastRun*, the values of the dictionary must be type **string**.  
- We recommend using the time of the most recently created incident as the new last run.
- If there is an error pulling incidents with ***fetch-incidents***, *demisto.setLastRun* will not execute.

```python
demisto.setLastRun({
    'start_time': timestamp_to_datestring(last_incident['time'])
})
```

### Send the Incidents to Cortex XSOAR
When all of the incidents are created, the *demisto.incidents()* function returns an array of incidents in Cortex XSOAR.  
This is similar to the *demisto.results()* function, but is used exclusively to handle incident objects.

#### Example

```python
# this command will create incidents in Cortex XSOAR
demisto.incidents(incidents)
```

If there are no incidents to return,  *demisto.incidents()* returns an empty list.
```python
# returning an empty list will keep the status as ok but no new incidents are created.
demisto.incidents([])
```

## Fetch History
In XSOAR versions 6.8 and above, it is possible to observe the results of the last **fetch-incidents**/**fetch-indicators** runs using the Fetch History modal. For more details, visit the [Fetch History](https://xsoar.pan.dev/docs/reference/articles/troubleshooting-guide#fetch-history) documentation.

When implementing a **fetch-incidents** command, in some cases we can populate extra data for the following columns in the modal:

1. **Message** - In long-running integrations, the info/error message given in `demisto.updateModuleHealth()` will be displayed in the **Message** column. Use the *is_error* boolean argument of this method to determine the message type. For example:
   
   ```python
   demisto.updateModuleHealth("Could not connect to client.", is_error=True)
   ```
   The above line will produce a new record in the modal, and its **Message** value will be `Error: Could not connect to client.`.

2. **Source IDs** - If incidents on the third-party product have IDs, it is possible to display them in the **Source IDs** column by adding the `dbotMirrorId` field as part of the incident dictionary. For example:
   
   ```python
   demisto.incidents([
       {"name": "This is an incident.", "dbotMirrorId": "123"},
       {"name": "This is another incident.", "dbotMirrorId": "124"},
   ])
   ```
   The above will produce a new record in the modal, and its **Source IDs** value will be `123, 124`.
   
   **Note:** the population of the fetch history information occurs **before** the classification, therefore this field must be defined at the integration code level rather than the classification and mapping level.

## Fetch Missing Incidents with Generic Lookback Methods
This advanced feature uses generic lookback methods for fetching missing incidents because of indexing issues in the 3rd party product. For more information [click here](https://xsoar.pan.dev/docs/integrations/fetch-incidents-lookback).

## Fetch Best Practices
The following best practices expand on the basic structure shown above. They aim to keep your fetch flow safe to re-run, easy to unit test, and predictable when something goes wrong.

### Structuring the Fetch Function
- Keep all fetch logic inside a dedicated function (for example, `fetch_incidents_command()`), and let `main()` simply dispatch to it. This keeps `main()` clean and makes the fetch function easy to test.
- The fetch function is the natural owner of the full cycle: reading `demisto.params()` and `demisto.getLastRun()`, calling the API, deduplicating results, sending them to Cortex XSOAR with `demisto.incidents()` (or `send_events_to_xsiam()` for event collectors), and writing the new state back with `demisto.setLastRun()`.
- Internal helpers (pagination, deduplication, parsing, etc.) work better when they take their inputs as explicit arguments rather than reaching for `demisto.*` globals — it makes them straightforward to unit test in isolation.

### Designing the Client Methods Used by Fetch
- Client methods used by fetch should accept at least `start_time`, an optional `end_time`, and `limit`. This keeps the calling code simple and reusable.
- Return the raw API response (a list of dicts) and leave the XSOAR-specific transformation (building the incident dict, mapping severities, etc.) to the fetch function. Mixing the two concerns makes the client harder to reuse from other commands.
- If the API uses pagination, prefer to handle it inside the client method and return the aggregated results, so the fetch function doesn't have to know about page tokens or offsets.

### Inheriting from the Base API Modules
- When starting a new integration, consider inheriting from `BaseContentApiModule` and `ContentClientApiModule`. They already implement authentication, HTTP handling, parameter parsing, and retries, so you don't have to write that boilerplate again.

### Pagination

#### Loop Safety
A pagination loop is essentially "fetch a page → ask for the next page → repeat". Without a stop condition you can easily get an infinite loop, especially if the API misbehaves. A safe loop should:

- Have a hard upper bound — either the user-configured `max_fetch` or a constant such as `MAX_PAGES = 100` — so it can never run forever.
- Stop as soon as the API returns no more results, or the pagination token comes back empty/`None`.
- Stop once you've accumulated enough items to satisfy `max_fetch`, even mid-page. Save the pagination state in `lastRun` and resume from there on the next cycle.

#### When the API Has More Events Than `max_fetch` Per Cycle
Some APIs produce more events per fetch interval than you can reasonably pull in one cycle. In that case, pick one of the two strategies below and stick with it for the whole flow — mixing them tends to cause subtle gaps or duplicates.

**Cursor-based (preferred when the API exposes a stable cursor):**
1. Fetch up to `max_fetch` items and save the `next_token` in `lastRun`.
2. On the next cycle, resume from `next_token` instead of re-querying from the beginning.
3. Only advance the base timestamp (`last_fetch_time`) once `next_token` is empty for the current time window.

**Timestamp + dedup (when no cursor is available):**
1. Fetch up to `max_fetch` items ordered by timestamp ascending.
2. Save `last_fetch_time` (the timestamp of the last item you returned) and `seen_ids` (the IDs of all items sharing that timestamp) in `lastRun`.
3. On the next cycle, query from `last_fetch_time` *inclusive* and filter out anything already in `seen_ids` (see [Avoiding Duplicates](#avoiding-duplicates)).

### What to Store in `lastRun`

#### Useful State Fields
Your `lastRun` should carry just enough state to resume fetching cleanly. The most common fields are:

| Field | Purpose | Example |
|-------|---------|---------|
| `last_fetch_time` | Timestamp of the last successfully fetched item (ISO 8601 UTC) | `"2024-03-15T10:30:00Z"` |
| `seen_ids` | IDs of items fetched in the last timestamp window, used for dedup | `["alert-123", "alert-124"]` |
| `next_token` | Pagination cursor for cross-cycle pagination | `"eyJwYWdlIjogMn0="` |
| `last_id` | Last processed item ID, for APIs that paginate by ID | `"alert-124"` |

#### Avoiding Duplicates
APIs that sort by timestamp will sometimes return items with the exact same timestamp across two fetch cycles. A simple way to handle it:

1. Remember the IDs of all items that share the most recent timestamp by storing them in `seen_ids`.
2. On the next fetch, query from that same timestamp (inclusive) and skip anything you already have in `seen_ids`.
3. Once the timestamp moves forward, clear `seen_ids` and start fresh.
4. If items don't have a native unique ID, you can derive one — for example by hashing the item's key fields with `hashlib.sha256(json.dumps(item, sort_keys=True).encode()).hexdigest()`.
5. Save the updated state back to `lastRun`.

#### Keeping `lastRun` Small and JSON-Friendly
- Treat `lastRun` as a place for *metadata* (timestamps, IDs, tokens) — not for the events or incidents themselves. Putting the fetched events list into `lastRun` is a common source of state-size issues. If you find yourself doing that, the fix is usually to send the events out via `demisto.incidents()` / `send_events_to_xsiam()` and only keep small pointers (timestamps, IDs, tokens) in the state.
- Keep `seen_ids` from growing without bound. A practical rule is to trim it once it goes past something like 1000 entries, or switch to a timestamp-only strategy with a small look-back window.
- Stick to JSON-safe types (strings, numbers, lists). Avoid `datetime` objects, sets, or anything that doesn't survive a round-trip through `json.dumps`.

#### First-Run Defaults
- For **fetch-incidents**, when `lastRun` is empty fall back to the user-configured `first_fetch` parameter (commonly `"3 days"`).
- Parse `first_fetch` with `dateparser` or `arg_to_datetime` so users can write it as `"3 days"`, an ISO date, etc.

### Shaping the Incident Dict

#### Required Fields
Each fetched item should be turned into an incident dict that XSOAR knows how to display and map:

| XSOAR Field | Source | Notes |
|-------------|--------|-------|
| `name` | Alert title / event summary | Use something a human can read at a glance, not an opaque ID |
| `occurred` | Event timestamp | ISO 8601 UTC string |
| `severity` | Vendor severity | Map to the XSOAR scale (see [Mapping Severity](#mapping-severity)) |
| `type` | Incident classification | Use the configured `incidentType` or derive it from the event |
| `rawJSON` | Full raw API response | `json.dumps(raw_item)` — keep all original fields so mappers and classifiers have everything to work with |

#### Mapping Severity
- Use the `IncidentSeverity` enum from `CommonServerPython` instead of hardcoding numeric severity values — it makes the mapping self-documenting and resilient to enum changes.
- Provide a sensible default (typically `LOW`) for severity values the vendor sends that you don't recognize.
- Compare severity strings case-insensitively — vendors are inconsistent about casing.

#### Normalizing Timestamps
- Store timestamps in `occurred`, `lastRun`, or context outputs as ISO 8601 UTC strings. This avoids timezone confusion later.
- Parse vendor timestamps with `dateparser.parse()` or `arg_to_datetime()`, then format with `.isoformat()` or `datetime.strftime()`.
- If the vendor returns epoch seconds or milliseconds, convert to a `datetime` with `tz=timezone.utc` before formatting.

### Respecting `max_fetch`
- Make sure `max_fetch` is defined in the integration YAML with a reasonable `defaultvalue`.
- Read it once at the start of the fetch function and treat it as the upper bound for the whole cycle.
- Stop accumulating results as soon as you hit it, even if the current page still has items left — those will come back on the next cycle.

### Recovering from Partial Failures
A fetch cycle may partially succeed: you fetch a couple of pages, then the API times out. The friendliest behavior in that case is:

- Return the items you did manage to fetch instead of throwing them away.
- Update `lastRun` to point at the last item you successfully processed, so the next cycle resumes from there rather than re-fetching from the original start time.
- Log the failure with `demisto.error()` so it's easy to see what happened.

### Logging Inside the Fetch Flow

#### What to Avoid Logging
Logs from fetch flows tend to end up in shared troubleshooting bundles, so it's worth being careful about what ends up there:

- Don't log raw API response bodies — they can be huge and often contain sensitive data.
- Don't log credentials, tokens, API keys, or authorization headers, at any level.
- Don't log full incident or event payloads. Counts and IDs are usually enough to diagnose problems.
- Don't log PII such as end-user emails, usernames, or IP addresses.

#### Prefixing Log Messages
Prefixing each log message with a short tag for the subsystem makes logs much easier to filter later. A common convention:

| Prefix | When to use |
|--------|-------------|
| `[Fetch]` | Start/end of a fetch cycle, overall status |
| `[HTTP Call]` | Outgoing HTTP requests and responses |
| `[HTTP Error]` | HTTP-level failures (status codes, timeouts) |
| `[Pagination Loop]` | Page iteration progress, thresholds, cursor state |
| `[Dedup]` | Deduplication filtering, skipped/retained counts |
| `[Token Request]` | OAuth or token acquisition and refresh |
| `[Token Cache]` | Token cache hits, misses, expiry checks |
| `[Config]` | Parameter validation and configuration loading |
| `[Test Module]` | `test-module` connectivity checks |
| `[Date Helper]` | Date parsing and normalization |

## Troubleshooting
To troubleshoot ***fetch-incident***, execute `!integration_instance_name-fetch debug-mode=true` in the Playground to return the incidents.  

<img src="/doc_imgs/integrations/70272523-0f34f300-17b1-11ea-89a0-e4e0e359f614.png" width="480"></img>
