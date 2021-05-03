---
id: scheduled-commands
title: Scheduled Commands
---

### Available from XSOAR version 6.2.0 and above.

<img width="533" src="../doc_imgs/integrations/polling-command.png"></img>

It's possible for a command to schedule a future execution for another command.

The playbook will not proceed to the next task until it is done with all scheduled commands. i.e. until there is no future execution scheduled.
When the playbook is waiting for a command execution it does not use a worker, as workers are only used at the time commands are executed.

Use cases for using scheduled commands include:
* ***Polling Flow*** - The command cannot return the full result in a single execution (likely because it's waiting for a remote process to finish execution). Scheduled commands enable to set the command to try again later, and return the full result when it can. Example use cases are `Sandbox Detonation` and `Autofocus samples search`.

### YAML Prerequisite
* ***Integration***: In the integration yml, under the command root add `polling: true`.
* ***Script***: In the script yml, in the root of the file add `polling: true`.

For an example, see the [Autofocus V2](https://github.com/demisto/content/blob/master/Packs/AutoFocus/Integrations/AutofocusV2/AutofocusV2.py) `autofocus-samples-search` command.

### ScheduleCommand Class
`ScheduleCommand` is an optional class that enables scheduling commands via the command results.

| Arg               | Type   | Description                                                                                                                                                                                |
|-------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| command                        | str    | The command that will run after `next_run_in_seconds` has passed.
| next_run_in_seconds            | int    | How long to wait before executing the command.
| args (optional)                | dict   | Arguments to use when executing the command.
| timeout_in_seconds (optional)  | int    | Number of seconds until the polling sequence will timeout.

When provided to [CommandResults](./code-conventions#commandresults) it will transform its result into a ***schedule result***.
When the time comes for the next command to run, it will be executed.
The scheduled command can return another ***schedule result***, that will schedule another schedule command and so on.

The interval between each run is determined by `next_run_in_seconds`, however it will never be less than 10 seconds.

The schedule sequence will be complete when either one of three terminating actions happen:

1. ***Done*** - The integration will finish a schedule sequence by **not returning** a schedule result. The sequence will continue as long as a schedule result was returned. By returning no schedule result, the sequence will be done.
2. ***Error*** - The schedule sequence will finish with an error when a command in the sequence returns an error result.
3. ***Timeout (automatically handled)*** - The schedule sequence will finish execution with a timeout error when the timeout is reached. XSOAR will return the timeout error entry automatically.

#### Code Example
In the example below, if the `status` is not `complete` then a result with `schedule_config` will be returned which will trigger in 60 seconds a poll for the search. This will be done in the next run as well, and again until its status is complete.

```python
def search_sessions_with_polling_command(args):
    ScheduledCommand.raise_error_if_not_supported()
    interval_in_secs = int(args.get('interval_in_seconds', 60))
    if 'af_cookie' not in args:
        # create new search
        command_results = search_sessions_command(args)
        outputs = command_results.outputs
        af_cookie = outputs.get('AFCookie')
        if outputs.get('Status') != 'complete':
            polling_args = {
                'af_cookie': af_cookie,
                'interval_in_seconds': interval_in_secs,
                'polling': True
            }
            schedule_config = ScheduledCommand(command='autofocus-search-sessions',
                                               next_run_in_seconds=interval_in_secs,
                                               args=polling_args, timeout_in_seconds=600)
            command_results.scheduled_command = schedule_config
        else:
            # continue to look for search results
            args['af_cookie'] = af_cookie
    else:
        # get search status
        command_results, status = sessions_search_results_command(args)
        if status != 'complete':
            # schedule next poll
            polling_args = {
                'af_cookie': args.get('af_cookie'),
                'interval_in_seconds': interval_in_secs,
                'polling': True
            }
            schedule_config = ScheduledCommand(command='autofocus-search-sessions',
                                               next_run_in_seconds=interval_in_secs,
                                               args=polling_args, timeout_in_seconds=600)
            command_results.scheduled_command = schedule_config
    return command_results
```
