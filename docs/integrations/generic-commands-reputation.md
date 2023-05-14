---
id: generic-commands-reputation
title: Generic Reputation Commands
---


## Background and motivation

XSOAR has an abundance of integrations with reputation providers, for example, VirusTotal, AlienVault OTX, MISP, etc. 
Every integration that returns a reputation about an indicator must implement the generic reputation commands and calculate a [DBot Score](../integrations/dbot).

When creating commands that enrich indicators, the commands should be named according to the indicator: !ip, !domain, etc. This naming convention allows commands from multiple integrations to be run together to enrich an indicator. For example, running !ip ip=8.8.8.8 can trigger multiple integrations that gather information about the IP address.

The easiest (and best) way to return indicator context is using one of the classes under `Common` (`Common.IP`, `Common.URL`, etc). For more information, see [here](context-and-outputs#return-ip-reputation). A simple example for returning indicators is the [`Ipinfo_v2` integration](https://github.com/demisto/content/blob/master/Packs/ipinfo/Integrations/ipinfo_v2/ipinfo_v2.py)


## Generic reputation commands

### **file file=**

**Description:** Runs reputation on files.

```yaml
- name: file
   arguments:
   - name: file
     default: true
     description: List of files.
     isArray: true
```


### **ip ip=**
**Description:** Runs reputation on IPs.

```yaml
- name: ip
   arguments:
   - name: ip
     default: true
     description: List of IPs.
     isArray: true
```


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

**Description:** Runs reputation on domains.

```yaml
- name: domain
   arguments:
   - name: domain
     default: true
     description: List of domains.
     isArray: true
```

### **email email=**

**Description:** Runs reputation on emails.

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
