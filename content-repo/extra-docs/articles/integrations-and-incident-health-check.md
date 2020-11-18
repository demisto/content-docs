---
id: integrations-and-incident-health-check
title: Integrations and Incidents Health Check
description: This Integrations and Incidents Health Check content pack enables system users to review all of the enabled failed integrations, incidents, and playbooks.
---
 
 
## Pack usage
 
As part of this pack, you will get out-of-the-box, full layouts, dashboards, incident types, and incident fields. All of these are easily customizable to suit the needs of your organization. You can configure the job on an hourly/daily/weekly basis to perform the health check. The job will run the checkup playbook that tests all enabled integrations and searches for open incidents with errors to get their status and retrieve the error information. Additionally, this job will update the dashboards for visibility.
 
### Playbooks
 
| Playbook Names | Description | Notes |
|---------------- | ------------- | ------------- |
| JOB - Integrations and Playbooks Health Check | You should run this playbook as a scheduled job. The playbook checks the health of all enabled integrations and open incidents | Under the playbook inputs, you can add recipients * to send the health check report* via email |
| Integrations and Playbooks Health Check - Running Scripts | This playbook is triggered by a 'JOB - Integrations and Playbooks Health' playbook responsible for running failed integrations and failed incidents scripts. The playbook may run separately from the main playbook to run health tests on enabled integrations and open incidents | This sub-playbook is **responsible for running the health check scripts** |
| JOB - Integrations and Playbooks Health Check - Lists handling | This playbook is triggered by a 'JOB - Integrations and Playbooks Health' playbook and is responsible for creating or updating related XSOAR lists | This sub-playbook is **responsible for save the scripts data to XSOAR list** |
 ---
 
Besides running the sub-playbooks, The master playbook "JOB - Integrations and Playbooks Health Check" will also:
Send the health check report to the recipients from the playbook inputs.
If another health check investigation is open (incident nor a job):
The playbook will **check if analyst notes were added** to the failed integrations and failed incidents grids and **copy** them to the new investigation.
The playbook will link the old investigation to the new one and close the old investigation due to irrelevance.
Re-run the health check tests. It is a manual action because you will want to re-run them only after fixing the issues and not before.
 
### Incident Layouts
The incident type contains two layouts: one for failed integrations and the other for failed incidents.
In the failed integrations layout, we see the number of failed instances, their category, the number of totals checked (AKA enabled) instances, and the grid that contains details with why they failed. 
The column 'Analyst Notes' in the grid is for **manual** use for tracking and adds comments about the integration status.
The same for failed incidents layout, we have the number of failed incidents, the total number of errors, the number of unassigned incidents (AKA incidents that failed, and no one knows because no one assigned for those incidents). We also have here the top failed commands and playbook names that failed. And the grid as you saw in the integrations layout with the analyst notes.
 
Note: When the master playbook copies the analyst note from the integration \ incident to the new investigation, the old investigation's date is added.
 
### Dashboards and Lists
The dashboard widgets use the data from the lists created or updated by the playbook.
The dashboard **isn't** a real-time view **The dashboard displays are the data for the time the playbook was running.**
For example, if the job/playbook runs once a day, the dashboard data will be updated once a day (at the same time the playbook is running).
 
## Before You Start
 
The playbooks in the pack use two scripts to check the integrations and incidents. 
"Demisto REST API" integration is mandatory for one of the scripts to run.
**To get the REST API key do the following:**
1. Go to 'Setting' -> 'INTEGRATIONS' -> 'API Keys'
2. Click "Get Your Key" -> Write the key name -> Click "Generate Key."
3. **Copy** the generated key
4. Paste the generated key in the "Demisto REST API" integration configuration.
 
 
## Pack Configurations
 
You can run the master playbook "JOB - Integrations and Playbooks Health Check" as an incident or as a scheduled job **In both cases, the type of the incident or job must be "Integrations and Playbooks Health Check."**
 
### Job Configurations
 
**To configure the scheduled job:**
**Go to 'Jobs'** -> Click "New Job" to create the new job.
In the job configuration:
Choose when you want the job to run. We recommend running the job on a daily \ weekly basis.
Write the job name.
Type - **The incident type must be "Integrations and Playbooks Health Check."**
Playbook - the playbook is *automatically filled* when choosing the "Integrations and Playbooks Health Check" type; if not supplied, the playbook should be "JOB - Integrations and Playbooks Health Check."
You can fill the rest of the requested fields, but is it not mandatory.
Lastly, click the "Create new job."
Note: if you create a new incident, not via the job, **The incident type needs to be "Integrations and Playbooks Health Check."**
 
 
