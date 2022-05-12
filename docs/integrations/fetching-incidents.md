---
id: fetching-incidents
title: Fetching Incidents
---

Cortex XSOAR can pull events from 3rd party tools and convert them into actionable incidents. There are a few important parts that are necessary to keep in mind while doing so and they are outlined below.

## The `fetch-incidents` Command
The `fetch incidents` command is the function that Cortex XSOAR calls every minute to import new incidents and is triggered by the "Fetches incidents" parameter in the integration configuration. It is not necessary to configure the `fetch-incidents` command in the Integration Settings.

![screen shot 2019-01-07 at 15 35 01](/doc_imgs/integrations/50771147-6aedb800-1292-11e9-833f-b5dd13e3507b.png)


Let's walk through the example below:

First we open up the command called "fetch-incidents". Make sure that the command is also referenced in the execution block as well.

```python
def fetch_incidents():
      # your implementation here


if demisto.command() == 'fetch-incidents':
      fetch_incidents()

```

## Last Run
`demisto.getLastRun()` is the function that retrieves the previous run time. To avoid duplicating incidents, it's important that Cortex XSOAR only fetches events that occurred since the last time the function was run. This helps avoid duplicate incidents.

```python
    # demisto.getLastRun() will returns an obj with the previous run in it.
    last_run = str(demisto.getLastRun())
```
Note that the value of `demisto.getLastRun()` is not stored in between CLI command runs, but only in the incident fetch flow on the server side. Therefore, if you print out the value of `demisto.getLastRun()` in the integration code, its value will appear as `{}`.

For debugging, you can save the value of `demisto.getLastRun()` to integration context, which does persist in between CLI commmand runs, or run the `fetch_incidents()` function twice within the same command run.

## First Run
When an integration runs for the first time, the Last Run time will not be in the integration context. We catch this from failing by using an ```if``` statement. When the last run time is not specified, we use a time that is specified in the integration settings.

It is best practices to allow a customer to specify how far back in time they wish to fetch incidents on the first run. This is a configurable Parameter in the integration settings.

## Query and Parameters

Queries and parameters allow for filtering of events to take place. In some cases, a customer may only wish to import certain event types into Cortex XSOAR. In this case, they would need to query the API for only that specific event type. These should be configurable Parameters in the integration settings.

The following example shows how we use both **First Run** and the **Query** option:
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

## Fetch Limit 
An important parameter is the `Fetch Limit` parameter. Using this parameter the customer can enforce the maximum number of incidents to fetch per fetch command. In order to maintain optimal load on XSOAR we recommend enforcing a limit of 200 incidents per fetch. Notice that should a customer enter a larger number or a blank parameter the `Test` button should fail.


## Creating an Incident
Incidents are created by building an array of incident objects. These object all must contain the ```name``` of the incident, when the incident ```occurred``` as well as the ```rawJSON``` for the incident.

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
        'rawJSON': json.dumps(event)  # the original event, this will allow mapping of the event in the mapping stage. Don't forget to `json.dumps`
    }
    incidents.append(incident)
```

### rawJSON
When fetching incidents, it's important to include the ```rawJSON``` key in the incident field, which enables event mapping. Mapping is how an event gets imported into Cortex XSOAR, since it allows a customer to choose which data from the event to be mapped to their proper fields. An example of this is below:

```python
incident = {
    'name': event['name'],        # name is required field, must be set
    'occurred': '2019-10-23T10:00:00Z', # occurred is optional date - must be string of a format ISO8601
    'rawJSON': json.dumps(event)  # set the original event to rawJSON, this will allow mapping of the event. Don't forget to `json.dumps`
}
```

### Setting Last Run
When the last of the events have been retrieved, we need to save the new last run time to the integration context. This timestamp will be used the next time the ```fetch-incidents``` function is run.
When setting the last run object, it's important to know that the values of the dictionary must be of type `string`.  
We recommend using the time of the most recently created incident as the new last run.

```python
demisto.setLastRun({
    'start_time': timestamp_to_datestring(last_incident['time'])
})
```

When pulling incidents with ***fetch-incidents*** the ```setLastRun``` will not execute if there is an error with ***fetch-incidents***.

### Sending the Incidents to Cortex XSOAR
When all of the incidents have been created, we return the array of incidents by using the ```demisto.incidents()``` function. This is similar to the ```demisto.results()``` function, but is used exclusively to handle incident objects.

An example of it's usage is below:

```python
# this command will create incidents in Cortex XSOAR
demisto.incidents(incidents)
```

If you do not have any incidents to return then just return an empty list to ```demisto.incidents()``` function.
```python
# returning an empty list will keep the status as ok but no new incidents are created.
demisto.incidents([])
```

## Fetch History
In XSOAR Versions 6.8 and above, it is possible to observe the last **fetch-incidents**/**fetch-indicators** runs using the Fetch History modal. To view the modal, click the button with the history icon next to the Integration Instance settings.
<img src="/doc_imgs/incidents/fetchhistory.gif"></img>

The following fields are stored for each record:

1. **Pulled At** - The date and time when the fetch run was completed.
1. **Duration** - How long did the fetch take.
1. **Last Run** - The contents of the last run object.
1. **Message** - Depending on the fetch run status, will be one of the following:
   a. If successfully finished, how many Incidents/Indicators were pulled or dropped. If nothing was pulled or dropped, the message will be "Completed".
   a. In case of an error, the error details.
   a. In Long-Running Integrations, the info/error message forwarded to `demisto.updateModuleHealth()`. The *is_error* boolean argument of this method determines the message type.
1. **Source IDs** - If available, displays the Incident IDs as they appear in the 3rd-party product. The IDs are collected from Incidents that contain the `dbotMirrorId` field.
   Note: the `dbotMirrorId` field should be determined at the integration level rather than the mapping level.

### Server Configurations
| Key | Description | Default Value |
| --- | --- | --- |
| **fetch.history.size** | The amount of records stored for every instance. | 20 |
| **fetch.history.enabled** | Whether or not the feature is enabled. | true |

## Troubleshooting
For troubleshooting fetch-incident execute `!integration_instance_name-fetch` in the Playground, it should return the incidents.
<img src="/doc_imgs/integrations/70272523-0f34f300-17b1-11ea-89a0-e4e0e359f614.png" width="480"></img>
