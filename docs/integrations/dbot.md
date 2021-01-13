---
id: dbot
title: Reputation and DBotScore
---

DBot is the Cortex XSOAR machine learning bot which ingests information about indicators to determine if they are malicious or not. Since DBot requires a very specific dataset, we must format our data as per this article.

## Context Format
```python
"DBotScore": {
  "Indicator" : "foo@demi.com",
  "Type": "email",
  "Vendor": "JoeSecurity",
  "Score": 3,
  "Reliability": "A: Completely reliable"
} 
```

The DBot score must be at the root level of the context and contain **all** the required keys as listed below.

| Key | Meaning | Required
| --- | --- | --- |
| Indicator | Can be: IP, SHA1, MD5, SHA256, Email, or Url | Required |
| Type | Can be: ip, file, email, or url | Required |
| Vendor | This is the vendor reporting the score of the indicator| Required |
| Score | An int representing the status of the indicator. See Score Types below| Required |
| Reliability | Reliability of the source providing the intelligence data. See Reliability Levels below| Optional |


## Reliability Level
The reliability of an intelligence-data source influences the reputation of an indicator and the values for
indicator fields when merging indicators.  
The values are case sensitive.

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
Unknown score can be interpeted in two ways: 

1. The vendor returns an "Unknown" score for the indicator.
2. The vendor returns nothing on the indicator.

In both cases we mark the indicator score as Unknown.

## Malicious
If the DBot score is returned as a "3" or "Bad", we need to add to the context that a malicious indicator was found. To do this, we add an additional key to the URL, IP, or File context called "Malicious" as shown below:

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

Malicious has two key values, "Vendor" and "Description". Vendor is the entity reporting the malicious indicator and description explains briefly what was found. For example:


```python
"URL": {
    "Data": "http://viruswarehouse.com",
    "Malicious": {
        "Vendor": "VirusTotal",
        "Description": "Wannacry ransomware detected"
    }
}
```

**Please Note**: We are unable to use the Cortex XSOAR Transformers (DT) within the DBot score context. 

For example, using the following in your DBot context, will not work:

```python
DBotScore(val.Indicator == obj.Indicator)
```
