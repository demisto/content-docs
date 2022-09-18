---
id: indicator-fields
title: Indicator Fields
---

As of March 2022, with the release of the Common Types content pack v3.2.2X, changes have been made to the structure of indicator fields, to align them more closely with STIX standards.

- All indicator layouts have been modified to better represent the changes.

These changes enable you to more easily share and work with IOCs. Like STIX, Cortex XSOAR indicators are divided into two categories, STIX Domain Objects (SDOs) and STIX Cyber-observable Objects (SCOs). The category determines which fields are presented in the layout of that specific IOC. In Cortex XSOAR, all SCOs can be used in a relationship with either SDOs or SCOs.

Some of the descriptions below are taken directly from [STIX documentation](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_axjijf603msy).

**IOC Fields Changes**

Each IOC table of fields is separated into three parts:
1. System Fields - fields created and managed by Cortex XSOAR.
2. Custom Core Fields - custom fields shared by all IOCS of the same time (SDO or SCO). (Fields may be empty.)
3. Custom Unique Fields - fields unique to a specific type of IOC. If a user associates more fields with the IOC, the additional fields will also be treated as unique.

## Cyber-observables Objects (SCO)

### Account

Similar to STIX *User Account Object*, this type represents a user account in various platforms - such as operating system, social media accounts, Active Directory, etc. The value defining the object is usually the username used to log in.

| System Fields      | Description |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Blocked | A Boolean switch to mark the object as blocked in the user environment |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `account--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Account Type | Specifies the type of the account, comes from `account-type-ov` by STIX |
| Creation Date | The date the account was created (not the date the indicator was created) |
| Display Name | The display name of the account as it is shown in user interfaces |
| Groups | The groups the account is a member of |
| User ID | The account's unique ID according to the system it was taken from |

### Domain / DomainGlob

Network domain name, similar to STIX *Domain Name Object*. The value is the domain address.

| System Fields      | Description  |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Blocked | A Boolean switch to mark the object as blocked in the user environment |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `domain--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Creation Date | The date the domain was created |
| DNS Records | All types of DNS records with a timestamp and their values (GRID) |
| Expiration Date | Domain expiry date |
| Certificates | Any certificates issued for the domain |
| WHOIS Records | Any records from WHOIS about the domain (GRID) |

### Email

A single user email address.

| System Fields      | Description  |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Blocked | A Boolean switch to mark the object as blocked in the user environment |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `email--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| None |

### File
Represents a single file. For backward compatibility, the indicator has multiple fields for different types of hashes. New hashes, however, should be stored under the “Hashes” grid field. The file value should be its hash (either MD5, SHA-1, SHA-256, or SHA-512, in that order).

| System Fields      | Description |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Blocked | A Boolean switch to mark the object as blocked in the user environment |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `file--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Creation Date | File creation date |
| File Extension | File extension |
| Associated File Names | Names the file is associated with |
| File Type | Type of the file |
| Hashes | Any hashes not specified in a separate field (GRID) |
| imphash | imphash |
| MD5 | MD5 Hash |
| Modified Date | When the file was modified on origin |
| Path | Path to the file |
| Quarantined | Was the file quarantined |
| SHA1 | SHA1 Hash |
| SHA256 | SHA256 Hash |
| SHA512 | SHA512 Hash |
| Size | File size |
| SSDeep   | SSDeep Hash |

### IPv4 / IPv6 / CIDR / IPv6CIDR

Represent an IP address and its subnet (CIDR). If no subnet is provided, the address is treated as a single IP (same as a /32 subnet).

| System Fields      | Description |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Blocked | A Boolean switch to mark the object as blocked in the user environment |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `type--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Geo Country | Country where the object is located |
| Geo Location | A set of coordinates for the object |
| WHOIS records | Any records from WHOIS about the domain (GRID) |

### URL

Represents the properties of a uniform resource locator.

| System Fields      | Description |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Blocked | A Boolean switch to mark the object as blocked in the user environment |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `url--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Certificates | Any certificates issued for the domain |



## Domain Objects (SDO)

### Attack Pattern

