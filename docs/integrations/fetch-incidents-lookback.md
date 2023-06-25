---
id: fetch-incidents-lookback
title: Fetch Missing Incidents with Generic Lookback Methods
---

### Use case
During a ***fetch-incidents*** run, some edge-case scenarios may cause missing incidents from the third-party product.  
The most common scenarios are:
* Indexing issues in the product: For example, if incident A was created before incident B and only B was indexed, ***fetch-incidents*** will fetch only B and not A. If A was indexed after the fetch was called, the next fetch will fetch only from the created time of B.
* An update in the incident information: Some implementations of ***fetch-incidents*** use a query filter to fetch only specific incidents. If initially an incident did not match the query (meaning, it was not fetched) but at some point was updated so that it now matches the query, ***fetch-incidents*** will not pull the updated incident because the time to fetch it already passed.

### Solution
The *look_back* parameter enables configuring how far back in time (in minutes) ***fetch-incidents*** will look to get the incidents that were created a while ago but indexed a few minutes ago.  
In addition, the **LastRun** object stores the following fields to be used by the lookback methods:
- **time** - The time to fetch the next fetch call (as in a regular fetch).
- **limit** - The maximum number of incidents retrieved in the next fetch. If the current fetch run has the same start_time as the last fetch (determined in **get_fetch_run_time_range()**), this field will be increased by the limit instance parameter value, and then incidents retrieved in the last fetch will be filtered out.
- **found_incident_ids** - The IDs of incidents fetched in previous runs. Used for filtering duplicates in the next runs.

### Lookback Methods
Lookback is implemented using the following generic methods. For more information about lookback generic methods, see [CommonServerPython](https://xsoar.pan.dev/docs/reference/api/common-server-python).

- **get_fetch_run_time_range()** - Using the last run object and other parameters, this method calculates and retrieves the time range in which to fetch.  
   If the *look_back* parameter is defined, then the start time will always be greater than or equal to `now - look_back`.

- **filter_incidents_by_duplicates_and_limit()** - After getting the incidents using the third-party API call, you need to filter out the duplicate incidents.  
From the example above, after incident A is indexed the next fetch will get incidents A and B, but B must be filtered out since it was already fetched.  
**Note:**
If after filtering duplicates you have more incidents than the limit, ***fetch-incidents*** will get only up to the limit number of incidents.

- **update_last_run_object()** - Updates the existing last run object.  
The function updates the found IDs from the **get_found_incident_ids** function and also updates the new time and limit from the  **create_updated_last_run_object** function and returns the updated last run object.

### Helper Methods  

The following helpers are used in the above lookback methods, and should not be used when implementing ***fetch-incidents*** in the integration.

- **get_latest_incident_created_time()** - Given a list of incidents and the created time field, this function will return the latest incident created time.

- **remove_old_incidents_ids()** - Removes old incident IDs from the last run object to avoid overloading.

- **get_found_incident_ids()** - Returns a list of the new fetched incident IDs. This is saved in the last run object and used to filter duplicates in the next ***fetch-incidents*** call.

- **create_updated_last_run_object()** - Creates a new last run object with a new time and limit for the next fetch.


### Example Fetch with Lookback
```python
def fetch_incidents(params: dict):

    incidents = []

    fetch_limit_param = params.get('limit')
    look_back = int(params.get('look_back', 0))
    first_fetch = params.get('first_fetch')
    time_zone = params.get('time_zone', 0)

    last_run = demisto.getLastRun()

    # If the start time in the current fetch is the same as the start time in the previous fetch, the fetch_limit may be different from the fetch_limit_param.
    fetch_limit = last_run.get('limit') or fetch_limit_param

    # It's important to get here the end_fetch_time to pass it into the update_last_run_object function.
    start_fetch_time, end_fetch_time = get_fetch_run_time_range(last_run=last_run, first_fetch=first_fetch,
                                                                look_back=look_back, timezone=time_zone)

    # Here you insert functions for building the query and sending the API call to get the incidents. For example:
    query = build_query(start_fetch_time, end_fetch_time, fetch_limit)
    incidents_res = get_incidents_request(query)

    incidents = filter_incidents_by_duplicates_and_limit(incidents_res=incidents_res, last_run=last_run,
                                                         fetch_limit=fetch_limit_param, id_field='incident_id')

    last_run = update_last_run_object(last_run=last_run, incidents=incidents, fetch_limit=fetch_limit_param,
                                      start_fetch_time=start_fetch_time, end_fetch_time=end_fetch_time, look_back=look_back, 
                                      created_time_field='created', id_field='incident_id')

    demisto.incidents(incidents)
    demisto.setLastRun(last_run)
```

### Notes:
- Fetching incidents is flexible and you can use the various functions according to your needs.
- You can also use the generic methods for regular ***fetch-incidents*** without lookback.
- If the *look_back* value is increased by *k* minutes, you may get duplicate incidents for the *k* minutes that overlap with the previous fetch.
