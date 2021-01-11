---
id: documentation_tips
title: Documentation - Best Practices
---

This document describes the desired documentation standards in XSOAR content entities, and contains examples that can be very useful when writing documentation.

## Entities Description Field
### For playbook and scripts, use the following guideline:
- Should start with the verb that describes what the entity does.
- There's a limited space for descriptions, so we don't want to waste space (and time) with words that don't matter. 

Bad example: The XYZ playbook is a playbook that...
  We should shorten the description to what matters most.  
Good example: Executes as a sub-playbook and enriches indicators from the list.    

**More examples:**  

- Investigates an access incident by gathering user and IP information, and handling the incident based on the stages in "Handling an incident - Computer Security Incident Handling Guide" by NIST.
- Blocks domains using Palo Alto Networks Panorama or Firewall External Dynamic Lists.
- Enables you to get all of the corresponding file hashes for a file even if there is only one hash type available.
- Uses generic polling to get saved question results.

### For integrations:  
The description should summarize all of the currently supported endpoints into a sentence that users can digest.

**For example:**  
- Use the *IronDefense* integration to rate alerts, update alert statuses, add comments to alerts, and to report observed bad activity. 
- Use the *Gmail* integration to send/receive emails, manage user accounts, and listen to specified mailboxes and folders. 

## Fetch Incidents/Indicators section
Common parameters for this section are:

| Parameter name | Display name |
|---|---|
| First fetch | `First fetch timestamp (<number> <time unit>, e.g., 12 hours, 7 days, 3 months, 1 year)` |
| Fetch size | `The maximum number of results to return per fetch. The default is 50.` |

- Any other important information for fetching incidents from the service should be added as a parameter.

It’s important to add documentation about the fetch function (especially the first fetch) that is not obvious from looking at the integration. This could be done in the README file or the detailed description.   
For example: `By default, the integration will import PagerDuty incidents data as Demisto incidents. All incidents created in the minute prior to the configuration of Fetch Incidents and up to the current time will be imported.`

## Common Integration Parameters
The most commonly used integration parameters:

| Parameter name | Display name |
|---|---|
| API token/key | API Token/ API Key/ API Secret. This parameter should match the product. |
| URL | Server URL |
| insecure | Trust any certificate (not secure) |
| proxy |  Use system proxy settings |
| Threshold | The minimum number/severity/score ... |
| Limit | The maximum number of... |


## Common Command Arguments
| Argument type | Description Template | Example |
|---|---|---|
| Boolean | If “true”... If “false”... Default is “true”. | If “true”, will return full results. If “false”, will return partial results. Default is “true”. |
| String | The... | The User name of the user whose endpoint is being blocked. |
| Integer | - The number of...\n  - The total number of…\n - The maximum number\n | - The number of times the script attempted to run. - The total number of matches. - The maximum number of results to return. | 
| Array | A comma-separated list of | A comma-separated list of IP addresses... |
| List of predetermined options | The…. Can be “optionA”, “optionB”, or  “optionC”. | The severity oh the incident to fetch. Can be "Low", "High" or "Critical" | 


## Outputs
Try to be as specific as possible regarding what the output really does.  
For example, if the context path is:  `Tripwire.Version.exists`  
A bad description will be: `Exists of element versions.`  
A good description will be: `True if the version of the element exists.`

| Argument type | Description Template | Example |
|---|---|---|
| Boolean | If “true”... If “false”... Default is “true”. | If “true”, will return full results. If “false”, will return partial results. Default is “true”. |
| String | The... | The User name of the user whose endpoint is being blocked. |
| Integer | - The number of...\n  - The total number of…\n - The maximum number\n | - The number of times the script attempted to run. - The total number of matches. - The maximum number of results to return. | 
| Array | A comma-separated list of | A comma-separated list of IP addresses... |
| List of predetermined options | The…. Can be “optionA”, “optionB”, or  “optionC”. | The severity oh the incident to fetch. Can be "Low", "High" or "Critical" | 
| Unknown  | - An array of...\n - A list of…\n -A dictionary of... | A list of indicators associated to.. | 
| Date | - The date and time that...\n - The date and time when... | The date and time when the indicator was last updated. The date format is: YYYYMMDDThhmmss, where "T" denotes the start of the value for time, in UTC time. |
