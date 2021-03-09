---
id: relationship
title: Indicators relationship
---

Cortex XSOAR relationship can be created between any indicator in XSOAR.

Since relation requires a very specific dataset, we must format our data as per this article.

# Indicators relasionship



## Relation data structure

The Data structure xsoar server expect to get is :

| Key | Type | Required| Description | Example |
| --- | --- | --- | --- | --- |
| Name | String | Required | Relationship name. | Relation A -> B. |
| ReverseName | String | Required | Reverse relationship name. | Relation B -> A. |
| RelationType | String | Required | Relation type (stix2.1) | uses |
| EntityA | String | Required | Source entity. | Bootstrap attack        |
| EntityAFamily | String | Required | Source entity familiy.                            | STIX Attack Pattern |
| EntityB | String | Required | Destination entity. | 10.140.50.9 |
| EntityBFamily | String | Required | Destination entity familiy. | IP |
| CreatedInSystem | Date | Optional | First time created in xsoar system. ([ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format) | 2019-10-23T10:11:00Z |
| UpdatedInSystemBySource | Date | Optional | Last time modified in xsoar system. ([ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format) | 2020-10-24T10:11:00Z |
| Sources.[i].Reliability     | String | Optional | The [reliability](https://xsoar.pan.dev/docs/integrations/dbot#reliability-level) of an intelligence-data source. | A+ |
| Sources.[i].CreatedInSystem | Date | Required | First time created in xsoar system. ([ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format) | 2019-10-23T10:11:00Z |
| Sources.[i].UpdatedInSystem | Date | Required | Last time modified in xsoar system by source. ([ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format) | 2020-10-24T10:11:00Z |
| Sources.[i].Brand           | String | Optional | Relation brand name. | Feed service |
| Sources.[i].Instance        | String | Optional | Relation instance name. | Instance_1_Feed_service |
| Sources.[i].IsManual        | Boolean | Optional | True if relation modified manualy else false. | False |

Example:

```python
"Relationships": [{
  "Name": "Relation A -> B.",
  "ReverseName": "Relation B -> A.",
  "RelationType":"uses",
  "EntityA": "STIX Attack Pattern",
  "EntityAFamily": "Bootstrap attack",
  "EntityB": "10.140.50.9",
  "EntityBFamily": "IP",
  "CreatedInSystem": "2019-10-23T10:11:00Z",
  "UpdatedInSystemBySource": "2020-10-24T10:11:00Z",
  "Sources": [{
    "Reliability": "A+",
    "CreatedInSystem": "2019-10-23T10:11:00Z",
    "UpdatedInSystem": "2020-10-24T10:11:00Z",
    "Brand": "Feed service",
    "Instance": "Instance_1_Feed_service",
    "IsManual", "False",
  }, ...]
}, ...]
```

## Code samples

### Integration

```python
demisto.results("")
```



### Automation

```python
demisto.results("")
```

