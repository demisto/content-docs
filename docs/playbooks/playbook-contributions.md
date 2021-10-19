---
id: playbook-contributions
title: Playbook Contribution Guide  
---
## Introduction  
This guide is intended to guide you through the process of contributing playbooks to our content, after they were created through the user interface.   
  
## Guidelines
* For general guidelines on **how to create playbooks**, visit our [Creating Playbooks](../playbooks/playbooks) article.
* Playbooks can be be divided into 2 categories depending on their usage. Technically, they are the same, but usage-wise, there are some differences. "Parent" playbooks are playbooks that run as the main playbook of an incident. The other type is "sub-playbooks", which are just playbooks that are being called by another playbook. 
Examples of parent playbooks can be `Phishing Investigation - Generic v2`, or `Endpoint Malware Investigation - Generic` because an incident starts with them. 
Examples of sub-playbooks are `IP Enrichment - Generic v2` or `Retrieve File From Endpoint - Generic`, because they are steps we take as part of the bigger investigation.
What one needs to consider is that since sub-playbooks are used as part of a bigger investigation, **they should have inputs and outputs.** Make sure that the data you want to get from a sub-playbook is defined in the outputs, so that it can be used outside of that playbook. Since sub-playbooks are building blocks that will preferably be usable in other playbooks and use-cases, you should define **generic inputs** for them as explained in our [context standards](../integrations/context-standards-about) article.
* Test playbooks can be used for testing integration commands individually (checking that they work and return the right inputs/outputs), but in the sense of playbooks - test playbooks should test a **certain scenario** of the investigation. For example, the test of `Phishing Investigation - Generic v2` creates an incident and attaches an email, and then makes sure that the URL contained in the email was found to be malicious (as it should be).

## Exporting playbooks  
- Your playbooks contain playbook and task descriptions by now and they should be able to run smoothly.  
- In order to contribute your newly created playbooks, they have to be exported via the "Export" button in playbook view mode:  
![image](https://user-images.githubusercontent.com/43602124/69058801-07d5c180-0a1d-11ea-8bd0-9dfd874b51b5.png)  
 - The playbook will be exported as a YML file. Use demisto-sdk command `demisto-sdk format -i <path to playbook yml>` against the YML file. The command will modify some fields in the file to normalize it with the rest of the playbooks in our content, and will output a file with the prefix `playbook-` in the filename. That is the file you have to use from now on.  

 ## Pull Request  
- Your playbooks will only be reviewed after finalizing the code-review stage.  
- We will review your playbooks and comment for any needed changes.  
  
  
We value your time and willingness to contribute. Thank you for contributing to our content!
