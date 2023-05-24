---
id: playbooks-extend-context
title: Extend Context
---
There are situations where the data returned by an integration or command is not exactly what you need. For example, when you run the command `!ad-get-user name="sampleName"`, you receive information about the user's dn, email, and more. However, you might only want the name of the user's manager. And you might want to store that information in a specific field.

Cortex XSOAR enables you to do that using the Extend Context feature. Extend Context can be used as in the situation above, or when you want to run a command multiple times and save the output to a different key each time. Using our `!ad-get-user` command from above, run the command once to retrieve the user, and once to retrieve the user's manager. Also, there are situations where an integration is configured to display only some of the information that you is retrieved. The information is shown in context-data, but there is more available. For example, when you run a command to retrieve offenses from a SIEM, only some of the information is displayed, per the configuration of the instance. You can use Extend Context to retrieve the additional information and place it in a new field.

By default, when you run a command, either from the command line or as part of a script or playbook, a subset of JSON fields are returned. To display the full JSON response, run the command using the raw-response=true flag.

## Extending Context
You can extend context either in a playbook task, or directly from the command line. Whichever method you use, Cortex XSOAR recommends that you first run your command with the raw-response=true flag. This will help you identify the information that you want to add to your extended data.

### Extend Context in a Playbook Task
1. Navigate to **Advanced** tab of the relevant playbook task.
2. In the **Extend context** field, enter the name of the field in which you want the information to appear and the value you want to return.
   In our example above, using the ad-get-user command, you could enter user=attributes.displayname to place the user's name in the user key.

   To include more than one field, separate the fields with a double colon. For example:
   user=attributes.displayName::manager=attributes.manager

3. To output only the values for Extend context and ignore the standard output for the command, select the Ignore Outputs checkbox.

   **Note**: While this will improve performance, only the values that you request in the Extend Context field will be returned. In addition, you cannot use Field Mapping as there is no output to which to map the fields.

### Extend Context using the Command Line

1. Run your command with the extend-context flag:
   `!<commandName> <argumentName> <value> extend-context=contextKey=JsonOutputPath`
   Using our example for the ad-get-user command above, to add the user and manager fields to context, run the command `!ad-get-user username=${user.manager.username} extend-context=manager=attributes.manager::user=attributes.displayName`.

2. To output only the values that you set as Extend context, run the command with the ignore-ouput flag=true.
   `!ad-get-user username=${user.manager.username} extend-context=manager=attributes.manager::user=attributes.displayName ignore-output=true`.

## Examples
This section provides several examples that you could implement in your environments.

### QRadar Offenses 

When querying QRadar for offenses based on certain criteria, by default the system returns 11 fields, including event count, offense type, description, and more. 

1. Run the command `!qradar-offenses raw-response="true"`. 
   You see that there are an additional 20 fields or so that are retrieved. 

2. Identify the fields that you want to add and run your command. For example, to retrieve the number of devices affected by a given offense as well as the domain in which those devices reside, run the following command:
   `!qradar-offenses extend-context=device-count=device_count::domain-id=domain_id`

### DT Syntax to Get Select Keys from List of Dictionaries

DT syntax is supported within the extend-context value. You can use DT to get select keys of interest from a command that returns a list of dictionaries containing many keys. For example, the findIndicators automation returns a long list of indicator properties, but you may only be interested in saving the value and the indicator_type to minimize the size of the context data.

1. Run the command `!findIndicators size=2 query="type:IP" raw-response=true`. You will see a list of two dictionaries containing 20+ items.
2. Use the following value for `extend-context` to save only `value` and `indicator_type` into a context key called `FoundIndicators`:

   ```
   !findIndicators size=2 query="type:IP" extend-context=`FoundIndicators=.={"value": val.value, "indicator_type": val.indicator_type}`
   ```
3. Use the following value for `extend-context` to save only the incident `name`, `status`, and `id` to a key called `FoundIncidents`:
   ```
   !SearchIncidentsV2 id=<ANY_INCIDENT_ID> extend-context=`FoundIncidents=Contents.data={"name": val.name, "status": val.status, "id": val.id}` ignore-outputs=true
   ```

For more information on the Extend Context feature, see the [Cortex XSOAR Administrator's Guide](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/6.11/Cortex-XSOAR-Administrator-Guide/Extend-Context).
