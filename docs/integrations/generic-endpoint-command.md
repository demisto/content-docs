---
id: generic-endpoint-command
title: Generic Endpoint Command
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


## Integrations for reference

[GuardiCoreV2](https://github.com/demisto/content/tree/master/Packs/GuardiCore) 

[CrowdStrikeFalcon](https://github.com/demisto/content/tree/master/Packs/CrowdStrikeFalcon) 
