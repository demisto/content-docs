---
id: context-and-outputs
title: Context and Outputs
---

## Overview

The Context is a map (dictionary) / JSON object that is created for each incident and is used to store structured results from the integration commands and automation scripts. The Context keys are strings and the values can be strings, numbers, objects, and arrays.

The main use of the Context is to pass data between playbook tasks, one task stores its output in the Context and the other task reads that output from the Context and uses it.

Let's look at a real world example that can show you how the Context is used:

For example **ThreatStream** integration has the command **threatstream-analysis-report**. 
The command returns the report of a file or URL that was submitted to the sandbox.

#### The response from the REST API
```json
{
    "Category": "File",
    "Duration": 68,
    "Network": [
        {
            "UdpDestination": "8.8.8.8",
            "UdpPort": 53,
            "UdpSource": "192.168.2.4"
        },
        {
            "UdpDestination": "192.168.2.4",
            "UdpPort": 65324,
            "UdpSource": "8.8.8.8"
        },
        {
            "UdpDestination": "192.168.2.4",
            "UdpPort": 54896,
            "UdpSource": "8.8.8.8"
        }
    ],
    "ReportID": "413336",
    "Started": "2019-05-30 14:05:25",
    "Verdict": "Benign"
}
```

#### Integration YML
In the integration YAML file, the command outputs are defined as such:
**BrandName.Object.PropertyName**

For each output entry, you have three fields; Context Path, Description and Type. Their uses are as follows:
* **Context Path** - This is a Dot Notation representation of the path to access the Context.
* **Description** - A short description of what this Context entry represents.
* **Type** - Indicating the type of value that is located at the path. Enables Cortex XSOAR to format the data correctly.

