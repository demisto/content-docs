---
id: generic-command-endpoint
title: Generic Command Endpoint
---


## Background and motivation

XSOAR has an abundance of integrations with endpoint providers, for example, GuardiCoreV2,  CrowdStrikeFalcon, etc. 



## Generic endpoint command

**endpoint**

## Description 
Returns information about an endpoint.

```yaml
- name: endpoint
   arguments:
   - default: false
     description: The endpoint ID.
     isArray: false
     name: id
     required: false
     secret: false
    - default: true
     description: The endpoint IP address.
     isArray: false
     name: ip
     required: false
     secret: false
    - default: false
     description: The endpoint hostname.
     isArray: false
     name: hostname
     required: false
     secret: false
    deprecated: false
```

## Outputs

| Path | Type | 	Description |
| --- | --- | --- |
| Endpoint.Hostname	| String	| The endpoint's hostname.  |
| Endpoint.OS	| String	| The endpoint's operation system. |
| Endpoint.OSVersion	| String	| The endpoint's operation system version. |
| Endpoint.IPAddress	| String	| The endpoint's IP address. |
| Endpoint.ID	| String	| The endpoint's ID. |
| Endpoint.Status	| String	| The endpoint's status. |
| Endpoint.IsIsolated	| String	| The endpoint's isolation status. |
| Endpoint.MACAddress	| String	| The endpoint's MAC address. |
| Endpoint.Vendor	| String	| The integration name of the endpoint vendor. |

## Integrations for reference

[GuardiCoreV2](https://github.com/demisto/content/tree/master/Packs/GuardiCore) 

[CrowdStrikeFalcon](https://github.com/demisto/content/tree/master/Packs/CrowdStrikeFalcon) 
