---
id: iam-integrations
title: Developing an IAM Integration
---

## What is an IAM integration?

Cortex XSOAR version 6.0 and above supports the **Identity and Access Management** (IAM) use case, by offering the **[Identity Lifecycle Management](https://xsoar.pan.dev/docs/reference/articles/identity-lifecycle-management)** premium pack, along with additional IAM integrations. The **IAM integrations** are our tool to synchronize employee data between the XSOAR platform and the applications used in many organizations, such as Okta, Active Directory, Slack or Workday. All of these integrations must implement the basic management operations, such as commands for creating, retrieving, updating, and deleting or disabling users in a provisioning workflow. The integrations  must also adhere to a standard, as the workflows can be generalized or completely customized to fit into an organization's environment.
The following article describes how to initialize a template for an IAM integration and implement the commands.

## Create a new IAM integration

Use the **HelloIAMWorld** template to initialize a new IAM integration (replace “MyIntegration” with your integration name):
```
demisto-sdk init --integration -n MyIntegration -t HelloIAMWorld
```
**Note:** The HelloIAMWorld template, like any other IAM Integration, imports the [IAMApiModule](#iamapimodule-script-classes) script classes which implement most of the logic of the integration. The changes that need to be made to complete the development of the integration are detailed below.

After executing the above **init** command, a new integration directory named “MyIntegration” will be created under your current working directory. The following files will be generated in this directory:
- **MyIntegration.py** - includes a template for the client class. **You must implement all of the class methods.** You may implement non-management operation commands as well, if needed.
- **MyIntegration.yml** - unless there are additional commands to implement in the integration, the only changes in the yml file should be: 
Declaration of specific configuration parameters and default values for [mapper](#mappers) names.
Specification of the test playbook.
- **MyIntegration_description.md** - if necessary, add an explanation about how to configure an integration instance in XSOAR.
- **MyIntegration_test.py** - make sure the unit-tests pass when the integration is ready.
- Additional files: **MyIntegration_image.png**, **README.md**, **Pipfile**, **Pipfile.lock**, **command_examples**.

## IAM Commands need to be supported

### **iam-create-user**

**Description**

Creates a user. If the user already exists, updates it. If the user exists but is disabled, it enables the user.

**Inputs**

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| user-profile | User Profile indicator details. | Required |
| allow-enable | When set to true, after the command executes, the status of the user in the 3rd-party integration will be active. | Optional |


**Example**

```
!iam-create-user user-profile=`{"email": "demistotest@paloaltonetworks.com", "givenname": "test", "surname": "test"}`
```

**Outputs**

```
{
 "IAM": {
   "Vendor": {
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
   },
   "UserProfile": {
       "email": "demistotest@paloaltonetworks.com",
       "givenname": "test",
       "surname": "test"
   }
 }
}
```

**How to implement**

Complete the **client.create_user()** method, which should retrieve an [IAMUserAppData](#iamuserappdata) object that contains the data of the user in the application.
Implementation example: [HelloIAMWorld](https://github.com/demisto/content/blob/master/Packs/HelloIAMWorld/Integrations/HelloIAMWorld/HelloIAMWorld.py#L55)


### **iam-get-user**

**Description**

Returns information about a user.

**Input**

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| user-profile | User Profile indicator details. | Required |

**Example**

```
!iam-get-user user-profile=`{"email": "demistotest@paloaltonetworks.com"}`
```

**Outputs**

```
{
 "IAM": {
   "Vendor": {
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
   },
   "UserProfile": {
       "email": "demistotest@paloaltonetworks.com"
   }
 }
}
```

**How to implement**

Complete the **client.get_user()** method, which should retrieve an [IAMUserAppData](#iamuserappdata) object that contains the data of the user in the application.
* [HelloIAMWorld Implementation example](https://github.com/demisto/content/blob/master/Packs/HelloIAMWorld/Integrations/HelloIAMWorld/HelloIAMWorld.py#L26)


### **iam-update-user**

**Description**

Updates a user.
* If the user exists but is disabled, enables the user.
* If *create_if_not_exists* parameter is marked and the user does not exist in the application, creates the user.

**Inputs**

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| user-profile | User Profile indicator details. | Required |
| allow-enable | When set to true, after the command executes, the status of the user in the 3rd-party integration will be active. | Optional |

**Example**

```
!iam-update-user user-profile=`{"email": "demistotest@paloaltonetworks.com", "givenname": "John"}` allow-enable=true
```

**Outputs**

```
{
 "IAM": {
   "Vendor": {
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
   },
   "UserProfile": {
       "email": "demistotest@paloaltonetworks.com",
       "givenname": “John"
   }
 }
}
```

**How to implement**

Complete the **client.update_user()** and **client.enable_user()** methods, each should retrieve an [IAMUserAppData](#iamuserappdata) object that contains the data of the user in the application.
* [HelloIAMWorld Implementation Example - Update](https://github.com/demisto/content/blob/master/Packs/HelloIAMWorld/Integrations/HelloIAMWorld/HelloIAMWorld.py#L77)
* [HelloIAMWorld Implementation Example - Enable](https://github.com/demisto/content/blob/master/Packs/HelloIAMWorld/Integrations/HelloIAMWorld/HelloIAMWorld.py#L103)


### **iam-disable-user**

**Description**

Disables a user. If the API does not support disabling, deletes the user.

**Input**

| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| user-profile | User Profile indicator details. | Required |

**Example**

```
!iam-disable-user user-profile=`{"email": "demistotest@paloaltonetworks.com"}`
```

**Outputs**

```
{
 "IAM": {
   "Vendor": {
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
   },
   "UserProfile": {
       "email": "demistotest@paloaltonetworks.com"
   }
 }
}
```

**How to implement**

Complete the **client.disable_user()** method, which should retrieve an [IAMUserAppData](#iamuserappdata) object that contains the data of the user in the application.
* [HelloIAMWorld Implementation Example](https://github.com/demisto/content/blob/master/Packs/HelloIAMWorld/Integrations/HelloIAMWorld/HelloIAMWorld.py#L119)


### **get-mapping-fields**

**Description**

Retrieves a User Profile schema which holds all of the user fields within the application. Used for outgoing-mapping through the Get Schema option. 

**How to implement**

Complete the **client.get_app_fields()** method, which should retrieve a dictionary of fields and their descriptions.
* [HelloIAMWorld Implementation Example](https://github.com/demisto/content/blob/master/Packs/HelloIAMWorld/Integrations/HelloIAMWorld/HelloIAMWorld.py#L135)


### Additional Methods to Implement

1. **test_module()**: Validate the instance parameters and complete the instance testing by calling a test API endpoint from **client.test()**.
2. **handle_exception()**: Every API has its own error handling. For example, when a user does not exist, we can get an empty 200 response or 404 error response. Cortex XSOAR requires that the management operation commands not fail. Therefore, you must handle such cases by identifying them and setting the results according to the content of ***ERROR_CODES_TO_SKIP*** and the given [IAMActions](#iamactions) object.
3. **get_error_details()**: A helper function for the **handle_exception()** method, that parses the error information from the response.


## Mappers

Every management operation command receives a ***user-profile*** argument, which is mapped into different API standards for every integration. To properly map between the user data and the data from the integration, we sometimes need to define dedicated [Mappers](../incidents/incident-classification-mapping#map-event-attributes-to-fields). More specifically, we need an incoming mapper for the **iam-get-user** command, and an outgoing mapper for the **iam-create-user**, **iam-update-user** and **iam-disable-user** commands.

The mapper names should be the default values for "mapper-in" and "mapper-out" parameters of the integration instance. 

For integrations that support the [SCIM](http://www.simplecloud.info/) protocol, you can use the built in SCIM mappers in the IAM-SCIM pack.  

## IAMApiModule Script Classes

Every IAM integration imports the [IAMApiModule](https://github.com/demisto/content/blob/master/Packs/ApiModules/Scripts/IAMApiModule/IAMApiModule.py) script. This script contains classes which are used in the integration for several purposes.

### IAMCommand

The [IAMCommand](https://github.com/demisto/content/blob/master/Packs/ApiModules/Scripts/IAMApiModule/IAMApiModule.py#L273) class implements most of the logic of the management operation commands. For example, when calling the **iam-update-user** command of an integration, the integration will call the **update_user()** method of this class. The integration **client** object and the command **arguments** will be passed to this method as arguments.

### IAMUserProfile

An object of the [IAMUserProfile](https://github.com/demisto/content/blob/master/Packs/ApiModules/Scripts/IAMApiModule/IAMApiModule.py#L113) class holds the given user profile data, and facilitates the data mapping from the XSOAR format to the vendor format and vice-versa using the **map_object()** and **update_with_app_data()** class methods.

### IAMUserAppData

The [IAMUserAppData](https://github.com/demisto/content/blob/master/Packs/ApiModules/Scripts/IAMApiModule/IAMApiModule.py#L248) class holds user attributes retrieved from the 3rd-party. The return type of the client class methods.

### IAMErrors

The [IAMErrors](https://github.com/demisto/content/blob/master/Packs/ApiModules/Scripts/IAMApiModule/IAMApiModule.py#L6) class is an enum class for API errors which are not handled by the vendor. For example, some vendors might return an empty response with status code 200 for a GET user API call of a user that does not exist. In this case, we can identify in the code that is not a valid response and pass a custom error enum.

### IAMActions

The [IAMActions](https://github.com/demisto/content/blob/master/Packs/ApiModules/Scripts/IAMApiModule/IAMApiModule.py#L16) class is an enum class for all the IAM actions - get, update, create and disable.

### IAMVendorActionResult

This class is used in [IAMUserProfile](#iamuserprofile) class to create the outputs from the taken action.


## Integrations for reference
* [HelloIAMWorld](https://github.com/demisto/content/tree/master/Packs/HelloIAMWorld/Integrations/HelloIAMWorld)

* [Slack IAM](https://github.com/demisto/content/tree/master/Packs/Slack/Integrations/Slack_IAM)

* [Okta IAM](https://github.com/demisto/content/tree/master/Packs/Okta/Integrations/Okta_IAM)















