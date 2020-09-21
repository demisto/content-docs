---
id: generic-commands-iam
title: Generic IAM Commands
---


## Background and motivation

IAM integrations generally do not support CRUD (Create, Retrieve, Update, and Disable/Delete) operations for general user accounts or provisioning users. These integrations should adhere to a standard as the workflows can be generalized or completely customized to fit into an organization's environment.

## SCIM

IAM Integration commands should support the System for Cross Domain Identity Management (SCIM) standard when possible specifically for integration command level input. For more info about SCIM take a look [Here](https://en.wikipedia.org/wiki/System_for_Cross-domain_Identity_Management) and [Here](https://tools.ietf.org/html/rfc7644)

## Generic IAM Commands needs to be supported

### **get-user**

**Description:** Returns generic information about a user

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

**Description:** creates a user

**Input:** Fully populated SCIM User Json

**Input Examples:**

```json
{
  "userName": "demistotest@paloaltonetworks.com",
  "externalId": "demistotest@paloaltonetworks.com",
  "title": "Demisto Engineer",
  "active": true,
  "userType": "Employee",
  "name": {
    "familyName": "Test",
    "givenName": "Demisto"
  },
  "emails": [
    {
      "type": "work",
      "primary": true,
      "value": "demistotest@paloaltonetworks.com"
    }
  ],
  "phoneNumbers": [
    {
      "value": "555-555-5555",
      "type": "work"
    }
  ],
  "urn:scim:schemas:extension:enterprise:1.0": {
    "employeeNumber": "123456",
    "department": "IT",
    "alias": "demistotest",
    "division": "IT Division",
    "costCenter": "4130",
    "countryCode": "840",
    "managerflag": "true"
  }
}
```

**Sample output:**
```json
{
  "CreateUser": {
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

## **update-user**

**Description:** Updates a user

**Input:** Old SCIM User Json with at least id, username or email address populated and a new user in a fully populated SCIM Json format.

**Input Examples:**

```json
Old user:
{
  "id": "Zoom unique id here"
}

New user:
{
  "userName": "demistotest@paloaltonetworks.com",
  "externalId": "demistotest@paloaltonetworks.com",
  "title": "Demisto Engineer",
  "active": true,
  "userType": "Employee",
  "name": {
    "familyName": "Test",
    "givenName": "Demisto"
  },
  "emails": [
    {
      "type": "work",
      "primary": true,
      "value": "demistotest@paloaltonetworks.com"
    }
  ],
  "phoneNumbers": [
    {
      "value": "555-555-5555",
      "type": "work"
    }
  ]
}
```

**Sample output:**
```json
{
  "UpdateUser": {
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

## **enable-user**

**Description:** Enables a previously disabled user

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

**Sample output:**
```json

{
  "EnableUser": {
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

## **disable-user**

**Description:** Disables a user

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

**Sample output:**
```json

{
  "DisableUser": {
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

## Integrations for reference

[Zoom](https://github.com/demisto/content/pull/8511/files) 

