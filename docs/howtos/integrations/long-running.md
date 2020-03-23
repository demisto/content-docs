---
id: long-running
title: Long Running Containers
---

You can use long running containers to run specific processes in an integration forever.

## Getting Started

### Prerequisites
- Demisto v5.0 or later.

- The integration must be written in Python.

### Enable the longRunning property
To make an integration long running, you need to enable the `longRunning` property:
![image](../../doc_imgs/howtos/integrations/66122533-9b2b7280-e5e8-11e9-92de-f9fbe75b7250.png)

You will then have the `Long running instance` parameter:
![image](../../doc_imgs/howtos/integrations/66122634-e6458580-e5e8-11e9-9030-6514832c9422.png)

If you check the checkbox, the server will launch a long running container each time an instance is enabled. When the checkbox is unchecked or the instance is disabled, the container will die.
You can distinguish it from the rest of the containers by its name:
![image](../../doc_imgs/howtos/integrations/66122754-2d337b00-e5e9-11e9-8775-562e228e3fe6.png)


## Implementation
When the container runs, it calls a dedicated command in the integration, much like fetch-incidents. The command is called `long-running-execution` 
You'll have to implement it in your integration code. In order to run this code forever, you will need it to never stop executing, for example - a never ending loop (`while True`).

### Interaction with the server
Since the long running container does not run in a scope of an incident, it has no standard place to output results into.
For that we have dedicated functions to interact with the server:
* `addEntry` - Adds an entry to a specified incident War Room.
* `createIncidents` - Creates incidents according to a provided JSON. Unlike `demisto.incidents()`, this function requires actual incident fields in the JSON argument.
For example - `{'name': 'incident', 'type': 'Phishing', 'customFields': {'field1': 'value'}`.
* `findUser` - Find a Demisto user by a name or email. Useful for creating incidents.
* `handleEntitlementForUser` - Adds an entry with entitlement to a provided investigation.
* `updateModuleHealth` - Update the instance status. It's a way to reflect the container state to the user.
![image](../../doc_imgs/howtos/integrations/66123930-cb284500-e5eb-11e9-804d-6154423e6cee.png)
* `mirrorInvestigation` - For chat based integrations, mirror a provided Demisto investigation to the corresponding chat module.
* `directMessage` - For chat based integrations, handle free text sent from a user to the chat module and process it in the server.

### Manage container states 
One of the most important and useful aspects of the long running process is the integration context:
`demisto.setIntegrationContext(context)`
`demisto.getIntegrationContext()`
Use the integration context to store information and manage the state of the container per integration instance.
This context is stored in a format of a dict of `{'key': 'value'}`, where value **must** be a string. To store complex objects as values, parse them to JSON.

Use logging to notify and report different states inside the long running process - `demisto.info(str)` and `demisto.error(str)`. These will show up in the server log.

## Troubleshooting
Use `updateModuleHealth`, `info` and `error` to report errors and debug. It's also important to segregate the logic into functions so you'll be able to unit test them.

## Best practices
It's important to maintain a never ending process in the container. That means:

1. Never use `sys.exit()` (`return_error` and friends).
2. Always catch exceptions and log them.
3. Run in a never ending loop.

To run multiple processes in parallel, you can use async code. For an example you can check out the `Slack v2` or `Microsoft Teams` integrations.

## Invoking Long Running http Integrations via Demisto Server's route handling 

**Supported Demisto Server version**: 5.5 and above

Demisto supports setting up long running integrations which expose an HTTP endpoint. Such integrations include:
* Palo Alto Networks PAN-OS EDL Service
* Export Indicators Service
* Microsoft Teams

When you initiate these integrations, they listen on an incoming HTTP port. The port is configured via the **Listen Port** setting of the integration. The HTTP interface can be accessed directly over the port, for example by running curl locally on the Demisto Server machine (assuming the configured port is 7000 and HTTP is being used):
```
curl http://localhost:7000
```

**Important Note:** Each integration instance should be configured with a unique listening port number.

To access the integration over the listening port via the Demisto Server's DNS host, you would use (assuming the configured port is 7000 and http is being used) the url: `http://<demisto_dns>:7000`. This requires opening the port to external access. Usually this involves a firewall or security group modification. 

Starting with Demisto Server v5.5 there is an option to route the HTTP request via the Demisto Server's HTTPS endpoint. This is useful if you would like to avoid opening an additional port (the long running integration's port) on the Demisto Server's machine to outside access. 

To configure a long running integration to be accessed via Demisto Server's https endpoint perform the following:
* Configure the long running integration to listen on a unique port
* Make sure the long running integration is setup to use http (not https)
* Add the following advanced Server parameter:
  * Name: `instance.execute.external.<instance_name>`
  * Value: `true`
* For example for an instance named **edl** set the following:
  * Name: `instance.execute.external.edl`
  * Value: `true`

You will then be able to access the long running integration via the Demisto Server's https endpoint. The route to the integration will be available at:
```
https://<demisto_server_url>/instance/execute/<instance_name>
```
For example, to test access to an instance named `edl` run the following curl command from the Demisto Server's machine:
```
curl -k https://localhost/instance/execute/edl
```

There is also the option to set a default value that all http long running integrations are exposed via the Demisto's Server https endpoint. Do this by setting the following Server advanced parameter:
* Name: `instance.execute.external`
* Value: `true`

You can then also disable specific instances by setting:
* Name: `instance.execute.external.<instance_name>`
* Value: `false`







