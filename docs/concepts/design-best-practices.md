---
id: design-best-practices
title: Design Best Practices
---

In this section we captured some of the Design Best practices that you should be aware of while building an integration. If you have any doubts or questions, please reach out to us over Slack.

**Design Best Practices:**

- Make sure your integration is categorized correctly. Use cases can be helpful for the categorization as well as looking for similar integrations to the one you are working on.
- Is this a SaaS product, on-prem or both? Make sure to support both if needed. This is relevant for authentication methods and possibly different API (parameters/outputs).
- Logo must be under 10kb. Make sure to use the company logo (and not the product’s).
- When mapping score to DBot score stay as close as possible to the your scoring thresholds and categorization (these are usually documented/can be understood from the UI). DBot score reputation includes the following scores: 0 – unknown, 1 – good, 2 – suspicious, 3 – bad. Give users a threshold argument in order to let customers override and set another scoring logic.
- Add score thresholds and DBot score mapping to the integration documentation.
- Add generic reputation commands such as “!url,ip,file,domain”.
- Global Context outputs – Don’t forget global context outputs for DBot scoring and global indicators.
- When adding or removing indicators, add a message to the indicator timeline. The message should be something like the following: ***The indicator was added to XXX***. See [Demisto Results](../integrations/code-conventions#deprecated---demistoresults).
- Be sure to check the top [Use Cases](use-cases). If those are supported via api make sure to include them in the integration.
- Time arguments – When the command supports filtering results by time, use start + end time parameters (if supported by UI), and a timeframe parameter, that accepts inputs such as “4 days ago”, “5 minutes ago”, etc.
- The data you return should make sense to an analyst (convert Epoch timestamps, decrypt data if needed. If you return IDs, make sure to return the original asset name, category type, group name etc.)
- Make sure the parameters and command descriptions are descriptive enough
- Stay as true to your product as possible: keep the same names as used by your product, the UI is a good baseline for what the human readable should look like.
- Stick to the naming convention of the commands: ***PRODUCTNAME-OBJECTNAME-ACTION***. In this structure, it is easier to find the right object in the UI.
- Context limitation – If the result can include a lot of data, limit the context size.
- Polling playbook & check status command – If the command can take more than a few seconds (vulnerability scan, complex search, detonation, etc) make sure to add a polling playbook. If implemented, do remember to include a “status” command as well.
- Backwards compatibility – Don’t break it. Few suggested workarounds: keep the old context, add new paths as needed and update the outputs accordingly, if a command needs major changes, deprecate it and add a new one
