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

## Integrations for reference

[AutoFocus](https://github.com/demisto/content/tree/master/Packs/AutoFocus/Integrations/AutofocusV2) 
[MISP](https://github.com/demisto/content/tree/master/Packs/MISP/Integrations/MISP_V2)
[DeHashed](https://github.com/demisto/content/tree/master/Packs/DeHashed/Integrations/DeHashed)
