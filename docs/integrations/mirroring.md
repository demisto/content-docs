---
id: mirroring_integration
title: Mirroring Integration
---

Cortex XSOAR version 6.0.0 adds support for Mirroring Integrations. These integrations allow you to mirror incidents/tickets/cases from other services.  
For example: Another XSOAR server, Cortex XDR, ServiceNow. In addition, when mapping the incident fields, mirroring enables you to pull the database schema from the integration, which brings all of the available fields into Cortex XSOAR. For more information about working with the schema, see the Select schema option described [here](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/incidents/classification-and-mapping/create-a-mapper.html).

An example mirroring integration can be seen [here](https://github.com/demisto/content/tree/master/Packs/ServiceNow/Integrations/ServiceNowv2).

Mirroring integrations are developed the same as other integrations. They provide a few extra configuration parameters and APIs.

:::note 
**For Cortex XSOAR versions 6.1.0 and earlier**: Once an incident field is changed manually within XSOAR, it will be marked as "dirty" and will not be updated by the mirroring process in XSOAR throughout the life of the incident. It should be noted that in the case outbound mirroring is enabled, any changes to the incident in XSOAR will however still be reflected in the external system.
:::

## Supported Server Version
Mirroring is only supported from version 6.0.0 and on.


## Required Parameters
A Mirroring Integration's YAML file should have the following parameters (under the scripts section):
```yml
  isfetch: true
  ismappable: true
  isremotesyncin: true
  isremotesyncout: true
```
Where:
- **isfetch** determines if the integration fetches incidents.
- **ismappable** determines if the remote schema can be retrieved for this integration.
- **isremotesyncin** determines if mirroring from the 3rd party integration to XSOAR is supported.
- **isremotesyncout** determines if mirroring from XSOAR to the 3rd party integration is supported.

## Commands
Use the following commands to implement a mirroring integration.  
*Note that when mirroring both incoming and outgoing data, all the commands are required. For mirroring in only one direction, only some of the commands are required.*
- `test-module` - this is the command that is run when the `Test` button in the configuration panel of an integration is clicked.
- `fetch-incidents` - this is the command that fetches new incidents to Cortex XSOAR.
- `get-modified-remote-data` - available from Cortex XSOAR version 6.1.0. This command queries for incidents that were modified since the last update. If the command is implemented in the integration, the **get-remote-data** command will only be performed on incidents returned from this command, rather than on all existing incidents. This command is executed every 1 minute for each individual **integration's instance**. 
If the command is not implemented, make sure to raise `NotImplementedError` so `get-remote-data` will be called instead. If the command fails return an error entry with one of the following sub-strings: `API rate limit` or `skip update` (exact case) to signal to the Server that there is an issue and it should not continue to `get-remote-data`. 
- `get-remote-data` - this command gets new information about the incidents in the remote system and updates *existing* incidents in Cortex XSOAR. If an API rate limit error occures, this method should an error with substring `"API rate limit"`, so that the sync loop will start from the failed incident.
This command is executed every 1 minute for each individual **incident** fetched by the integration.
- `update-remote-system` - this command updates the remote system with the information we have in the mirrored incidents within Cortex XSOAR. This command is executed whenever the individual incident is changed in Cortex XSOAR.
- `get-mapping-fields` - this command pulls the remote schema for the different incident types, and their associated incident fields, from the remote system. This enables users to map XSOAR fields to the 3rd-party integration fields in the outgoing mapper. This command is being called when selecting the **Select schema** option in the **Get data** configuration in a classifier or a mapper.

## Special Server Configurations
- `sync.mirror.job.enable` is to enable / disable the mirroring job - (default is **enabled**)
- `sync.mirror.job.delay` is the interval for the job in minutes - (default is **1 minute**)
- `sync.mirror.job.delayAdvanced` is mostly used for demos and overrides `sync.mirror.job.delay` and if specified is the interval for the job in seconds. Idea being that for demos you do not want to wait a min to show mirroring happened.

## How to implement mirroring functions
You can implement the following functions, using the classes described below, which are globally available through the CommonServerPython file.

### get-remote-data
* **GetRemoteDataArgs** - this is an object created to maintain all the arguments you receive from the server in order to use this command.
Arguments explanation:
  - *remote_incident_id* - contains the value of the `dbotMirrorId` field, which represents the id of the incident in the external system.
  - *last_update* - the time the incident was last updated.
* **GetRemoteDataResponse** - this is the object that maintains the format in which you should order the results from this function. You should use return_results on this object to make it work.
Arguments explanation:
  - *mirrored_object* - this is essentially the object(dict) of whatever you are trying to mirror - incident in most cases. If there are only entries (no change to incident), you can return `{}` as the first entry. 
  - *entries* - a list of entries to add to your incident. If you want to close the incident, you can return an entry with `{"Contents": {"dbotIncidentClose": True, "closeReason": "some reason", "closeNotes": "Some note"}`. If you want to re-open a closed incident, you should return `{"Contents": {"dbotIncidentReopen": True}}`. Full entry syntax is supported, including marking it as a note.
  
An example for such a function could be:
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
              'Tags': ['tag1', 'tag2'],  # the list of tags to add to the entry
              'Note': False  # boolean, True for Note, False otherwise
          })

      remote_incident_id = new_incident_data['incident_id']
      new_incident_data['id'] = remote_incident_id
      return GetRemoteDataResponse(new_incident_data, parsed_entries)
    except Exception as e:
      if "Rate limit exceeded" in str(e):  # modify this according to the vendor's spesific message
          return_error("API rate limit")
