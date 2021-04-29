---
id: scheduled-commands
title: Scheduled Commands
---

### available from XSOAR version 6.2.0 and up

<img width="533" src="../doc_imgs/integrations/polling-command.png"></img>

It's possible for a command to schedule a future execution for another command with predetermined `next_run` time and `args` as well as `timeout`.

Use cases for using a scheduled commands include:
1. ***Polling Flow*** - The command cannot return the full result in a single execution (likely because it's waiting for a remote process to finish execution). Scheduled commands enable to set the command to try again later, and return the full result when it can. example use cases: `Sandbox Detonation`, `Autofocus samples search`.
2. ***Rate Limiting*** - The command cannot perform the required action because the instance has reached its rate limit. Scheduled commands enable to set the command to try again later to check if the rate limit was removed, so the command can be executed.
3. ***Concurrency*** - The command cannot perform the required action because the instance has reached its concurrence limit. Scheduled commands enable to set the command to try again later (preferably with an exponential backoff).

### YAML Prerequisite
* ***Integration***: In the integration yml, under the command root add `polling: true`.
* ***Script***: In the script yml, in the root of the file add `polling: true`.

See for an example: Autofocus V2 `autofocus-samples-search` command.

### ScheduleMetadata
The `ScheduleMetadata` is an optional class that enables scheduling commands via the command results.

#### ScheduleMetadata Class Arguments
| Arg               | Type   | Description                                                                                                                                                                                |
|-------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| command                | str    | The command that'll run after next_run_in_seconds has passed.
| next_run_in_seconds    | int    | How long to wait before executing the command.
| args                   | dict   | Arguments to use when executing the command.
| timeout_in_seconds     | int    | Number of seconds until the polling sequence will timeout.

When provided to a [CommandResults](./code-conventions#commandresults) it transforms its result to a ***schedule result***.
When the time comes for the next command to run, it'll be executed.
The scheduled command can return another ***schedule result***, that will schedule another schedule command and so on.

The schedule sequence will be complete when either one of 3 terminating actions happen:

1. ***Done*** - The schedule sequence is done, indicated by a command execution without any schedule result.
2. ***Error*** - The command encountered an error, indicated by an error result.
3. ***Timeout (automatically handled)*** - The schedule sequence reached the timeout, in which case a timeout error entry will be returned automatically.

#### Code Example
In the example below if the `status` is not `complete` then a result with `schedule_config` will be returned to trigger in 60 seconds a poll for the search. This will be done in the next run as well, and again until its status is complete.

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
