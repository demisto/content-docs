---
id: api_execution_metric_reporting
title: API Execution Metric Reporting
---

Cortex XSOAR version 6.8 adds support for API Execution Metric Reporting.

## Supported Server Version
API Execution Metric Reporting is supported from version 6.8.


## Implementing API Execution Metric Reporting
For metric data to be stored, an integration must return an `execution_metrics` command result, as part of the returned response.

An example of how a command may implement the `ExecutionMetrics` object is as follows:
```python
# An instance of ExecutionMetrics must be instantiated to begin capturing metric results.
execution_metrics = ExecutionMetrics()
command_results = []

urls = ['sample_url.com/successful', 'sample_url.com/general-error', 'sample_url.com/ratelimited']

for url in urls:
    # Your implementation will likely have it's own logic regarding what the result is of an API call.
    if url.is_success:
        # When a result is to be recorded, it's necessary to increment the metric by a given amount. 
        execution_metrics.success += 1
    elif url.is_general_error:
        # Many metric types are supported including a generic error.
        execution_metrics.general_error += 1
    elif url.is_quota_error:
        # As well as some specific error types.
        execution_metrics.quota_error += 1
    command_results.append(
        CommandResults(readable_output=f"Item - {url} has been processed")
    )
# When a command run is complete, simply return the metrics object as a command result.
command_results.append(execution_metrics.metrics)
```

## Rate Limiting
If a service that an integration is being developed implements API throttling, using [Scheduled Commands](./../integrations/scheduled-commands) in addition to metric reporting, it can help you to have insight into your API usage. With these reported metrics, you can make informed decisions regarding your service licenses.

The following example shows you how this implementation could look like.

```python
# An instance of ExecutionMetrics must be instantiated to begin capturing metric results.
execution_metrics = ExecutionMetrics()
command_results = []
items_to_schedule = []

# Enrichment commands will often accept an array of items.
urls = argToList(demisto.args().get('url'))
for url in urls:
    demisto.args()['url'] = url
    # Each item should be processed.
    response, metrics = submit_url(client, url)
    if response.get('is_error'):
        # Report the errors depending on your implementation
        execution_metrics.general_error += 1
        continue
    # If an item is part of a scheduled command, try to add logic which will prevent metrics from being reported for each retry.
    if metrics == MetricTypes.QUOTA_ERROR:
        if not command.is_polling():
            execution_metrics.quota_error += 1
            continue
        # Add the items which failed to a list to be scheduled.
        items_to_schedule.append(url)
        continue
    # Don't forget to log your successes too.
    execution_metrics.success += 1
# From Cortex XSOAR version 6.1 and above, scheduling is supported. It's best to check if a command can be scheduled.
if supports_polling():
    if len(items_to_schedule) > 0:
        # If a command can be scheduled, implement some logic which is in line with the service's usage recommendations.
        scheduled_items = schedule_polling(items_to_schedule)
        command_results.append(scheduled_items)
# Finally, make sure to add the execution metrics to the command results.
if execution_metrics.metrics is not None and execution_metrics.is_supported():
    command_results.append(execution_metrics.metrics)
```

If an item has been scheduled and after exhausting the permitted retries, a `TimeoutError` metric is automatically reported for the quantity of `ItemsRemaining`, which is reported in the Scheduled Command.
## Dashboards
API Execution Metric reporting was implemented to present the information via a dashboard to help provide insight into an integration's usage of an API service. 

In general, if your integration is using a service where the results of the API calls may be of importance to determine usage, it is best practice to also include a widget in the content pack.

## Permitted Metric Types
Each metric type results in additional metric records being created in the telemetry database. To prevent excessive records from being created, metric types other than those defined in the default list are automatically converted to a `GeneralError`.

| Metric Type  | Description                               |
|--------------|-------------------------------------------|
| GeneralError | A generic error type.                     |
| OutOfQuota   | Out of quota metric type.                 |
| AuthError    | Authentication error type.                |
| ServiceError | Service error type.                       |
| RetryTimeout | Failed to retrieve result before timeout. |
| Successful   | A successful metric type.                 |

## Special Server Configurations
- `telemetry.realtime.metric.types.allow.all` enables / disables metric types other than those permitted by default. - (default is **disabled**)
