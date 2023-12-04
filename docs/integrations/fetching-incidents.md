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

## Troubleshooting
To troubleshoot ***fetch-incident***, execute `!integration_instance_name-fetch debug-mode=true` in the Playground to return the incidents.  

<img src="/doc_imgs/integrations/70272523-0f34f300-17b1-11ea-89a0-e4e0e359f614.png" width="480"></img>