```

### get-modified-remote-data
* **GetModifiedRemoteDataArgs** - this is an object created to maintain all the arguments you receive from the server in order to use this command.
Arguments explanation:
  - *last_update* - Date string represents the last time we retrieved modified incidents for this integration.
* **GetModifiedRemoteDataResponse** - this is the object that maintains the format in which you should order the results from this function. You should use `return_results` on this object to make it work.
Arguments explanation. **You must provide one of the following:**
  - *modified_incident_ids* - a list of strings representing incident IDs that were modified since the last check. Later `get-remote-data` command will run on only modified incidents.
  - *modified_incident_entries* - a list of entries containing the full incident data. In this case, `get-remote-data` **will not be called**.
* **skip update** - in case of failure, in order to notify the server that the command failed and prevent execution of **get-remote-data** commands, return error which contains the string `"skip update"`.

An example for such a function could be:
```python
def get_modified_remote_data_command(client, args):
    remote_args = GetModifiedRemoteDataArgs(args)
    last_update = remote_args.last_update
    last_update_utc = dateparser.parse(last_update, settings={'TIMEZONE': 'UTC'})  # convert to utc format
    
    raw_incidents = client.get_incidents(gte_modification_time=last_update_utc, limit=100)
    modified_incident_ids = list()
    for raw_incident in raw_incidents:
        incident_id = raw_incident.get('incident_id')
        modified_incident_ids.append(incident_id)

    return GetModifiedRemoteDataResponse(modified_incident_ids)
```

### update-remote-system
* **UpdateRemoteSystemArgs** - this is an object created to maintain all the arguments you receive from the server in order to use this command.
Arguments explanation:
  - *data* - represents the data of the current incident - a dictionary object `{key: value}`.
  - *entries* - represents the entries from your current incident - a list of dictionary objects representing the entries.
  - *remote_incident_id* - contains the value of the dbotMirrorId field, which represents the id of the incident in the external system. 
  - *inc_status* - the status of the incident(numeric value, could be used with IncidentStatus from CommonServerPython).
  - *delta* - represents the dictionary of fields which have changed from the last update - a dictionary object `{key: value}` containing only the changed fields.
  - *incident_changed* which is boolean to tell us if the incident itself changed. Because incident might not change but we want to send mirrored entries over.
  
An example for such a function could be:
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
        demisto.debug(f'Got the following delta keys {str(list(parsed_args.delta.keys()))}')
        
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
* **SchemeTypeMapping** - the object used to keep the correct structure of the mapping for the fetched incident type.
* **GetMappingFieldsResponse** - the object used to gather all your SchemeTypeMapping and then parse them properly into the results using the return_results command.
Usage example:
```python
def get_mapping_fields_command():
    xdr_incident_type_scheme = SchemeTypeMapping(type_name='incident type example')
    for field in ['field1', 'field2', 'field3']:
        xdr_incident_type_scheme.add_field(name=field, description='the description for the field')

    return GetMappingFieldsResponse(xdr_incident_type_scheme)

```

## Incident fields on a XSOAR incident 
The following incident fields must be configured either in the integration or the instance mapping:
* **dbotMirrorDirection** - valid values are Both, In, or Out.
* **dbotMirrorId** - represents the id of the incident in the external system.
* **dbotMirrorInstance** - the instance through which you will be mirroring.
- **dbotDirtyFields** for fields we changed locally and hence will not be updated from remote
- **dbotCurrentDirtyFields** for fields that are going to be sent remotely as delta in the next iteration of the job - probably should remain invisible to the end user
- **dbotMirrorLastSync** timestamp that includes last time we synched this incident with remote system 
* **dbotMirrorTags** - tags for mirrored-out entries (comment/files).

## Debugging

* **getMirrorStatistics** command - a hidden command that returns mirroring statistics: total mirrored, rate limited, last run, closed incident records and closed rate limited incident records.
* **getSyncMirrorRecords** - a hidden command that returns records that hold internal mirroring metadata for each mirrored incident
* **get-remote-data** - is runnable through the war room if the command is defined in the yml file.
* **get-modified-remote-data** - is runnable through the war room if the command is defined in the yml file.
* **get-mapping-fields** - is runnable through the war room with no arguments and see the results.
* **purgeClosedSyncMirrorRecords** - receives 2 arguments: mandatory `dbotMirrorInstance` for which integration to purge and optional `olderThan` in days. Since this bucket is forever growing (with all the closed incidents that are mirrored), might be a good idea to purge when you're sure that there will be no update from the remote system on the really old incidents.
