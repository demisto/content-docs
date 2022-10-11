---
id: dbot
title: Reputation and DBotScore
---

DBot is the Cortex XSOAR machine learning bot, which ingests information about indicators to determine if they are malicious. Since DBot requires a very specific dataset, you must format the data according to this article. As described in the [generic reputation command](./integrations/generic-commands-reputation#background-and-motivation) article, when developing an integration that implements a generic reputation command, it is necessary also to create a corresponding DBot score object.

## Context Format
```python
"DBotScore": {
  "Indicator" : "foo@demi.com",
  "Type": "email",
  "Vendor": "JoeSecurity",
  "Score": 3,
  "Reliability": "A - Completely reliable"
} 
```

The DBot score must be at the root level of the context and contain **all** the required keys, as listed below.

| Key | Meaning | Required
| --- | --- | --- |
| Indicator | The indicator value. | Required |
| Type | The indicator type. Can be: ip, file, email, url, cve, account, cider, domainglob, certificate, or cryptocurrency. | Required |
| Vendor | The vendor reporting the score of the indicator.| Required |
| Score | An integer regarding the status of the indicator. See [Score Types](#score-types) below.| Required |
| Reliability | The reliability of the source providing the intelligence data. See [Reliability Level](#reliability-level) below.| Required |
| Message | Optional message to show an API response. For example, `"Not found"`. | Optional |

## Reliability Level
When merging indicators, the reliability of an intelligence-data source influences the reputation of an indicator and the values for
indicator fields. Integration that outputs a DBotScore object, and hence defines each indicator's reliability, should allow the user to manually configure the default reliability for the created indicator DBotScore. This is done by adding a **Source Reliability** parameter to the integration which is later used when creating the object.
**NOTE:** The values are case sensitive.

``` 
  A+ - 3rd party enrichment  
  A - Completely reliable 
  B - Usually reliable  
  C - Fairly reliable  
  D - Not usually reliable  
  E - Unreliable  
  F - Reliability cannot be judged  
 ```

## Score Types
Dbot uses an integer to represent the reputation of an indicator.

| Number | Reputation |
| --- | --- |
| 0 | Unknown |
| 1 | Good |
| 2 | Suspicious |
| 3 | Bad |

## Unknown
An unknown score can be interpeted in the following ways: 

1. The vendor returns an "Unknown" score for the indicator.
2. The vendor returns nothing on the indicator.

In both cases, you mark the indicator score as Unknown, but in the second case you need to add a message: `"No results found"`.

## Malicious
If the DBot score is returned as a `"3"` or `"Bad"`, you need to add to the context that a malicious indicator was found. To do this, add an additional key to the `URL`, `IP`, or `File` context called `"Malicious"` as shown below:

```python
demisto.results({
     "Type": entryTypes["note"],
     "EntryContext": {
        "URL": {
            "Data": "STRING, The URL",
            "Malicious": {
                "Vendor": "STRING, Vendor reporting the malicious status",
                "Description": "STRING, Description of the malicious url"
            }
        },
         "File": {
            " SHA1/MD5/SHA256": "STRING, The File Hash",
            "Malicious": {
                "Vendor": "STRING, Vendor reporting the malicious status",
                "Description": "STRING, Description of the malicious hash"
            }
        },
         "IP": {
            "Address": "STRING, The IP",
            "Malicious":{
                "Vendor": "STRING, Vendor reporting malicious",
                "Description": "STRING, Description about why IP was determined malicious"
        },
        },
         "Domain": {
            "Name": "STRING, The Domain",
            "Malicious": {
                "Vendor": "STRING, Vendor reporting the malicious status",
                "Description": "STRING, Description of the malicious domain"
            }
        }
    }
})
```

`Malicious` has two key values: `"Vendor"` and `"Description"`. The `Vendor` is the entity reporting the malicious indicator. The `Description` explains briefly what was found. For example:


```python
"URL": {
    "Data": "http://viruswarehouse.com",
    "Malicious": {
        "Vendor": "VirusTotal",
        "Description": "Wannacry ransomware detected"
    }
}
```

**NOTE**: It is not possible to use the Cortex XSOAR Transformers (DT) within the DBot score context. For example, using the following in your DBot context, will not work:

```python
DBotScore(val.Indicator == obj.Indicator)
```
