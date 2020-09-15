---
id: generic-iam-commands
title: Generic IAM Commands
---


## Background and motivation

Today the current XSOAR platform supports over 250+ integrations. however, these integrations generally do not support CRUD (Create, Retrieve, Update, and Disable/Delete) operations for general user accounts or provisioning users. IAM integrations should adhere to a standard as the workflows can be generalized or completely customized to fit into an organization's environment.

## SCIM

IAM Integration commands should support the System for Cross Domain Identity Management (SCIM) standard when possible specifically for integration command level input. For more info about SCIM take a look [Here](https://en.wikipedia.org/wiki/System_for_Cross-domain_Identity_Management) and [Here](https://tools.ietf.org/html/rfc7644)

## Generic IAM Commands needs to be supported

### **get-user**

**Description:** returns generic information about a user

**Input:** SCIM User Json with at least id, username or email address populated

**Input Examples:**

```json
{"id": "WCG8E1ZHS"}
```

```json
{"userName": "demistotest@paloaltonetworks.com"}
```

```json
{
  "emails": [
    {
      "type": "work",
      "primary": true,
      "value": "demistotest@paloaltonetworks.com"
    }
  ]
}
```

```json
{
  "userName": "demistotest@paloaltonetworks.com",
  "emails": [
    {
      "type": "work",
      "primary": true,
      "value": "demistotest@paloaltonetworks.com"
    }
  ]
}
```

**Sample output:**
```json
{
  "GetUser": {
    "brand": "Zoom",
    "instanceName": "Instance name here",
    "success": true,
    "active": true,
    "id": "Zoom Unique Id here",
    "username": "demistotest@paloaltonetworks.com",
    "email": "demistotest@paloaltonetworks.com",
    "errorCode": "null for success response",
    "errorMessage": "null for success response",
    "details": {
      "Zoom Payload can go as is here in json format": ""
    }
  }
}
```

## **create-user**
TBD

## **enable-user**
TBD

## **disable-user**
TBD

## **update-user**
TBD

## Integrations for reference

[Zoom](https://github.com/demisto/content/pull/8511/files) 

