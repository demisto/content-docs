---
id: scheduled-commands
title: Scheduled Commands
---

### Available from XSOAR version 6.2.0 and above.

<img width="533" src="../doc_imgs/integrations/polling-command.png"></img>

It's possible for a command to schedule a future execution for another command.

Use cases for using scheduled commands include:
1. ***Polling Flow*** - The command cannot return the full result in a single execution (likely because it's waiting for a remote process to finish execution). Scheduled commands enable to set the command to try again later, and return the full result when it can. Example use cases are `Sandbox Detonation` and `Autofocus samples search`.
2. ***Rate Limiting*** - The command cannot perform the required action because the instance has reached its rate limit. Enable Scheduled commands to try again later in order to check if the rate limit has been removed. If so, the command can be executed.
3. ***Concurrency*** - The command cannot perform the required action because the instance has reached its concurrent limit. Scheduled commands are enabled to set the command to try again later (preferably with exponential backoff).

### YAML Prerequisite
* ***Integration***: In the integration yml, under the command root add `polling: true`.
* ***Script***: In the script yml, in the root of the file add `polling: true`.

For an example, see the Autofocus V2 `autofocus-samples-search` command.

### Common.ScheduledCommandConfiguration
`ScheduleMetadata` is an optional class that enables scheduling commands via the command results.

#### ScheduleMetadata Class Arguments
| Arg               | Type   | Description                                                                                                                                                                                |
|-------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| command                | str    | The command that will run after `next_run_in_seconds` has passed.
| next_run_in_seconds    | int    | How long to wait before executing the command.
| args                   | dict   | Arguments to use when executing the command.
| timeout_in_seconds     | int    | Number of seconds until the polling sequence will timeout.

When provided to [CommandResults](./code-conventions#commandresults) it will transform its result into a ***schedule result***.
When the time comes for the next command to run, it will be executed.
The scheduled command can return another ***schedule result***, that will schedule another schedule command and so on.

The schedule sequence will be complete when either one of three terminating actions happen:

1. ***Done*** - The schedule sequence is done, indicated by a command execution without any schedule result.
2. ***Error*** - The command encountered an error, indicated by an error result.
3. ***Timeout (automatically handled)*** - The schedule sequence reached the timeout, in which case a timeout error entry will be returned automatically.

#### Code Example
In the example below, if the `status` is not `complete` then a result with `schedule_config` will be returned which will trigger in 60 seconds a poll for the search. This will be done in the next run as well, and again until its status is complete.

```python
if status != 'complete':
    interval_in_secs = 60
    polling_args = {
        'af_cookie': af_cookie,
        'interval_in_seconds': interval_in_secs
    }
    schedule_config = Common.ScheduledCommandConfiguration(command='autofocus-search-samples',
                                                          next_run_in_seconds=interval_in_secs,
                                                          args=polling_args, 
                                                          timeout_in_seconds=600
    )
    return_results(CommandResults(scheduled_command_config=schedule_config))
```
