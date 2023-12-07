---
id: ransomware
title: Ransomware 
description: Identify, investigate, and contain the ransomware attack.
---
> **Note**: Post Intrusion Ransomware Investigation is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve.

This pack is used to identify, investigate, and contain ransomware attacks.


## Pack Workflow
When a ransomware attack is detected, for example by your endpoint protection service, this pack is used to identify, investigate, and contain the ransomware attack.

When the incident is created in XSOAR, the **Post Intrusion Ransomware Investigation** playbook extracts account and endpoint information, which is used in the investigation. 

The Ransomware pack requires the ransom note and an example of an encrypted file `(<1MB)` to try to identify the ransomware and find a recovery tool via the [online database](https://id-ransomware.malwarehunterteam.com/).

If defined, relevant stakeholders will be notified of the attack automatically.

For a proper recovery process, it is essential to determine the incident timeline, which is a manual task executed in the playbook. Prior attacker actions must be investigated, as data encryption is the final step in the attack.

The playbook includes options to further investigate the activity of the user whose files were encrypted, and identify additional endpoints that experienced the attack.

If auto-remediation is approved, the malicious indicators from the ransom note are automatically blocked. Alternatively, the containment can be done manually.


## In This Pack
The Ransomware content pack includes several content items.

### Playbooks
There is one playbook - **Post Intrusion Ransomware Investigation**: This playbook helps you better understand the status of the attack by collecting the information needed from your environment, performing the required investigation steps, containing the incident, and displaying the data with the **Post Intrusion Ransomware** incident layout.
The playbook inputs are:
- **AutoIsolation**: Indication whether to perform auto-isolation for the infected endpoint. Default is False.
- **NotificationEmail**: A comma-separated list of email addresses to notify if there is a possibility of the ransomware spreading and infecting other endpoints. Can be a CSV list.
- **EmailBody**: The notification email sent to the specified email addresses in case of an attack. The default message includes a general notice and the incident ID.

### Incident Types
There is 1 incident type - **Post Intrusion Ransomware**.

### Incident Fields
There are 12 incident fields.

| **Incident field** | **Description** |
|------------------ | ------------- |
| Ransomware Approximate Number Of Encrypted Endpoints | The number of endpoints found encrypted by the ransomware. |
| Ransomware Cryptocurrency Address | The ransomware cryptocurrency address. |
| Ransomware Cryptocurrency Address Type | The type of the ransomware cryptocurrency. |
| Ransomware Data Encryption Status | Indication whether data is currently encrypted or not. |
| Ransomware Email | The email address for communication with the ransomware operators group. |
| Ransomware Encrypted File Owner | The user who encrypted the files across the domain. |
| Ransomware Note | The ransom note. Sample ransom note available [here](#Sample-Ransom-Note).| 
| Ransomware Onion Address | The onion service addresses for communication with the ransomware operators group. |
| Ransomware Recovery Tool | The name of the recovery tool for the ransomware, if available. | 
| Ransomware Strain | Ransomware ID. |

### Automations
There are 2 automations in this pack.

- **RansomwareDataEncryptionStatus**: Returns the **Ransomware Data Encryption Status** in the **Post Intrusion Ransomware Investigation** playbook and the **Post Intrusion Ransomware** layout.
- **RansomwareHostWidget**: Returns the **Ransomware Approximate Number Of Encrypted Endpoints** in the **Post Intrusion Ransomware** incident/layout.

### Layout
There is 1 layout - **Post Intrusion Ransomware**

There are 5 sections in the layout to display the information collected about the attack and the indicators extracted.

| **Layout sections** | **Description** |
|------------------ | ------------- |
| Ransomware Details | Displays the information collected about the attack. For example, the ransomware strain, the number of estimated encrypted endpoints, and whether a recovery tool is available. |
| Indicators | Lists the indicators extracted from the ransom note and information about them. You can drill down into each indicator by viewing it in the Indicator Quick View. |
| Ransomware Data Encryption Status | Indication whether data is currently encrypted or not. |
| Hosts Count | The number of endpoints found encrypted by the ransomware. |
| War Room updates | War Room note entries. |

## Before You Start (prereqs)
In order to use this pack you need to configure an instance of the following integrations. See the documentation for each integration for detailed instructions. 

- Fetch incidents integration: the integration you are using to fetch and ingest ransomware incidents, for example, Palo Alto Networks Cortex XDR.
- [Active Directory Query V2](https://xsoar.pan.dev/docs/reference/integrations/active-directory-query-v2): Includes the **Active Directory Investigation** playbook, which investigates changes and manipulation in Active Directory Access Control Lists (ACLs). 
- [Rasterize](https://xsoar.pan.dev/docs/reference/integrations/rasterize): Converts URLs, PDF files, and emails to an image file or PDF file - used for ransom note manipulation. 
- [Cryptocurrency](https://xsoar.pan.dev/docs/reference/integrations/cryptocurrency): Classifies Cryptocurrency indicators as suspicious when ingested.

## Pack Configurations
You need to perform the following step before you start using the **Post Intrusion Ransomware Investigation** playbook to handle ransomware attacks.

### Incident Mapping

When using a 3rd party tool to identify and ingest ransomware attacks (such as Palo Alto Networks Cortex XDR), you need to map the **Usernames** and **Hostnames** fields. For more information about mapping, see [Classification & Mapping](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/incidents/classification-and-mapping).

For example, for Palo Alto Networks Cortex XDR the **users** and **hosts** fields should be mapped to XSOAR **Usernames** and **Hostnames** fields, respectively. 

## Testing the Pack
After you install the pack and perform all required prerequisites, test the pack to make sure everything works. There are two ways to test this pack, either manually create an incident or ingest an incident of type **Post Intrusion Ransomware**.

### Manual Test

The section in the **Post Intrusion Ransomware Investigation** playbook that includes endpoint and account enrichment can't be executed during the manual test. Therefore, the endpoint can't be isolated, nor can the account be disabled. 

1. Create a new incident.
3. Configure the **Post Intrusion Ransomware Investigation** playbook inputs.
4. Use the sample ransom note available [here](#Sample-Ransom-Note).

### Ingestion Test

1. Configure an instance of the integration that you will use to ingest and create incidents of type **Post Intrusion Ransomware**.
2. Map the corresponding fields from the integration to **Usernames** and **Hostnames**.
3. Verify that the **Post Intrusion Ransomware Investigation** playbook is the default playbook and configure its inputs.
4. Start ingesting the incidents.

## Integrations
Integrations required for this pack.

- Fetch incidents integration: the integration you are using to fetch and ingest ransomware incidents, for example, Palo Alto Networks Cortex XDR.
- Active Directory Query V2 - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/active-directory-query-v2)
- Rasterize - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/rasterize)
- Cryptocurrency - [(see the documentation)](https://xsoar.pan.dev/docs/reference/integrations/cryptocurrency)

## Sample Ransom Note
```
Hi!
Your files are encrypted.
All encrypted files for this computer has extension: .1401
—
If for some reason you read this text before the encryption ended,
this can be understood by the fact that the computer slows down,
and your heart rate has increased due to the ability to turn it off,
then we recommend that you move away from the computer and accept that you have been compromised,
rebooting/shutdown will cause you to lose files without the possibility of recovery and even god will not be able to help you,
it could be files on the network belonging to other users, sure you want to take that responsibility?
—
Our encryption algorithms are very strong and your files are very well protected, you can’t hope to recover them without our help.
The only way to get your files back is to cooperate with us and get the decrypter program.
Do not try to recover your files without a decrypt program, you may damage them and then they will be impossible to recover.
We advise you to contact us as soon as possible, otherwise there is a possibility that your files will never be returned.
For us this is just business and to prove to you our seriousness, we will decrypt you some files for free,
but we will not wait for your letter for a long time, mail can be abused, we are moving on, hurry up with the decision.

Сontact us:
kazkavkovkiz@cock.li
Hariliuios@tutanota.com

Download and install tor-browser: https://torproject.org/
auzbdiguv5qtp37xoma3n4xfchr62duxtdiu4cfrrwbxgckipd4aktxid.onion
azefmozbmelwjc4elhoim2q3t3y4z3yoodczvqagtquvwzhx763f4jtyd.onion

Personal Code:
{code_1401:smjErehmmb8LN/ANr+7IThQKwUq3HbWCnh6hI5U0QmCXxlLi+E
vx5Fcfp3p4q8GUCIEw9pQzIHugCWZqozxmIES39ohGqXRDXKkv
Ri/rJHtNC3J8BRvrrbqFYkJrDrwLLBBK7127c3qEyJf8EyOXhn
WNQ7dH6oAO6qAejWIE0XH73AqHeQ1hiAeiB3U7vviDKLzYTG9z
V/DoxL9iM4CUbz8ZtVpqeIO7mw0OWcsx5oHkXVqGXg1SziRPKT
d58WyzVj5niEeKrAlRhd9eJb00pEtFcw==}

BTC Wallets
1AGNa15ZQXAZUgFiqJ2i7Z2DPU2J6hW62i
1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2
3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy
bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq
```
