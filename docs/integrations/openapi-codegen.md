---
id: openapi-codegen
title: OpenAPI (Swagger) Code-Gen
---

## Generating Cortex XSOAR integrations with the OpenAPI(Swagger) code-gen tool
It is possible to generate a Cortex XSOAR integration package (YAML and Python files) with a dedicated tool in the Cortex XSOAR (demisto) SDK.
The integration will be usable right away after generation.

### Requirements
* OpenAPI (Swagger) specification file (v2.0 is recommended) in JSON format.
* Cortex XSOAR (demisto) SDK 

### Steps
1. Install the Cortex XSOAR SDK: `pip3 install demisto-sdk`.
2. Run the `demisto-sdk openapi-codegen` command. See this [document](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/openapi_codegen/README.md) for command examples. 
3. Follow the instructions to generate the Cortex XSOAR integration files.
4. Use `demisto-sdk unify` to create a unified integration YAML file from the integration files.
5. Use `demisto-sdk upload` to upload the generated integration to Cortex XSOAR.
6. Set up an instance and run the integration commands.

### Video Tutorial
<video controls>
    <source src="https://github.com/demisto/content-assets/raw/master/Assets/OpenAPICodegen/openapicodegen.mp4"
            type="video/mp4"/>
    Sorry, your browser doesn't support embedded videos. You can download the video at: https://github.com/demisto/content-assets/raw/master/Assets/OpenAPICodegen/openapicodegen.mp4 
</video>
