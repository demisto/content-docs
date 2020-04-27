---
id: context-and-outputs
title: Context and Outputs
---

# Overview

Context is a map (dictionary) /JSON object that is created for each incident and is used to store structured results from the integration commands and automation scripts. The context keys are strings and the values can be strings, numbers, objects, and arrays.

The main use of context is to pass data between playbook tasks, one task stores output in the context and the other task reads that output from the context and uses it.

Let's look at a real world example that can show you how context is used:

For example **ThreatStream** integration has command **threatstream-analysis-report**. 
Returns the report of a file or URL that was submitted to the sandbox.

#### REST API returns
```json
{
    "Category": "File",
    "Completed": "2019-05-30 14:06:33",
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
    "Verdict": "Benign",
    "VmID": "",
    "VmName": ""
}
```

#### Integration YML
In the integration YAML file, the command outputs are defined as such:
**BrandName.Object.PropertyName**

In the context menu, you will see three fields; Context Path, Description and Type. Their uses are as follows:
* **Context Path** - This is a Dot Notation representation of the path to access the context
* **Description** - A short description of what the context is
* **Type** - Indicating the type of value that is located at the path enables Cortex XSOAR to format the data correctly

Use [json-to-outputs](https://github.com/demisto/demisto-sdk#convert-json-to-demisto-outputs) command in 
[demisto-sdk](https://github.com/demisto/demisto-sdk) tool to convert JSON into yml.
<br/>*Example:* `demisto-sdk json-to-outputs -c threatstream-analysis-report -p ThreatStream.Analysis` 

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
- contextPath: ThreatStream.Analysis.Completed
  description: Detonation completion time.
  type: String
- contextPath: ThreatStream.Analysis.Duration
  description: Duration of the detonation (in seconds).
  type: Number
- contextPath: ThreatStream.Analysis.VmName
  description: The name of the VM.
  type: String
- contextPath: ThreatStream.Analysis.VmID
  description: The ID of the VM.
  type: String
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
    "Completed": "2019-05-30 14:06:33",
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
    "Verdict": "Benign",
    "VmID": "",
    "VmName": ""
} # assume that we get this response from the service

command_results = CommandResults(
    outputs_prefix='ThreatStream.Analysis',
    outputs_key_field='ReportID',
    outputs=response_from_api
)
return_results(command_result)
```

**Notes**: 
  - The code **must** match the context path in the yml.
  - You can output the API response as is to the context as value, under the brand name key.
    That is, no need to modify the API response and map it to human readable keys.
    You might see old integrations in which this map exist, but this is no longer required. 

#### Reputation commands outputs `!ip` `!domain` `!url` `!cve` `!file`

**IP - Example**
```python
dbot_score = Common.DBotScore(
    indicator='8.8.8.8',
    indicator_type=DBotScoreType.IP,
    integration_name='Virus Total',
    score=DBotScore.GOOD
)

ip = Common.IP(
    ip='8.8.8.8',
    asn='Google LLC',
    dbot_score=dbot_score
)

command_results = CommandResults(
    indicators=[ip]
)

return_results(command_results)
```

**Domain - Example**
```python
dbot_score = Common.DBotScore(
    indicator='8.8.8.8',
    indicator_type=DBotScoreType.IP,
    integration_name='Virus Total',
    score=Common.DBotScore.GOOD
)

domain = Common.Domain(
    domain='google.com',
    dns='ns3.google.com',
    whois=WHOIS(
        registrar_name='MarkMonitor Inc.',
        registrar_abuse_email='abusecomplaints@markmonitor.com'
    )
)

command_results = CommandResults(
    indicators=[domain]
)

return_results(command_results)
```

### Examples:
- [Return data (common case)](#return-data) 
- [Return results with custom markdown](return-custom-markdown)
- [Return potentially malicious file](return-file)
- [Return non malicious file (e.g. reports)](return-entry-file)
- [Return IP reputation](#return-ip-reputation)
- [Return Domain reputation](#return-domain-reputation)
- [Return URL reputation](#return-url-reputation)
- [Return File reputation](#return-file-reputation)
- [Return CVE reputation](#return-cve-reputation)

#### <a name='return-data'></a> Return Data (common case)
*Code*
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

*YAML Definition*
```yaml
outputs:
- contextPath: PrismaCloud.Alert.id
  description: 'The alert id'
  type: Number
- contextPath: PrismaCloud.Alert.name
  description: 'The alert name'
  type: String
```

*Markdown*
### Results
|id|name|
|---|---|
| 100 | alert1 |
| 200 | alert2 |

*Context - The way it stored in incident context*
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


#### <a name='return-custom-markdown'></a> Return results with custom markdown
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

markdown = '## This is header<br/><br/>'
markdown += tableToMarkdown('Table title', alerts, headers=['id', 'name'])

results = CommandResults(
    readable_output=markdown,
    outputs_prefix='PrismaCompute.Alert',
    outputs_key_field='id',
    outputs=alerts
)
return_results(results)
```

*Markdown*
## This is header</br></br>
### Table title
|id|name|
|---|---|
| 100 | alert1 |
| 200 | alert2 |

#### <a name='return-file'></a> Return file (potentially malicious - e.g. email attachment)
*Code*
```python
file_entry = fileResult(filename='file.txt', data='file content')
demisto.results(file_entry)
```

*YAML*
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


#### <a name='return-entry-file'></a> Return file (non malicious - e.g. reports)
*Code*
```python
file_entry = fileResult(filename='file.txt', data='file content', file_type=EntryType.ENTRY_INFO_FILE)
demisto.results(file_entry)
```

*YAML*
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

#### <a name='return-ip-reputation'></a> Return IP reputation
```python
ip_reputation_from_autofocus = {
    'indicator': '5.5.5.5',
    'asn': '12345',
    'confidence': 95
}

if ip_reputation_from_autofocus['confidence'] >= 90:
    score = Common.DBotScore.BAD
if ip_reputation_from_autofocus['confidence'] >= 50:
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
    indicators=[ip]
)

return_results(results)
```

*Context - The way it stored in incident context*
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

*YAML Definition*
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

# This is standard context output - https://xsoar.pan.dev/docs/integrations/context-standards#ip
- contextPath: IP.Address
  description: IP address
  type: String
- contextPath: IP.ASN
  description: 'The autonomous system name for the IP address, for example: AS8948.'
  type: String

# Reputation commands usually should return DBotScore object - https://xsoar.pan.dev/docs/integrations/context-standards#dbot-score
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



*Markdown*
### Results
|asn|confidence|indicator|
|---|---|---|
| 12345 | 95 | 5.5.5.5 |


#### <a name='return-domain-reputation'></a> Return Domain reputation
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
    whois=Common.WHOIS(
        domain_status=domain_raw.get('status'),
        name_servers=domain_raw.get('name_servers'),
        registrar_name=domain_raw.get('registrar'),
        expiration_date=domain_raw.get('expiration_date')
    ),
    dbot_score=dbot_score
)

results = CommandResults(
    outputs_prefix='Autofocus.Domain',
    outputs_key_field='domain',
    outputs=domain_raw,
    indicators=[domain]
)

return_results(results)
```

*YAML Definition*
```yaml
# Reputation commands usually should return DBotScore object - https://xsoar.pan.dev/docs/integrations/context-standards#dbot-score
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

# This is standard context output - https://xsoar.pan.dev/docs/integrations/context-standards#ip
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

*Context - The way it stored in incident context*
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

#### <a name='return-url-reputation'></a> Return URL reputation
```python

```

#### <a name='return-file-reputation'></a> Return File reputation
```python

```

#### <a name='return-cve-reputation'></a> Return CVE reputation
```python

```



### DT (Cortex XSOAR Transform Language)
In the above example, we observe the entry context using ```(val.ReportID == obj.ReportID)```. This works to *tie together* related entry context objects. In this instance, we are using the value of the ReportID key as the unique identifier to search through the existing context and link related objects. This prevents data from being overwritten as well as further enriches an existing entry with more information. Learn more about linking context [here](dt).