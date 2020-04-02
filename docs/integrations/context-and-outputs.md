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

return_outputs(
    readable_outputs=tableToMarkdown(f'Analysis Report {report_id}', [response_from_api]),
    outputs={
        'ThreatStream.Analysis(val.ReportID == obj.ReportID)': response_from_api
    },
    raw_response=response_from_api
)
```

**Notes**: 
  - The code **must** match the context path in the yml.
  - You can output the API response as is to the context as value, under the brand name key.
    That is, no need to modify the API response and map it to human readable keys.
    You might see old integrations in which this map exist, but this is no longer required. 

### DT (Cortex XSOAR Transform Language)
In the above example, we observe the entry context using ```(val.ReportID == obj.ReportID)```. This works to *tie together* related entry context objects. In this instance, we are using the value of the ReportID key as the unique identifier to search through the existing context and link related objects. This prevents data from being overwritten as well as further enriches an existing entry with more information. Learn more about linking context [here](dt).