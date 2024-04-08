---
id: mirroring_integration
title: Mirroring Integration
---

Mirroring integrations enable mirroring incidents, tickets, and cases from other services in Cortex XSOAR.  
For example, incidents, tickets, or cases from another Cortex XSOAR tenant, Cortex XDR, or ServiceNow can be mirrored in your Cortex XSOAR tenant. In addition, when mapping incident fields, mirroring enables you to pull the database schema from the integration, which brings all of the available fields into Cortex XSOAR. For more information about working with the schema, see the **Select schema** option described [here](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/6.12/Cortex-XSOAR-Administrator-Guide/Create-a-Mapper).

An example of a mirroring integration can be seen [here](https://github.com/demisto/content/tree/master/Packs/ServiceNow/Integrations/ServiceNowv2).

Mirroring integrations are developed the same as other integrations, with a few extra configuration parameters and APIs.

:::note 
For Cortex XSOAR versions 6.1.0 and earlier, once an incident field is changed manually within Cortex XSOAR, it is marked as "dirty" and will not be updated by the mirroring process in Cortex XSOAR throughout the incident lifecycle. However, if outbound mirroring is enabled, any changes to the incident in Cortex XSOAR will still be reflected in the external system.
:::

## Supported Server Version
Mirroring is supported from version 6.0.0 and later.


## Required Parameters
A mirroring integration's YAML file should have the following parameters (under the scripts section):
```yml
  isfetch: true
  ismappable: true
  isremotesyncin: true
  isremotesyncout: true
```
- *isfetch*: Determines if the integration fetches incidents.
- *ismappable*: Determines if the remote schema can be retrieved for this integration.
- *isremotesyncin*: Determines if mirroring from the third-party integration to Cortex XSOAR is supported.
- *isremotesyncout*: Determines if mirroring from Cortex XSOAR to the third-party integration is supported.


## Optional Parameters
A mirroring integration may include the following optional parameters:
- *incidents_fetch_query*: Determines the query to fetch incidents with.
- *comment_tag*, *work_notes_tag*, *file_tag*: Available tags for marking incident entries.
- *mirror_direction*: Determines which mirroring directions are available (options are None, Incoming, Outgoing and 'Incoming and Outgoing').
- *close_incident*: Checkbox that determines if mirrored Cortex XSOAR incidents will be closed when the corresponding incident is closed.
- *close_out*: Checkbox that determines if mirrored incidents will be closed when the corresponding Cortex XSOAR incident is closed.

## Commands
Use the following commands to implement a mirroring integration.  
**Note:**  
When mirroring both incoming and outgoing data, all the commands are required. For mirroring in only one direction, only some of the commands are required.  
- ***test-module***: Runs when the `Test` button in the configuration panel of an integration is clicked.
- ***fetch-incidents***: Fetches new incidents into Cortex XSOAR.
- ***get-modified-remote-data***: (Available from Cortex XSOAR version 6.1.0) Queries for incidents that were modified since the last update. If the command is implemented in the integration, the ***get-remote-data*** command will only be performed on incidents returned from this command, rather than on all existing incidents. This command is executed every 1 minute for each individual integration instance. 
If the command is not implemented, raise `NotImplementedError` so ***get-remote-data*** will be called instead. If the command fails to return an error entry with one of the following sub-strings: `API rate limit` or `skip update` (exact case), it signals to the server that there is an issue and it should not continue with the ***get-remote-data*** command. 
- ***get-remote-data***: Gets new information about the incidents in the remote system and updates *existing* incidents in Cortex XSOAR. If an API rate limit error occurs, this method should return an error with substring `"API rate limit"`, so that the sync loop will start from the failed incident.
This command is executed every 1 minute for each individual **incident** fetched by the integration.
- ***update-remote-system***: Updates the remote system with the information we have in the mirrored incidents within Cortex XSOAR. This command is executed whenever the individual incident is changed in Cortex XSOAR.
- ***get-mapping-fields***: Pulls the remote schema for the different incident types, and their associated incident fields, from the remote system. This enables users to map Cortex XSOAR fields to the 3rd-party integration fields in the outgoing mapper. This command is called when selecting the *Select schema* option in the *Get data* configuration in a classifier or a mapper.

## Special Server Configurations
- `sync.mirror.job.enable`: Enables / disables the mirroring job (default is **enabled**).
- `sync.mirror.job.delay`: The interval for the job in minutes (default is **1 minute**).
- `sync.mirror.job.delayAdvanced`: Used for demos so you do not have to wait a minute to show that mirroring happened. Overrides `sync.mirror.job.delay`, and if specified is the interval for the job in seconds.   

## Implement Mirroring Functions
You can implement the following functions, using the classes described below, which are globally available through the CommonServerPython file.

### get-remote-data
* **GetRemoteDataArgs**: Maintains all the arguments you receive from the server in order to use this command.
Arguments:  
  - *remote_incident_id*: Contains the value of the `dbotMirrorId` field, which represents the ID of the incident in the external system.
  - *last_update*: The time the incident was last updated.
* **GetRemoteDataResponse**: Maintains the format in which you should order the results from this function. Use return_results on this object to make it work.
Arguments:    
  - *mirrored_object*: The object(dict) of whatever you are trying to mirror, usually the incident. If there are only entries (no change to incident), you can return `{}` as the first entry. 
  - *entries*: A list of entries to add to your incident. If you want to close the incident, you can return an entry with `{"Contents": {"dbotIncidentClose": True, "closeReason": "some reason", "closeNotes": "Some note"}`. If you want to re-open a closed incident, you should return `{"Contents": {"dbotIncidentReopen": True}}`. Full entry syntax is supported, including marking it as a note.
  
#### Example of an Implementation of `get_remote_data_command`
```python
def get_remote_data_command(client, args):
    parsed_args = GetRemoteDataArgs(args)
    try:
      new_incident_data: Dict = client.get_incident_data(parsed_args.remote_incident_id, parsed_args.last_update)    
      raw_entries: List[dict] = client.get_incident_entries(parsed_args.remote_incident_id, parsed_args.last_update)
      parsed_entries = []
      for entry in raw_entries:
          parsed_entries.append({       
              'Type': EntryType.NOTE,
              'Contents': entry.get('contents'),
              'ContentsFormat': EntryFormat.TEXT,
              'Tags': ['tag1', 'tag2'],  # a list of tags to add to the entry
              'Note': False  # boolean: True for Note, False otherwise
          })

      remote_incident_id = new_incident_data['incident_id']
      new_incident_data['id'] = remote_incident_id
      return GetRemoteDataResponse(new_incident_data, parsed_entries)
    except Exception as e:
      if "Rate limit exceeded" in str(e):  # modify this according to the vendor's spesific message
          return_error("API rate limit")
```

### get-modified-remote-data
* **GetModifiedRemoteDataArgs**: Maintains all the arguments you receive from the server in order to use this command.
Arguments:  
  - *last_update*: Date string that represents the last time we retrieved modified incidents for this integration.
* **GetModifiedRemoteDataResponse**: Maintains the format in which you should order the results from this function. Use `return_results` on this object to make it work.
Arguments:
**You must provide one of the following:**
  - *modified_incident_ids*: A list of strings representing incident IDs that were modified since the last check. Later the `get-remote-data` command will run on only modified incidents.
  - *modified_incident_entries*: A list of entries containing the full incident data. In this case, `get-remote-data` will not be called.
* **skip update**: In case of a failure. In order to notify the server that the command failed and prevent execution of the **get-remote-data** commands, returns an error that contains the string `"skip update"`.

#### Example of an Implementation of `get_modified_remote_data_command`
```python
def get_modified_remote_data_command(client, args):
    remote_args = GetModifiedRemoteDataArgs(args)
    last_update = remote_args.last_update
    last_update_utc = dateparser.parse(last_update, settings={'TIMEZONE': 'UTC'})  # converts to a UTC timestamp
    
    raw_incidents = client.get_incidents(gte_modification_time=last_update_utc, limit=100)
    modified_incident_ids = list()
    for raw_incident in raw_incidents:
        incident_id = raw_incident.get('incident_id')
        modified_incident_ids.append(incident_id)

    return GetModifiedRemoteDataResponse(modified_incident_ids)
```
* **Last Mirror Run (Available from 6.6)**  
[get_last_mirror_run()](https://xsoar.pan.dev/docs/reference/api/common-server-python#get_last_mirror_run) retrieves the previous mirror run data that was set. You can set the last run of the mirror using [set_last_mirror_run()](https://xsoar.pan.dev/docs/reference/api/common-server-python#set_last_mirror_run). Storing and getting this data (a dictionary) enables you to control the *lastUpdate* timestamp from the integration or any other data you want to save between mirror runs.
 
#### Example of an Implementation of `get_modified_remote_data_command`
```python
def get_modified_remote_data_command(client, args):
    last_update = get_last_mirror_run().get("last_update")
    last_mirror_incident_id = get_last_mirror_run().get("last_incident_id")
    last_update_utc = dateparser.parse(last_update, settings={'TIMEZONE': 'UTC'})  # convert to utc format
    
    raw_incidents = client.get_incidents(gte_modification_time=last_update_utc, limit=100)
    modified_incident_ids = list()
    for raw_incident in raw_incidents:
        incident_id = raw_incident.get('incident_id')
        modified_incident_ids.append(incident_id)
        last_mirror_incident_id = incident_id
    
    # Following is an example for storing the last update to be now and the last incident ID that was handled but we can use it in any other way
    set_last_mirror_run({"last_update": datetime.datetime.now(datetime.timezone.utc), "last_incident_id": last_mirror_incident_id})
    return GetModifiedRemoteDataResponse(modified_incident_ids)
```

### update-remote-system
* **UpdateRemoteSystemArgs**: Maintains all the arguments you receive from the server in order to use this command.
  - *data*: Represents the data of the current incident - a dictionary object `{key: value}`.
  - *entries*: Represents the entries from your current incident - a list of dictionary objects representing the entries.
  - *remote_incident_id*: Contains the value of the dbotMirrorId field, which represents the ID of the incident in the external system. 
  - *inc_status*: The status of the incident(numeric value, could be used with IncidentStatus from CommonServerPython).
  - *delta*: Represents the dictionary of fields that changed from the last update - a dictionary object `{key: value}` containing only the changed fields.
  - *incident_changed*: A boolean indicating if the incident changed. An incident might not change, but we want to send mirrored entries over.
  
#### Example of an Implementation of `update_remote_system_command`
```python
def update_remote_system_command(client: Client, args: Dict[str, Any]) -> str:
    """update-remote-system command: pushes local changes to the remote system

    :type client: ``Client``
    :param client: XSOAR client to use

    :type args: ``Dict[str, Any]``
    :param args:
        all command arguments, usually passed from ``demisto.args()``.
        ``args['data']`` the data to send to the remote system
        ``args['entries']`` the entries to send to the remote system
        ``args['incidentChanged']`` boolean telling us if the local incident indeed changed or not
        ``args['remoteId']`` the remote incident id

    :return:
        ``str`` containing the remote incident id - really important if the incident is newly created remotely

    :rtype: ``str``
    """
    parsed_args = UpdateRemoteSystemArgs(args)
    if parsed_args.delta:
        demisto.debug(f'Got the following delta keys {list(parsed_args.delta)}')
        
    demisto.debug(f'Sending incident with remote ID [{parsed_args.remote_incident_id}] to remote system\n')
    new_incident_id: str = parsed_args.remote_incident_id
    updated_incident = {}
    if not parsed_args.remote_incident_id or parsed_args.incident_changed:
        if parsed_args.remote_incident_id:
            # First, get the incident as we need the version
            old_incident = client.get_incident(incident_id=parsed_args.remote_incident_id)
            for changed_key in parsed_args.delta.keys():
                old_incident[changed_key] = parsed_args.delta[changed_key]  # type: ignore

            parsed_args.data = old_incident

        else:
            parsed_args.data['createInvestigation'] = True

        updated_incident = client.update_incident(incident=parsed_args.data)
        new_incident_id = updated_incident['id']
        demisto.debug(f'Got back ID [{new_incident_id}]')

    else:
        demisto.debug(f'Skipping updating remote incident fields [{parsed_args.remote_incident_id}] as it is '
                      f'not new nor changed.')

    if parsed_args.entries:
        for entry in parsed_args.entries:
            demisto.debug(f'Sending entry {entry.get("id")}')
            client.add_incident_entry(incident_id=new_incident_id, entry=entry)

    # Close incident if relevant
    if updated_incident and parsed_args.inc_status == IncidentStatus.DONE:
        demisto.debug(f'Closing remote incident {new_incident_id}')
        client.close_incident(
            new_incident_id,
            updated_incident.get('version'),  # type: ignore
            parsed_args.data.get('closeReason'),
            parsed_args.data.get('closeNotes')
        )

    return new_incident_id

```
### get-mapping-fields
* **SchemeTypeMapping**: Keeps the correct structure of the mapping for the fetched incident type.
* **GetMappingFieldsResponse**: Gathers all your SchemeTypeMapping and then parses them properly into the results using the return_results_command.

#### Example of an Implementation of `get_mapping_fields_command`
```python
def get_mapping_fields_command():
    xdr_incident_type_scheme = SchemeTypeMapping(type_name='incident type example')
    for field in ['field1', 'field2', 'field3']:
        xdr_incident_type_scheme.add_field(name=field, description='the description for the field')

    return GetMappingFieldsResponse(xdr_incident_type_scheme)

```

## Incident Fields on a Cortex XSOAR Incident 
The following incident fields must be configured either in the integration or in the integration instance mapping:
* **dbotMirrorDirection**: Valid values are Both, In, or Out.
* **dbotMirrorId**: The ID of the incident in the external system.
* **dbotMirrorInstance**: The instance through which you will be mirroring.
- **dbotDirtyFields**: Fields we changed locally and therefore will not be updated from the remote.
- **dbotCurrentDirtyFields**: Fields that are going to be sent remotely as a delta in the next iteration of the job (should remain invisible to the end user).
- **dbotMirrorLastSync**: Timestamp in UTC indicating the last time we synced this incident with the remote system.
* **dbotMirrorTags**: Tags for mirrored-out entries (comment/files).

## Debugging

* **getMirrorStatistics**: A hidden command that returns mirroring statistics: total mirrored, rate limited, last run, closed incident records and closed rate limited incident records.
* **getSyncMirrorRecords**: A hidden command that returns records that hold internal mirroring metadata for each mirrored incident.
* **get-remote-data**: Runnable through the War Room if the command is defined in the YAML file.
* **get-modified-remote-data**: Runnable through the War Room if the command is defined in the YAML file.
* **get-mapping-fields**: Runnable through the War Room with no arguments and displays the results.
* **purgeClosedSyncMirrorRecords**: Receives two arguments: mandatory `dbotMirrorInstance` for which integration to purge and optional `olderThan` in days. Since this bucket is continuously growing with all the closed incidents that are mirrored, it is recommended to purge when you're sure that there will be no update from the remote system on old incidents.
* **triggerDebugMirroringRun**: (Available from 6.6) Runnable from the War Room in order to debug a full mirroring run over existing incidents. You can add an incident ID to the command to get information about a specific incident. If no ID is given, the incident will be loaded from the War Room context. The output of this command is a unique debug log file that includes logs for the entire mirroring flow. In addition, this debug log includes the content of the integrations' debug-mode logs. An example for running the command from the cli is `!triggerDebugMirroringRun incidentId=50`
  
   **Note:**
   This command triggers real mirroring actions, for example, updating incidents and fields.

## Troubleshooting and Tips

* When using a custom mapper, make sure it has the required mirroring incident fields (dbotMirrorDirection, dbotMirrorId and dbotMirrorInstance), more information can be found under the "Incident Fields on a Cortex XSOAR Incident" section.
* The mapper the incident goes through upon creation configures whether the incident will be mirrored and in which direction. 
* When switching between different mappers with different incident fields, for mirroring to work with the new incident fields, delete the old incidents and re-fetch them with the new mapper.
* Mirroring continues to work after reopening an incident in Cortex XSOAR. Mirroring entries works only for active incidents, while mirroring fields also works for pending incidents.
* If you change the display name from "incident", mirroring will not work.
* Closed incidents in Cortex XSOAR, will not receive mirrored updates from the remote system, unless the incident is re-opened in Cortex XSOAR.
