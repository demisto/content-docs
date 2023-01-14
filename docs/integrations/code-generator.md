---
id: code-generator
title: Integration Code Generator
description: Generate an XSOAR Integration from a json config file
---

Use the `demisto-sdk generate-integration` command to generate an XSOAR integration from an integration config json file. The json config file can be generated from a postman collection via the `demisto sdk postman-codegen` [command](./postman-codegen).

## Options
*  **-h, --help**
*  **-i, --input**  
   Config json file. postman-codegen command generates the config file.
*  **-o, --output**  
   (Optional) The output directory. Default is the current directory.

## Example
```
demisto-sdk generate-integration -i config-VirusTotal.json -o /output/path
```
The above command generates `integration-VirusTotal.yml` file under `/output/path` directory.

## Integration config json file
**Example File:**  [URLScan generated config file](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/postman_codegen/resources/config-urlscanio.json)

|Field Name|Field Type|Description|Examples|Is Required|
|----------|----------|-----------|--------|-----------|
|name|string|The integration name. The command sets the integration id the same as the name. Spaces and special characters will be removed.  | VirusTotal | Required |
| display_name | string | The display name for the integration. This may be different than the name. | Virus Total | Required |
| description | string | A brief description of what the integration will do. | Analyzes suspicious hashes, URLs, domains, and IP addresses. | Required |
| category | string | The field/subject the integration relates to, in high level. | Data Enrichment & Threat Intelligence | Required |
|command_prefix|string|The prefix to all the commands. The prefix should be:<br />- lower cased<br />- separated with dashes|vt,virustotal|Required|
| docker_image | string | Docker image full name with version. | demisto/python3:3.9.2.17957 | Required | 
|url|string|The default value for integration `Server URL` parameter.|https://www.virustotal.com|Optional|
|base_url_path|string|Suffix for the integration `Server URL` parameter. If the API url contains constant suffix like `/vtapi/v2`|vtapi/v2|Optional|
|auth|object|Determines which authentication method is used to connect to the method. See the [Authentication section](#authentication) for more detail.||Optional|
|context_path|string|Prefix for every command outputs. Must not contain spaces nor special characters. |VirusTotal -> VirusTotal.IP.source|Required|
| code_type | string | The code the integration is written in. | python | Required |
| code_subtype | string | The subtype of the code. | python3 | Required |
| is_fetch | Boolean | Whether the integration should run periodically to ingest events and create incidents. | false | Optional |
|fix_code|bool|If true, run autopep8 to format the Python code. The default and the recommended value is `true`|true|Optional|



## Authentication
This section defines the way the integration authenticates with 3rd party product/service.
Supported authentication types:

**API Key as part of the header example**

Generates `api_key` integration parameter.
```
"auth": {
     "type": "apikey",
     "apikey": [
         {
             "key": "in",
             "value": "header",
             "type": "string"
         },
         {
             "key": "key",
             "value": "Authorization",
             "type": "string"
         }
     ]
 }
```
---
**API Key as part of the query example**

Generates `api_key` integration parameter.
```
"auth": {
     "type": "apikey",
     "apikey": [
         {
             "key": "in",
             "value": "query",
             "type": "string"
         },
         {
             "key": "key",
             "value": "apikey",
             "type": "string"
         }
     ]
 }
```
---
**Basic authentication example**

The command generates `credentials` parameter of type `Authentication`.
```
"auth": {
     "type": "basic"
 }
```

**API Token bearer**

The command generates `api_key` integration parameter. The paramater will be passed in `"Authorization": "Bearer TOKEN_HERE"` as part of the request header.
```
"auth": {
     "type": "bearer"
}
```


## Parameters
Supported parameter types:
- STRING
- NUMBER
- ENCRYPTED
- BOOLEAN
- AUTH
- DOWNLOAD_LINK
- TEXT_AREA
- INCIDENT_TYPE
- TEXT_AREA_ENCRYPTED
- SINGLE_SELECT
- MULTI_SELECT

```
"params": [
     {
         "name": "url",
         "display": "Server URL",
         "defaultvalue": "https://www.virustotal.com",
         "type_": "STRING",
         "required": true
     },
     {
         "name": "proxy",
         "display": "Use system proxy settings",
         "defaultvalue": "",
         "type_": "BOOLEAN",
         "required": false
     },
     {
         "name": "apikey",
         "display": "API Key",
         "defaultvalue": "",
         "type_": "ENCRYPTED",
         "required": true
     }
 ]
```

## Commands
|Field Name|Field Type|Description|Examples|Is Required|
|----------|----------|-----------|--------|-----------|
|commands|list|List of integration commands.||Required|
|commands.name|string|Command name. Should be lower case and should not contain spaces nor special characters.|scan-file|Required|
|commands.context_path|string|Context path object for this specific command. For example if the command returns Report object, the set this field to `Report`.|Report, IP, Event|Required|
|commands.root_object|string|In case you don't want to return the whole response as it is, and just a specific field of it. Note: only single nested layer is supported - for example if response is `{layer1:{layer2:{...}}}` it is possible to access `layer1` but not `layer2`. |result, scan|Optional|
|commands.unique_key|string|Unique/Identifier key field from the response/outputs.|id, sha1, name|Optional|
|commands.headers|list|Request headers.|`[{"Content-Type": "application/json"},{"Accept": "application/json"}]`|Optional|
|commands.body_format|object|Defines the structure and the format of the request body. In case the request contains body, this field must be passed. Keys that wrapped with `{}` will be replaced with command args.|```{"user": {"name": "{user}", "id": "{id}", "status": "create"}```<br />`"{name}"` and `"{id}"` will be replaced with `name` and `id` command input args.|Optional|
|commands.upload_file|object|Not supported yet.| |Optional|
|commands.returns_file|object|Not supported yet.| |Optional|
|commands.returns_entry_file|object|Not supported yet.| |Optional|

**Example**
```
 "commands": [
     {
         "name": "url-report",
         "url_path": "vtapi/v2/url/report",
         "http_method": "GET",
         "description": "URL Report description",
         "context_path": "",
         "root_object": "",
         "headers": null,
         "unique_key": "",
         "body_format": null,
         "upload_file": false,
         "returns_file": false,
         "returns_entry_file": false,
         "arguments": [
             {
                 "name": "resource",
                 "description": "",
                 "required": false,
                 "is_array": false,
                 "default_value": "",
                 "predefined_values": [],
                 "ref": null,
                 "type_": null,
                 "in_": "query",
                 "in_object": null
             }
         ],
         "outputs": [
             {
                 "name": "scan_id",
                 "description": "",
                 "type_": "String"
             },
             {
                 "name": "response_code",
                 "description": "",
                 "type_": "Number"
             }
         ]
     }
 ]
```

## Arguments
|Field Name|Field Type|Description|Examples|Is Required|
|----------|----------|-----------|--------|-----------|
|commands.arguments|list|List of command arguments. These arguments will be passed as part of the request.| |Optional|
|commands.arguments.in_|string|Possible values are `query` `url` `body`.<br />If set to `query`, the argument will be passed in the request url query in the following format: `?resource={resource}`.<br />If set to `body`, the argument will be passed in the request body.<br />If set to `url`, the argument will be passed as part of the url in the following format: `/vtapi/v2/url/{resource}`.|query, url, body|Required|
|commands.arguments.description|string|Argument description.|Machine ID to be used to stop the isolation. e.g. 0a3250e0693a109f1affc9217be9459028aa8426|Optional|
|commands.arguments.required|boolean|Set to `true` if the argument is mandatory.|false|Optional|
|commands.arguments.is_array|boolean|Set to `true` if the argument is of type array.|`xdr-get-incidents` receives argument of type array `incident_id_list`. When list of ids passed, the command returns all the incidents with the corresponding ids.|Optional|
|commands.arguments.default_value|string|Argument initial value.|`size`/`limit` arguments usually will have default values like `50`|Optional|
|commands.arguments.predefined_values|list|List of strings. If the argument has predefined list of possible values, then set this field.|['low','medium','high']|Optional|
|commands.arguments.type_|string|Argument casting and conversion.|`int` -> `size = int(size)`, `array` -> `scan_ids = argToList(scan_ids)`|Optional|
|commands.arguments.in_object|list|Not supported yet.| |Optional|

**Example**
```
"arguments": [
    {
        "name": "size",
        "description": "Number of incidents to return.",
        "required": false,
        "is_array": false,
        "default_value": "10",
        "predefined_values": [],
        "ref": null,
        "type_": null,
        "in_": "query",
        "in_object": null
    }
]
```

## Outputs
|Field Name|Field Type|Description|Examples|Is Required|
|----------|----------|-----------|--------|-----------|
|commands.outputs|list|List of command outputs.| |Optional|
|commands.outputs.name|string|JSON path to this field/output|`scan_id`, `alerts.severity`|Required|
|commands.outputs.description|string|Something that will describe what this field is|Severity of the alert, possible values are `low` `medium` and `high`|Optional|
|commands.outputs.type_|string|Field/output type.|`String`, `Number`, `Date`postman_codegen_test.py:107, `Unknown`|Optional|

**Example**
```
 "outputs": [
    {
        "name": "scan_id",
        "description": "",
        "type_": "String"
    },
    {
        "name": "response_code",
        "description": "",
        "type_": "Number"
    }
]
```

## Request Body
Defines the structure and the format of the request body. `body_format` must contain a value in case the request contains a body. Keys that wrapped with `{}` will be replaced with command args.
Request example: 
- `POST` request with body.
- User creates the command with two arguments, `name` and `id`.
- In the `body_format` they are passed as `"{name}"` and `{"id"}`.

Request body:
```
{
   "profile": {
      "name": "some name",
      "id": "some id",
      "status": "created"
   }
}
```

In config file:
```
"body_format": {
   "profile": {
      "name": "{name}",
      "id": "{id}",
      "status": "created"
   }
}
```

Will generate code like:
```python
def create_profile(self, name, id):
    ...

    data = {
       "profile": {
          "name": name,
          "id": id,
          "status": "created"
       }
    }

    response = self._http_request('POST', 'api/v1/profile', params=params, json_data=data, headers=headers)

    return response
```


## Example files
* [URLScan Postman Collection v2.1](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/postman_codegen/resources/urlscan.io.postman_collection.json)
* [URLScan generated config file](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/postman_codegen/resources/config-urlscanio.json)
* [URLScan generated integration yml](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/postman_codegen/resources/integration-urlscanio.yml)
