---
id: yaml-file
title: Integrations and Scripts Metadata YAML File
sidebar_label: Metadata YAML File
---

All the metadata of your integration is included in the YAML file: think of it as key, value set for your integration. When pushing content for public release, your YAML file must follow certain structural requirements in order to work properly. In this section we will review the various parts of the Cortex XSOAR YAML file.

**Note**: Automation Scripts also have a metadata YML file that follows a very similar structure.

## Common Fields
The Common Fields section contains information that the Cortex XSOAR server will use to identify your integration. See the example below:

```yml
commonfields:
  id: New Integration
  version: -1
```

This section accepts the following information:

| Name | Description |
| --- | --- |
| **id** | A *unique* identifier for your integration |
| **version** | Setting the value to -1 will lock the integration from being modified |

## Basic Information

Observe the following:

```yml
name: MaxMind GeoIP2
display: MaxMind GeoIP2
category: Data Enrichment & Threat Intelligence
image: data:image/png;base64,**Base64 of Image Here**
description: Enriches IP addresses
detaileddescription: 'The MaxMind GeoIP2 integration allows you to query the MaxMind
  API service and retrieve a JSON of all details. '
```

**Note**: You can find all categories options here: https://xsoar.pan.dev/docs/documentation/pack-docs#pack-keywords-tags-use-cases--categories

The following is an explanation of these fields:

| Name | Description |
| --- | --- |
| **name** | The name of your integration. This *may* be different than the display name |
| **display** | This is the display name for your integration |
| **category** | The applicable category |
| **image** | The Icon that will be used for the integration. Please note that this image must be in Base64. Ask the design team to provide you with a compatible image  |
| **description** | A brief description of what your integration will do |
| **detaileddescription** | This description should go into more detail about how your integration works as well as requirements for the integration to work |


## Configuration
In this section, we specify the configuration requirements that are necessary for the integration to operate.

```yml
configuration:
- display: API Key
  name: apikey
  defaultvalue: ""
  type: 0
  required: true
- display: Use system proxy
  name: proxy
  defaultvalue: ""
  type: 8
  required: false
```

An explanation of these fields is as follows:

| Name | Description |
| --- | --- |
| **display** | The display name for the field. |
| **name** | The parameter which is used within the integration |
| **defaultvalue** | If there is a default for the field, it should be located here |
| **type** | An Integer that represents the type for the field. |
| | Type 0 - Short text field |
| | Type 4 - Encrypted text field |
| | Type 8 - Boolean checkbox |
| | Type 9 - Authentication text - allows switching to credentials |
| | Type 12 - Long text block |
| | Type 13 - special use - automatically added - Incident type single select dropdown |
| | Type 15 - Single select dropdown |
| | Type 16 - Multiple select dropdown |
| **required** | Boolean value to indicate that the parameter is required |
| **additionalinfo** | Additional info about the field, will appear under a question mark in the configuration panel |
| **fromlicense** | Specifies to take the credentials from the xsoar license. (relevant to type 9) |

Integration parameters may be hidden from the XSOAR UI, using the optional `hidden` field.

- To hide the parameter in all marketplaces (XSOAR, XSOAR_SAAS, XSOAR_ON_PREM, XSIAM), use a boolean `true`.
- To hide the parameter in specific content marketplace versions, provide list of marketplace version names (e.g. `xsoar` (XSOAR 6 and XSOAR 8), `xsoar_on_prem` (XSOAR 6), `xsoar_saas` (XSOAR 8), `marketplacev2` (XSIAM) or `xpanse` (XPANSE))

## Script

This section is where your code will reside. Review the example below:

```yml
script:
  script: |
    import requests
    import collections

    def explain_yaml():
        if user.understands is False:
            re_read_documentation()

  type: python
  subtype: python3
  dockerimage: demisto/python3:3.7.5.3066
```
Type indicates the language your integration is written in. Cortex XSOAR currently supports Python and JavaScript. When using Python specifying `subtype` field is required (either: `python2` or `python3`). Additionally, when using Python `dockerimage` should be specified. If `dockerimage` is not specified a default Python 2 image will be used.

## Commands
The command section tells Cortex XSOAR what arguments are required for your command as well as what the outputs are.

```yml
  commands:
  - name: command-name
    arguments:
    - name: command-argument
      required: true
      default: false
      isArray: false
      secret: true
      description: This is a description for the argument
    outputs:
    - contextPath: Example.Sample.Name
      description: The name of the sample
      type: string
    - contextPath: Example.Sample.ID
      description: The ID for the sample
      type: string
    description: Sample description for the command-name function
  runonce: false
```
An explanation of these fields is as follows:
#### Command:
| Name | Description | Standard |
| --- | --- | ---|
| **name** | The name of the command. | `vendorname-command` |
| **description** | A description for the command. | |
| **runonce** | Boolean. Indicates if the command runs repeatedly. | |

#### Command arguments:
| Name | Description | Standard |
| --- | --- | ---|
| **name** | The name of the argument. | `argumnt_name` |
| **required** | Boolean. Is the argument required. |  |
| **default** | Boolean. If set to true, the user could pass a value for this argument without specifying the argument name. For example if the argument called `ip` is marked as default, running the following: `!ip 1.1.1.1` will be equivelent to running `!ip ip=1.1.1.1`. Note that only one argument per command can be set as the default. | |
| **isArray** | Boolean. Does the argument accepts a CSV list of input values. If this is set to true, the command will run once, instead for each input. |
| **secret** | Boolean. If set to true, the argument value will not be printed in war room when the command runs. |
| **execution** | Boolean. If set to true, the command will be marked as `Potentially harmful`. |
| **description** | A description of the argument. | |

#### Command outputs:
| Name | Description | Standard |
| --- | --- | ---|
| **contextPath** | The dot notation representation of the context. | `Product.Entity.EntityDetails` |
| **description** | Description of the context item. | |
| **type** | The type which the context item will be formatted. | Available options are: Unknown, String, Number, Date, Boolean. |

## Version and Tests
The last section of the YAML file provides Cortex XSOAR with information regarding what version is supported and tests. See the example below:

```yml
fromversion: 6.5.0
tests:
  - Sample Integration Test
```

From version indicates the server version that is supported with the integration. If the server version is below the fromversion, the integration will not display in the Settings area.

Tests instructs the Cortex XSOAR CircleCI tool which test to run to verify that the integration is working. 

If you want to run all of the tests you will need to add to the tests section ```Run all tests``` as the test you would like to run.


***

If you want to live a life of shame and disappoint your team, you can opt to not run any tests by adding ```No test - <reason>``` as a test you would like to run. You can attempt to earn back the respect of your team by writing a reason for skipping the test and we *may* consider it.


***

Please take into consideration that both the automatic and the manual mechanisms are working side by side and don't override each other, and don't worry it will not cause the same test to run more than once.


## Entry Types

| ID | Name | Details |
| --- | --- | --- |
| 1 | Note | A note is a text entry in the war room. |
| 2 | Download Agent | Internal use only |
| 3 | File | A file and it's metadata will be displayed |
| 4 | Error | Observed with a red background, this indicates that a command did not run successfully. |
| 5 | Pinned | Internal use only |
| 6 | User Management | Internal use only |
| 7 | Image | An image will be displayed in the war room. |
| 8 | Playground Error | An error has occurred in the playground |
| 9 | Entry Info File | Used in the `FileResult` function in ServerCommon. This is similar to the `file` entry type. |
| 10-14 | Reserved | This is for future entry types |
| 15 | Map | Posts a map location in the war room. **Please note**: This will require an API key from Google maps. |