Attack Patterns are a type of TTP (Tactics, Techniques and Procedures) that describe ways that adversaries attempt to compromise targets. Attack Patterns are used to help categorize attacks, generalize specific attacks to the patterns that they follow, and provide detailed information about how attacks are performed. An example of an attack pattern is "spear phishing": a common type of attack where an attacker sends a carefully crafted email message to a party with the intent of getting them to click a link or open an attachment to deliver malware. Attack Patterns can also be more specific, such as spear phishing as practiced by a particular threat actor (for example, they might generally say that the target won a contest) can also be an Attack Pattern.

| System Fields      | Description |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `attack-pattern--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Kill Chain Phases | The list of Kill Chain Phases for which this Attack Pattern is used |
| External References | List of external references consisting of a source and ID. For example: `{source: mitere, id: T1189}` |

### Campaign

A Campaign is a grouping of adversarial behaviors that describes a set of malicious activities or attacks (sometimes called waves) that occur over a period of time against a specific set of targets. Campaigns usually have well defined objectives and may be part of an intrusion set.
 
Campaigns are often attributed to an intrusion set and threat actors. The threat actors may reuse known infrastructure from the intrusion set or may set up new infrastructure specifically for conducting that campaign.
 
Campaigns can be characterized by their objectives and the incidents they cause, people or resources they target, and the resources (infrastructure, intelligence, malware, tools, etc.) they use.
 
For example, a Campaign could be used to describe a crime syndicate's attack using a specific variant of malware and new C2 servers against the executives of ACME Bank during the summer of 2020 in order to gain secret information about an upcoming merger with another bank.

| System Fields      | Description |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `campaign--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Aliases | Alternative names used to identify this campaign |
| Objective | The campaign’s primary goal, objective, desired outcome, or intended effect|

### Course of Action

A Course of Action is an action taken either to prevent an attack or to respond to an attack that is in progress. It may describe technical, automatable responses (applying patches, reconfiguring firewalls), but can also describe higher level actions such as employee training or policy changes. For example, a Course of Action to mitigate a vulnerability could describe applying the patch that fixes it.

| System Fields      | Description  |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `course-of-action--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Action | RESERVED – To capture structured/automated courses of action |

### CVE

To preserve backward compatibility, our vulnerability indicator is referred to as *CVE*, but it is  equivalent to the Vulnerability object defined by STIX. Unlike STIX, in TIM the object is identified by its CVE number. A vulnerability is a weakness or defect in the requirements, designs, or implementations of the computational logic (code) found in software and some hardware components (firmware) that can be directly exploited to negatively impact the confidentiality, integrity, or availability of that system.

| System Fields      | Description  |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `vulnerability--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| CVSS Version |The version of the CVSS scoring system |
| CVSS Score |The score given to the CVE |
| CVSS Vector |The full CVSS vector |
| CVSS Table |All CVSS data by Metric - Value pairs |

### Infrastructure

The Infrastructure SDO represents a type of TTP and describes any systems, software services and any associated physical or virtual resources intended to support some purpose (for example, C2 servers used as part of an attack, a device or server that is part of a defense, database servers targeted by an attack, etc.). While elements of an attack can be represented by other SDOs or SCOs, the Infrastructure SDO represents a named group of related data that constitutes the infrastructure.

| System Fields      | Description  |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `infrastructure--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Aliases   |Alternative names used to identify this infrastructure. |
| Infrastructure types |The type of infrastructure being described. Values should come from STIX `infrastructure-type-ov` open vocabulary|

### Intrusion Set

An Intrusion Set is a grouped set of adversarial behaviors and resources with common properties that is believed to be orchestrated by a single organization. An Intrusion Set may capture multiple Campaigns or other activities that are all tied together by shared attributes indicating a commonly known or unknown Threat Actor. New activity can be attributed to an Intrusion Set even if the Threat Actors behind the attack are not known. Threat Actors can move from supporting one Intrusion Set to supporting another, or they may support multiple Intrusion Sets.

Whereas a Campaign is a set of attacks over a period of time against a specific set of targets to achieve an objective, an Intrusion Set is the entire attack package and may be used over a very long period of time in multiple Campaigns to achieve potentially multiple purposes.

| System Fields      | Description |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `intrusion-set--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Aliases   | Alternative names used to identify this Intrusion Set |
| Goals | The high-level goals of this Intrusion Set, namely, what are they trying to do |
| Primary Motivation | The primary reason, motivation, or purpose behind this Intrusion Set. Values should come from STIX `attack-motivation-ov` open vocabulary.|
| Secondary Motivation |The secondary reason, motivation, or purpose behind this Intrusion Set. Values should come from STIX `attack-motivation-ov` open vocabulary.|
| Resource level |Specifies the organizational level at which this Intrusion Set typically works. Values should come from STIX `attack-resource-level-ov` open vocabulary.|

