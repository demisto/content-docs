---
id: task-complete 
title: taskComplete 
---
You can use this command to mark a playbook task as completed. For example, you might need to include the taskComplete command in a SLA breach script, to close a task and force the playbook to continue running after the SLA has been breached. You can also use the taskComplete command to add an action button in an incident layout, that can be used to mark a specific playbook task as complete. 

| Argument         | Description           | 
| ------------- |-------------|   
| id     | Specify the task ID or tag to complete.      |   
| parentPlaybookID     | Parent playbook task ID, will limit task identification by tags to this sub-playbook only.      |   
| incidentId     | Incident ID where this task belongs to. Defaults to current incident.      |   
| comment     | Task completion comment.      |   
| input     | Conditional task completion selection.      |   
| allowSkipped     | Allow doing actions on skipped tasks (default is Yes).  |   
| isAutoRun     | When set to true, the task will be executed. Default is false. Relevant only for automation/playbook tasks. When set to false, the task is completed immediately.  |   
| args     | Set only if you set isAutoRun=true. Passing input arguments to the task automation/playbook for execution. The args must be of JSON format where the key is the name of the script/command/playbook argument name. Example: \{"ARG_NAME":"ARG_VALUE"\}      |   

   
