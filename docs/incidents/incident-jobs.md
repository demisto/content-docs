---
id: incident-jobs
title: Jobs
---
You can create scheduled events in Cortex XSOAR using jobs. Jobs are triggered either by time-triggered events or feed-triggered events. For example, you can define a feed-triggered job to trigger a playbook when a specified TIM feed finishes a fetch operation for new indicators. Or you can schedule a time-triggered job that runs nightly and removes expired indicators.

For a better understanding of how jobs are implemented to trigger playbooks, read the [tutorial for adding indicators to a SIEM](https://xsoar.pan.dev/docs/reference/articles/tim-edl).

## Create a Job

1. Navigate to **Jobs**.

1. Click **New Job**.

1. Determine if the job is time-triggered or feed-triggered. 
	* Time-triggered jobs run at pre-determined times. You can schedule the job to run at a recurring time or one time at a specific time or date. 
	* Feed-triggered jobs run when a feed has completed an operation. For example, a TIM feed has finished ingesting new indicators.

### Time-triggered Jobs
1. To configure the job to recur, select **Recurring**. <br/> Determine at which intervals the job recurs, when it starts, and when the job expires. 
You can also configure the recurring job using a cron expresion. To do so, click **Switch to Cron view** and enter the expression. For assistance in defining the cron expression, click **Show cron examples**. <br/> To configure the job to run once, enter a date and time in the **Start at** field.

![Time-triggered Job](/doc_imgs/incidents/Jobs_Time-Triggered_Basic.png)

1. Enter the information in the job configuration fields. Explanations of the job configuration fields are available below under Job Fields Reference.

1. Configure how the job behaves when a previous of the instance of the job is already running. 
	1. Under **Queue Handling**, select **Notify the owner** to inform the user listed under the **Owner** field that an instance of the job is already running.

	1. Determine the job behavior:
		* **Don't trigger a new job instance** - the current job continues to run and a new job is not triggered.

		* **Cancel the previous job instance and trigger a new job instance** - the current job that is running is cancelled and new job is triggered.

		* **Trigger a new job instance and run concurrently with the previous instance** - the current job continues to run and a new job is triggred in parallel. 

	![Time-triggered Queue Handling](/doc_imgs/incidents/Jobs_Time-Triggered_Queue-handling.png)	

1. Click **Create new job**. 


### Feed-triggered Jobs

1. Determine if the job is triggered when any feed has completed its operation or only when a specific feed(s) has completed its operation.

1. Enter a meaningful name for the job.

1. Select the playbook that runs when this job is triggered.

1. Add tags to apply to the job. You can use these tags as a search parameter in the system.

1. Click **Create new job**. 

![Feed-triggered Job](/doc_imgs/incidents/Jobs_Feed-Triggered.png)

## Job Fields Reference

The following table lists the fields available when defining a job, and their descriptions.

| Name | Description | 
| ------ | ------ |
| Recurring | Determine if the job is triggered at a pre-determined time interval. |
| Tags | Add tags to apply to the job. You can use these tags as a search parameter in the system. |
| Name | Enter a meaningful name for the job. |
| Owner | Assign an owner to the incident. |
| Role | Select the role who can access the incident. |
| Type | Determine the incident type created by this job. |
| Severity | Determine the severity of the incident that is created. |
| Playbook | Determine which playbook to run when this job is triggered. |
| Labels | Select the labels that are available in the incident type. |
| Phase | Select the phase of the investigation in which this incident is opened. |
| Details | Enter details that should appear within the incident. |
| Attachments | Click the clip to add attachments to the job. |
| Notify the owner | Sends a message to the job owner using one of the notification methods configured in Cortex XSOAR. |

For more information about jobs, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/playbooks/create-a-job).