### Malware

Malware is a type of TTP that represents malicious code. It generally refers to a program that is inserted into a system, usually covertly. The intent is to compromise the confidentiality, integrity, or availability of the victim's data, applications, or operating system (OS) or otherwise annoy or disrupt the victim.

| System Fields      | Description |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `malware--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Aliases   | A list of other names the malware is known as |
| Architecture | The processor architectures (e.g., x86, ARM, etc.) that the malware instance or family is executable on. The values should come from the STIX `processor-architecture-ov` open vocabulary. |
| Capabilities | Any of the capabilities identified for the malware instance or family. The values should come from STIX `malware-capabilities-ov` open vocabulary |
| Implementation Languages |The programming language(s) used to implement the malware instance or family. The values should come from the STIX `implementation-language-ov` open vocabulary.|
| Is Malware Family | Whether the object represents a malware family (if true) or a malware instance (if false)|
| Malware Types | Which type of malware. Values should come from STIX `malware-type-ov` open vocabulary|
| Operating System Refs | Identifier of a software object |

### Report

Reports are collections of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including context and related details. They are used to group related threat intelligence together so that it can be published as a comprehensive cyber threat story.

| System Fields      | Description |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `report--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Publications   | Links to publications of the report |


### Threat Actor

Threat Actors are individuals, groups, or organizations believed to be operating with malicious intent. A Threat Actor is not an Intrusion Set but may support or be affiliated with various Intrusion Sets, groups, or organizations over time.

| System Fields      | Description |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `threat-actor--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Alias   | A list of other names the threat actor is known as  |
| Geo country   | The country the threat actor is associated with  |
| Goals   | The high-level goals of this Threat Actor, namely, what are they trying to do |
| Resource Level   | The organizational level at which this Threat Actor typically works. Values for this property should come from STIX `attack-resource-level-ov` open vocabulary.|
| Primary Motivation   | The primary reason, motivation, or purpose behind this Threat Actor. Values for this property should come from STIX `attack-motivation-ov` open vocabulary.|
| Secondary Motivation   | The secondary reasons, motivations, or purposes behind this Threat Actor. Values for this property should come from STIX `attack-motivation-ov` open vocabulary. |
| Sophistication   | The skill, specific knowledge, special training, or expertise a Threat Actor must have to perform the attack. Values for this property should come from STIX `threat-actor-sophistication-ov` open vocabulary. |
| Threat actor type   | The type(s) of this threat actor. Values should come from STIX `threat-actor-type-ov` open vocabulary. |


### Tool

Tools are legitimate software that can be used by threat actors to perform attacks. Knowing how and when threat actors use such tools can help you understand how campaigns are executed. Unlike malware, these tools or software packages are often found on a system and have legitimate purposes for power users, system administrators, network administrators, or even regular users. Remote access tools (e.g., RDP) and network scanning tools (e.g., Nmap) are examples of tools that may be used by a Threat Actor during an attack.


| System Fields      | Description  |
| ----------- | ----------- |
| Value | Defines the indicator on Cortex XSOAR. The value is the main key for the object in the system. |
| Verdict | Malicious, Suspicious, Benign or Unknown |
| Expiration | The expiration date of the object |
| Source Time Stamp | When the object was created in the system |
| Modified | When the object was last modified |

| Custom Fields - Core | Description |
| ----------- | ----------- |
| Community Notes | Comments and freeform notes regarding the indicator |
| Description | The description of the object |
| STIX ID | The STIX ID for the object in the format of `tool--<UUID>` |
| Tags | Tags attached to the object |
| Traffic Light Protocol | Red, Amber, Green or White |

| Custom Fields - Unique | Description |
| ----------- | ----------- |
| Alias   | Alternative names used to identify this tool |
| Tool Types   | The kind(s) of tool(s) being described. Values for this property should come from STIX `tool-type-ov` open vocabulary.|
| Tool Version   | The version identifier associated with the tool.|
| Kill Chain Phrases   | The list of Kill Chain Phases for which this Attack Pattern is used |










