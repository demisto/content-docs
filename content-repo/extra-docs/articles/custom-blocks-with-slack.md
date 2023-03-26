---
title: Creating Custom SlackAsk Blocks
description: Slack Blocks require some additional details to work properly with SlackAsk.
---

Please note that much of this tutorial can be done automatically for you by using the `SlackBlockBuilder`. If you wish to create your own scripts, then this article is relevant for you.

To use custom blocks in SlackV3, you will first need to define the block structure in JSON format. Slack's Block Kit Builder (https://app.slack.com/block-kit-builder/) can be used to design and generate the JSON structure.

Next, you will need to generate the entitlement which will be used to tie the reply back to the playbook. Please refer to the [entitlement article](https://xsoar.pan.dev/docs/integrations/entitlements) for more information.

Once you have the entitlement string, you will need to create the following:

```python
value = json.dumps({
        'entitlement': entitlement,
        'reply': reply
    })
```

This JSON string will need to be placed in a very specific part of _each_ element of your blocks as shown below:

```python
element = {
            'type': 'button',
            'text': {
                'type': 'plain_text',
                'emoji': True,
                'text': option['text']
            },
            'value': value <--- Here the above JSON string should reside
        }
```

Once the blocks have the correct entitlements, you may prepare the arguments to send the blocks as follows:

```python
args['blocks'] = json.dumps({
            'blocks': blocks, <--- Your custom blocks should be here
            'entitlement': entitlement_string, <--- The entitlement you generated should be here as well
            'reply': reply,
            'expiry': expiry,
            'default_response': default_response
        })
```

Finally, you can send your blocks using the `send-notification` command along with the arguments you have formatted above.