---
id: context-standards-recommended
title: Recommended Context Standards
---

Below are examples of how each entity should be formed in the entry context.

## Ticket
The following is the format for a ticket.
```json
"Ticket": {
    "ID": "STRING, The ID of the ticket.",
    "Creator": "STRING, The user who created the ticket.",
    "Assignee": "STRING, The user assigned to the ticket.",
    "State": "STRING, The status of the ticket. Can be "closed", "open", or "on hold".",
    "Description": "STRING The summary of the ticket."
}
```

**In YAML**
```yaml
outputs:
- contextPath: Ticket.ID
  description: The ID of the ticket.
  type: String
- contextPath: Ticket.Creator
  description: The user who created the ticket.
  type: String
- contextPath: Ticket.Assignee
  description: The user assigned to the ticket.
  type: String
- contextPath: Ticket.State
  description: The status of the ticket. Can be "closed", "open", or "on hold".
  type: String
- contextPath: Ticket.Description
  description: The summary of the ticket.
  type: String
```
## Account
The following is the format for an Account entity.
```json
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
    "IsEnabled": "BOOL, Whether the account is enabled or disabled. 'True' means the account is enabled.",
    "CloudApplications": [
      {
        "ApplicationName": "STRING, Cloud application name that is assosciated with this account"
      }
    ],
    "ChangePasswordAtNextLogin": "BOOL, Whether this account should change its password at the next login",
    "IsInternal": "BOOL, Whether this account is internal or external to the organization",
    "Manager": {
      "Email": "STRING, The email address of the manager.",
      "DisplayName": "STRING, The display name of the manager."
    }
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
- contextPath: Account.CloudApplications.Application Name
  description: Cloud application name that is assosciated with this account.
  type: String
- contextPath: Account.ChangePasswordAtNextLogin
  description: Whether this account should change its password at the next login. 'True' means the account have to change its password.
  type: Bool
- contextPath: Account.IsInternal
  description: Whether the account is internal or external to the organization. 'True' means the account is internal.
  type: Bool
- contextPath: Account.Manager.Email
  description: The email address of the manager.
  type: String
- contextPath: Account.Manager.DisplayName
  description: The display name of the manager.
  type: String


```

## Registry Key
The following is the format for a Registry Key.
```json
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


## Event
The following is the format for an Event.
```json
"Event": {
    "Type": "STRING, The type of event, for example: "ePO", "Protectwise", "DAM".",
    "ID": "STRING, The unique identifier of the event.",
    "Name": "STRING, The name of the event.",
    "Sensor": "STRING, The sensor that indicated the event.",
    "Rule": "STRING, The rule that triggered the event."
}
```

**In YAML**
```yaml
outputs:
- contextPath: Event.Type
  description: "The type of event, for example: "ePO", "Protectwise", "DAM"."
  type: String
- contextPath: Event.ID
  description: "The unique identifier of the event"
  type: String
- contextPath: Event.Name
  description: "The name of the event."
  type: String
- contextPath: Event.Sensor
  description: "The sensor that indicated the event."
  type: String
- contextPath: Event.Rule
  description: "The rule that triggered the event."
  type: String
```

## Service
The following is the format for a Service.
```json
"Service": {
    "Name": "STRING, The name of the service.",
    "BinPath": "STRING, The path of the /bin folder.",
    "CommandLine": "STRING, The full command line (including arguments).",
    "StartType": "STRING, How the service was started.",
    "State": "STRING, The status of the service."
}
```

**In YAML**
```yaml
outputs:
- contextPath: Service.Namee
  description: "The name of the service."
  type: String
- contextPath: Service.BinPath
  description: "The path of the /bin folder."
  type: String
- contextPath: Service.CommandLine
  description: "The full command line (including arguments)."
  type: String
- contextPath: Service.StartType
  description: "How the service was started."
  type: String
- contextPath: Service.State
  description: "The status of the service."
  type: String
```

## Process
The following is the format for a process.
```json
"Process": {
    "Name": "STRING, The name of the process.",
    "PID": "STRING, The PID of the process.",
    "Hostname": "STRING, The endpoint on which the process was seen.",
    "MD5": "STRING, The MD5 hash of the process.",
    "SHA1": "STRING, The SHA1 hash of the process.",
    "CommandLine": "STRING, The full command line (including arguments).",
    "Path": "STRING, The file system path to the binary file.",
    "Start Time": "DATE, The timestamp of the process start time.",
    "End Time": "DATE, The timestamp of the process end time.",
    "Parent": "STRING, Parent process objects.",
    "Sibling": "LIST, Sibling process objects.",
    "Child": "LIST, Child process objects."
}
```

**In YAML**
```yaml
outputs:
- contextPath: Process.Name
  description: "The name of the process."
  type: String
- contextPath: Process.PID
  description: "The PID of the process."
  type: String
- contextPath: Process.Hostname
  description: "The endpoint on which the process was seen."
  type: String
- contextPath: Process.MD5
  description: "The MD5 hash of the process."
  type: String
- contextPath: Process.SHA1
  description: "The SHA1 hash of the process."
  type: String
  - contextPath: Process.CommandLine
  description: "The full command line (including arguments)."
  type: String
- contextPath: Process.Path
  description: "The file system path to the binary file."
  type: String
- contextPath: Process.Start Time
  description: "The timestamp of the process start time."
  type: String
- contextPath: Process.End Time
  description: "The timestamp of the process end time."
  type: String
- contextPath: Process.Parent
  description: "Parent process objects."
  type: String
  - contextPath: Process.Sibling
  description: "Sibling process objects."
  type: String
- contextPath: Process.Child
  description: "Child process objects."
  type: String
```

