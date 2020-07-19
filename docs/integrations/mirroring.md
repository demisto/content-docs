---
id: mirroring_integration
title: Mirroring Integration
---

Server version 6.0.0 adds support for Mirroring Integrations. These integrations allow you to mirror incidents/tickets/cases from other services for example: Another XSOAR server, Cortex XDR, ServiceNow

An example Mirroring Integration can be seen [here](https://github.com/demisto/content/tree/master/Packs/XSOARMirroring/Integrations/XSOARMirroring).

Mirroring Integrations are developed the same as other Integrations. They provide a few extra configuration parameters and APIs.


## Supported Server Version
Mirroring Integration's YAML file _must_ have the following field `fromversion: 6.0.0`. This is because Mirroring Integrations are only supported from Server version 6.0.0 and onwards.


## Required Parameters
Mirroring integration should have the following parameters in the integration YAML file:
```yml
  isfetch: true
  ismappable: true
  isremotesyncin: true
  isremotesyncout: true
```
While the `ismappable` and `isremotesyncin` are used for getting information from a remote incident, And the `isremotesyncout` for updating remote data.

## Commands
Mirroring Integration should have some and at some cases all(When using full mirror in and out) of the following commands:
- `test-module` - this is the command that is run when the `Test` button in the configuration panel of an integration is clicked.
- `fetch-incidents` - this is the command that fetches new incidents to Cortex XSOAR.
- `get-remote-data` - this command takes new information about the incidents in the remote system and updates the *already existing* incidents in Cortex XSOAR. This command is being executed every 1 minute. 
- `update-remote-system` - this command updates the remote system with the information we have in the mirrored incidents within Cortex XSOAR. This command is being executed every 1 minute.
- `get-mapping-fields` - this command will pull the different incident types and their associated incident fields from the remote system, it will be used in the Mirror out configuration page in the XSOAR UI.

## Usefull objects to use in your code
All the functions explained here are globally available through the CommonServerPython file.

### get-remote-data
* GetRemoteDateArgs - this is an object created to maintain all the argument you receive from the server in order to use this command.
* GetRemoteDataResponse - this this is the object that maintains the format in which you should order the results from this function. You should use return_results on this object to make it work.

### get-mapping-fields
* UpdateRemoteSystemArgs - this is an object created to maintain all the argument you receive from the server in order to use this command.

### get-mapping-fields
* SchemeTypeMapping - this is the object you should use to keep the correct structure of the mapping for the fetched incident type.
* GetMappingFieldsResponse - this is the object to gather all your SchemeTypeMapping and then to parse them properly into the results using the return_results command.
