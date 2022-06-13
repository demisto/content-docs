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
The ***fetch-incidents*** command is the function that Cortex XSOAR calls every minute to import new incidents. It is triggered by the *Fetches incidents* parameter in the integration configuration. It is not necessary to configure the ***fetch-incidents*** command in the integration settings.

![screen shot 2019-01-07 at 15 35 01](/doc_imgs/integrations/50771147-6aedb800-1292-11e9-833f-b5dd13e3507b.png)

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
This advanced feature uses generic lookback methods for fetching missing incidents.

### Use case
During a ***fetch-incidents*** run, some edge-case scenarios may cause missing incidents from the third-party product.  
The most common scenarios are:
* Indexing issues in the product: For example, if incident A was created before incident B and only B was indexed, ***fetch-incidents*** will fetch only B and not A. If A was indexed after the fetch was called, the next fetch will fetch only from the created time of B.
* An update in the incident information: Some implementations of ***fetch-incidents*** use a query filter to fetch only specific incidents. If initially an incident did not match the query (meaning, it was not fetched) but at some point was updated so that it now matches the query, ***fetch-incidents*** will not pull the updated incident because the time to fetch it already passed.

### Solution
The *look_back* parameter enables configuring how far back in time (in minutes) ***fetch-incidents*** will look to get the incidents that were created a while ago but indexed a few minutes ago.  
In addition, the **LastRun** object stores the following fields to be used by the lookback methods:
- **time** - The time to fetch the next fetch call (as in a regular fetch).
- **limit** - The maximum number of incidents retrieved in the next fetch. If the current fetch run has the same start_time as the last fetch (determined in **get_fetch_run_time_range()**), this field will be increased by the limit instance parameter value, and then incidents retrieved in the last fetch will be filtered out.
- **found_incident_ids** - The IDs of incidents fetched in previous runs. Used for filtering duplicates in the next runs.

### Lookback Methods
Lookback is implemented using the following generic methods. For more information about lookback generic methods, see [CommonServerPython](https://xsoar.pan.dev/docs/reference/api/common-server-python).

- **get_fetch_run_time_range()** - Using the last run object and other parameters, this method calculates and retrieves the time range in which to fetch.  
   If the *look_back* parameter is defined, then the start time will always be greater than or equal to `now - look_back`.

- **filter_incidents_by_duplicates_and_limit()** - After getting the incidents using the third-party API call, you need to filter out the duplicate incidents.  
From the example above, after incident A is indexed the next fetch will get incidents A and B, but B must be filtered out since it was already fetched.  
**Note:**
If after filtering duplicates you have more incidents than the limit, ***fetch-incidents*** will get only up to the limit number of incidents.

- **update_last_run_object()** - Updates the existing last run object.  
The function updates the found IDs from the **get_found_incident_ids** function and also updates the new time and limit from the  **create_updated_last_run_object** function and returns the updated last run object.

### Helper Methods  

The following helpers are used in the above lookback methods, and should not be used when implementing ***fetch-incidents*** in the integration.

- **get_latest_incident_created_time()** - Given a list of incidents and the created time field, this function will return the latest incident created time.

- **remove_old_incidents_ids()** - Removes old incident IDs from the last run object to avoid overloading.

- **get_found_incident_ids()** - Returns a list of the new fetched incident IDs. This is saved in the last run object and used to filter duplicates in the next ***fetch-incidents*** call.

- **create_updated_last_run_object()** - Creates a new last run object with a new time and limit for the next fetch.


### Example Fetch with Lookback
```python
def fetch_incidents(params: dict):

    incidents = []

    fetch_limit_param = params.get('limit')
    look_back = int(params.get('look_back', 0))
    first_fetch = params.get('first_fetch')
    time_zone = params.get('time_zone', 0)

    last_run = demisto.getLastRun()

    # If the start time in the current fetch is the same as the start time in the previous fetch, the fetch_limit may be different from the fetch_limit_param.
    fetch_limit = last_run.get('limit') or fetch_limit_param

    # It's important to get here the end_fetch_time to pass it into the update_last_run_object function.
    start_fetch_time, end_fetch_time = get_fetch_run_time_range(last_run=last_run, first_fetch=first_fetch,
                                                                look_back=look_back, timezone=time_zone)

    # Here you insert functions for building the query and sending the API call to get the incidents. For example:
    query = build_query(start_fetch_time, end_fetch_time, fetch_limit)
    incidents_res = get_incidents_request(query)

    incidents = filter_incidents_by_duplicates_and_limit(incidents_res=incidents_res, last_run=last_run,
                                                         fetch_limit=fetch_limit_param, id_field='incident_id')

    last_run = update_last_run_object(last_run=last_run, incidents=incidents, fetch_limit=fetch_limit_param,
                                      start_fetch_time=start_fetch_time, end_fetch_time=end_fetch_time, look_back=look_back, 
                                      created_time_field='created', id_field='incident_id')

    demisto.incidents(incidents)
    demisto.setLastRun(last_run)
```

### Notes:
- Fetching incidents is flexible and you can use the various functions according to your needs.
- You can also use the generic methods for regular ***fetch-incidents*** without lookback.
- If the *look_back* value is increased by *k* minutes, you may get duplicate incidents for the *k* minutes that overlap with the previous fetch.

## Troubleshooting
To troubleshoot ***fetch-incident***, execute `!integration_instance_name-fetch debug-mode=true` in the Playground to return the incidents.  

<img src="/doc_imgs/integrations/70272523-0f34f300-17b1-11ea-89a0-e4e0e359f614.png" width="480"></img>
