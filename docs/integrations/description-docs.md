---
id: description-docs
title: Integration Description File
---

The integration description file is designated to help the XSOAR users to easily configure an instance of the chosen integration.

## Path
The description file should be placed along with all of the integraion's files. 

For example, if the Pack name is `HelloWorld` and the integration name is also `HelloWorld`, the description file path is:
```
~/.../content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld_description.md
```


## Data
The description file should contain details on how to configure an instance of the integration, together with the relevant details needed from the product that are important to perform an easy configuration.
The file's content can include troubleshooting tips and advanced details for different configuration cases.

:::note 
This should not be confused with integration README.md which is the integration documentation document.
:::
