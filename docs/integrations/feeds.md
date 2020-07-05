---
id: feeds
title: Feed Integrations
---
Server version 5.5.0 adds support for Feed Integrations. Feed Integrations allow fetching indicators from feeds, for example TAXII,
AutoFocus, Office 365, and so on.

An example Feed Integration can be seen [here](https://github.com/demisto/content/tree/master/Packs/FeedOffice365/Integrations/FeedOffice365).

Feed Integrations are developed the same as other Integrations. They provide a few extra configuration parameters and APIs.


## Naming Convention
Feed Integration names (`id`, `name` and `display` fields) should end with the word **Feed**. This consistent naming convention ensures that users can easily understand what the Integration is used for.

## Supported Server Version
Feed Integration's YAML file _must_ have the following field `fromversion: 5.5.0`. This is because Feed Integrations are only supported from Server version 5.5.0 and onwards.


## Required Parameters
Every Feed integration should have the following parameters in the integration YAML file:
```yml
- display: Fetch indicators
  name: feed
  defaultvalue: true
  type: 8
  required: false
- display: Indicator Reputation
  name: feedReputation
  defaultvalue: feedInstanceReputationNotSet
  type: 18
  required: false
  options:
  - None
  - Good
  - Suspicious
  - Bad
  additionalinfo: Indicators from this integration instance will be marked with this
    reputation
- display: Source Reliability
  name: feedReliability
  defaultvalue: F - Reliability cannot be judged
  type: 15
  required: true
  options:
  - A - Completely reliable
  - B - Usually reliable
  - C - Fairly reliable
  - D - Not usually reliable
  - E - Unreliable
  - F - Reliability cannot be judged
  additionalinfo: Reliability of the source providing the intelligence data
- display: ""
  name: feedExpirationPolicy
  defaultvalue: indicatorType
  type: 17
  required: false
  options:
  - never
  - interval
  - indicatorType
  - suddenDeath
- display: ""
  name: feedExpirationInterval
  defaultvalue: "20160"
  type: 1
  required: false
- display: Feed Fetch Interval
  name: feedFetchInterval
  defaultvalue: "240"
  type: 19
  required: false
- display: Bypass exclusion list
  name: feedBypassExclusionList
  defaultvalue: ""
  type: 8
  required: false
  additionalinfo: When selected, the exclusion list is ignored for indicators from
    this feed. This means that if an indicator from this feed is on the exclusion
    list, the indicator might still be added to the system.
```
The `defaultvalue` of the `feedReputation`, `feedReliability`, `feedExpirationPolicy`, and `feedFetchInterval` parameters should be set according to the qualities associated with the feed source for which you are developing a feed integration.

## Commands
Every Feed Integration will at minimum have three commands:
- `test-module` - this is the command that is run when the `Test` button in the configuration panel of an integration is clicked.
- `<product-prefix>-get-indicators` - where `<product-prefix>` is replaced by the name of the Product or Vendor source providing the feed. So for example, if you were developing a feed integration for Microsoft Intune this command might be called `msintune-get-indicators`. This command should fetch a limited number of indicators from the feed source and display them in the war room.
- `fetch-indicators` - this command will initiate a request to the feed endpoint, format the data fetched from the endpoint to conform to Cortex XSOAR's expected input format and create new indicators. If the integration instance is configured to `Fetch indicators`, then this is the command that will be executed at the specified `Feed Fetch Interval`.

## API Command: demisto.createIndicators()
Use the `demisto.createIndicators()` function  when the `fetch-indicators` command is executed. Let's look at an example `main()` from an existing Feed Integration.
```python
def main():
    params = demisto.params()

    client = Client(params.get('insecure'),
                    params.get('proxy'))

    command = demisto.command()
    demisto.info(f'Command being called is {command}')
    # Switch case
    commands = {
        'test-module': module_test_command,
        'tor-get-indicators': get_indicators_command
    }
    try:
        if demisto.command() == 'fetch-indicators':
            indicators = fetch_indicators_command(client)
            # we submit the indicators in batches
            for b in batch(indicators, batch_size=2000):
                demisto.createIndicators(b)
        else:
            readable_output, outputs, raw_response = commands[command](client, demisto.args())
            return_outputs(readable_output, outputs, raw_response)
    except Exception as e:
        raise Exception(f'Error in {SOURCE_NAME} Integration [{e}]')
```
The `batch` function is imported from `CommonServerPython`. We see that indicators are returned from calling `fetch_indicators_command` and are passed to `demisto.createIndicators` in batches.

### Indicator Objects
Indicator Objects passed to `demisto.createIndicators`. Let's look at an example,
```python
{
    "value": value,
    "type": raw_json['type'],
    "rawJSON": raw_json,
    "fields": {'recordedfutureevidencedetails': lower_case_evidence_details_keys},
    "score": score
}
```
Let's review the object key and values.
* `"value"` - _required_. The indicator value, e.g. `"8.8.8.8"`.
* `"type"` - _required_. The indicator type (types as defined in Cortex XSOAR), e.g. `"IP"`. One can use the `FeedIndicatorType` class to populate this field. This class, which is imported from `CommonServerPython` has all of the indicator types that come out of the box with Cortex XSOAR. It appears as follows,
    ```python
    class FeedIndicatorType(object):
        """Type of Indicator (Reputations), used in TIP integrations"""
        Account = "Account"
        CVE = "CVE"
        Domain = "Domain"
        DomainGlob = "DomainGlob"
        Email = "Email"
        File = "File"
        FQDN = "Domain"
        MD5 = "File MD5"
        SHA1 = "File SHA-1"
        SHA256 = "File SHA-256"
        Host = "Host"
        IP = "IP"
        CIDR = "CIDR"
        IPv6 = "IPv6"
        IPv6CIDR = "IPv6CIDR"
        Registry = "Registry Key"
        SSDeep = "ssdeep"
        URL = "URL"
    ```
* `"rawJSON"` - _required_. This dictionary should contain the `"value"` and `"type"` fields as well as any other unmodified data returned from the feed source about an indicator.
* `"fields"` - _optional_. A dictionary that maps values to existing indicator fields defined in Cortex XSOAR where the key is the `cliname` of an indicator field. 
   To see the full list of possible fields:
   * Go to the `Settings` section in Cortex XSOAR.
   * Click the `ADVANCED` tab. 
   * Go to the `Fields` section and filter `indicator` fields.
   * To inspect a specific field - tick the box near the field name and click `Edit.
* `"score"` - _optional_. The reputation score to assign to the indicator object, scores range from 0 to 3 where 0 - None, 1 - Good, 2 - Suspicious, and 3 - Bad. Assign a value only if you wish to explicitly assign a score to an indicator in your code. Typically, indicator reputation is set at a Feed Integration configuration level by setting the `Indicator Reputation` parameter when configuring an instance.

*Note:* In indicators of type "File", if you have multiple hash types for the same file (i.e. MD5, SHA256, etc.), you can use the corresponding `"fields"` to associate all hashes to the same object. The supported fields are: `md5`, `sha1`, `sha256`, `sha512`, `ssdeep`. You can use any of the aforementioned hash types as the indicator value for an indicator of type "File".
