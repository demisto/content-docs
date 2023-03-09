---
id: scheduled-commands
title: Scheduled Commands
---

### Available from Cortex XSOAR version 6.2.0 and later.

<img width="533" src="/doc_imgs/integrations/polling-command.png"></img>

A command can schedule the future execution of another command.

The playbook does not proceed to the next task until it is done with all scheduled commands, i.e. until there is no future execution scheduled.
When the playbook is waiting for a command execution it does not use a worker, as workers are only used at the time commands are executed.

Use cases for scheduled commands include:
* ***Polling Flow*** - The command cannot return the full result in a single execution (possibly because a remote process hasn't finished execution). Scheduled commands enable you to try the command again later, and return the full results when available. Examples include `Sandbox Detonation` and `Autofocus samples search`.

### YAML Prerequisite
* ***Integration***: In the integration yml, under the command root, add `polling: true`.
* ***Script***: In the script yml, in the root of the file, add `polling: true`.

## The polling_function Decorator
The `polling_function` decorator can be used to save much of the boilerplate code you would otherwise need to implement yourself to write a polling function.

All functions implementing this decorator must always return a PollResult object.

Note: **args must be the first parameter in the function definition and call.**
#### Code Example
In the example below, we are polling against the `client.call_api` function. 

If the api has a successful response, we return our results wrapped in a PollResult object. 

Otherwise, we return whether to `continue_to_poll` according to the results of the `should_not_keep_polling` function. (Note, either a boolean or a predicate can be passed to continue_to_poll)
```python
@polling_function('cs-falcon-sandbox-result')
def some_polling_command(args: Dict[str, Any], client: Client):
    key = get_api_id(args)
    api_response = client.call_api()
    successful_response = api_response.status_code == 200

    if successful_response:
        success_return = show_successful_response()
        return PollResult(success_return)

    else:
        error_response = CommandResults(raw_response=report_response,
                                        readable_output='API returned an error',
                                        entry_type=entryTypes['error'])

        return PollResult(continue_to_poll=lambda: not should_not_keep_polling(client, key), response=error_response)
```

#### polling_function arguments

| Arg                  | Type | Description                                                              | Default           |
|----------------------|------|--------------------------------------------------------------------------|-------------------|
| name                 | str  | The name of the command                                                  |                   |
| interval             | int  | How many seconds until the next run                                      | 30                |
| timeout              | int  | How long to poll until timeout                                           | 600               |
| poll_message         | str  | The message to display in the war room while polling                     | Fetching Results: |
| polling_arg_name     | str  | The name of the argument to indicate polling should be done              | polling           |
| requires_polling_arg | bool | Whether a polling argument should be expected as one of the demisto args | True              |


#### The PollResult Class
 
| Arg               | Type                  | Description                                                                                     |
|-------------------|-----------------------|-------------------------------------------------------------------------------------------------|
| response          | Any                   | The response of the command in the event of success, or in case of failure but Polling is false |
| continue_to_poll  | Union[bool, Callable] | Wether to return a ScheduledCommand to the server to keep polling.                              |
| args_for_next_run | Dict                  | The arguments to use in the next iteration. Will use the input args in case of None. Important: if you are using this argument, you must add the argument to the .yml file with the attribute "hidden: true", that way the polling command will recognise the argument for the next run.        |
| partial_result    | CommandResults        | CommandResults to return, even though we will poll again                                        |

One last thing regarding the decorator, to Ignore Scheduled War Room Entries (as indicated below) add `hide_polling_output` as a boolean argument to the command in the yml file. 

For example see the [cs-falcon-sandbox-scan](https://github.com/demisto/content/blob/849fee1dfe10907158e5c307dd367284accee2a0/Packs/CrowdStrikeFalconSandbox/Integrations/CrowdStrikeFalconSandboxV2/CrowdStrikeFalconSandboxV2.yml#L65) command.

### A more complicated example

Say we are trying to implement a command that submits a url for analysis and then polls for the result.  The proper way to implement this would be to split this flow into two commands. The submit command, and the find command. The find command will be a polling command, and is useful on its own without the context of submit. We want to perform the submit command once and poll on the get_result command until we have a response.

We will then have the **submit-file** command call the **find-url** command.

```python
@polling_function('find-url')
def find_url_command(args: Dict[str, Any], client: Client):
    api_response = client.call_api(args.get('url')
    successful_response = api_response.status_code == 200

    if successful_response:
        success_return = show_successful_response(api_response)
        return PollResult(success_return)

    else:
        error_response = CommandResults(raw_response=report_response,
                                        readable_output='API returned an error',
                                        entry_type=entryTypes['error'])

        return PollResult(continue_to_poll=True, response=error_response)
        
def submit_url_command(args: Dict[str, Any], client: Client):
    client.submit_url(args.get('url))
    return find_url_command(args, client)
```


<details>
    <summary>If this decorator doesnt cover a specific usecase, read the advanced section: </summary>

### ScheduledCommand Class
`ScheduledCommand` is an optional class that enables scheduling commands via the command results.

| Arg               | Type   | Description                                                                                                                                                                                |
|-------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| command                        | str    | The command that runs after `next_run_in_seconds` has passed.
| next_run_in_seconds            | int    | How long to wait before executing the command.
| args (optional)                | dict   | Arguments to use when executing the command.
| timeout_in_seconds (optional)  | int    | Number of seconds until the polling sequence timeouts.

When provided to [CommandResults](./code-conventions#commandresults) it transforms the result into a ***schedule result***.
After the `next_run_in_seconds` delay, the command will be executed.
The scheduled command can return another ***schedule result***, that schedules another scheduled command and so on.

The interval between each run is determined by `next_run_in_seconds`, however it will never be less than 10 seconds.

The schedule sequence completes when any one of three terminating actions occur:

1. ***Done*** - The integration finishes a schedule sequence by **not returning** a schedule result. Otherwise, the sequence continues as long as a schedule result is returned. 
2. ***Error*** - The schedule sequence finishes with an error when a command in the sequence returns an error result.
3. ***Timeout (automatically handled)*** - The schedule sequence finishes execution with a timeout error when the timeout is reached. Cortex XSOAR will return the timeout error entry automatically.

#### How to Ignore Scheduled War Room Entries
You can prevent printing the `Scheduled Entries` to the War Room when there is no output. However, this is possible only for entries that are subsequent to the first entry, since the first entry is expected to provide context about the expected final result. In other words, the first entry is always expected to have a result, but the entries that come after it may be empty until a non-scheduled result is returned.

It makes sense to prevent printing to the War Room until the final result is available, since the `schedule` icon provides the scheduling context via its tooltip
.
To prevent War Room entries while using a `ScheduledCommand`, return a `CommandResults` with just a `scheduled_command`. For example:
```python
return_results(CommandResults(scheduled_command=scheduled_command))
```

#### Code Example
In the example below, if the `status` is not `complete` then a result with `scheduled_command` is returned. After `interval_in_seconds` seconds (60 by default), the result schedules a poll for the search status and result. This is done in the next run as well, and repeats until the status is complete.

```python
def run_polling_command(args: dict, cmd: str, search_function: Callable, results_function: Callable):
    interval_in_secs = int(args.get('interval_in_seconds', 60))
    if 'af_cookie' not in args:
        # create new search
        command_results = search_function(args)
        outputs = command_results.outputs
        af_cookie = outputs.get('AFCookie')
        if outputs.get('Status') != 'complete':
            polling_args = {
                'af_cookie': af_cookie,
                'interval_in_seconds': interval_in_secs,
                'polling': True,
                **args
            }
            scheduled_command = ScheduledCommand(
                command=cmd,
                next_run_in_seconds=interval_in_secs,
                args=polling_args,
                timeout_in_seconds=600)
            command_results.scheduled_command = scheduled_command
            return command_results
        else:
            # continue to look for search results
            args['af_cookie'] = af_cookie
    # get search status
    command_results, status = results_function(args)
    if status != 'complete':
        # schedule next poll
        polling_args = {
            'af_cookie': args.get('af_cookie'),
            'interval_in_seconds': interval_in_secs,
            'polling': True,
            **args
        }
        scheduled_command = ScheduledCommand(
            command=cmd,
            next_run_in_seconds=interval_in_secs,
            args=polling_args,
            timeout_in_seconds=600)

        # result with scheduled_command only - no update to the war room
        command_results = CommandResults(scheduled_command=scheduled_command)
    return command_results
```

### How to use with demisto.executeCommand
When using `demisto.executeCommand()` a command or a script that returns schedule result **will not schedule** a command execution. However, its result will contain the schedule metadata.

It's recommended to create a new result with `ScheduledCommand` class to schedule a future script execution.

**Advanced users** can extract the schedule metadata, and use it when scheduling the future script execution.
The schedule metadata fields are: `PollingCommand`, `NextRun`, `Timeout` `PollingArgs` (for reference see: [demisto.results](./code-conventions#deprecated---demistoresults)).

#### Code Example
Given the command `autofocus-search-samples`, that may return a ***schedule result*** (if it has `Metadata.polling` in its fields, and `af_cookie` in its `Contents`), or a non-scheduled result, the wrapping script `AutoFocusSearchScript` can handle it like so:
```python
args = demisto.args()
samples_result = demisto.executeCommand('autofocus-search-samples', **args)
script_results = []
if samples_result and not isError(samples_result[0]):
    if demisto.get(samples_result[0], 'Metadata.polling'):  # result has polling metadata
        # extract the af_cookie from the results
        af_cookie = demisto.get(samples_result[0], 'Contents.AFCookie')
        if not af_cookie:
            raise ValueError('af_cookie is missing from schedule result.')
        schedule_args = {
            'af_cookie': af_cookie,
            'polling': True
        }
        schedule_command = 'AutoFocusSearchScript'
        # take the timeout and next_run from the polling fields
        schedule_timeout = demisto.get(samples_result[0], 'Timeout')
        schedule_next_run = demisto.get(samples_result[0], 'NextRun')
        scheduled_command = ScheduledCommand(
            command=schedule_command,
            next_run_in_seconds=int(schedule_next_run),
            args=schedule_args,
            timeout_in_seconds=int(schedule_timeout)
        )
        readable_output = "Autofocus search created successfully."
        script_results.append(CommandResults(
            readable_output=readable_output,
            scheduled_command=scheduled_command
        ))
    else:
        readable_output = "Autofocus search is done, see result below."
        script_results.append(CommandResults(readable_output=readable_output))
        script_results.extend(samples_result)
return_results(script_results)
```
</details>
