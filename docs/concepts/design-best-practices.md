---
id: design-best-practices
title: Design Best Practices
---

In this section we captured some of the Design Best practices that you should be aware of while building an integration.
Please keep in mind to keep it simple - each command/api call at its time.
If you have any doubts or questions, please reach out to us over Slack.
 
**Design Best Practices:**
 
**Integration categories:** 
 
Make sure your integration is categorized correctly by choosing one of the following:

Import events as incidents
Threat Intel Feeds
Analytics & SIEM
Authentication
Data Enrichment & Threat Intelligence
Database
Endpoint
Forensics & Malware Analysis
Messaging
Utilities
Vulnerability Management

Use cases can be helpful for the categorization as well as looking for similar integrations to the one you are working on.




**Product platform:**

Important parameter to take into consideration in the design is the integrated product platform: SaaS product, on-prem or both? Make sure to support both if needed. This Can have a major impact on authentication methods and possibly different API (parameters/outputs).


**Data clarity:**

The data that returns to the analyst should be clear as possible (convert Epoch timestamps, decrypt data if needed. If you return IDs, make sure to return the original asset name, category type, group name etc.), additionally make sure the parameters and command descriptions are descriptive as possible.
Stay as true to your product as possible: keep the same names as used by your product, the UI is a good baseline for what the human readable should look like



**DBot score:**

When mapping score to DBot score, stay as close as possible to the integrated product scoring thresholds and categorization (these are usually documented or can be found in the UI  of the integrated product). DBot score reputation includes the following scores:
0 – unknown
1 – good
2 – suspicious
3 – bad
Give users a threshold argument in order to let customers override and set another scoring logic, Specify the score thresholds and DBot score mapping to the integration documentation.

Check the top [Use Cases](https://xsoar.pan.dev/docs/concepts/use-cases). If those are supported via api make sure to include them in the integration.
Make sure to set generic commands that will indicate the entity reputation such as “!url,ip,file,domain,hash”.
When adding or removing indicators, define a message to the indicator timeline. The message should be as the following: ***The indicator was added to XXX***. See [Demisto Results](https://xsoar.pan.dev/docs/integrations/code-conventions#deprecated---demistoresults).



**Global Context:**

Global Context outputs are important, when an analyst will execute commands/playbooks it will give him the option to receive information from multiple integrated products, additionally don’t forget [global context outputs](https://xsoar.pan.dev/docs/integrations/code-conventions#deprecated---demistoresults) for DBot scoring and global indicators.



.

**Commands :**

Use the following naming convention of the commands: ***PRODUCTNAME-OBJECTNAME-ACTION***. In this structure, this will make it easier for the analyst to find the right object in the UI.

Polling playbook & check status command – If the command can take more than a few seconds (vulnerability scan, complex query, file detonation in sandbox, etc) make sure to add a [polling playbook](https://xsoar.pan.dev/docs/playbooks/generic-polling). If implemented, do remember to include a “status” command as well.

Time arguments – When the command supports filtering results by time, use start and end time parameters (if supported by UI), and a timeframe parameter, that accepts inputs such as “4 days ago”, “5 minutes ago”, etc.



**Backwards compatibility:**

Don’t break it, in XOAR components such as playbooks rely on previous inputs,few workarounds suggestions: keep the old context, add new paths as needed and update the outputs accordingly, if a command needs major changes, deprecate it and create a new one.


**limitations:**

Logo must be under 10kb. Make sure to use the company logo ( not the product’s).
Context limitation – If the result contains more than 50 entries, limit the context size.


