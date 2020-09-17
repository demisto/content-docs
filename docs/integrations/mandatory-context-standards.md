---
id: mandatory-context-standards
title: Mandatory Context Standards
---

## File
The following is the format for a file.

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
        }
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
```

## IP
The following is the format for an IP entity

```json
"IP": {
    "Address": "STRING, IP address",
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
    }
}
```

**In YAML**
```yaml
outputs:- 
contextPath: IP.Address
  description: IP address
  type: String
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

```

## Endpoint
The following is the format for an Endpoint.

```python
"Endpoint": {
    "Hostname": "STRING, The hostname that is mapped to this endpoint.",
    "ID": "STRING, The unique ID within the tool retrieving the endpoint.",
    "IPAddress": "STRING, The IP address of the endpoint.",
    "Domain": "STRING, The domain of the endpoint.",
    "MACAddress": "STRING, The MAC address of the endpoint.",
    "DHCPServer": "STRING, The DHCP server of the endpoint.",
    "OS": "STRING, Endpoint OS.",
    "OSVersion": "STRING, OS version.",
    "BIOSVersion": "STRING, BIOS version.",
    "Model": "STRING, The model of the machine or device.",
    "Memory": "INT, Memory on this endpoint.",
    "Processors": "INT, The number of processors.",
    "Processor": "STRING, The model of the processor.",
    "IsIsolated": "BOOLEAN, Whether this endpoint isolated or not."
}
```

**In YAML**
```yaml

```

## Email Object
The following is the format for an Email Object.
```json
"Email": {
    "To": "STRING, The recipient of the email.",
    "From": "STRING, The sender of the email.",
    "CC": "STRING, Email addresses CC'ed to the email.",
    "BCC": "STRING, Email addresses BCC'ed to the email.",
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
    }
}
```

**In YAML**
```yaml
outputs:
- contextPath: Domain.Name
  description: 'The domain name, for example: "google.com".'
  type: String
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
```

## URL
The following is the format for a URL entity.
```json
"URL": {
    "Data": "STRING, The URL",
    "Malicious": {
        "Vendor": "STRING, The vendor reporting the URL as malicious.",
        "Description": "STRING, A description of the malicious URL."
    },
    "DetectionEngines": "NUMBER, The total number of engines that checked the indicator.",
    "PositiveDetections": "NUMBER, The number of engines that positively detected the indicator as malicious."
}
```

**In YAML**
```yaml
outputs:
- contextPath: URL.Data
  description: The URL
  type: String
- contextPath: URL.DetectionEngines
  description: The total number of engines that checked the indicator.
  type: String
- contextPath: URL.PositiveDetections
  description: The number of engines that positively detected the indicator as malicious.
  type: String
- contextPath: URL.Malicious.Vendor
  description: The vendor reporting the URL as malicious.
  type: String
- contextPath: URL.Malicious.Description
  description: A description of the malicious URL.
  type: String
```

## CVE
The following is the format for a CVE.
```python
"CVE": {
    "ID": "STRING, The ID of the CVE, for example: CVE-2015-1653",
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

## Account
The following is the format for an Account entity.
```python
"Account": {
    "Type": "STRING, The account type. The most common value is 'AD', but can be 'LocalOS', 'Google', 'AppleID', ... ",
    "ID": "STRING, The unique ID for the account (integration specific). For AD accounts this is the Distinguished Name (DN).",
    "Username": "STRING, The username in the relevant system.",
    "DisplayName": "STRING, The display name.",
    "Groups": "STRING, Groups to which the account belongs (integration specific). For example, for AD these are groups of which the account is memberOf.",
    "Domain": "STRING, The domain of the account.",
    "OrganizationUnit": "STRING, The Organization Unit (OU) of the account.",
    "Email": {
        "Address": "STRING, The email address of the account."
    },
    "TelephoneNumber": "STRING, The phone number associated with the account.",
    "Office": "STRING, The office where the person associated with the account works.",
    "JobTitle": "STRING, The job title of the account.",
    "Department": "STRING, The department of the account.",
    "Country": "STRING, The country associated with the account.",
    "State": "STRING, The state where the account works.",
    "City": "STRING, The city associated with the account.",
    "Street": "STRING, The street associated with the account.",
    "IsEnabled": "BOOL, Whether the account is enabled or disabled. 'True' means the account is enabled."
}
```

**In YAML**
```yaml
outputs:
- contextPath: Account.Type
  description: The account type. The most common value is 'AD', but can be 'LocalOS', 'Google', 'AppleID'
  type: String
- contextPath: Account.ID
  description: The unique ID for the account (integration specific). For AD accounts this is the Distinguished Name (DN).
  type: String
- contextPath: Account.Username
  description: The username in the relevant system.
  type: String
- contextPath: Account.DisplayName
  description: The display name.
  type: String
- contextPath: Account.Groups
  description: Groups to which the account belongs (integration specific). For example, for AD these are groups of which the account is memberOf.
  type: String
- contextPath: Account.Domain
  description: The domain of the account.
  type: String
- contextPath: Account.OrganizationUnit
  description: The Organization Unit (OU) of the account.
  type: String
- contextPath: Account.Email.Address
  description: The email address of the account.
  type: String
- contextPath: Account.TelephoneNumber
  description: The phone number associated with the account.
  type: String
- contextPath: Account.Office
  description: The office where the person associated with the account works.
  type: String
- contextPath: Account.JobTitle
  description: The job title of the account.
  type: String
- contextPath: Account.Department
  description: The department of the account.
  type: String
- contextPath: Account.Country
  description: The country associated with the account.
  type: String
- contextPath: Account.State
  description: The state where the account works.
  type: String
- contextPath: Account.City
  description: The city associated with the account.
  type: String
- contextPath: Account.Street
  description: The street associated with the account.
  type: String
- contextPath: Account.IsEnabled
  description: Whether the account is enabled or disabled. 'True' means the account is enabled.
  type: Bool
```

## Registry Key
The following is the format for a Registry Key.
```python
"RegistryKey": {
    "Path": "STRING, The path to the registry key",
    "Name": "STRING, The name of registry key.",
    "Value": "STRING, The value at the given RegistryKey."
}
```

**In YAML**
```yaml
outputs:
- contextPath: RegistryKey.Path
  description: The path to the registry key
  type: String
- contextPath: RegistryKey.Name
  description: The name of registry key.
  type: String
- contextPath: RegistryKey.Value
  description: The value at the given RegistryKey.
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

## Event
The following is the format for an Event.
```python
"Event": {
    "Type": "STRING, The type of event, for example: "ePO", "Protectwise", "DAM".",
    "ID": "STRING, The unique identifier of the event.",
    "Name": "STRING, The name of the event.",
    "Sensor": "STRING, The sensor that indicated the event.",
    "Rule": "STRING, The rule that triggered the event."
}
``` 

## InfoFile
The following is the expected format for an InfoFile
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
    "Score": "The actual score."
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

```
