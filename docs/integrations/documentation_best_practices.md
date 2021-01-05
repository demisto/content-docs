---
id: documentation_tips
title: Documentation - Best Practices
---

## New entities descriptions in the RN
When a new integration/script/playbook is first released, the release notes are generated automatically with the 'description' field in the entity's yml file.

### For playbook and scripts, use the following guideline:
- Should start with the verb that describes what the entity does.
- There's a limited space for descriptions, so we don't want to waste space (and time) with words that don't matter. 

Bad example: The XYZ playbook is a playbook that...
  We should shorten the description to what matters most.  
Good example: Executes as a sub-playbook and enriches indicators from the list.    

**More examples:**

- **Access Investigation - Generic - NIST**  
Investigates an access incident by gathering user and IP information, and handling the incident based on the stages in "Handling an incident - Computer Security Incident Handling Guide" by NIST.

- **PAN-OS - Block Domain - External Dynamic List**  
Blocks domains using Palo Alto Networks Panorama or Firewall External Dynamic Lists.

- **Convert file hash to corresponding hashes**  
Enables you to get all of the corresponding file hashes for a file even if there is only one hash type available.

- **Tanium - Get Saved Question Result**  
Uses generic polling to get saved question results.

- **Endpoint Malware Investigation - Generic**  
This playbook is triggered by a malware incident from an Endpoint type integration. The playbook performs enrichment, detonation, and hunting within the organization, and remediation on the malware.

- **NIST - Handling an Incident Template**  
This playbook contains the phases to handling an incident as described in the Handling an Incident section of NIST - Computer Security Incident Handling Guide.


### For integrations:  
The description should summarize all of the currently supported endpoints into a sentence that users can digest.

**For example:**  
- Use the *IronDefense* integration to rate alerts, update alert statuses, add comments to alerts, and to report observed bad activity. 
- Use the *Gmail* integration to send/receive emails, manage user accounts, and listen to specified mailboxes and folders. 

## Detailed Description (<integration_name>_description.md)
In the detailed description, we want to provide the supported use cases of the integration, and any important things that the customers need to know. Give as much information as you think the user of this integration needs to succeed. Permission levels, credentials, keys, etc.  
If there are permissions required on the integration level, list them in the description. If commands have separate permissions, mention that fact in the description, but document the required permission on the command level.

**Common cases are:**

- How to get credentials
- How to get API Key/Secret
- How to get Applications ID

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
