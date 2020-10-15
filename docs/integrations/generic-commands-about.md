---
id: generic-commands-about
title: Generic Commands
---


## About Generic Commands

Today the current XSOAR platform supports over 450+ integrations. 
Some commands can be generalized across similar integrations and allow combining data from various sources or running in parallel on more than one integration:

* reputation commands for example `!file` can gather reputation from multiple connected integrations to one indicator.
* IAM generic commands for example `create-user` creates a user on all connected integrations that implement it. 

These commands can be used both on all integrations or with `using` parameter on a specific instance of an integration.  



