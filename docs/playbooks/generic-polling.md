---
id: generic-polling
title: Generic Polling
---

When working with certain 3rd party products (detonation, scan, search, etc.) occasionally we'll find ourselves having to wait for a process to finish on the remote host before we can continue. In those cases, the playbook should stop and wait for the process to complete on the 3rd party product, and continue when it's done.

We can't achieve via integrations or automations due to hardware limitations. One method for achieving this is using the `GenericPolling` playbook.

## What it does
The playbook periodically polls the status of a process being executed on a remote host, and when the host returns that the process execution is done, the playbook finishes execution.

:::note 
If the timeout was reached, the playbook will succesfully finish. Make sure to validate the process was completed. 
:::

## How to use
Follow these instructions to use the `GenericPolling` playbook.
### Prerequisites:
* **Start command** - Command that will fetch the initial state of the process and save it to the context. This command will usually start the process that should be polled. For example:
  * Detonation - `joe-analysis-submit-sample` - Submit a sample for analysis (will be detonated as part of the analysis).
  * Scan - `nexpose-start-assets-scan` - Starts a scan for specified asset IP addresses and host names.
  * Search - `qradar-searches` - Searches in QRadar using AQL.
* **Polling command** - Command that will poll the status of the process and save it to the context. The input of this command **must be checked** as **Is array** - this will allow the playbook to poll at once more than a single process being executed. For example:
  * Detonation - `joe-analysis-info` - Returns the status of the analysis execution.
  * Scan - `nexpose-get-scan` - Returns the specified scan.
  * Search - `qradar-get-search` - Gets a specific search id and status.

### Inputs
* **Ids** - A list of process IDs to poll (usually a previous task output).
* **PollingCommandName** - Name of the polling command to run.
* **PollingCommandArgName** - Argument name of the polling command. The argument should be the name of the process identifier (usually an ID).
* **dt** - [Cortex XSOAR Transform Language](../integrations/dt) filter to be checked against the polling command result. Polling will stop when no results are returned from the DT filter.
* **Interval** - Interval between each poll (default is 1 minute).
* **Timeout** - The amount of time that'll pass until the playbook will stop waiting for the process to finish. After this time has passed the playbook will finish running, even if it didn't get a satisfactory result (the action is done executing).
* **Additional polling command arguments** - If the polling command has more than a single argument you can add their names via this input, for example: `arg1,arg2,...`. 
* **AdditionalPollingCommandArgValues** -  If the polling command has more than a single argument you can add their values via this input for example: `value1,value2,...`. 

## Example
### [Detonate File – JoeSecurity](https://github.com/demisto/content/blob/master/Packs/JoeSecurity/Playbooks/playbook-Detonate_File_-_JoeSecurity.yml)
![image](../doc_imgs/playbooks/66270734-7ee53b00-e85f-11e9-8566-e0118774070e.png)

* **Start command** - `joe-analysis-submit-sample` - Starts a new analysis of a file in Joe Security.
* **Polling command** - `joe-analysis-info` - Returns the status of the analysis execution.
* **Argument name** - `webid` - argument name of the polling command. 
* **Context path to store poll results** - `Joe.Analysis`
  * **ID context path** - `WebID` - Stores the ID of the process to be polled.
  * **Status context path** - `Status` - Stores the status of the process. 
* **Possible values returned from polling command**: `starting, running, finished`. 
* **DT** - We want a list of IDs of the processes that are still running. Let's explain how it's built:
`Path.To.Object(val.Status !== ‘finished’).ID`
Get the object that has a status other than ‘running’, then get its ID field.
The polling is done only once the result is `finished`. The dt filter will return an empty result in that case - which triggers the playbook to stop running. 

## Limitations
* **Global context** is not supported.
* **GenericPolling**  doesn't work properly in the Playground, thus, testing should be done within an incident.
* Does not run from **playground**.
* Polling command must support list argument.
![image](../doc_imgs/playbooks/66293071-7d168880-e8ee-11e9-9d55-e8ae1e09fe0e.png)

## Troubleshooting
* **Playbook is "stuck" on `Waiting for polling to complete`:** Since generic polling schedules tasks outside the context of the playbook (not visible in the playbook run), a lot of errors appear only in the War Room. Go to the incident War Room and check for errors or warnings related to GenericPolling tasks.
* **GenericPolling task is completed but status is still not "finished":** If the timeout was reached, the playbook will succesfully finish even if there are still items that are not completed. Try increasing the timeout value for the GenericPolling task.
* **The integration returnes an ID not found error when running from GenericPolling, however when running manualy, it finishes successfully:** Some products cannot handle consecutive requests for querying an action status right after the request to perform the action itself. After you initiate the action, try adding a `Sleep` task before calling the **GenericPolling** sub-playbook.
