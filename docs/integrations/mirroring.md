---
id: mirroring_integration
title: Mirroring Integration
---

Server version 6.0.0 adds support for Mirroring Integrations. These integrations allow you to mirror incidents/tickets/cases from other services.  
For example: Another XSOAR server, Cortex XDR, ServiceNow

An example Mirroring Integration can be seen [here](https://github.com/demisto/content/tree/master/Packs/XSOARMirroring/Integrations/XSOARMirroring).

Mirroring Integrations are developed the same as other Integrations. They provide a few extra configuration parameters and APIs.


## Supported Server Version
A Mirroring Integration's YAML file _must_ have the following field `fromversion: 6.0.0`. This is because Mirroring Integrations are only supported from Server version 6.0.0 and on.


## Required Parameters
A Mirroring Integration's YAML file should have the following parameters (under the scripts section):
```yml
  isfetch: true
  ismappable: true
  isremotesyncin: true
  isremotesyncout: true
```
Where:
- isfetch determines if the integration fetches incidents.
- ismappable determines if the remote schema can be accessed.
- isremotesyncin determines if mirroring from the 3rd party integration to XSOAR is supported.
- isremotesyncout determines if mirroring from XSOAR to the 3rd party integration is supported.

## Commands
Use the following commands to implement a mirroring integration.  
*Note that when mirroring both incoming and outgoing data, all the commands are required. For mirroring in only one direction, only some of the commands are required.*
- `test-module` - this is the command that is run when the `Test` button in the configuration panel of an integration is clicked.
- `fetch-incidents` - this is the command that fetches new incidents to Cortex XSOAR.
- `get-remote-data` - this command gets new information about the incidents in the remote system and updates *existing* incidents in Cortex XSOAR. This command is executed every 1 minute for each individual incident. 
- `update-remote-system` - this command updates the remote system with the information we have in the mirrored incidents within Cortex XSOAR. This command is executed whenever the incident is changed in Cortex XSOAR.
- `get-mapping-fields` - this command pulls the different incident types and their associated incident fields from the remote system. This enables users to map XSOAR fields to the 3rd-party integration fields in the outgoing mapper. 

## Useful objects to use in your code
All the functions explained here are globally available through the CommonServerPython file.

### get-remote-data
* GetRemoteDataArgs - this is an object created to maintain all the arguments you receive from the server in order to use this command.
Arguments explanation:
  - remote_incident_id - the remote incident id.
  - last_update - the time the incident was last updated - our recommendation would be to use the arg_to_timestamp function to parse it into a timestamp.
* GetRemoteDataResponse - this is the object that maintains the format in which you should order the results from this function. You should use return_results on this object to make it work.
Arguments explanation:
  - mirrored_object - this is essentially the object(dict) of whatever you are trying to mirror - incident in most cases.
  - entries - a list of entries to add to your incident.
  
An example for such a function could be:
```python
def get_remote_data_command(client, args):
    parsed_args = GetRemoteDateArgs(args)
    new_incident_data: Dict = client.get_incident_data(parsed_args.remote_incident_id, parsed_args.last_update)    new_incident_data: Dict = client.get_incident_data(parsed_args.remote_incident_id, parsed_args.last_update)
    raw_entries: List[dict] = client.get_incident_entries(parsed_args.remote_incident_id, parsed_args.last_update)
    parsed_entries = []
    for entry in raw_entries:
        parsed_entries.append({       
            'Type': entry.get('type'),
            'Category': entry.get('category'),
            'Contents': entry.get('contents'),
            'ContentsFormat': entry.get('format'),
            'Tags': entry.get('tags'),  # the list of tags to add to the entry
            'Note': entry.get('note')  # boolean, True for Note, False otherwise
        })
    
    remote_incident_id = new_incident_data['incident_id']
    new_incident_data['id'] = remote_incident_id
    return GetRemoteDataResponse(new_incident_data, parsed_entries)
```

### update-remote-system
* UpdateRemoteSystemArgs - this is an object created to maintain all the arguments you receive from the server in order to use this command.
Arguments explanation:
  - data - represents the data of the current incident - a dictionary object `{key: value}`.
  - entries - represents the entries from your current incident - a list of dictionary objects representing the entries.
  - remote_incident_id - the dbotMirrorID, which is the incident's ID in the 3rd party integration. 
  - inc_status - the status of the incident(numeric value, could be used with IncidentStatus from CommonServerPython).
  - delta - represents the dictionary of fields which have changed from the last update - a dictionary object `{key: value}` containing only the changed fields.
  
An example for such a function could be:
```
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
* SchemeTypeMapping - the object used to keep the correct structure of the mapping for the fetched incident type.
* GetMappingFieldsResponse - the object used to gather all your SchemeTypeMapping and then parse them properly into the results using the return_results command.
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
* dbotMirrorDirection - valid values are Both, In, or Out.
* dbotMirrorId - represents the id of the incident in the external system.
* dbotMirrorInstance - the instance through which you will be mirroring.

Useful fields:
* dbotMirrorTags - tags for mirrored-out entries (comment/files).

## Debugging

* getMirrorStatistics command - a hidden command that returns mirroring statistics: total mirrored, rate limited, and last run.
* getSyncMirrorRecords - a hidden command that returns records that hold internal mirroring metadata for each mirrored incident
* get-remote-data - is runnable through the war room with the relevant arguments and see the results.
* get-mapping-fields - is runnable through the war room with no arguments and see the results.
