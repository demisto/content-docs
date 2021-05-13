---
id: context-standards-mandatory
title: Mandatory Context Standards
---

This article describes the standerd context schema used for the system indicators and the DBot Score object. 
There is no need to manually output this in your code, instead, use the builtin classes as described in the [Context Use Cases](../integrations/context-and-outputs#context-use-cases) article.

## File
The following is the format for a file. File here refers to the file indicator or a binary file that could potentially be malicious, and might be checked for reputation or sent to a sandbox. 

```json
"File": {
        "Name": "STRING, The full file name (including file extension).",
        "EntryID": "STRING, The ID for locating the file in the War Room.",
        "Size": "INT, The size of the file in bytes.",
        "MD5": "STRING, The MD5 hash of the file.",
        "SHA1": "STRING, The SHA1 hash of the file.",
        "SHA256": "STRING, The SHA256 hash of the file.",
        "SHA512": "STRING The SHA512 hash of the file.",
        "SSDeep": "STRING, The ssdeep hash of the file (same as displayed in file entries).",
        "Extension": "STRING, The file extension, for example: 'xls'.",
        "Type": "STRING, The file type, as determined by libmagic (same as displayed in file entries).",
        "Hostname": "STRING, The name of the host where the file was found. Should match Path.",
        "Path": "STRING, The path where the file is located.",
        "Company": "STRING, The name of the company that released a binary.",
        "ProductName": "STRING, The name of the product to which this file belongs.",
        "DigitalSignature": {
            "Publisher": "STRING, The publisher of the digital signature for the file."
        },
        "Actor": "STRING, The actor reference.",
        "Tags": "STRING, Tags of the file.",
        "Signature": {
            "Authentihash": "STRING, The authentication hash.",
            "Copyright": "STRING, Copyright information.",
            "Description": "STRING, A description of the signature.",
            "FileVersion": "STRING, The file version.",
            "InternalName": "STRING, The internal name of the file.",
            "OriginalName": "STRING, The original name of the file."            
        },
        "Malicious": {
             "Vendor": "STRING, The vendor that reported the file as malicious.",
             "Description": "STRING, A description explaining why the file was determined to be malicious."
        },
        "EntityA": "STRING, The source of the relationship.",
        "EntityB": "STRING, The destination of the relationship.",
        "Relationship": "STRING, The name of the relationship.",
        "EntityAType": "STRING, The type of the source of the relationship.",
        "EntityBType": "STRING, The type of the destination of the relationship.",
        "FeedRelatedIndicators": {
             "value": "STRING, Indicators that are associated with the file.",
             "type": "STRING, The type of the indicators that are associated with the file",
             "description": "STRING, The description of the indicators that are associated with the file."
        },
        "MalwareFamily": "STRING, The malware family associated with the file.",
        "Campaign": "STRING, The campaign associated with the file.",
        "TrafficLightProtocol": "STRING, The Traffic Light Protocol (TLP) color that is suitable for the file.",
        "CommunityNotes": {
            "note": "STRING, Notes on the file that were given by the community.",
            "timestamp": "DATE, The time in which the note was published."
        },
        "Publications": {
            "source": "STRING, The source in which the article was published.",
            "title": "STRING, The name of the article.",
            "link": "STRING, A link to the original article.",
            "timestamp": "DATE, The time in which the article was published."
        },
        "Behavior": {
            "details": "STRING, The technical details which are relevant to the behavior.",
            "title": "STRING, The behavior associated with the file."
        },
        "ThreatTypes": {
            "threatcategory": "STRING, The threat category associated to this indicator by the source vendor. For example, Phishing, Control, TOR, etc.",
            "threatcategoryconfidence": "STRING, Threat Category Confidence is the confidence level provided by the vendor for the threat type category For example a confidence of 90 for threat type category 'malware' means that the vendor rates that this is 90% confidence of being a malware."
        },
        "Imphash": "STRING, The Imphash hash of the file.",
        "Quarantined": "BOOL, Is the file quarantined or not.",
        "Organization": "STRING, The organization of the file.",
        "AssociatedFileNames": "STRING, File names that are known as associated to the file."
}
```

**In YAML**
```yaml
outputs:
- contextPath: File.Name
  description: The full file name (including file extension).
  type: String
- contextPath: File.EntryID
  description: The ID for locating the file in the War Room.
  type: String
- contextPath: File.Size
  description: The size of the file in bytes.
  type: Number
- contextPath: File.MD5
  description: The MD5 hash of the file.
  type: String
- contextPath: File.SHA1
  description: The SHA1 hash of the file.
  type: String
- contextPath: File.SHA256
  description: The SHA1 hash of the file.
  type: String
- contextPath: File.SHA512
  description: The SHA512 hash of the file.
  type: String
- contextPath: File.SSDeep
  description: The ssdeep hash of the file (same as displayed in file entries).
  type: String
- contextPath: File.Extension
  description: "The file extension, for example: 'xls'."
  type: String
- contextPath: File.Type
  description: The file type, as determined by libmagic (same as displayed in file entries).
  type: String
- contextPath: File.Hostname
  description: The name of the host where the file was found. Should match Path.
  type: String
- contextPath: File.Path
  description: The path where the file is located.
  type: String
- contextPath: File.Company
  description: The name of the company that released a binary.
  type: String
- contextPath: File.ProductName
  description: The name of the product to which this file belongs.
  type: String
- contextPath: File.DigitalSignature.Publisher
  description: The publisher of the digital signature for the file.
  type: String
- contextPath: File.Actor
  description: The actor reference.
  type: String
- contextPath: File.Tags
  description: (List) Tags of the file.
  type: Unknown
- contextPath: File.FeedRelatedIndicators.value
  description: Indicators that are associated with the file.
  type: String
- contextPath: File.FeedRelatedIndicators.type
  description: The type of the indicators that are associated with the file.
  type: String
- contextPath: File.FeedRelatedIndicators.description
  description: The description of the indicators that are associated with the file.
  type: String
- contextPath: File.MalwareFamily
  description: The malware family associated with the file.
  type: String
- contextPath: File.Signature.Authentihash
  description: The authentication hash.
  type: String
- contextPath: File.Signature.Copyright
  description: Copyright information.
  type: String
- contextPath: File.Signature.Description
  description: A description of the signature.
  type: String
- contextPath: File.Signature.FileVersion
  description: The file version.
  type: String
- contextPath: File.Signature.InternalName
  description: The internal name of the file.
  type: String
- contextPath: File.Signature.OriginalName
  description: The original name of the file.
  type: String
- contextPath: File.Malicious.Vendor
  description: The vendor that reported the file as malicious.
  type: String
- contextPath: File.Malicious.Description
  description: A description explaining why the file was determined to be malicious.
  type: String
- contextPath: File.Relationships.EntityA
  description: The source of the relationship.
  type: string
- contextPath: File.Relationships.EntityB
  description: The destination of the relationship.
  type: string
- contextPath: File.Relationships.Relationship
  description: The name of the relationship.
  type: string
- contextPath: File.Relationships.EntityAType
  description: The type of the source of the relationship.
  type: string
- contextPath: File.Relationships.EntityBType
  description: The type of the destination of the relationship.
  type: string
- contextPath: File.Campaign
  description: The campaign associated with the file.
  type: String
- contextPath: File.TrafficLightProtocol
  description: The Traffic Light Protocol (TLP) color that is suitable for the file.
  type: String
- contextPath: File.CommunityNotes.note
  description: Notes on the file that were given by the community.
  type: String
- contextPath: File.CommunityNotes.timestamp
  description: The time in which the note was published.
  type: Date
- contextPath: File.Publications.source
  description: The source in which the article was published.
  type: String
- contextPath: File.Publications.title
  description: The name of the article.
  type: String
- contextPath: File.Publications.link
  description: A link to the original article.
  type: String
- contextPath: File.Publications.timestamp
  description: The time in which the article was published.
  type: Date
- contextPath: File.Behavior.details
  description: The technical details which are relevant to the behavior.
  type: String
- contextPath: File.Behavior.title
  description: The behavior associated with the file.
  type: String
- contextPath: File.ThreatTypes.threatcategory
  description: The threat category associated to this indicator by the source vendor. For example, Phishing, Control, TOR, etc.
  type: String
- contextPath: File.ThreatTypes.threatcategoryconfidence
  description: Threat Category Confidence is the confidence level provided by the vendor for the threat type category For example a confidence of 90 for threat type category 'malware' means that the vendor rates that this is 90% confidence of being a malware.
  type: String
- contextPath: File.Imphash
  description: The Imphash hash of the file.
  type: String
- contextPath: File.Quarantined
  description: Is the file quarantined or not.
  type: Bool
- contextPath: File.Organization
  description: The organization of the file.
  type: String
- contextPath: File.AssociatedFileNames
  description: File names that are known as associated to the file.
  type: String
```

## IP
The following is the format for an IP entity

```json
"IP": {
    "Address": "STRING, IP address",
    "EntityA": "STRING, The source of the relationship.",
    "EntityB": "STRING, The destination of the relationship.",
    "Relationship": "STRING, The name of the relationship.",
    "EntityAType": "STRING, The type of the source of the relationship.",
    "EntityBType": "STRING, The type of the destination of the relationship.",
    "ASN": "STRING, The autonomous system name for the IP address, for example: 'AS8948'.",
    "Hostname": "STRING, The hostname that is mapped to this IP address.",
    "Geo":{
        "Location": "STRING, The geolocation where the IP address is located, in the format: latitude:longitude.",
        "Country": "STRING, The country in which the IP address is located.",
        "Description": "STRING, Additional information about the location."
    },
    "DetectionEngines": "NUMBER, The total number of engines that checked the indicator.",
    "PositiveDetections": "NUMBEr, The number of engines that positively detected the indicator as malicious.",
    "Malicious":{
        "Vendor": "STRING, The vendor reporting the IP address as malicious.",
        "Description": "STRING, A description explaining why the IP address was reported as malicious."
    },
    "Tags": "STRING, Tags of the IP.",
    "FeedRelatedIndicators": {
         "value": "STRING, Indicators that are associated with the IP.",
         "type": "STRING, The type of the indicators that are associated with the IP",
         "description": "STRING, The description of the indicators that are associated with the IP."
    },
    "MalwareFamily": "STRING, The malware family associated with the IP.",
    "Organization": {
         "Name": "STRING, The organization of the IP.",
         "Type": "STRING, The organization type of the IP."
    },
    "ASOwner": "STRING, The autonomous system owner of the IP.",
    "Region": "STRING, The region in which the IP is located.",
    "Port": "STRING, Ports that are associated with the IP.",
    "Internal": "BOOL, Whether or not the IP is internal or external.",
    "UpdatedDate": "DATE, The date that the IP was last updated.",
    "Registrar": {
        "Abuse":{
            "Name": "STRING, The name of the contact for reporting abuse.",
            "Address": "STRING, The address of the contact for reporting abuse.",
            "Country": "STRING, The country of the contact for reporting abuse.",
            "Network": "STRING, The network of the contact for reporting abuse.",
            "Phone": "STRING, The phone number of the contact for reporting abuse.",
            "Email": "STRING, The email address of the contact for reporting abuse.",
    }},
    "Campaign": "STRING, The campaign associated with the IP.",
    "TrafficLightProtocol": "STRING, The Traffic Light Protocol (TLP) color that is suitable for the IP.",
    "CommunityNotes": {
        "note": "STRING, Notes on the IP that were given by the community.",
        "timestamp": "DATE, The time in which the note was published."
    },
    "Publications": {
        "source": "STRING, The source in which the article was published.",
        "title": "STRING, The name of the article.",
        "link": "STRING, A link to the original article.",
        "timestamp": "DATE, The time in which the article was published."
    },
    "ThreatTypes": {
        "threatcategory": "STRING, The threat category associated to this indicator by the source vendor. For example, Phishing, Control, TOR, etc.",
        "threatcategoryconfidence": "STRING, Threat Category Confidence is the confidence level provided by the vendor for the threat type category For example a confidence of 90 for threat type category 'malware' means that the vendor rates that this is 90% confidence of being a malware."
    }
}
```

**In YAML**
```yaml
outputs:
- contextPath: IP.Address
  description: IP address
  type: String
- contextPath: IP.Relationships.EntityA
  description: The source of the relationship.
  type: string
- contextPath: IP.Relationships.EntityB
  description: The destination of the relationship.
  type: string
- contextPath: IP.Relationships.Relationship
  description: The name of the relationship.
  type: string
- contextPath: IP.Relationships.EntityAType
  description: The type of the source of the relationship.
  type: string
- contextPath: IP.Relationships.EntityBType
  description: The type of the destination of the relationship.
  type: string
- contextPath: IP.ASN
  description: 'The autonomous system name for the IP address, for example: "AS8948".'
  type: String
- contextPath: IP.Hostname
  description: The hostname that is mapped to this IP address.
  type: String
- contextPath: IP.Geo.Location
  description: 'The geolocation where the IP address is located, in the format: latitude:longitude.'
  type: String
- contextPath: IP.Geo.Country
  description: The country in which the IP address is located.
  type: String
- contextPath: IP.Geo.Description
  description: Additional information about the location.
  type: String
- contextPath: IP.DetectionEngines
  description: The total number of engines that checked the indicator.
  type: Number
- contextPath: IP.PositiveDetections
  description: The number of engines that positively detected the indicator as malicious.
  type: Number
- contextPath: IP.Malicious.Vendor
  description: The vendor reporting the IP address as malicious.
  type: String
- contextPath: IP.Malicious.Description
  description: A description explaining why the IP address was reported as malicious.
  type: String
- contextPath: IP.Tags
  description: (List) Tags of the IP.
  type: Unknown
- contextPath: IP.FeedRelatedIndicators.value
  description: Indicators that are associated with the IP.
  type: String
- contextPath: IP.FeedRelatedIndicators.type
  description: The type of the indicators that are associated with the IP.
  type: String
- contextPath: IP.FeedRelatedIndicators.description
  description: The description of the indicators that are associated with the IP.
  type: String
- contextPath: IP.MalwareFamily
  description: The malware family associated with the IP.
  type: String
- contextPath: IP.Organization.Name
  description: The organization of the IP.
  type: String
- contextPath: IP.Organization.Type
  description: The organization type of the IP.
  type: String
- contextPath: IP.ASOwner
  description: The autonomous system owner of the IP.
  type: String
- contextPath: IP.Region
  description: The region in which the IP is located.
  type: String
- contextPath: IP.Port
  description: Ports that are associated with the IP.
  type: String
- contextPath: IP.Internal
  description: Whether or not the IP is internal or external.
  type: Bool
- contextPath: IP.UpdatedDate
  description: The date that the IP was last updated.
  type: Date
- contextPath: IP.Registrar.Abuse.Name
  description: The name of the contact for reporting abuse.
  type: String
- contextPath: IP.Registrar.Abuse.Address
  description: The address of the contact for reporting abuse.
  type: String
- contextPath: IP.Registrar.Abuse.Country
  description: The country of the contact for reporting abuse.
  type: String
- contextPath: IP.Registrar.Abuse.Network
  description: The network of the contact for reporting abuse.
  type: String
- contextPath: IP.Registrar.Abuse.Phone
  description: The phone number of the contact for reporting abuse.
  type: String
- contextPath: IP.Registrar.Abuse.Email
  description: The email address of the contact for reporting abuse.
  type: String
- contextPath: IP.Campaign
  description: The campaign associated with the IP.
  type: String
- contextPath: IP.TrafficLightProtocol
  description: The Traffic Light Protocol (TLP) color that is suitable for the IP.
  type: String
- contextPath: IP.CommunityNotes.note
  description: Notes on the IP that were given by the community.
  type: String
- contextPath: IP.CommunityNotes.timestamp
  description: The time in which the note was published.
  type: Date
- contextPath: IP.Publications.source
  description: The source in which the article was published.
  type: String
- contextPath: IP.Publications.title
  description: The name of the article.
  type: String
- contextPath: IP.Publications.link
  description: A link to the original article.
  type: String
- contextPath: IP.Publications.timestamp
  description: The time in which the article was published.
  type: Date
- contextPath: IP.ThreatTypes.threatcategory
  description: The threat category associated to this indicator by the source vendor. For example, Phishing, Control, TOR, etc.
  type: String
- contextPath: IP.ThreatTypes.threatcategoryconfidence
  description: Threat Category Confidence is the confidence level provided by the vendor for the threat type category For example a confidence of 90 for threat type category 'malware' means that the vendor rates that this is 90% confidence of being a malware.
  type: String

```

## Endpoint
The following is the format for an Endpoint.

```python
"Endpoint": {
    "Hostname": "STRING, The endpoint's hostname.",
    "EntityA": "STRING, The source of the relationship.",
    "EntityB": "STRING, The destination of the relationship.",
    "Relationship": "STRING, The name of the relationship.",
    "EntityAType": "STRING, The type of the source of the relationship.",
    "EntityBType": "STRING, The type of the destination of the relationship.",
    "ID": "STRING, The endpoint's ID.",
    "IPAddress": "STRING, The endpoint's IP address.",
    "Domain": "STRING, The endpoint's domain.",
    "MACAddress": "STRING, The endpoint's MAC address.",
    "DHCPServer": "STRING, The DHCP server of the endpoint.",
    "OS": "STRING, The endpoint's operation system.",
    "OSVersion": "STRING, The endpoint's operation system version.",
    "BIOSVersion": "STRING, The endpoint's BIOS version.",
    "Model": "STRING, The model of the machine or device.",
    "Memory": "INT, Memory on this endpoint.",
    "Processors": "INT, The number of processors.",
    "Processor": "STRING, The model of the processor.",
    "IsIsolated": "STRING, The endpoint's isolation status.",
    "Status": "STRING, The endpoint's status.",
    "Vendor": "STRING, The integration name of the endpoint vendor.",

}
```

**In YAML**
```yaml
    outputs:
    - contextPath: Endpoint.Hostname
      description: The endpoint's hostname.
      type: String
    - contextPath: Endpoint.Relationships.EntityA
      description: The source of the relationship.
      type: string
    - contextPath: Endpoint.Relationships.EntityB
      description: The destination of the relationship.
      type: string
    - contextPath: Endpoint.Relationships.Relationship
      description: The name of the relationship.
      type: string
    - contextPath: Endpoint.Relationships.EntityAType
      description: The type of the source of the relationship.
      type: string
    - contextPath: Endpoint.Relationships.EntityBType
      description: The type of the destination of the relationship.
      type: string
    - contextPath: Endpoint.OS
      description: The endpoint's operation system.
      type: String
    - contextPath: Endpoint.IPAddress
      description: The endpoint's IP address.
      type: String
    - contextPath: Endpoint.ID
      description: The endpoint's ID.
      type: String
    - contextPath: Endpoint.Status
      description: The endpoint's status.
      type: String
    - contextPath: Endpoint.IsIsolated
      description: The endpoint's isolation status.
      type: String
    - contextPath: Endpoint.MACAddress
      description: The endpoint's MAC address.
      type: String
    - contextPath: Endpoint.Vendor
      description: The integration name of the endpoint vendor.
      type: String
    - contextPath: Endpoint.Domain
      description: The endpoint's domain.
      type: String
    - contextPath: Endpoint.DHCPServer
      description: The DHCP server of the endpoint.
      type: String
    - contextPath: Endpoint.OSVersion
      description: The endpoint's operation system version.
      type: String
    - contextPath: Endpoint.BIOSVersion
      description: The endpoint's BIOS version.
      type: String
    - contextPath: Endpoint.Model
      description: The model of the machine or device.
      type: String
    - contextPath: Endpoint.Memory
      description: Memory on this endpoint.
      type: Int
    - contextPath: Endpoint.Processors
      description: The number of processors.
      type: Int
    - contextPath: Endpoint.Processor
      description: The model of the processor.
      type: String
```

## Email Object
The following is the format for an Email Object.
```json
"Email": {
    "To": "STRING, The recipient of the email.",
    "From": "STRING, The sender of the email.",
    "CC": "STRING, Email addresses CC'ed to the email.",
    "BCC": "STRING, Email addresses BCC'ed to the email.",
    "EntityA": "STRING, The source of the relationship.",
    "EntityB": "STRING, The destination of the relationship.",
    "Relationship": "STRING, The name of the relationship.",
    "EntityAType": "STRING, The type of the source of the relationship.",
    "EntityBType": "STRING, The type of the destination of the relationship.",
    "Format": "STRING, The format of the email.",
    "Body/HTML": "STRING, The HTML version of the email.",
    "Body/Text": "STRING, The plain-text version of the email.",
    "Subject": "STRING, The subject of the email.",
    "Headers": "STRING, The headers of the email.",
    "Attachments": [
        "entryID"
    ]
}
```

**In YAML**
```yaml
outputs:
- contextPath: Email.To
  description: The recipient of the email.
  type: String
- contextPath: Email.From
  description: The sender of the email.
  type: String
- contextPath: Email.CC
  description: Email addresses CC'ed to the email.
  type: String
- contextPath: Email.BCC
  description: Email addresses BCC'ed to the email.
  type: String
- contextPath: Email.Format
  description: The format of the email.
  type: String
- contextPath: Email.Relationships.EntityA
  description: The source of the relationship.
  type: string
- contextPath: Email.Relationships.EntityB
  description: The destination of the relationship.
  type: string
- contextPath: Email.Relationships.Relationship
  description: The name of the relationship.
  type: string
- contextPath: Email.Relationships.EntityAType
  description: The type of the source of the relationship.
  type: string
- contextPath: Email.Relationships.EntityBType
  description: The type of the destination of the relationship.
  type: string
- contextPath: Email.Body/HTML
  description: The HTML version of the email.
  type: String
- contextPath: Email.Body/Text
  description: The plain-text version of the email.
  type: String
- contextPath: Email.Subject
  description: The subject of the email.
  type: String
- contextPath: Email.Headers
  description: The headers of the email.
  type: String
- contextPath: Email.Attachment
  description: List<String> Entry IDs of email attachments
  type: Unknown
```

## Domain
The following is the format for a Domain. Please note that for WHOIS, the entity is a dictionary nested for the key "WHOIS".
```json 
"Domain": {
    "Name": "STRING, The domain name, for example: 'google.com'.",
    "EntityA": "STRING, The source of the relationship.",
    "EntityB": "STRING, The destination of the relationship.",
    "Relationship": "STRING, The name of the relationship.",
    "EntityAType": "STRING, The type of the source of the relationship.", 
    "EntityBType": "STRING, The type of the destination of the relationship.",
    "DNS": "STRING, A list of IP objects resolved by DNS.",
    "DetectionEngines": "NUMBER, The total number of engines that checked the indicator.",
    "PositiveDetections": "NUMBER, The number of engines that positively detected the indicator as malicious.",
    "CreationDate": "DATE, The date that the domain was created.",
    "UpdatedDate": "DATE, The date that the domain was last updated.",
    "ExpirationDate": "DATE, The expiration date of the domain.",
    "DomainStatus": "STRING, The status of the domain.",
    "NameServers": "STRING, Name servers of the domain.",
    "Organization": "STRING, The organization of the domain.",
    "Subdomains": "STRING, Subdomains of the domain.",
    "Admin": {
        "Country": "STRING, The country of the domain administrator.",
        "Email": "STRING, The email address of the domain administrator.",
        "Name": "STRING, The name of the domain administrator.",
        "Phone": "STRING, The phone number of the domain administrator."
    },
    "Registrant": {
        "Country": "STRING, The country of the registrant.",
        "Email": "STRING, The email address of the registrant.",
        "Name": "STRING, The name of the registrant.",
        "Phone": "STRING, The phone number for receiving abuse reports."
    },
    "Tags": "STRING, Tags of the domain.",
    "FeedRelatedIndicators": {
         "value": "STRING, Indicators that are associated with the domain.",
         "type": "STRING, The type of the indicators that are associated with the domin",
         "description": "STRING, The description of the indicators that are associated with the domain."
    },
    "MalwareFamily": "STRING, The malware family associated with the domain.",
    "WHOIS": {
        "DomainStatus": "STRING, The status of the domain.",
        "NameServers": "STRING, A list of name servers, for example: 'ns1.bla.com, ns2.bla.com'.",
        "CreationDate": "DATE, The date that the domain was created.",
        "UpdatedDate": "DATE, The date that the domain was last updated.",
        "ExpirationDate": "DATE, The date that the domain expires.",
        "Registrant": {
            "Name": "STRING, The name of the registrant.",
            "Email": "STRING, The email address of the registrant.",
            "Phone": "STRING, The phone number of the registrant."
        },
        "Registrar": {
            "Name": "STRING, The name of the registrar, for example: 'GoDaddy'.",
            "AbuseEmail": "STRING, The email address of the contact for reporting abuse.",
            "AbusePhone": "STRING, The phone number of contact for reporting abuse."
        },
        "Admin": {
            "Name": "STRING, The name of the domain administrator.",
            "Email": "STRING, The email address of the domain administrator.",
            "Phone": "STRING, The phone number of the domain administrator."
        }
    },
    "WHOIS/History": "List of Whois objects",
    "Malicious":{
        "Vendor": "STRING, The vendor reporting the domain as malicious.",
        "Description": "STRING, A description explaining why the domain was reported as malicious."
    },
   "DomainIDNName": "STRING, The internationalized domain name (IDN) of the domain.",
   "Port": "STRING, Ports that are associated with the domain.",
   "Internal": "BOOL, Whether or not the domain is internal or external.",
   "Category": "STRING, The category associated with the indicator.",
   "Campaign": "STRING, The campaign associated with the domain.",
   "TrafficLightProtocol": "STRING, The Traffic Light Protocol (TLP) color that is suitable for the domain.",
   "ThreatTypes": {
        "threatcategory": "STRING, The threat category associated to this indicator by the source vendor. For example, Phishing, Control, TOR, etc.",
        "threatcategoryconfidence": "STRING, Threat Category Confidence is the confidence level provided by the vendor for the threat type category For example a confidence of 90 for threat type category 'malware' means that the vendor rates that this is 90% confidence of being a malware."
   },
   "Geo":{
        "Location": "STRING, The geolocation where the domain address is located, in the format: latitude:longitude.",
        "Country": "STRING, The country in which the domain address is located.",
        "Description": "STRING, Additional information about the location."
   },
   "Tech": {
       "Country": "STRING, The country of the domain technical contact.",
       "Name": "STRING, The name of the domain technical contact.",
       "Organization": "STRING, The organization of the domain technical contact.",
       "Email": "STRING, The email address of the domain technical contact."
   },
   "CommunityNotes": {
        "note": "STRING, Notes on the domain that were given by the community.",
        "timestamp": "DATE, The time in which the note was published."
   },
   "Publications": {
        "source": "STRING, The source in which the article was published.",
        "title": "STRING, The name of the article.",
        "link": "STRING, A link to the original article.",
        "timestamp": "DATE, The time in which the article was published."
   },
   "Billing": "STRING, The billing address of the domain.",
   
}
```

**In YAML**
```yaml
outputs:
- contextPath: Domain.Name
  description: 'The domain name, for example: "google.com".'
  type: String
- contextPath: Domain.Relationships.EntityA
  description: The source of the relationship.
  type: string
- contextPath: Domain.Relationships.EntityB
  description: The destination of the relationship.
  type: string
- contextPath: Domain.Relationships.Relationship
  description: The name of the relationship.
  type: string
- contextPath: Domain.Relationships.EntityAType
  description: The type of the source of the relationship.
  type: string
- contextPath: Domain.Relationships.EntityBType
  description: The type of the destination of the relationship.
  type: string
- contextPath: Domain.DNS
  description: A list of IP objects resolved by DNS.
  type: String
- contextPath: Domain.DetectionEngines
  description: The total number of engines that checked the indicator.
  type: Number
- contextPath: Domain.PositiveDetections
  description: The number of engines that positively detected the indicator as malicious.
  type: Number
- contextPath: Domain.CreationDate
  description: The date that the domain was created.
  type: Date
- contextPath: Domain.UpdatedDate
  description: The date that the domain was last updated.
  type: String
- contextPath: Domain.ExpirationDate
  description: The expiration date of the domain.
  type: Date
- contextPath: Domain.DomainStatus
  description: The status of the domain.
  type: Datte
- contextPath: Domain.NameServers
  description: (List<String>) Name servers of the domain.  
  type: Unknown
- contextPath: Domain.Organization
  description: The organization of the domain.
  type: String
- contextPath: Domain.Subdomains
  description: (List<String>) Subdomains of the domain.
  type: Unknown
- contextPath: Domain.Admin.Country
  description: The country of the domain administrator.
  type: String
- contextPath: Domain.Admin.Email
  description: The email address of the domain administrator.
  type: String
- contextPath: Domain.Admin.Name
  description: The name of the domain administrator.
  type: String
- contextPath: Domain.Admin.Phone
  description: The phone number of the domain administrator.
  type: String
- contextPath: Domain.Registrant.Country
  description: The country of the registrant.
  type: String
- contextPath: Domain.Registrant.Email
  description: The email address of the registrant.
  type: String
- contextPath: Domain.Registrant.Name
  description: The name of the registrant.
  type: String
- contextPath: Domain.Registrant.Phone
  description: The phone number for receiving abuse reports.
  type: String
- contextPath: Domain.Tags
  description: (List) Tags of the domain.
  type: Unknown
- contextPath: Domain.FeedRelatedIndicators.value
  description: Indicators that are associated with the domain.
  type: String
- contextPath: Domain.FeedRelatedIndicators.type
  description: The type of the indicators that are associated with the domain.
  type: String
- contextPath: Domain.FeedRelatedIndicators.description
  description: The description of the indicators that are associated with the domain.
  type: String
- contextPath: Domain.MalwareFamily
  description: The malware family associated with the domain.
  type: String
- contextPath: Domain.WHOIS.DomainStatus
  description: The status of the domain.
  type: String
- contextPath: Domain.WHOIS.NameServers
  description: (List<String>) Name servers of the domain.
  type: String
- contextPath: Domain.WHOIS.CreationDate
  description: The date that the domain was created.
  type: Date
- contextPath: Domain.WHOIS.UpdatedDate
  description: The date that the domain was last updated.
  type: Date
- contextPath: Domain.WHOIS.ExpirationDate
  description: The expiration date of the domain.
  type: Date
- contextPath: Domain.WHOIS.Registrant.Name
  description: The name of the registrant.
  type: String
- contextPath: Domain.WHOIS.Registrant.Email
  description: The email address of the registrant.
  type: String
- contextPath: Domain.WHOIS.Registrant.Phone
  description: The phone number of the registrant.
  type: String
- contextPath: Domain.WHOIS.Registrar.Name
  description: 'The name of the registrar, for example: 'GoDaddy"'
  type: String
- contextPath: Domain.WHOIS.Registrar.AbuseEmail
  description: The email address of the contact for reporting abuse.
  type: String
- contextPath: Domain.WHOIS.Registrar.AbusePhone
  description: The phone number of contact for reporting abuse.
  type: String
- contextPath: Domain.WHOIS.Admin.Name
  description: The name of the domain administrator.
  type: String
- contextPath: Domain.WHOIS.Admin.Email
  description: The email address of the domain administrator.
  type: String
- contextPath: Domain.WHOIS.Admin.Phone
  description: The phone number of the domain administrator.
  type: String
- contextPath: Domain.WHOIS/History
  description: List of Whois objects
  type: String
- contextPath: Domain.Malicious.Vendor
  description: The vendor reporting the domain as malicious.
  type: String
- contextPath: Domain.Malicious.Description
  description: A description explaining why the domain was reported as malicious.
  type: String
- contextPath: Domain.DomainIDNName
  description: The internationalized domain name (IDN) of the domain.
  type: String
- contextPath: Domain.Port
  description: Ports that are associated with the domain.
  type: String
- contextPath: Domain.Internal
  description: Whether or not the domain is internal or external.
  type: Bool
- contextPath: Domain.Category
  description: The category associated with the indicator.
  type: String
- contextPath: Domain.Campaign
  description: The campaign associated with the domain.
  type: String
- contextPath: Domain.TrafficLightProtocol
  description: The Traffic Light Protocol (TLP) color that is suitable for the domain.
  type: String
- contextPath: Domain.ThreatTypes.threatcategory
  description: The threat category associated to this indicator by the source vendor. For example, Phishing, Control, TOR, etc.
  type: String
- contextPath: Domain.ThreatTypes.threatcategoryconfidence
  description: Threat Category Confidence is the confidence level provided by the vendor for the threat type category For example a confidence of 90 for threat type category 'malware' means that the vendor rates that this is 90% confidence of being a malware.
  type: String
- contextPath: Domain.Geo.Location
  description: 'The geolocation where the domain address is located, in the format: latitude:longitude.'
  type: String
- contextPath: Domain.Geo.Country
  description: The country in which the domain address is located.
  type: String
- contextPath: Domain.Geo.Description
  description: Additional information about the location.
  type: String
- contextPath: Domain.Tech.Country
  description: The country of the domain technical contact.
  type: String
- contextPath: Domain.Tech.Name
  description: The name of the domain technical contact.
  type: String
- contextPath: Domain.Tech.Organization
  description: The organization of the domain technical contact.
  type: String
- contextPath: Domain.Tech.Email
  description: The email address of the domain technical contact.
  type: String
- contextPath: Domain.CommunityNotes.note
  description: Notes on the domain that were given by the community.
  type: String
- contextPath: Domain.CommunityNotes.timestamp
  description: The time in which the note was published.
  type: Date
- contextPath: Domain.Publications.source
  description: The source in which the article was published.
  type: String
- contextPath: Domain.Publications.title
  description: The name of the article.
  type: String
- contextPath: Domain.Publications.link
  description: A link to the original article.
  type: String
- contextPath: Domain.Publications.timestamp
  description: The time in which the article was published.
  type: Date
- contextPath: Domain.Billing
  description: The billing address of the domain.
  type: String
```

## URL
The following is the format for a URL entity.
```json
"URL": {
    "Data": "STRING, The URL",
    "EntityA": "STRING, The source of the relationship.",
    "EntityB": "STRING, The destination of the relationship.",
    "Relationship": "STRING, The name of the relationship.",
    "EntityAType": "STRING, The type of the source of the relationship.",
    "EntityBType": "STRING, The type of the destination of the relationship.",
    "Malicious": {
        "Vendor": "STRING, The vendor reporting the URL as malicious.",
        "Description": "STRING, A description of the malicious URL."
    },
    "DetectionEngines": "NUMBER, The total number of engines that checked the indicator.",
    "PositiveDetections": "NUMBER, The number of engines that positively detected the indicator as malicious.",
    "Category": "STRING, The category associated with the indicator.",
    "Tags": "STRING, Tags of the URL.",
    "FeedRelatedIndicators": {
         "value": "STRING, Indicators that are associated with the URL.",
         "type": "STRING, The type of the indicators that are associated with the URL",
         "description": "STRING, The description of the indicators that are associated with the URL."
    },
    "MalwareFamily": "STRING, The malware family associated with the URL.",
    "Port": "STRING, Ports that are associated with the URL.",
    "Internal": "STRING, Whether or not the URL is internal or external.",
    "Campaign": "STRING, The campaign associated with the URL.",
    "TrafficLightProtocol": "STRING, The Traffic Light Protocol (TLP) color that is suitable for the URL.",
    "ThreatTypes": {
        "threatcategory": "STRING, The threat category associated to this indicator by the source vendor. For example, Phishing, Control, TOR, etc.",
        "threatcategoryconfidence": "STRING, Threat Category Confidence is the confidence level provided by the vendor for the threat type category For example a confidence of 90 for threat type category 'malware' means that the vendor rates that this is 90% confidence of being a malware."
    },
    "ASN": "STRING, The autonomous system name for the URL, for example: 'AS8948'.",
    "ASOwner": "STRING, The autonomous system owner of the URL.",
    "Geo": {
      "Country": "STRING, The country in which the URL is located."
    },
    "Organization": "STRING, The organization of the URL.",
    "CommunityNotes": {
        "note": "STRING, Notes on the URL that were given by the community.",
        "timestamp": "DATE, The time in which the note was published."
    },
    "Publications": {
        "source": "STRING, The source in which the article was published.",
        "title": "STRING, The name of the article.",
        "link": "STRING, A link to the original article.",
        "timestamp": "DATE, The time in which the article was published."
    }
}
```

**In YAML**
```yaml
outputs:
- contextPath: URL.Data
  description: The URL
  type: String
- contextPath: URL.Relationships.EntityA
  description: The source of the relationship.
  type: string
- contextPath: URL.Relationships.EntityB
  description: The destination of the relationship.
  type: string
- contextPath: URL.Relationships.Relationship
  description: The name of the relationship.
  type: string
- contextPath: URL.Relationships.EntityAType
  description: The type of the source of the relationship.
  type: string
- contextPath: URL.Relationships.EntityBType
  description: The type of the destination of the relationship.
  type: string
- contextPath: URL.DetectionEngines
  description: The total number of engines that checked the indicator.
  type: String
- contextPath: URL.PositiveDetections
  description: The number of engines that positively detected the indicator as malicious.
  type: String
- contextPath: URL.Category
  description: The category associated with the indicator.
  type: String
- contextPath: URL.Malicious.Vendor
  description: The vendor reporting the URL as malicious.
  type: String
- contextPath: URL.Malicious.Description
  description: A description of the malicious URL.
  type: String
- contextPath: URL.Tags
  description: (List) Tags of the URL.
  type: Unknown
- contextPath: URL.FeedRelatedIndicators.value
  description: Indicators that are associated with the URL.
  type: String
- contextPath: URL.FeedRelatedIndicators.type
  description: The type of the indicators that are associated with the URL.
  type: String
- contextPath: URL.FeedRelatedIndicators.description
  description: The description of the indicators that are associated with the URL.
  type: String
- contextPath: URL.MalwareFamily
  description: The malware family associated with the URL.
  type: String
- contextPath: URL.Port
  description: Ports that are associated with the URL.
  type: String
- contextPath: URL.Internal
  description: Whether or not the URL is internal or external.
  type: Bool
- contextPath: URL.Campaign
  description: The campaign associated with the URL.
  type: String
- contextPath: URL.TrafficLightProtocol
  description: The Traffic Light Protocol (TLP) color that is suitable for the URL.
  type: String
- contextPath: URL.ThreatTypes.threatcategory
  description: The threat category associated to this indicator by the source vendor. For example, Phishing, Control, TOR, etc.
  type: String
- contextPath: URL.ThreatTypes.threatcategoryconfidence
  description: Threat Category Confidence is the confidence level provided by the vendor for the threat type category For example a confidence of 90 for threat type category 'malware' means that the vendor rates that this is 90% confidence of being a malware.
  type: String
- contextPath: URL.ASN
  description: "The autonomous system name for the URL, for example: 'AS8948'."
  type: String
- contextPath: URL.ASOwner
  description:The autonomous system owner of the URL.
  type: String
- contextPath: URL.GeoCountry
  description: The country in which the URL is located.
  type: String
- contextPath: URL.Organization
  description:The organization of the URL.
  type: String
- contextPath: URL.CommunityNotes.note
  description: Notes on the URL that were given by the community.
  type: String
- contextPath: URL.CommunityNotes.timestamp
  description: The time in which the note was published.
  type: Date
- contextPath: URL.Publications.source
  description: The source in which the article was published.
  type: String
- contextPath: URL.Publications.title
  description: The name of the article.
  type: String
- contextPath: URL.Publications.link
  description: A link to the original article.
  type: String
- contextPath: URL.Publications.timestamp
  description: The time in which the article was published.
  type: Date
```

## CVE
The following is the format for a CVE.
```python
"CVE": {
    "ID": "STRING, The ID of the CVE, for example: CVE-2015-1653",
    "EntityA": "STRING, The source of the relationship.",
    "EntityB": "STRING, The destination of the relationship.",
    "Relationship": "STRING, The name of the relationship.",
    "EntityAType": "STRING, The type of the source of the relationship.",
    "EntityBType": "STRING, The type of the destination of the relationship.",
    "CVSS": "STRING, The CVSS of the CVE, for example: 10.0",
    "Published": "DATE, The timestamp of when the CVE was published.",
    "Modified": "DATE, The timestamp of when the CVE was last modified.",
    "Description": "STRING, A description of the CVE."
}
```

**In YAML**
```yaml
outputs:
- contextPath: CVE.ID
  description: 'The ID of the CVE, for example: CVE-2015-1653'
  type: String
- contextPath: CVE.Relationships.EntityA
  description: The source of the relationship.
  type: string
- contextPath: CVE.Relationships.EntityB
  description: The destination of the relationship.
  type: string
- contextPath: CVE.Relationships.Relationship
  description: The name of the relationship.
  type: string
- contextPath: CVE.Relationships.EntityAType
  description: The type of the source of the relationship.
  type: string
- contextPath: CVE.Relationships.EntityBType
  description: The type of the destination of the relationship.
  type: string
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

## Rule
The following is the format for a Rule.
```python
"Rule": {
    "Name": "STRING, The name of the rule.",
    "Condition": "STRING, The condition for the rule."
}
```

**In YAML**
```yaml

```

## InfoFile
The following is the expected format for an InfoFile. InfoFile is a file that isn't relevant as an indicator and is generally benign. For example, a report file that you are attaching to the incident.

```python
"InfoFile": {
    "Name": "STRING, The file name.",
    "EntryID": "STRING, The ID for locating the file in the War Room.",
    "Size": "INT, The size of the file (in bytes).",
    "Type": "STRING, The file type, as determined by libmagic (same as displayed in file entries).",
    "Extension": "STRING, The file extension.",
    "Info": "STRING, Basic information about the file."
}
```

**In YAML**
```yaml
outputs:
- contextPath: InfoFile.Name
  description: The file name.
  type: String
- contextPath: InfoFile.EntryID
  description: The ID for locating the file in the War Room.
  type: String
- contextPath: InfoFile.Size
  description: The size of the file (in bytes).
  type: Number
- contextPath: InfoFile.Type
  description: The file type, as determined by libmagic (same as displayed in file entries).
  type: String
- contextPath: InfoFile.Extension
  description: The file extension.
  type: String
- contextPath: InfoFile.Info
  description: Basic information about the file.
  type: String
```

## DBot Score
The following is the format for a DBot Score entry.
```python
"DBotScore": {
    "Indicator": "The indicator that was tested.",
    "Type": "The indicator type.",
    "Vendor": "The vendor used to calculate the score.",
    "Score": "The actual score.",
    "Reliability": "Reliability of the source providing the intelligence data."
}
```

**In YAML**
```yaml
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
- contextPath: DBotScore.Reliability
  description: Reliability of the source providing the intelligence data.
  type: String

```

## Certificate
The following is the format for an X509 certificate. 

```json
"Certificate": {
        "Name": "STRING, Name (CN or SAN) appearing in the certificate.",
        "SubjectDN": "STRING,  The Subject Distinguished Name of the certificate. This field includes the Common Name of the certificate.",
        "PEM": "STRING, Certificate in PEM format.",
        "IssuerDN": "STRING, The Issuer Distinguished Name of the certificate.",
        "SerialNumber": "STRING, The Serial Number of the certificate.",
        "ValidityNotAfter": "DATE, End of certificate validity period.",
        "ValidityNotBefore": "DATE, Start of certificate validity period.",
        "SubjectAlternativeName": {
          "Type": "STRING, Type of the SAN.",
          "Value": "STRING, Name of the SAN."
        },
        "SHA512": "STRING, SHA512 Fingerprint of the certificate in DER format.",
        "SHA256": "STRING, SHA256 Fingerprint of the certificate in DER format.",
        "SHA1": "STRING, SHA1 Fingerprint of the certificate in DER format.",
        "MD5": "STRING, MD5 Fingerprint of the certificate in DER format.",
        "PublicKey": {
          "Algorithm": "STRING, Algorithm used for public key of the certificate.",
          "Length": "NUMBER, Length in bits of the public key of the certificate.",
          "Modulus": "STRING, Certificate.PublicKey.Modulus",
          "Exponent": "NUMBER, Exponent of the public key for RSA keys.",
          "PublicKey": "STRING, The public key for DSA/Unknown keys.",
          "P": "STRING, The P parameter for DSA keys.",
          "Q": "STRING, The Q parameter for DSA keys.",
          "G": "STRING, The G parameter for DSA keys.",
          "X": "STRING, The X parameter for EC keys.",
          "Y": "STRING, The Y parameter for EC keys.",
          "Curve": "STRING, Curve of the Public Key for EC keys.",
          "Y": "STRING, The Y parameter for EC keys."
        },
        "SPKISHA256": "STRING, SHA256 fingerprint of the certificate Subject Public Key Info.",
        "Signature": {
          "Algorithm": "STRING, Algorithm used in the signature of the certificate.",
          "Signature": "STRING, Signature of the certificate."
        },
        "Extension": {
          "Critical": "BOOL, Critical flag of the certificate extension.",
          "OID": "STRING,  OID of the certificate extension.",
          "Name": "STRING, Name of the certificate extension.",
          "Value": "STRING, Value of the certificate extension."
        },
        "Malicious": {
             "Vendor": "STRING, The vendor that reported the certificate as malicious.",
             "Description": "STRING, A description explaining why the certificate was determined to be malicious."
        }
}
```

**In YAML**
```yaml
outputs:
- contextPath: Certificate.Name
  description: Name (CN or SAN) appearing in the certificate.
  type: String
- contextPath: Certificate.SubjectDN
  description: |
    The Subject Distinguished Name of the certificate.
    This field includes the Common Name of the certificate.
  type: String
- contextPath: Certificate.PEM
  description: Certificate in PEM format.
  type: String
- contextPath: Certificate.IssuerDN
  description: The Issuer Distinguished Name of the certificate.
  type: String
- contextPath: Certificate.SerialNumber
  description: The Serial Number of the certificate.
  type: String
- contextPath: Certificate.ValidityNotAfter
  description: End of certificate validity period.
  type: Date
- contextPath: Certificate.ValidityNotBefore
  description: Start of certificate validity period.
  type: Date
- contextPath: Certificate.SubjectAlternativeName.Type
  description: Type of the SAN.
  type: String
- contextPath: Certificate.SubjectAlternativeName.Value
  description: Name of the SAN.
  type: String
- contextPath: Certificate.SHA512
  description: SHA512 Fingerprint of the certificate in DER format.
  type: String
- contextPath: Certificate.SHA256
  description: SHA256 Fingerprint of the certificate in DER format.
  type: String
- contextPath: Certificate.SHA1
  description: SHA1 Fingerprint of the certificate in DER format.
  type: String
- contextPath: Certificate.MD5
  description: MD5 Fingerprint of the certificate in DER format.
  type: String
- contextPath: Certificate.PublicKey.Algorithm
  description: Algorithm used for public key of the certificate.
  type: String
- contextPath: Certificate.PublicKey.Length
  description: Length in bits of the public key of the certificate.
  type: Number
- contextPath: Certificate.PublicKey.Modulus
  description: Modulus of the public key for RSA keys.
  type: String
- contextPath: Certificate.PublicKey.Exponent
  description: Exponent of the public key for RSA keys.
  type: Number
- contextPath: Certificate.PublicKey.PublicKey
  description: The public key for DSA/Unknown keys.
  type: String
- contextPath: Certificate.PublicKey.P
  description: The P parameter for DSA keys.
  type: String
- contextPath: Certificate.PublicKey.Q
  description: The Q parameter for DSA keys.
  type: String
- contextPath: Certificate.PublicKey.G
  description: The G parameter for DSA keys.
  type: String
- contextPath: Certificate.PublicKey.X
  description: The X parameter for EC keys.
  type: String
- contextPath: Certificate.PublicKey.Y
  description: The Y parameter for EC keys.
  type: String
- contextPath: Certificate.PublicKey.Curve
  description: Curve of the Public Key for EC keys.
  type: String
- contextPath: Certificate.SPKISHA256
  description: SHA256 fingerprint of the certificate Subject Public Key Info.
  type: String
- contextPath: Certificate.Signature.Algorithm
  description: Algorithm used in the signature of the certificate.
  type: String
- contextPath: Certificate.Signature.Signature
  description: Signature of the certificate.
  type: String
- contextPath: Certificate.Extension.Critical
  description: Critical flag of the certificate extension.
  type: Bool
- contextPath: Certificate.Extension.OID
  description: OID of the certificate extension.
  type: String
- contextPath: Certificate.Extension.Name
  description: Name of the certificate extension.
  type: String
- contextPath: Certificate.Extension.Value
  description: Value of the certificate extension.
  type: Unknown
- contextPath: Certificate.Malicious.Vendor
  description: The vendor that reported the file as malicious.
  type: String
- contextPath: Certificate.Malicious.Description
  description: A description explaining why the file was determined to be malicious.
  type: String  
```
