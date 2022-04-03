---
id: playbook-settings
title: Playbook Settings
---
You can manage general playbook settings such as the name, who can edit and run the playbook, as well as for which incident types the playbook runs in the playbook settings.

1. From the **Playbooks** page, click on the playbook whose settings you want to manage.

2. In the upper right-hand corner, click **Settings**.

	1. Under **Roles**, select the roles for which the playbook is available.
	1. Under **Advanced**, determine if the playbook runs in quiet mode. <br/>
		When **Quiet Mode** is enabled for tasks or playbooks, the inputs and outputs are not displayed in the Work Plan view (but are still used during playbook execution) and indicators are not auto-extracted. Also, when you enable Quiet Mode, War Room entries are not created and inputs and outputs are not stored in the Work Plan. Quiet Mode improves performance by increasing playbook speed and saving database size, for example, when processing indicators from threat intel feeds. We recommend enabling Quiet Mode for tasks and playbooks that process a large amount of information.
		
	![Playbook Settings](/doc_imgs/playbooks/playbook-settings.png "Playbook Settings")

3. Click **Save Version**. 
