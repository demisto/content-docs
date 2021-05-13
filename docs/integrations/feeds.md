---
id: feeds
title: Feed Integrations
---
Server version 5.5.0 adds support for Feed integrations. Feed integrations allow fetching indicators from feeds, for example TAXII,
AutoFocus, Office 365, and so on.

An example Feed integration can be seen [here](https://github.com/demisto/content/tree/master/Packs/FeedOffice365/Integrations/FeedOffice365).

Feed integrations are developed the same as other integrations. They provide a few extra configuration parameters and APIs.


## Naming Convention
Feed Integration names (`id`, `name` and `display` fields) should end with the word **Feed**. This consistent naming convention ensures that users can easily understand what the integration is used for.

## Supported Server Version
A Feed integration's YAML file _must_ have the following field `fromversion: 5.5.0`. This is because Feed integrations are only supported from server version 5.5.0 and onwards.


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
    reputation.
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
  additionalinfo: Reliability of the source providing the intelligence data.
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

## Incremental Feeds
Incremental Feeds pull only new or modified indicators that have been sent from the 3rd party vendor. As the determination if the indicator is new or modified happens on the 3rd-party vendor's side, and only indicators that are new or modified are sent to Cortex XSOAR, all indicators coming from these feeds are labeled new or modified.

Examples of incremental feeds usually include feeds that fetch based on a time range. For example, a daily feed which provides new indicators for the last day or a feed which is immutable and provides indicators from a search date onwards.

To indicate to the Cortex XSOAR server that a feed is incremental, add the configuration parameter:  `feedIncremental`. If the user is not able to modify this setting, set the parameter to **hidden** with a `defaultValue` of **true**. For example:
```yml
- additionalinfo: Incremental feeds pull only new or modified indicators that have been sent from the integration. The determination if the indicator is new or modified happens on the 3rd-party vendor's side, so only indicators that are new or modified are sent to Cortex XSOAR. Therefore, all indicators coming from these feeds are labeled new or modified.
  defaultvalue: 'true'
  display: Incremental feed
  hidden: true
  name: feedIncremental
  required: false
  type: 8
```

If the feed supports both incremental and non-incremental modes, provide the configuration parameter as non-hidden. Thus, a user will be able to modify this settings as is fit. In the feed code inspect the `feedIncremental` parameter to perform the proper fetch logic.

Code examples of Incremental Feeds:
* [AutoFocus Daily Feed](https://github.com/demisto/content/blob/master/Packs/AutoFocus/Integrations/FeedAutofocusDaily/FeedAutofocusDaily.yml)
* [DHS Feed](https://github.com/demisto/content/blob/master/Packs/FeedDHS/Integrations/DHS_Feed/DHS_Feed.yml)

## Commands
Every Feed integration will at minimum have three commands:
- `test-module` - this is the command that is run when the `Test` button in the configuration panel of an integration is clicked.
- `<product-prefix>-get-indicators` - where `<product-prefix>` is replaced by the name of the Product or Vendor source providing the feed. So for example, if you were developing a feed integration for Microsoft Intune, this command might be called `msintune-get-indicators`. This command should fetch a limited number of indicators from the feed source and display them in the war room.
- `fetch-indicators` - this command will initiate a request to the feed endpoint, format the data fetched from the endpoint to conform to Cortex XSOAR's expected input format, and create new indicators. If the integration instance is configured to `Fetch indicators`, then this is the command that will be executed at the specified `Feed Fetch Interval`.

## API Command: demisto.createIndicators()
Use the `demisto.createIndicators()` function  when the `fetch-indicators` command is executed. Let's look at an example `main()` from an existing Feed integration.
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
* `"value"` - _required_. The indicator value, e.g., `"8.8.8.8"`.
* `"type"` - _required_. The indicator type (types as defined in Cortex XSOAR), e.g., `"IP"`. One can use the `FeedIndicatorType` class to populate this field. This class, which is imported from `CommonServerPython` has all of the indicator types that come out of the box with Cortex XSOAR. It appears as follows,
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
   * To inspect a specific field - tick the box near the field name and click `Edit`. Note that when inspecting a field, it's `cliname` is listed as `machinename`.
* `"relationships"` - _optional_. This list should contain a dictionary of values of the relationships. 
There are two way to create relationships:
   1. As part of creating an indicator.
   2. Creating only relationships without an indicator.

   For both ways use `demisto.createIndicators` 

Steps to create the relationships:
1. Create an `EntityRelationship` object with the relationships data. If more than one relationship exists, create a list and append all of the `EntityRelationship` objects to it.
   
   The name of the relationships should be one of the exisitng relationships : https://xsoar.pan.dev/docs/reference/api/common-server-python#relationships

   For more information, see: https://xsoar.pan.dev/docs/reference/api/common-server-python#entityrelationship
2. Use the `to_indicator()` function of the object to convert each object (or a list of objects) to the required format.
3. If the relationships is part of an indicator:
    
    - Add to the `relationship` key of the indicator the list after running `to_indicator`.

   If the relationship is not attached to an indicator:
   - We will need to create a dummy indicator whose value is `$$DummyIndicator$$` and add the relationships key with the list after running `to_indicator`.
   ```
   {
        "value": "$$DummyIndicator$$",
        "relationships": relationships_list
    }
   ```

![Indicator Fields in Cortex XSOAR](https://raw.githubusercontent.com/demisto/content-docs/b202510c98d7812711b7323ad21e9bcc23e0983d/static/img/Cortex%20XSOAR%20indicator%20fields.png)

*Note:* In indicators of type "File", if you have multiple hash types for the same file (i.e., MD5, SHA256, etc.), you can use the corresponding `"fields"` to associate all hashes to the same object. The supported fields are: `md5`, `sha1`, `sha256`, `sha512`, `ssdeep`. You can use any of the aforementioned hash types as the indicator value for an indicator of type "File".
