---
id: custom-indicator
title: Custom Indicator
description: Create a customized indicator
---

## Overview
**CustomIndicator** is a new type of an indicator, which allows you to create a customized Indicators.

## CustomIndicator Class

* It is part of the CommonServerPython.py
* functions:
    * __init__(self, indicator_type, value, dbot_score, params, prefix_str):
        * Description: Creates the CustomIndicator object.
        * Argumets:
          
            | argument | Description| type|
            | --- | --- | ---|
            | indicator_type | type name of the indicator.| Str
            | value | Value of the indicator. | Any
            | DBotScore | If custom indicator has a score then create and set a DBotScore object.| DBotScore
            | params |  A dictionary containing all the param names and their values.| Dict(Str,Any)
            | prefix_str | Will be used as the context path prefix.| Str
        * Returns: None
    
    * to_context(self):
        * Description: Returns the context of a customized Indicator.
        * Arguments: None
        * Returns: Dict(str,Any)
    
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
    params = {
        'param1': 'value1',
        'param2': 'value2',
    }
3. Create a CustomIndicator object with the parameters dictionary and the DBotScore object.
   ```python
    custom_indicator = Common.CustomIndicator(
        indicator_type='MyCustomIndicator',
        dbot_score=dbot_score,
        value=indicator_value,
        params=params,
        prefix_str='custom',
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
5.
    