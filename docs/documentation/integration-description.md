---
id: integration-description
title: Integration Description File
---


## General
The integration description file is designed to provide the supported use cases of the integration, as well as to help XSOAR users to easily configure an instance of the chosen integration.  
* Give as much information as you think the user of this integration needs to succeed. Permission levels, credentials, keys, etc.  
* If there are permissions required on the integration level, list them in the description. 
* If commands have separate permissions, mention that fact in the description, but document the required permission on the command level.

**Common cases are:**

- How to get credentials
- How to get API Key/Secret
- How to get Applications ID


## Path
The description file should be placed along with all of the integration's files. 

For example, if the Pack name is `HelloWorld` and the integration name is also `HelloWorld`, the description file path is:
```
~/.../content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld_description.md
```


## Data
The description file should contain details on how to configure an instance of the integration, together with the relevant details needed from the product that are important to perform an easy configuration.
The file's content can include troubleshooting tips and advanced details for different configuration cases.

:::note 
This should not be confused with the integration README file, documented [here](../documentation/readme_file).
:::

## Images
Images can be added to your documentation files. For information, see  [Images in Documentation Files](https://xsoar.pan.dev/docs/images_in_documentation_files).


## Example
This is the contents of the `HelloWorld_description.md` file:
```
## Hello World
- This section explains how to configure the instance of HelloWorld in Cortex XSOAR.
- You can use the following API Key: `43ea9b2d-4998-43a6-ae91-aba62a26868c`
```

### Cortex XSOAR versions up to 6.0


![](/doc_imgs/integrations/description_question_mark.png)

The content of the description file will be displayed:

![](/doc_imgs/integrations/description.md_example.png)

### Cortex XSOAR versions 6.1 and above

Starting from version 6.1, the content of the description file is shown on the side of the configuration data:

![](/doc_imgs/integrations/integration-config-panel-61.png)