Use [json-to-outputs](https://github.com/demisto/demisto-sdk#convert-json-to-demisto-outputs) command in 
[demisto-sdk](https://github.com/demisto/demisto-sdk) tool to convert JSON into yml.
**Example:** `demisto-sdk json-to-outputs -c threatstream-analysis-report -p ThreatStream.Analysis` 

```buildoutcfg
outputs:
- contextPath: ThreatStream.Analysis.ReportID
  description: The ID of the report submitted to the sandbox.
  type: String
- contextPath: ThreatStream.Analysis.Category
  description: The report category.
  type: String
- contextPath: ThreatStream.Analysis.Started
  description: Detonation start time.
  type: String
- contextPath: ThreatStream.Analysis.Duration
  description: Duration of the detonation (in seconds).
  type: Number
- contextPath: ThreatStream.Analysis.Network.UdpSource
  description: The source of UDP.
  type: String
- contextPath: ThreatStream.Analysis.Network.UdpDestination
  description: The destination of UDP.
  type: String
- contextPath: ThreatStream.Analysis.Network.UdpPort
  description: The port of the UDP.
  type: String
- contextPath: ThreatStream.Analysis.Verdict
  description: The verdict of the sandbox detonation.
  type: String
```

#### In the code
```python
report_id = '413336'

response_from_api = {
    "Category": "File",
    "Duration": 68,
    "Network": [
        {
            "UdpDestination": "8.8.8.8",
            "UdpPort": 53,
            "UdpSource": "192.168.2.4"
        },
        {
            "UdpDestination": "192.168.2.4",
            "UdpPort": 65324,
            "UdpSource": "8.8.8.8"
        },
        {
            "UdpDestination": "192.168.2.4",
            "UdpPort": 54896,
            "UdpSource": "8.8.8.8"
        }
    ],
    "ReportID": "413336",
    "Started": "2019-05-30 14:05:25",
    "Verdict": "Benign"
} # assume that we get this response from the service

command_results = CommandResults(
    outputs_prefix='ThreatStream.Analysis',
    outputs_key_field='ReportID',
    outputs=response_from_api
)
return_results(command_result)
```

:::note
  - The code **must** match the context path outputs specified in the YAML file.
  - You can output the API response as is to the context as a raw value, under the brand name key.
    There is no need to modify the API response and map it to human-readable keys.
    You might still see old integrations in which this type of mapping is performed, but this is not a requirement.
  - Avoid using dot and space characters in the context path keys.
:::

---

## Context Use Cases

:::caution Important Note
When setting `integration_name` with the vendor value, make sure it matches the name of the integration as defined in the [yml file](yaml-file#basic-information).
:::


### Return Data (common case)
```python
alerts = [
    {
        'id': 100,
        'name': 'alert1'
    },
    {
        'id': 200,
        'name': 'alert2'
    }
]

results = CommandResults(
    outputs_prefix='PrismaCompute.Alert',
    outputs_key_field='id',
    outputs=alerts
)
return_results(results)

```

**YAML Definition**
```yaml
outputs:
- contextPath: PrismaCompute.Alert.id
  description: 'The alert id'
  type: Number
- contextPath: PrismaCompute.Alert.name
  description: 'The alert name'
  type: String
```

**Markdown**
>#### Results
>|id|name|
>|---|---|
>| 100 | alert1 |
>| 200 | alert2 |

**Context Data - The way it is stored in the incident context data**
```json
{
  "PrismaCompute": {
    "Alert": [
      {
        "id": 100,
        "name": "alert1"
      },
      {
        "id": 200,
        "name": "alert2"
      }
    ]
  } 
}
```

---

### Return results with custom markdown
```python
alerts = [
    {
        'id': 100,
        'name': 'alert1'
    },
    {
        'id': 200,
        'name': 'alert2'
    }
]

markdown = '### This is the Header\n'
markdown += tableToMarkdown('Table Title', alerts, headers=['id', 'name'])

results = CommandResults(
    readable_output=markdown,
    outputs_prefix='PrismaCompute.Alert',
    outputs_key_field='id',
    outputs=alerts
)
return_results(results)
```

**Markdown**
>### This is the Header
>#### Table Title
>|id|name|
>|---|---|
>| 100 | alert1 |
>| 200 | alert2 |

---

### Return Data that has multiple unique identifier fields
:::note
Key fields are used to determine whether the data will be updated or added as new. [More info](./context-and-outputs#dt-cortex-xsoar-transform-language)
:::
```python
alerts = [
    {
        'id': 100,
        'name': 'alert1'
    },
    {
        'id': 200,
        'name': 'alert2'
    }
]

results = CommandResults(
    outputs_prefix='PrismaCompute.Alert',
    outputs_key_field=['id', 'name'],
    outputs=alerts
)
return_results(results)
```

---

### Return File
**Note**: *potentially malicious file - e.g. email attachment*

```python
file_entry = fileResult(filename='file.txt', data='file content')
return_results(file_entry)
```

**YAML Definition**
```yaml
outputs:
- contextPath: File.Size
  description: The size of the file.
  type: Number
- contextPath: File.SHA1
  description: The SHA1 hash of the file.
  type: String
- contextPath: File.SHA256
  description: The SHA256 hash of the file.
  type: String
- contextPath: File.Name
  description: The name of the file.
  type: String
- contextPath: File.SSDeep
  description: The SSDeep hash of the file.
  type: String
- contextPath: File.EntryID
  description: The entry ID of the file.
  type: String
- contextPath: File.Info
  description: File information.
  type: String
- contextPath: File.Type
  description: The file type.
  type: String
- contextPath: File.MD5
  description: The MD5 hash of the file.
  type: String
- contextPath: File.Extension
  description: The file extension.
  type: String
```
---

### Return Info File 
**Note**: *non malicious files - e.g. reports*

```python
file_entry = fileResult(filename='file.txt', data='file content', file_type=EntryType.ENTRY_INFO_FILE)
return_results(file_entry)
```

**YAML Definition**
```yaml
outputs:
- contextPath: InfoFile.Name
  description: FileName
  type: string
- contextPath: InfoFile.EntryID
  description: The EntryID of the report
  type: string
- contextPath: InfoFile.Size
  description: File Size
  type: number
- contextPath: InfoFile.Type
  description: File type e.g. "PE"
  type: string
- contextPath: InfoFile.Info
  description: Basic information of the file
  type: string
```
---

### Return IP reputation
For an integration usage example of how the code implements the indicator reputation command, see [AutofocusV2 integration](https://github.com/demisto/content/blob/master/Packs/AutoFocus/Integrations/AutofocusV2/AutofocusV2.py#L1381).  
```python
ip_reputation_from_autofocus = {
    'indicator': '5.5.5.5',
    'asn': '12345',
    'confidence': 95
}

if ip_reputation_from_autofocus['confidence'] >= 90:
    score = Common.DBotScore.BAD
elif ip_reputation_from_autofocus['confidence'] >= 50:
    score = Common.DBotScore.SUSPICIOUS
else:
    score = Common.DBotScore.GOOD

dbot_score = Common.DBotScore(
    indicator='5.5.5.5',
    indicator_type=DBotScoreType.IP,
    integration_name='Autofocus',
    score=score
)

ip = Common.IP(
    ip='5.5.5.5',
    asn=ip_reputation_from_autofocus['asn'],
    dbot_score=dbot_score
)

results = CommandResults(
    outputs_prefix='Autofocus.IP',
    outputs_key_field='indicator',
    outputs=ip_reputation_from_autofocus,
    indicator=ip
)

return_results(results)
```

**Context Data - The way it is stored in the incident context data**
```
{
    "Autofocus": {
        "IP": [
            {
                "indicator": "5.5.5.5", 
                "confidence": 95, 
                "asn": "12345"
            }
        ]
    }
    "IP": [
        {
            "ASN": "12345", 
            "Address": "5.5.5.5"
        }
    ], 
    "DBotScore": [
        {
            "Vendor": "Autofocus", 
            "Indicator": "5.5.5.5", 
            "Score": 2, 
            "Type": "ip"
        }
    ]
}
```

**YAML Definition**
```yaml
outputs:
- contextPath: Autofocus.IP.indicator
  description: IP address
  type: String
- contextPath: Autofocus.IP.condidence
  description: Indicator condidence between 0-99
  type: Number
- contextPath: Autofocus.IP.asn
  description: ASSN description
  type: String

# This is standard context output - https://xsoar.pan.dev/docs/integrations/context-standards-mandatory#ip
- contextPath: IP.Address
  description: IP address
  type: String
- contextPath: IP.ASN
  description: 'The autonomous system name for the IP address, for example: AS8948.'
  type: String

# Reputation commands usually should return DBotScore object - https://xsoar.pan.dev/docs/integrations/context-standards-mandatory#dbot-score
- contextPath: DBotScore.Indicator
  description: The indicator that was tested.
  type: String
- contextPath: DBotScore.Type
  description: The indicator type.
  type: String
- contextPath: DBotScore.Vendor
  description: The vendor used to calculate the score.
  type: String
- contextPath: DBotScore.Score
  description: The actual score.
  type: Number
```



**Markdown**
>#### Results
>|asn|confidence|indicator|
>|---|---|---|
>| 12345 | 95 | 5.5.5.5 |

---

### Return Domain reputation
For an integration usage example of how the code implements the indicator reputation command, see [AutofocusV2 integration](https://github.com/demisto/content/blob/master/Packs/AutoFocus/Integrations/AutofocusV2/AutofocusV2.py#L1443).  
```python
domain_raw = get_domain_from_autofocus('google.com')

if domain_raw.get('score') > 90:
    score = Common.DBotScore.BAD
elif domain_raw.get('score') > 60:
    score = Common.DBotScore.SUSPICIOUS
else:
    score = Common.DBotScore.GOOD

dbot_score = Common.DBotScore(
    indicator='google.com',
    indicator_type=DBotScoreType.DOMAIN,
    integration_name='Autofocus v2',
    score=score
)

domain = Common.Domain(
    domain='google.com',
    dns=domain_raw.get('dnssec'),
    creation_date=domain_raw.get('creation_date'),
    positive_detections=domain_raw.get('positive_detections'),
    detection_engines=domain_raw.get('detection_engines'),
    sub_domains=domain_raw.get('sub_domains'),
    domain_status=domain_raw.get('status'),
    name_servers=domain_raw.get('name_servers'),
    registrar_name=domain_raw.get('registrar'),
    expiration_date=domain_raw.get('expiration_date'),
    dbot_score=dbot_score
)

results = CommandResults(
    outputs_prefix='Autofocus.Domain',
    outputs_key_field='domain',
    outputs=domain_raw,
    indicator=domain
)

return_results(results)
```

*YAML Definition*
```yaml
# Reputation commands usually should return DBotScore object - https://xsoar.pan.dev/docs/integrations/context-standards-mandatory#dbot-score
- contextPath: DBotScore.Indicator
  description: The indicator that was tested.
  type: String
- contextPath: DBotScore.Type
  description: The indicator type.
  type: String
- contextPath: DBotScore.Vendor
  description: The vendor used to calculate the score.
  type: String
- contextPath: DBotScore.Score
  description: The actual score.
  type: Number

# This is standard context output - https://xsoar.pan.dev/docs/integrations/context-standards-mandatory#ip
- contextPath: Domain.Name
  description: 'The domain name, for example: "google.com".'
  type: String
- contextPath: Domain.CreationDate
  description: The date that the domain was created.
  type: Date
- contextPath: Domain.DNS
  description: A list of IP objects resolved by DNS.
  type: String
- contextPath: Domain.WHOIS.NameServers
  description: Name servers of the domain.
  type: String
- contextPath: Domain.WHOIS.Registrar.AbuseEmail
  description: The email address of the contact for reporting abuse.
  type: Unknown
- contextPath: Domain.WHOIS.Registrar.AbusePhone
  description: The phone number of contact for reporting abuse.
  type: Unknown
- contextPath: Domain.WHOIS.Registrar.Name
  description: 'The name of the registrar, for example: "GoDaddy".'
  type: String
- contextPath: Domain.WHOIS.ExpirationDate
  description: The expiration date of the domain.
  type: Date
- contextPath: Domain.WHOIS.DomainStatus
  description: The status of the domain.
  type: Unknown


- contextPath: AutofocusV2.Domain.address
  description: Domain admin address.
  type: String
- contextPath: AutofocusV2.Domain.city
  description: Domain admin city.
  type: String
- contextPath: AutofocusV2.Domain.country
  description: Domain admin country.
  type: String
- contextPath: AutofocusV2.Domain.creation_date
  description: Domain creation date.
  type: Date
- contextPath: AutofocusV2.Domain.dnssec
  description: DNSSEC status.
  type: String
- contextPath: AutofocusV2.Domain.domain
  description: The domain name.
  type: String
- contextPath: AutofocusV2.Domain.domain_name
  description: Domain name options.
  type: String
- contextPath: AutofocusV2.Domain.emails
  description: Contact emails.
  type: String
- contextPath: AutofocusV2.Domain.expiration_date
  description: Expiration date.
  type: Date
- contextPath: AutofocusV2.Domain.name
  description: Domain admin name.
  type: String
- contextPath: AutofocusV2.Domain.name_servers
  description: Name server.
  type: String
- contextPath: AutofocusV2.Domain.org
  description: Domain organization.
  type: String
- contextPath: AutofocusV2.Domain.referral_url
  description: Referral URL.
  type: Unknown
- contextPath: AutofocusV2.Domain.registrar
  description: Domain registrar.
  type: String
- contextPath: AutofocusV2.Domain.score
  description: Reputation score from HelloWorld for this domain (0 to 100, where higher
    is worse).
  type: Number
- contextPath: AutofocusV2.Domain.state
  description: Domain admin state.
  type: String
- contextPath: AutofocusV2.Domain.status
  description: Domain status.
  type: String
- contextPath: AutofocusV2.Domain.updated_date
  description: Updated date.
  type: Date
- contextPath: AutofocusV2.Domain.whois_server
  description: WHOIS server.
  type: String
- contextPath: AutofocusV2.Domain.zipcode
  description: Domain admin zipcode.
  type: Unknown


```

*Context Data - The way it is stored in the incident context data*
```json
{
    "Domain": {
        "CreationDate": [
            "1997-09-15 04:00:00", 
            "1997-09-15 00:00:00"
        ], 
        "Name": "google.com", 
        "DNS": "unsigned", 
        "WHOIS": {
            "NameServers": [
                "NS1.GOOGLE.COM", 
                "NS2.GOOGLE.COM", 
                "NS3.GOOGLE.COM", 
                "NS4.GOOGLE.COM", 
                "ns2.google.com", 
                "ns4.google.com", 
                "ns3.google.com", 
                "ns1.google.com"
            ], 
            "Registrar": {
                "AbuseEmail": null, 
                "AbusePhone": null, 
                "Name": "MarkMonitor, Inc."
            }, 
            "ExpirationDate": [
                "2028-09-14 04:00:00", 
                "2028-09-13 00:00:00"
            ], 
            "DomainStatus": [
                "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited", 
                "clientTransferProhibited https://icann.org/epp#clientTransferProhibited", 
                "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited", 
                "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited", 
                "serverTransferProhibited https://icann.org/epp#serverTransferProhibited", 
                "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited", 
                "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)", 
                "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)", 
                "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)", 
                "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)", 
                "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)", 
                "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"
            ]
        }
    }, 
    "DBotScore": {
        "Vendor": "Autofocus v2", 
        "Indicator": "google.com", 
        "Score": 2, 
        "Type": "domain"
    }, 
    "Autofocus": {
        "Domain": {
            "updated_date": [
                "2019-09-09 15:39:04", 
                "2019-09-09 08:39:04"
            ], 
            "status": [
                "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited", 
                "clientTransferProhibited https://icann.org/epp#clientTransferProhibited", 
                "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited", 
                "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited", 
                "serverTransferProhibited https://icann.org/epp#serverTransferProhibited", 
                "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited", 
                "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)", 
                "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)", 
                "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)", 
                "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)", 
                "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)", 
                "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"
            ], 
            "domain": "google.com", 
            "name": null, 
            "dnssec": "unsigned", 
            "city": null, 
            "expiration_date": [
                "2028-09-14 04:00:00", 
                "2028-09-13 00:00:00"
            ], 
            "domain_name": [
                "GOOGLE.COM", 
                "google.com"
            ], 
            "creation_date": [
                "1997-09-15 04:00:00", 
                "1997-09-15 00:00:00"
            ], 
            "whois_server": "whois.markmonitor.com", 
            "state": "CA", 
            "registrar": "MarkMonitor, Inc.", 
            "referral_url": null, 
            "address": null, 
            "name_servers": [
                "NS1.GOOGLE.COM", 
                "NS2.GOOGLE.COM", 
                "NS3.GOOGLE.COM", 
                "NS4.GOOGLE.COM", 
                "ns2.google.com", 
                "ns4.google.com", 
                "ns3.google.com", 
                "ns1.google.com"
            ], 
            "org": "Google LLC", 
            "country": "US", 
            "emails": [
                "abusecomplaints@markmonitor.com", 
                "whoisrequest@markmonitor.com"
            ], 
            "zipcode": null, 
            "score": 76
        }
        
        
    }
}
```

---

### Return URL reputation
For an integration usage example of how the code implements the indicator reputation command, see [AutofocusV2 integration](https://github.com/demisto/content/blob/master/Packs/AutoFocus/Integrations/AutofocusV2/AutofocusV2.py#L1521).

```python
url_arg = 'https://www.ynetto.co.il'
url_raw_response = {
    'url': 'https://www.ynetto.co.il',
    'verdict': 'Malicious',
    'detection_engines': 10,
    'positive_engines': 10
}

score = Common.DBotScore.GOOD
if url_raw_response.get('verdict') == 'Malicious':
    score = Common.DBotScore.BAD

dbot_score = Common.DBotScore(
    indicator=url_arg,
    indicator_type=DBotScoreType.URL,
    integration_name='Virus Total',
    score=score
)

url = Common.URL(
    url=url_arg,
    detection_engines=url_raw_response.get('detection_engines'),
    positive_detections=url_raw_response.get('positive_engines'),
    dbot_score=dbot_score
)

results = CommandResults(
    outputs_prefix='VirusTotal.URL',
    outputs_key_field='url',
    outputs=url_raw_response,
    indicator=url
)

return_results(results)
```

**YAML Definition**
```yaml
# Reputation commands usually should return DBotScore object - https://xsoar.pan.dev/docs/integrations/context-standards-mandatory#dbot-score
outputs:
- contextPath: DBotScore.Indicator
  description: The indicator that was tested.
  type: String
- contextPath: DBotScore.Type
  description: The indicator type.
  type: String
- contextPath: DBotScore.Vendor
  description: The vendor used to calculate the score.
  type: String
- contextPath: DBotScore.Score
  description: The actual score.
  type: Number

# Reputation commands usually should return DBotScore object - https://xsoar.pan.dev/docs/integrations/context-standards-mandatory#url
- contextPath: URL.Data
  description: The URL
  type: String
- contextPath: URL.DetectionEngines
  description: The total number of engines that checked the indicator.
  type: String
- contextPath: URL.PositiveDetections
  description: The number of engines that positively detected the indicator as malicious.
  type: String
- contextPath: URL.Malicious.Vendor
  description: The vendor reporting the URL as malicious.
  type: String
- contextPath: URL.Malicious.Description
  description: A description of the malicious URL.
  type: String

- contextPath: VirusTotal.URL.url
  description: The URL
  type: String
- contextPath: VirusTotal.URL.verdict
  description: Verdict can be Malicious or Benign
  type: String
- contextPath: VirusTotal.URL.detection_engines
  description: Number of engines
  type: Number
- contextPath: VirusTotal.URL.positive_engines
  description: Number of positive engines
  type: Number
```


**Context Data - The way it is stored in the incident context data**
```json
{
    "URL": {
        "Data": "https://www.ynetto.co.il",
        "DetectionEngines": 10,
        "PositiveDetections": 10,
        "Malicious": {
            "Vendor": "Virus Total",
            "Description": null
        }
    },
    "DBotScore": {
        "Indicator": "https://www.ynetto.co.il",
        "Type": "url",
        "Vendor": "Virus Total",
        "Score": 3
    },
    "VirusTotal": {
        "URL": {
            "url": "https://www.ynetto.co.il",
            "verdict": "Malicious",
            "detection_engines": 10,
            "positive_engines": 10
        }
    }
}
```

---

### Return File/Hash reputation
For an integration usage example of how the code implements the indicator reputation command, see [AutofocusV2 integration](https://github.com/demisto/content/blob/master/Packs/AutoFocus/Integrations/AutofocusV2/AutofocusV2.py#L1584) or [CrowdsrikeMalquery](https://github.com/demisto/content/blob/master/Packs/CrowdStrikeMalquery/Integrations/CrowdStrikeMalquery/CrowdStrikeMalquery.py#L292).
```python
md5 = '9498ff82a64ff445398c8426ed63ea5b'
hash_reputation_response = {
    "md5": "9498ff82a64ff445398c8426ed63ea5b",
    "permalink": "https://www.virustotal.com/file/8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1c17c4ab19a/analysis/1587134153/",
    "positives": 58,
    "resource": "9498FF82A64FF445398C8426ED63EA5B",
    "response_code": 1,
    "scan_date": "2020-04-17 14:35:53",
    "scan_id": "8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1c17c4ab19a-1587134153",
    "sha1": "36f9ca40b3ce96fcee1cf1d4a7222935536fd25b",
    "sha256": "8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1c17c4ab19a",
    "total": 70,
    "verbose_msg": "Scan finished, information embedded"
}

score = Common.DBotScore.GOOD
if hash_reputation_response.get('positives') > 20:
    score = Common.DBotScore.BAD
if hash_reputation_response.get('positives') > 3:
    score = Common.DBotScore.SUSPICIOUS


dbot_score = Common.DBotScore(
    indicator=md5,
    indicator_type=DBotScoreType.FILE,
    integration_name='Virus Total',
    score=score,
    malicious_description=hash_reputation_response.get('verbose_msg')
)

file = Common.File(
    md5=md5,
    sha1=hash_reputation_response.get('sha1'),
    sha256=hash_reputation_response.get('sha256'),
    dbot_score=dbot_score
)

results = CommandResults(
    outputs_prefix='VirusTotal.File',
    outputs_key_field='md5',
    outputs=hash_reputation_response,
    indicator=file
)

return_results(results)
```

**YAML Definition**
```yaml
outputs:
# Reputation commands usually should return DBotScore object - https://xsoar.pan.dev/docs/integrations/context-standards-mandatory#file
- contextPath: File.Name
  description: The full file name (including file extension).
  type: String
- contextPath: File.MD5
  description: The MD5 hash of the file.
  type: String
- contextPath: File.SHA1
  description: The SHA1 hash of the file.
  type: String
- contextPath: File.SHA256
  description: The SHA256 hash of the file.
  type: String
- contextPath: File.Malicious.Vendor
  description: The vendor that reported the file as malicious.
  type: String
- contextPath: File.Malicious.Description
  description: A description explaining why the file was determined to be malicious.
  type: String
  
# Reputation commands usually should return DBotScore object - https://xsoar.pan.dev/docs/integrations/context-standards-mandatory#dbot-score
- contextPath: DBotScore.Indicator
  description: The indicator that was tested.
  type: String
- contextPath: DBotScore.Type
  description: The indicator type.
  type: String
- contextPath: DBotScore.Vendor
  description: The vendor used to calculate the score.
  type: String
- contextPath: DBotScore.Score
  description: The actual score.
  type: Number
  
- contextPath: VirusTotal.File.md5
  description: The MD5 hash of the file.
  type: String
- contextPath: VirusTotal.File.permalink
  description: Link to the file report
  type: String
- contextPath: VirusTotal.File.positives
  description: Number of positive engines
  type: Number
- contextPath: VirusTotal.File.resource
  description: The resource
  type: String
- contextPath: VirusTotal.File.response_code
  description: Response code, it is a number between 1-10
  type: Number
- contextPath: VirusTotal.File.scan_date
  description: Scan date of a format 2010-05-15 03:38:44
  type: Date
- contextPath: VirusTotal.File.scan_id
  description: Scan ID
  type: String
- contextPath: VirusTotal.File.sha1
  description: The SHA1 hash of the file.
  type: String
- contextPath: VirusTotal.File.sha256
  description: The SHA256 hash of the file.
  type: String
- contextPath: VirusTotal.File.total
  description: Total number of engines
  type: Number
- contextPath: VirusTotal.File.verbose_msg
  description: Verbose message about the hash
  type: String
```

**Context Data - The way it is stored in the incident context data**
```json
{
    "File": {
        "MD5": "9498ff82a64ff445398c8426ed63ea5b",
        "SHA1": "36f9ca40b3ce96fcee1cf1d4a7222935536fd25b",
        "SHA256": "8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1c17c4ab19a"
    },
    "DBotScore": {
        "Indicator": "9498ff82a64ff445398c8426ed63ea5b",
        "Type": "file",
        "Vendor": "Virus Total",
        "Score": 2
    },
    "VirusTotal": {
        "File": {
            "md5": "9498ff82a64ff445398c8426ed63ea5b",
            "permalink": "https://www.virustotal.com/file/8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1c17c4ab19a/analysis/1587134153/",
            "positives": 58,
            "resource": "9498FF82A64FF445398C8426ED63EA5B",
            "response_code": 1,
            "scan_date": "2020-04-17 14:35:53",
            "scan_id": "8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1c17c4ab19a-1587134153",
            "sha1": "36f9ca40b3ce96fcee1cf1d4a7222935536fd25b",
            "sha256": "8b2e701e91101955c73865589a4c72999aeabc11043f712e05fdb1c17c4ab19a",
            "total": 70,
            "verbose_msg": "Scan finished, information embedded"
        }
    }
}
```

---

### Return CVE reputation
For an integration usage example of how the code implements the indicator reputation command, see [CVESearchV2](https://github.com/demisto/content/blob/master/Packs/CVESearch/Integrations/CVESearchV2/CVESearchV2.py#L136).
```python
cve_arg = 'CVE-2015-1653'

cve_raw_response = {
    "Modified": "2018-10-12T22:08:00",
    "Published": "2015-04-14T20:59:00",
    "assigner": "cve@mitre.org",
    "cvss": 4.3,
    "cvss-time": "2018-10-12T22:08:00",
    "cwe": "CWE-79",
    "id": "CVE-2015-1653",
    "references": [
        "http://www.securitytracker.com/id/1032111",
        "https://docs.microsoft.com/en-us/security-updates/securitybulletins/2015/ms15-036"
    ],
    "summary": "Cross-site scripting (XSS) vulnerability in Microsoft ",
}

cve = Common.CVE(
    id=cve_arg,
    cvss=cve_raw_response.get('cvss'),
    description=cve_raw_response.get('summary'),
    published=cve_raw_response.get('Published'),
    modified=cve_raw_response.get('Modified')
)

results = CommandResults(
    outputs_prefix='CVEMitre.CVE',
    outputs_key_field='id',
    outputs=cve_raw_response,
    indicator=cve
)

return_results(results)
```

**YAML Definition**
```yaml
outputs:
- contextPath: CVE.ID
  description: 'The ID of the CVE, for example: CVE-2015-1653'
  type: String
- contextPath: CVE.CVSS
  description: 'The CVSS of the CVE, for example: 10.0'
  type: String
- contextPath: CVE.Published
  description: The timestamp of when the CVE was published.
  type: Date
- contextPath: CVE.Modified
  description: The timestamp of when the CVE was last modified.
  type: Date
- contextPath: CVE.Description
  description: A description of the CVE.
  type: String
```

**Context Data - The way it is stored in the incident context data**
```json
{
    "CVE": {
        "ID": "CVE-2015-1653",
        "CVSS": 4.3,
        "Published": "2015-04-14T20:59:00",
        "Modified": "2018-10-12T22:08:00",
        "Description": "Cross-site scripting (XSS) vulnerability in Microsoft "
    },
    "CVEMitre": {
        "CVE": {
            "Modified": "2018-10-12T22:08:00",
            "Published": "2015-04-14T20:59:00",
            "assigner": "cve@mitre.org",
            "cvss": 4.3,
            "cvss-time": "2018-10-12T22:08:00",
            "cwe": "CWE-79",
            "id": "CVE-2015-1653",
            "references": [
                "http://www.securitytracker.com/id/1032111",
                "https://docs.microsoft.com/en-us/security-updates/securitybulletins/2015/ms15-036"
            ],
            "summary": "Cross-site scripting (XSS) vulnerability in Microsoft "
        }
    }
}
```

---
### Return Custom Indicators
For more information, see [CustomIndicatorDemo](https://xsoar.pan.dev/docs/reference/integrations/custom-indicator-demo#this-integration-is-part-of-the-developer-tools-pack). For a usage example of the CustomIndicator helper class, see [CustomIndicatorDemo](https://github.com/demisto/content/blob/2ae363a31f9ead0fce09d3c8b36bc02b7b21d89c/Packs/DeveloperTools/Integrations/CustomIndicatorDemo/CustomIndicatorDemo.py#L60) .

```python
 score = Common.DBotScore.GOOD
 indicator_value = 'custom_value'
 dbot_score = Common.DBotScore(
     indicator=indicator_value,
     indicator_type=DBotScoreType.CUSTOM,
     integration_name='DummyIntegration',
     score=score
 )
 data = {
     'param1': 'value1',
     'param2': 'value2',
 }
 custom_indicator = Common.CustomIndicator(
     indicator_type='MyCustomIndicator',
     dbot_score=dbot_score,
     value=indicator_value,
     data=data,
     context_prefix='custom',
 )
 return CommandResults(
     readable_output='custom_value',
     outputs=result,
     outputs_prefix='Demo.Result',
     outputs_key_field='test_key_field',
     indicator=custom_indicator
 )
 ```

**Context Data - The way it is stored in the incident context data**
```
{
    DBotScore
    [
        {
            "Indicator": "custom_value",
            "Score": 1,
            "Type": "MyCustomIndicator",
            "Vendor": "CustomIndicatorDemo"
        }
    ]
    Demo.Result
    {
        "dummy": "test"
    }
    custom
    [
        {
            "value": "custom_value",
            "param1": "value1",
            "param2": "value2"
        }
    ]
}
```
**YAML Definition**
```yaml
   outputs:
    - contextPath: Demo.Result.dummy
      description: The command's output
      type: String
    - contextPath: custom.param1
      description: custom data field of the indicator
      type: String
    - contextPath: custom.param2
      description: custom data field of the indicator
      type: String
    - contextPath: custom.value
      description: value of the indicator
      type: String
    - contextPath: DBotScore.Indicator
      description: The indicator value
      type: String
    - contextPath: DBotScore.Type
      description: The indicator type.
      type: String
    - contextPath: DBotScore.Vendor
      description: The vendor used to calculate the score.
      type: String
    - contextPath: DBotScore.Score
      description: The actual score.
      type: Number
```
---
### Return Multiple Indicators
For an integration usage example of how the code implements the indicator reputation command, see [MispV3](https://github.com/demisto/content/blob/b5342c522d44aec8f31f4ee0fc8ad269ac970903/Packs/MISP/Integrations/MISPV3/MISPV3.py#L578).
In case you need to return multiple indicators (i.e. IPs) in the same call, you should return a list of `CommandResults`, as shown in the following example.

```python
ip_reputations_from_autofocus = [
    {
      'indicator': '5.5.5.5',
      'asn': '12345',
      'confidence': 95
    },
    {
      'indicator': '4.4.4.4',
      'asn': '54321',
      'confidence': 73
    }
]

command_results_list: List[CommandResults] = []

for ip_reputation in ip_reputations_from_autofocus:
    if ip_reputation['confidence'] >= 90:
        score = Common.DBotScore.BAD
    elif ip_reputation['confidence'] >= 50:
        score = Common.DBotScore.SUSPICIOUS
    else:
        score = Common.DBotScore.GOOD

    dbot_score = Common.DBotScore(
        indicator=ip_reputation['indicator'],
        indicator_type=DBotScoreType.IP,
        integration_name='Autofocus',
        score=score
    )

    ip = Common.IP(
        ip=ip_reputation['indicator'],
        asn=ip_reputation['asn'],
        dbot_score=dbot_score
    )

    command_results_list.append(CommandResults(
        outputs_prefix='Autofocus.IP',
        outputs_key_field='indicator',
        outputs=ip_reputation,
        indicator=ip
    ))

return_results(command_results_list)
```

**Context Data - The way it is stored in the incident context data**
```
{
    "Autofocus": {
        "IP": [
            {
                "indicator": "5.5.5.5", 
                "confidence": 95, 
                "asn": "12345"
            },
            {
                "indicator": "4.4.4.4", 
                "confidence": 73, 
                "asn": "54321"
            }
        ]
    }
    "IP": [
        {
            "ASN": "12345", 
            "Address": "5.5.5.5"
        },
        {
            "ASN": "54321", 
            "Address": "4.4.4.4"
        }
    ], 
    "DBotScore": [
        {
            "Vendor": "Autofocus", 
            "Indicator": "5.5.5.5", 
            "Score": 2, 
            "Type": "ip"
        },
        {
            "Vendor": "Autofocus", 
            "Indicator": "4.4.4.4", 
            "Score": 1, 
            "Type": "ip"
        }
    ]
}
```

**YAML Definition**
```yaml
outputs:
- contextPath: Autofocus.IP.indicator
  description: IP address
  type: String
- contextPath: Autofocus.IP.condidence
  description: Indicator condidence between 0-99
  type: Number
- contextPath: Autofocus.IP.asn
  description: ASSN description
  type: String

# This is standard context output - https://xsoar.pan.dev/docs/integrations/context-standards-mandatory#ip
- contextPath: IP.Address
  description: IP address
  type: String
- contextPath: IP.ASN
  description: 'The autonomous system name for the IP address, for example: AS8948.'
  type: String

# Reputation commands usually should return DBotScore object - https://xsoar.pan.dev/docs/integrations/context-standards-mandatory#dbot-score
- contextPath: DBotScore.Indicator
  description: The indicator that was tested.
  type: String
- contextPath: DBotScore.Type
  description: The indicator type.
  type: String
- contextPath: DBotScore.Vendor
  description: The vendor used to calculate the score.
  type: String
- contextPath: DBotScore.Score
  description: The actual score.
  type: Number
```



**Markdown**
>#### Results
>|asn|confidence|indicator|
>|---|---|---|
>| 12345 | 95 | 5.5.5.5 |
>| 54321 | 73 | 4.4.4.4 |

---

### DT (Cortex XSOAR Transform Language)
In the above example, we observe the entry context using ```(val.ReportID == obj.ReportID)```. This works to *tie together* related entry context objects. In this instance, we are using the value of the ReportID key as the unique identifier to search through the existing context and link related objects. This prevents data from being overwritten as well as further enriches an existing entry with more information. Learn more about linking context [here](dt).
