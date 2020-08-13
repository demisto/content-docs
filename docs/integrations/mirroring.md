---
id: mirroring_integration
title: Mirroring Integration
---

Server version 6.0.0 adds support for Mirroring Integrations. These integrations allow you to mirror incidents/tickets/cases from other services.  
For example: Another XSOAR server, Cortex XDR, ServiceNow

An example Mirroring Integration can be seen [here](https://github.com/demisto/content/tree/master/Packs/XSOARMirroring/Integrations/XSOARMirroring).

Mirroring Integrations are developed the same as other Integrations. They provide a few extra configuration parameters and APIs.


## Supported Server Version
Mirroring Integration's YAML file _must_ have the following field `fromversion: 6.0.0`. This is because Mirroring Integrations are only supported from Server version 6.0.0 and onwards.


## Required Parameters
Mirroring integration should have the following parameters in the integration YAML file(under the scripts section):
```yml
  isfetch: true
  ismappable: true
  isremotesyncin: true
  isremotesyncout: true
```
While the `ismappable` and `isremotesyncin` are used for getting information from a remote incident, And the `isremotesyncout` for updating remote data.

## Commands
Use the following commands to implement a mirroring integration.  
*Note that when mirroring both incoming and outgoing data all the commands are required, while only some of the commands are required for a one-way mirror.*
- `test-module` - this is the command that is run when the `Test` button in the configuration panel of an integration is clicked.
- `fetch-incidents` - this is the command that fetches new incidents to Cortex XSOAR.
- `get-remote-data` - this command takes new information about the incidents in the remote system and updates the *already existing* incidents in Cortex XSOAR. This command is being executed every 1 minute. 
- `update-remote-system` - this command updates the remote system with the information we have in the mirrored incidents within Cortex XSOAR. This command is being executed every 1 minute.
- `get-mapping-fields` - this command will pull the different incident types and their associated incident fields from the remote system, it will be used in the Mirror out configuration page in the XSOAR UI.

## Useful objects to use in your code
All the functions explained here are globally available through the CommonServerPython file.

### get-remote-data
* GetRemoteDateArgs - this is an object created to maintain all the argument you receive from the server in order to use this command.
Arguments explanation:
  - remote_incident_id - the remote incident id.
  - last_update - the time the incident was last updated - our recommendation would be to use the arg_to_timestamp function to parse it into a timestamp.
* GetRemoteDataResponse - this is the object that maintains the format in which you should order the results from this function. You should use return_results on this object to make it work.
Arguments explanation:
  - mirrored_object - this is essentially the object(dict) of whatever you are trying to mirror - incident in most cases.
  - entries - a list of entries to add to your incident - for instance:
```buildoutcfg
{
    'Type': entry.get('type'),
    'Category': entry.get('category'),
    'Contents': entry.get('contents'),
    'ContentsFormat': entry.get('format'),
    'Tags': entry.get('tags'),  # the list of tags to add to the entry
    'Note': entry.get('note')  # boolean, True for Note, False otherwise
}
```

### update-remote-system
* UpdateRemoteSystemArgs - this is an object created to maintain all the arguments you receive from the server in order to use this command.
Arguments explanation:
  - data - will represent the data of the current incident - a dictionary object `{key: value}`
  - entries - will represent the entries from your current incident - a list of dictionaries objects representing the entries
  - remote_incident_id - the remote incident id - string, the id of the incident.
  - inc_status - the status of the incident(numeric value, could be used with IncidentStatus from CommonServerPython)
  - delta - will represent the dictionary of fields which have changed from the last update - a dictionary object `{key: value}` containing only the changed fields.

### get-mapping-fields
* SchemeTypeMapping - this is the object you should use to keep the correct structure of the mapping for the fetched incident type.
* GetMappingFieldsResponse - this is the object to gather all your SchemeTypeMapping and then to parse them properly into the results using the return_results command.
Usage example:
```python
def get_mapping_fields_command():
    xdr_incident_type_scheme = SchemeTypeMapping(type_name=XDR_INCIDENT_TYPE_NAME)
    for field in XDR_INCIDENT_FIELDS:
        xdr_incident_type_scheme.add_field(name=field, description=XDR_INCIDENT_FIELDS[field].get('description'))

    return GetMappingFieldsResponse(xdr_incident_type_scheme)

```

## Incident fields on a XSOAR incident 
There are few incident fields you need to configure to get going on the system.
* dbotMirrorDirection - Both or In
* dbotMirrorId - represents the id of the incident in the external system
* dbotMirrorInstance - the instance that will perform the mirroring

Useful fields:
* dbotMirrorTags - tags for mirrored-out entries (comment/files).

## Debugging

* getMirrorStatistics command - a hidden command that returns mirroring statistics: total mirrored, rate limited, and last run.
* getSyncMirrorRecords - a hidden command that returns records that hold internal mirroring metadata for each mirrored incident
* get-remote-data - is runnable through the war room with the relevant arguments and see the results.
* get-mapping-fields - is runnable through the war room with no arguments and see the results.

Also important to note:

DO NOT change dbot mirroring fields for existing incidents after they were set
