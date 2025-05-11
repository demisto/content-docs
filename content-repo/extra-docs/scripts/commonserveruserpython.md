---
id: common-server-user-python
title: CommonServerUserPython 
---

Common user-defined code that is merged into each script and integrated during execution. You can use this script to define functions used by scripts and integrations. For example, you can add a common error function for logging that wraps `demisto.error` and includes extra environment information. Then you can call this function in custom integrations and scripts.  

**Note:** The code is not merged into system integrations. It only merges into scripts (custom/system) and custom integrations.  

Since this code will get merged into system scripts, **it is important that the syntax be compatible with both Python 2 and Python 3.**

**Note:** From October 1, 2025, Python 2 will no longer be supported.

To disable merging the code into system scripts, set the `content.oob.script.use_common_user` advanced Server parameter to `false`.
## Script Data
---

| **Name** | **Description** |
| --- | --- |
| Script Type | python |
| Tags | infra, server |


## Inputs
---
There are no inputs for this script.

## Outputs
---
There are no outputs for this script.
