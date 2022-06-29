---
id: playbooks-inputs-outputs
title: Inputs and Outputs
---
Playbooks and tasks have inputs, which are data pieces that are present in the playbook or task. The inputs are often manipulated or enriched and they produce outputs. The inputs might come from the incident itself, such the role to whom to assign the incident, or an input can be provided by an integration. For example, when an Active Directory integration is used in a task to extract a user's credentials. 

![Playbook Inputs](/doc_imgs/playbooks/Playbooks_Inputs.png)

In the image above, we see a playbook that is triggered based on context data, meaning an incident, and we see that the first two inputs are the SrcIP, which comes from the *incident.src* key, and DstIP, which is retrieved from *incident.dst*. 

In addition, the playbook itself creates output objects whose entries will serve the tasks throughout the playbook. 

![Playbook Inputs](/doc_imgs/playbooks/Playbooks_Outputs.png)

For example, we create a list of endpoint IP addresses which can later be enriched by an IP enrichment task. Or a list of endpoint MAC addresses which can be used to possibly get information about the hosts that were affected by the incident. 

In addition, outputs can be data that was extracted or derived from the inputs. For example, in the following image we received the user's credentials from Active Directory, and used those credentials to retrieve the user's email address, manager, and any groups to which they belong.

![Playbook Inputs](/doc_imgs/playbooks/Playbooks_Input-Output.png)

In turn, an output can then serve as input for a subsequent task. For example, the user's manager who was returned as an output in the image above, can be used as an input to retrieve information from Active Directory.

![Playbook Inputs](/doc_imgs/playbooks/Playbooks_Account-Manager.png)

Notice that the input for this task is Account.Manager, which is the output we highlighted in the playbooks inputs, above.

