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

![image](/doc_imgs/integrations/66122533-9b2b7280-e5e8-11e9-92de-f9fbe75b7250.png)

You will then have the `Long running instance` parameter:

![image](/doc_imgs/integrations/66122634-e6458580-e5e8-11e9-9030-6514832c9422.png)

If you check the checkbox, the server will launch a long running container each time an instance is enabled. When the checkbox is unchecked or the instance is disabled, the container will die.
You can distinguish it from the rest of the containers by its name:

![image](/doc_imgs/integrations/66122754-2d337b00-e5e9-11e9-8775-562e228e3fe6.png)

Certain integrations are long-running by default so they do not include the "Long Running Instance" checkbox. Examples of such integrations include:

- Generic Export Indicators Service (EDL)
- Generic Webhook
- AWS SNS Listener
- TAXII2 Server
- TAXIIServer

In these cases, the long-running behavior is inherent and cannot be modified.
These integrations can operate in either "single engine" mode or "no engine" mode.

**Single Engine:** 
1. Select your engine in the integration configuration.
2. When the engine is selected, a new field called "Listen Port" will appear.
3. Specify the port number that the instance will use.

**No Engine:**
1. Select "no engine" in the integration configuration.
2. Click **Save** and the server automatically assigns a port for the instance.

  Note: If you select **No Engine**, the listen port is assigned only after saving the configuration. If you click on "Test" before clicking on "Save", the server will assign a temporary port until the  instance starts running. Please make sure to click **Save**, not **Save & Exit**.
  If you configured the instance but exited before saving, you will need to create a new instance and follow the steps outlined above.
  In Cortex XSOAR 8.9, the behavior for "No Engine" will change, and the listen port will be assigned immediately upon configuration, eliminating the need to save the instance manually.

## Implementation
When the container runs, it calls a dedicated command in the integration, much like fetch-incidents. The command is called `long-running-execution` 
You'll have to implement it in your integration code. In order to run this code forever, you will need it to never stop executing, for example - a never ending loop (`while True`).

### Interaction with the server
Since the long running container does not run in a scope of an incident, it has no standard place to output results into.
For that we have dedicated functions to interact with the server:
* `addEntry` - Adds an entry to a specified incident War Room.
For more details, see the [API reference](https://xsoar.pan.dev/docs/reference/api/demisto-class#addentry).
* `createIncidents` - Creates incidents according to a provided JSON.
For more details, see the [API reference](https://xsoar.pan.dev/docs/reference/api/demisto-class#createincidents).
* `findUser` - Find a Cortex XSOAR user by a name or email. Useful for creating incidents.
For more details, see the [API reference](https://xsoar.pan.dev/docs/reference/api/demisto-class#finduser).
* `handleEntitlementForUser` - Adds an entry with entitlement to a provided investigation.
For more details, see the [API reference](https://xsoar.pan.dev/docs/reference/api/demisto-class#handleentitlementforuser).
* `updateModuleHealth` - Update the instance status. It's a way to reflect the container state to the user.
For more details, see the [API reference](https://xsoar.pan.dev/docs/reference/api/demisto-class#updatemodulehealth).

  ![image](/doc_imgs/integrations/66123930-cb284500-e5eb-11e9-804d-6154423e6cee.png)
* `mirrorInvestigation` - For chat based integrations, mirror a provided Cortex XSOAR investigation to the corresponding chat module.
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

## Invoking HTTP Integrations via Cortex XSOAR Server's route handling 
For more details, see the following article: [Invoking Long Running HTTP Integrations via Server's HTTPS endpoint](../reference/articles/long-running-invoke).

