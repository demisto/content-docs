---
id: generic-commands-iam
title: Generic IAM Commands
---


## Background and motivation

IAM integrations generally do not support CRUD (Create, Retrieve, Update, and Disable/Delete) operations for general user accounts or provisioning users. These integrations should adhere to a standard as the workflows can be generalized or completely customized to fit into an organization's environment.

## Mappers
In order to properly map between the generic IAM user fields and the data from the integration, we need to define an incoming [Mapper](../incidents/incident-classification-mapping#map-event-attributes-to-fields) for the **get-user** command and an outgoing mapper for the create, update and disable commands. 

The mapper names should be the default values for "mapper-in" and "mapper-out" parameters of the inegration instance. 

For integrations that support the [SCIM](http://www.simplecloud.info/) protcol, you can use the built in SCIM mappers in the IAM-SCIM pack.  


## Generic IAM Commands needs to be supported

### **iam-get-user**

**Description:** Returns information about a user

**Input:** User profile which contains the email of the users we would like to retrieve  
**Input Examples:**
```
!iam-get-user user-profile=`{"email": "demistotest@paloaltonetworks.com"}`
```

**Sample output:**
```json
{
  "IAM.Vendor": {
    "brand": "Vendor", 
    "instanceName": "Instance name here",
    "success": true,
    "active": true,
    "id": "Unique Id here",
    "username": "demistotest@paloaltonetworks.com",
    "email": "demistotest@paloaltonetworks.com",
    "errorCode": "null for success response",
    "errorMessage": "null for success response",
    "details": {
      "Payload can go as is here in json format": ""
    }
  }
}
```

## **iam-create-user**

**Description:** creates a user

**Input:** User Profile with the new user data

**Input Examples:**

```
!iam-create-user user-profile=`{"email": "demistotest@paloaltonetworks.com", "givenname": "test", "surname": "test"}`
```

**Sample output:**
```json
{
  "IAM.Vendor": {
    "brand": "Vendor",
    "instanceName": "Instance name here",
    "success": true,
    "active": true,
    "id": "Unique Id here",
    "username": "demistotest@paloaltonetworks.com",
    "email": "demistotest@paloaltonetworks.com",
    "errorCode": "null for success response",
    "errorMessage": "null for success response",
    "details": {
      "Payload can go as is here in json format": ""
    }
  }
}
```

## **update-user**

**Description:** Updates a user

**Input:** 
User Profile with the updated user data.
allow-enable: enable this user

**Input Examples:**

```
!iam-update-user user-profile=`{"email": "demistotest@paloaltonetworks.com", "givenname": "John"}` allow-enable=true
```

**Sample output:**
```json
{
  "IAM.Vendor": {
    "brand": "Vendor",
    "instanceName": "Instance name here",
    "success": true,
    "active": true,
    "id": "Unique Id here",
    "username": "demistotest@paloaltonetworks.com",
    "email": "demistotest@paloaltonetworks.com",
    "errorCode": "null for success response",
    "errorMessage": "null for success response",
    "details": {
      "Payload can go as is here in json format": ""
    }
  }
}
```

## **iam-disable-user**

**Description:** Disables a user

**Input:** User Profile which contains the user id to disable

**Input Examples:**

```
!iam-disable-user user-profile=`{"email": "demistotest@paloaltonetworks.com"}`
```


**Sample output:**
```json

{
  "IAM.Vendor": {
    "brand": "Vendor",
    "instanceName": "Instance name here",
    "success": true,
    "active": false,
    "id": "Unique Id here",
    "username": "demistotest@paloaltonetworks.com",
    "email": "demistotest@paloaltonetworks.com",
    "errorCode": "null for success response",
    "errorMessage": "null for success response",
    "details": {
      "Payload can go as is here in json format": ""
    }
  }
}

```

## Integrations for reference

[HelloIAMWorld](https://github.com/demisto/content/tree/master/Packs/HelloIAMWorld/Integrations/HelloIAMWorld) 
[Okta](https://github.com/demisto/content/tree/master/Packs/Okta/Integrations/Okta_IAM)
[ServiceNow](https://github.com/demisto/content/tree/master/Packs/ServiceNow/Integrations/ServiceNow_IAM)
