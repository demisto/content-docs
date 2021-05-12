---
id: generic-commands-reputation
title: Generic Reputation Commands
---


## Background and motivation

XSOAR has an abudance of integrations with reputation providers for example VirusTotal, AlienVault OTX, MISP etc. 
Every Integration that returns a reputation about an indicator must implement the generic repuation commands and calculate [DBot Score](../dbot)

## Generic reputation commands

### **file file=**

**Description:** Runs reputation on files.

```yaml
- name: file
   arguments:
   - name: file
     default: true
     description: List of Files.
     isArray: true
```


### **ip ip=**

```yaml
- name: ip
   arguments:
   - name: ip
     default: true
     description: List of IPs.
     isArray: true
```
**Description:** Runs reputation on IPs.

### **url url=**

**Description:** Runs reputation on URLs.

```yaml
- name: url
   arguments:
   - name: url
     default: true
     description: List of URLs.
     isArray: true
```

### **domain domain=**

**Description:** Runs reputation on Domains.

```yaml
- name: domain
   arguments:
   - name: domain
     default: true
     description: List of Domains.
     isArray: true
```

### **email email=**

**Description:** Runs reputation on Emails.

```yaml
- name: email
   arguments:
   - name: email
     default: true
     description: List of emails.
     isArray: true
```

### **cve cve=**

**Description:** Runs reputation on CVEs.

```yaml
- name: cve
   arguments:
   - name: cve
     default: true
     description: List of CVEs.
     isArray: true
```
### Relationships:

Integrations that have the `create relationships` parameter create relationships as part of the reputation commands.
```
- defaultvalue: 'true'
  additionalinfo: Create relationships between indicators as part of Enrichment.
  display: Create relationships
  name: create_relationships
  required: false
  type: 8
```

#### Steps how to create relationships:
1. Create an `EntityRelationship` object with the relationships data. If more then one relationships exists, create a list and append all of the `EntityRelationship` objects to it.
 - The name of the relationships should be one of the exisitng relationships : https://xsoar.pan.dev/docs/reference/api/common-server-python#relationships
   For more information visit: https://xsoar.pan.dev/docs/reference/api/common-server-python#entityrelationship
2. Use the Common object when creating the indicator and set in the relationships key the list of `EntityRelationship` objects.
3. Use CommandResults, set the relationships key the list of `EntityRelationship` objects.

## Integrations for reference

[AutoFocus](https://github.com/demisto/content/tree/master/Packs/AutoFocus/Integrations/AutofocusV2) 
[AlienVault OTX](https://github.com/demisto/content/tree/master/Packs/AlienVault_OTX) 
[MISP](https://github.com/demisto/content/tree/master/Packs/MISP/Integrations/MISP_V2)
[DeHashed](https://github.com/demisto/content/tree/master/Packs/DeHashed/Integrations/DeHashed)
