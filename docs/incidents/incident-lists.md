---
id: incident-lists
title: Lists
---
Lists can be created in the Cortex XSOAR UI and modified to be used in scripts and War Rooms. A list can contain items of the same type in any format that would be useful. These are later parsed by, and can be modified by, scripts. For example, you might need to create a list of emails, or a list of known trusted IPs (allow list), etc.

The Lists content item must be in JSON format and can be imported independently or as part of a pack.  


## Create a List

1. Navigate to **Settings** > **Advanced** > **Lists**.

1. Click **Add a List**.

1. (Multi-tenant) From the dropdown list, select the propagation labels to propagate the list to the relevant tenants.

1. In the *Content Type* field, select the way the data is store under the data key in the json file.

1. To restrict access to the list, in the Permissions section, select the *Read Only* and *Read and edit* roles.

1. Click **Save Version**. 

1. Exit the list editor.
3. Export the list by clicking ![download button](/doc_imgs/integrations/50277516-4d74bd80-044d-11e9-94b6-5195dd0db796.png).


### Add Lists to your Project

1. Save your newly created list to the Lists directory in your pack as a JSON file. 
   - The Lists directory is *Packs/<pack_name>/Lists/*. 
   - The name of the file should be *list-<list_name>.json*.
2. In the list json file that you created, edit the *id* field so that it is identical to the *name* field.

3. Modify the value in the *version* field to -1 to prevent user changes.

   For example the top of your JSON file should look like this:

   ```json

   id: <name of your list>
   version: -1
   name: <name of your list>
   ```

### Example of a Lists JSON File

The following is an example of a list-checked_integrations.json file.

        {
	        "allRead": false,
        	"allReadWrite": false,
        	"data": "Cylance Protect v2_instance_1,Demisto REST API_instance_1,Image OCR_default_instance,McAfee ESM v2_instance_1,Microsoft Defender Advanced Threat Protection_instance_2,Rasterize_default_instance,Trend Micro Deep Security_instance_1,Where is the egg?_default_instance,d2,fcm_default_instance,vt,ad-login,ad-query,splunk",
        	"dbotCreatedBy": "",
        	"description": "",
        	"fromVersion": "6.5.0",
        	"hasRole": false,
        	"id": "checked integrations",
        	"itemVersion": "",
        	"locked": false,
        	"name": "checked integrations",
        	"nameLocked": false,
        	"packID": "",
        	"previousAllRead": false,
        	"previousAllReadWrite": false,
        	"previousRoles": [],
        	"roles": [],
        	"system": false,
        	"tags": null,
        	"toVersion": "",
        	"truncated": false,
        	"type": "plain_text",
        	"version": -1
        }

### Import a List
You can import a content item list.

1. Navigate to **Settings** > **Advanced** > **Lists**.
2. Click ![import button](/doc_imgs/integrations/50277516-4d74bd80-044d-11e9-94b6-5195dd0db796.png).
3. Navigate to and select the content list to import.
4. Click *Open*.
