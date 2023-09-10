---
id: custom-indicator
title: Custom Indicator
description: Create a customized indicator
---

## Overview
**CustomIndicator** is a new helper class which can be used to create a customized indicator.
## CustomIndicator Class

* The CustomIndicator class can get any custom name for the indicator.
* Unlike other indicators, the CustomIndicator can have any parameters. It can be passed by the *data* argument, which is a dictionary where the key is the parameter name and the value is the parameter's value.
* The CustomIndicator can have a custom context data prefix, which is passed by the *prefix_str* argument.
  
* **Functions**:
    
    *       init(self, indicator_type, value, dbot_score, params, prefix_str):
        * Description: Creates the CustomIndicator object.
        * Arguments:
          
            | argument | Description| type|
            | --- | --- | ---|
            | indicator_type | The type name of the indicator.| String
            | value | Value of the indicator. | Any
            | dbot_score | If the custom indicator has a score,  create and set a DBotScore object.| DBotScore
            | data | A dictionary containing all the parameter names and their values.| Dict(String,Any)
            | context_prefix | Used as the context path prefix.| String
        * Returns: None
    
    *       to_context(self):
        * Description: Returns the context of a customized indicator.
        * Arguments: None
        * Returns: Dict(String,Any)
    
## How To Use
1. Create a DBotScore object.
   ```python
    score = Common.DBotScore.GOOD
    indicator_value = 'custom_value'
    dbot_score = Common.DBotScore(
        indicator=indicator_value,
        indicator_type=DBotScoreType.CUSTOM,
        integration_name='DummyIntegration',
        score=score
    )
2. Create a dictionary containing the parameters needed for the customized indicator.
   ```python    
    data = {
        'param1': 'value1',
        'param2': 'value2',
    }
3. Create a CustomIndicator object with the parameters dictionary and the DBotScore object.
   ```python
    custom_indicator = Common.CustomIndicator(
        indicator_type='MyCustomIndicator',
        dbot_score=dbot_score,
        value=indicator_value,
        data=data,
        context_prefix='custom',
    )
4. Return the result of the command
   ```python
    return CommandResults(
        readable_output='Custom Indicator result',
        outputs=result,
        outputs_prefix='Demo.CUSTOM',
        outputs_key_field='test_key_field',
        indicator=custom_indicator
    )

5. Follow the guides below to add your new indicator type to your XSOAR instance:
   
    a.  [Create an indicator type](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Administrator-Guide/Create-an-Indicator-Type).
    
    b. [Create and map indicator fields](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Administrator-Guide/Create-a-Custom-Indicator-Field).
    
    c. [Customize the layout for your indicator](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Administrator-Guide/Customize-an-Indicator-Type-Layout).
    
    d. Create a regex in your indicator type, so the indicator will be enriched.
