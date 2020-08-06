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
2. Run the `demisto-sdk openapi-codegen` command. Using the arguments and examples below. 
3. Follow the instructions to generate the Cortex XSOAR integration files.
4. Use `demisto-sdk unify` to create a unified integration YAML file from the integration files.
5. Use `demisto-sdk upload` to upload the generated integration to Cortex XSOAR.
6. Set up an instance and run the integration commands.

### Command instructions

#### Arguments

* **'-h', '--help'**

    Show command help.

* **'-i', '--input_file'**

    The swagger file to load in JSON format.

* **'-cf', '--config_file'**

    The integration configuration file. It is created in the first run of the command.

* **'-n', '--base_name'**

    The base filename to use for the generated files.

* **'-o', '--output_dir'**

    Directory to store the output in (default is current working directory).

* **'-pr', '--command_prefix'**

    Add a prefix to each command in the code.

* **'-c', '--context_path'**

    Context output path.

* **'-u', '--unique_keys'**

    Comma separated unique keys to use in context paths (case sensitive).

* **'-r', '--root_objects'**

    Comma separated JSON root objects to use in command outputs (case sensitive).

* **'-v', '--verbose'**

    Be verbose with the log output.

* **'-f', '--fix_code'**

    Fix the python code using autopep8.

* **'-a', '--use_default'**

    Use the automatically generated integration configuration (Skip the second run).

#### Examples
```
demisto-sdk openapi-codegen -i pet_swagger.json -n PetStore -o PetStoreIntegration -u "id" -r "Pet"
```

This will create an integration configuration for the PetStore swagger file in the `PetStoreIntegration` directory.
It will use `id` to identify unique properties in outputs and `Pet` to identify root objects in the outputs.
That configuration can be modified and will be used in a second run of the command.
<br/>
```
demisto-sdk openapi-codegen -i pet_swagger.json -n PetStore -o PetStoreIntegration -u "id" -r "Pet" -cf "PetStoreIntegration/PetStore.json"
```

This will create the Cortex XSOAR integration for the PetStore swagger file using the configuration file located in PetStoreIntegration/PetStore.json.
<br/>
 ```
demisto-sdk openapi-codegen -i pet_swagger.json -n PetStore -o PetStoreIntegration -u "id" -r "Pet" -a
```

This will create the Cortex XSOAR integration for the PetStore swagger file using the generated configuration file, thus skipping the second run of the command.


### Video Tutorial
<video controls>
    <source src="https://github.com/demisto/content-assets/raw/master/Assets/OpenAPICodegen/openapicodegen.mp4"
            type="video/mp4"/>
    Sorry, your browser doesn't support embedded videos. You can download the video at: https://github.com/demisto/content-assets/raw/master/Assets/OpenAPICodegen/openapicodegen.mp4 
</video>
