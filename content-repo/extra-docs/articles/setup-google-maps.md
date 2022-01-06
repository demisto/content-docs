---
id: google-maps
title: Setup Google Maps in Cortex XSOAR using an Automation
description: How to setup Google Maps in Cortex XSOAR using an automation.
---

You need to set up Google Maps in Cortex XSOAR before using either the [ShowOnMap](https://xsoar.pan.dev/docs/reference/scripts/show-on-map) or the `ShowLocationOnMap` automation. To use Google Maps, you need to create a `Google Maps Platform API` from a Google Cloud account that has [billing enabled](https://developers.google.com/maps/documentation/javascript/cloud-setup#billing). After creating the API, you need to add it to Cortex XSOAR. You can then use the `ShowOnMap` automation.
If using the `ShowLocationOnMap` automation, to view the map, you need to add the automation to a indicator layout. 


1. In **Google Cloud Platform**, do the following:
   1. Create a [Google Cloud Project](https://developers.google.com/maps/documentation/javascript/cloud-setup).
   2. Create a [Google Maps Platform API](https://developers.google.com/maps/documentation/javascript/get-api-key) for your project.

   3. Enable APIs and Services (**API & Services>Dashboard**> **ENABLE APIS AND SERVICES**).
   4. Enable **Maps JavaScriptAPI**.
   5. Create the [Google Maps Platform API key](https://developers.google.com/maps/documentation/javascript/get-api-key#creating-api-keys) ( **Credentials**> **CREATE CREDENTIALS>API key**).
   6. Copy the Google Maps Platform API key.
2. Add the [Google Maps Platform API key to Cortex XSOAR](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA14u000000oMOUCA2&lang=en_US%E2%80%A9).
   1. Select **Settings > ABOUT > Troubleshooting> Add Server Configuration.**
   2. Add the following key and value: 

      | Key | Value |  
      | ----|----- | 
      | `UI.google.api.key`| `Google Maps Plafom API Key` (copied from step 1.3 above)|
    1. Click **Save**.
        <br/> You can now run the `ShowOnMap` automation in Cortex XSOAR. For example in the CLI type, `!ShowOnMap lat=6.1287 lng=1.2215`.
3. (`ShowLocationOnMap` automation only) [Customize an  indicator layout](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-5/cortex-xsoar-admin/manage-indicators/understand-indicators/customize-indicator-view-layouts/customize-an-indicator-type-layout.html).
   1. If using an out-of-the box layout, such as IP, duplicate/detach the layout.
   2. Edit the layout.
   3. Drop and drag the **General Purpose Dynamic Section** onto the indicator page.
   4. In the **General Purpose Dynamic Section**, click **Edit button>Edit section settings**.
   5. Edit the name as required. <br/> In this example, we will call it `ShowLocationOnMap-Sample-Layout`.
   6. In the **Automation Script** field, select **ShowLocationOnMap**.
    <br/> ![ShowLocatioOnMap](../../../master/docs/doc_imgs/reference/google-maps-gen-purpose.png).
   7. Click **OK**.

4. Add the indicator layout to an indicator type.
   1. Go to **Settings>OBJECTS SETUP>Indicators**.
   2. Select the indicator type and click **Edit**.
   3. In the **Layout** section select the layout you added in step 3.
   <br/> ![google-maps-indicator-type](../../../master/docs/doc_imgs/reference/google-maps-indicator-type.png)
   4. Click **Save**.

5. In the **Threat Intel** page, select a relevant indicator that has a value for the **GeoLocation** field. The map should be shown in the field that you created.
    <br/> ![googlemaps](../../../master/docs/doc_imgs/reference/google-maps-map.png)
      <br/> If you do not have an indicator that has a value for the **GeoLocation** field to test the indicator, edit the indicator and in the **GeoLocation** field, type `6.1287,1.2215`.
