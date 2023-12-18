---
id: capture-the-flag-preparation
title: Prepare your instance for Capture The Flag
description: How to prepare your Cortex XSOAR instance to run Cortex XSOAR's Capture The Flag challenge.
---
![ xsoar ctf csi image](../../../docs/doc_imgs/reference/CaptureTheFlag/ctfcsiimage.jpg)

# Introduction
The Cortex XSOAR 8 Capture the Flag challenges (CTFs) provide a fun and engaging way for your audience or teams to learn about Cortex XSOAR.
The CTFs can be completed in 1 hour and can easily be incorporated into an event for SOC practitioners. 


## Install CTF content Pack

The XSOAR CTF consists of two content packs:
 - Capture The Flag - 01
 - Capture The Flag - 02
It is recommended to install "Capture The Flag - 01" and "Capture The Flag - 02" in this order. 
1. Navigate to Cortex XSOAR Marketplace.
2. Search for "Capture The Flag - 01" and click **install**. 
3. After "Capture The Flag - 01" is installed, search for "Capture The Flag - 02" and click **Install**. 
Once the CTFs are installed, you will see a green checkmark by the CTF packs. 
 

![ xsoar ctf csi image](../../../docs/doc_imgs/reference/CaptureTheFlag/marketplace_search_for_ctf.png)

# Prepare Your CTF playbook.
After you install the CTF 1 and CTF 2 content packs from Marketplace,
You must run the “Prepare your CTF” playbook. The wizard will provide instructions on how to configure instances that are required for 
running the CTF. It will also check the system for any missing items.


## Install and Configure VirusTotal and Unit42 Atoms Feed
Unit 42 ATOMs Feed provides access to published IOCs that contain known malicious indicators. 
VirusTotal (API v3) will analyze suspicious hashes, URLs, domains, and IP addresses.   
You will need these two integrations for the CTF.
1. Go to *Playbooks* and search for “Prepare your CTF”.
![image](../../../docs/doc_imgs/reference/CaptureTheFlag/image6.png)
2. Click **View** to open the playbook.
![image](../../../docs/doc_imgs/reference/CaptureTheFlag/image9.png)
3. Click **Run** to run the playbook.
![image](../../../docs/doc_imgs/reference/CaptureTheFlag/image8.png)
The playbook will first check if VirusTotal and Unit 42 feeds are installed. If it is not installed, then follow the instructions to configure those from Marketplace. Here are the links to VirusTotal and Unit 42 ATOMs Feed. (Those integrations will enrich indicators and provide useful information to TIM).
![image](../../../docs/doc_imgs/reference/CaptureTheFlag/image11.png)
4. After installing VirusTotal and Unit 42 Feed, configure instances for those integrations. Click **Settings & Info** > **Settings** > **Instances**.
![image](../../../docs/doc_imgs/reference/CaptureTheFlag/image10.png)
5. Search for VirusTotal and add an instance of VirusTotal. Create your own VirusTotal account and retrieve the API key from there. (See the Help in the integration settings.)
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image13.png)
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image12.png)
6. Search for Unit 42 ATOMs Feed and add an instance of Unit 42 ATOMs Feed. Create your own Unit 42 ATOMs Feed account and retrieve the API key from there. (See the Help located in the integration settings.)
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image16.png)
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image14.png)


## Configure XDR-CTF and OHMYVT_CTF integrations.
The XDR-CTF and OHMYVT_CTF integrations were configured by default when you installed the CTF content pack. But you must configure an instance of each of those integrations. 
1. Go to the *Playbooks* section and open the “Prepare your CTF” playbook and rerun it. To rerun, click **Stop** and then **Run**.
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image15.png)
    If the previous configurations were configured correctly, the playbook will check for an XDR – CTF instance and a custom integration named “OHMYVT_CTF”.
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image18.png)
2. To configure Cortex XDR – IR CTF and OHMYVT_CTF instances, go to **Settings & Info** > **Settings** > **Instances**.
Search for XDR - IR CTF and configure an instance by clicking **+Add Instance**.
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image19.png)

Leave all the default settings and click **Save & Exit**.
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image20.png)
3. Now search for OHMYVT_CTF and click **+ Add instance**.
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image21.png)
Leave all the default settings and click **Save & Exit**.
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image22.png)


## Verify RDP brute force incident

You can now analyze and investigate various aspects of an RDP incident ingested from Cortex XDR. This incident is automatically created for you. In the following step, you will verify that the incident exists in the database and all the indicators from that incident have been extracted successfully.  
1. After configuring XDR – IR CTF and OHMYVT_CTF, go back to the **Playbooks** section and open the “Prepare your CTF” playbook and rerun it by clicking **Stop** and then **Run**.

Now, the playbook will stop at the step “Ensure the following”. For this step, you are asked to check the following:

-[ ] The incidents created successfully - wait until the incident for BruteForece stops on the manual task that classifies the incident.
-[ ] Indicators extracted properly.

![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image23.png)

2. Click **Incidents** and search for the incident name: “XDR Incident 413 - 'Possible external RDP Brute-Force' generated by XDR Analytics detected on host dc1env12apc05 involving user env12\administrator”.
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image24.png)
3. Open the incident and click the *Investigation* tab and ensure that the indicators have been extracted properly. 
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image1.png)
4. Go back to the *Playbooks* section and open the “Prepare your CTF” playbook and click **Mark Completed** for the “Ensure the following” step.
![image](../../../docs/doc_imgs/reference/CaptureTheFlag/image2.png)
If you need to rerun the playbook, click **Stop** and then **Run**.


## Final Validation

When the validation is complete and the malicious IP is tagged, the playbook will stop at the step “You are all set!” 
![iamge](../../../docs/doc_imgs/reference/CaptureTheFlag/image3.png)

### <center>Let the Games Begin. All the best!</center>
