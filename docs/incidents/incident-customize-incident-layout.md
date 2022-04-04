---
id: incident-customize-incident-layout
title: Customize Incident Layouts
---
After configuring your fields and incident types, it is important to build or customize the layout to ensure that you are seeing the information that is germane to the incident type. For example, for a phishing incident you will want to see email headers, which would not be relevant for an access incident. Additionally, while some information might be relevant for multiple incident types, its location in one incident type might require more prominence than in another incident type.

You can customize almost every aspects of the layout, including, but not limited to:

* which tabs appear
* in which order do they appear
* who has permissions to view the tabs
* which information appears and how is it displayed

You can add dynamic sections to a layout, such as a graph of the number of bad indicators, their source, and severity. Also, you can use queries to filter the information in the dynamic section to suit your exact needs.

## Customize an Incident Type Layout

1. Navigate to **Settings** -> **Advanced** -> **Incident Types**.

2. Select the incident type whose layout you want to edit and click **Edit Layout**.
   You are presented with the current layout, which is populated with demo data so you can see how the fields fit.

3. (Optional) Drag and drop the tabs to reorder their appearance. For example, drag the **War Room** so it appears after the **Work Plan**. You can also click **+New tab** to add a tab that currently does not exist.

### Manage general settings for a tab

You can configure which tabs appear and for whom, as well as duplicate or remove tabs from the layout.

1. Hover over the tab that you want to configure.

2. Click the gear icon. 

   You are presented with the following options:

   * Rename

   * Duplicate

   * Delete

   * Hide

   * Viewing Permissions

	a. To limit the roles for whom the tab appears, click **Viewing Permissions**.

	b. Select the role(s) who can view the tab and click **Save**.

### Define Section Properties

You can determine how a section in the layout appears in the layout. For example, does the section include the section header or not. You can also configure the fields to appear in rows or as cards. For example, if you know that some of the field values will be very long, you are better off using rows. If you know that the field values are short, you might want to use cards so you can fit more fields in a section.

![Align as Cards](/doc_imgs/incidents/Layout-Builder_Section-Cards.png "Align as Cards")

To remove or duplicate a section, or change its properties:

1. Click the section title. In the image above, that is Timeline Information.

2. Click the pencil icon and select the relevant option.

To change the information that appears in dynamic sections:

1. Click the section title. For example, Indicators.

2. Click the pencil icon and select **Edit section settings**.

3. Under **Query**, enter the parameters by which you want to filter the information that appears. 

   For example, to see all indicators of type IP and with a reputation of Bad that were found by a specific feed since March 1st 2020, enter Type:IP and reputation:Bad and firstseenbyfeed:>="2020-03-01T00:00:00 +0200".

  ![Dynamic Section Query](/doc_imgs/incidents/Layout-Builder_Dynamic-Section-Query.png "Dynamic Section Query")

4. Click **OK**.

### Add New Sections or Fields to a Layout

You can add new sections or fields to the layout by dragging and dropping them from the **Library** on the left into the layout. For example, insert a new field that you created into a new, or already existing, section.

## Layout file structure

Layout structure differs before and after Cortex XSOAR version 6.0.

#### Up to Cortex XSOAR version 6.0

Each layout kind should be represented in one file, as exported from Cortex XSOAR, with addition of the field `"toVersion": "5.9.9"`.

The file should be named `layout-<KIND>-<TYPE>.json`, e.g. `layout-details-Phishing.json`

#### Cortex XSOAR version 6.0 and above

Cortex XSOAR version 6.0 introduces better layout management. As part of it, all the kinds and types (i.e. detailsV2, edit, etc...) of layouts are consolidated in one file, as described below.

The layout file exported from the system contains all the required fields, but the `"fromVersion": "6.0.0"` that needs to be added.

Note: for the layout to be associated with incident/indicator type, the layout ID should be populated in the `layout` attribute in the incident/indicator type JSON file.

 - Filename: `layoutscontainer-<TYPE>`, e.g. `layoutscontainer-Phishing.json`
 - Files contents:
 ```json
 {
    "id": string,                   // Usually is the incident/indicator type ID
    "group": incident OR indicator, // Layout entity type
    "name": string,                 // Display name
    "description": string,          // Short description of the layout
    "version": -1,
    "fromVersion": "6.0.0",
    "details": object,              // Optional layout type (Legacy)
    "detailsV2": object,            // Optional layout type
    "edit": object,                 // Optional layout type
    "close": object,                // Optional layout type
    "quickView": object,            // Optional layout type
    "mobile": object,               // Optional layout type
    "indicatorsDetails": object,    // Optional layout type
    "indicatorsQuickView": object   // Optional layout type
 }
 ```
 
 For example, see [Phishing incident layout](https://github.com/demisto/content/blob/master/Packs/Phishing/Layouts/layoutscontainer-Phishing.json).
 
 
### Demo Video: how to convert Layout files to version 6.0 and above
 
 
 <video controls>
    <source src="https://github.com/demisto/content-assets/raw/9f10fd6817ad98aff05e604f5d9068428a7e8ed3/Assets/xsoar.pan.dev/Convert_XSOAR_Layouts_from_5.5_to_6.0.mp4"
            type="video/mp4"/>
    Sorry, your browser doesn't support embedded videos. You can download the video at: https://github.com/demisto/content-assets/blob/9f10fd6817ad98aff05e604f5d9068428a7e8ed3/Assets/xsoar.pan.dev/Convert_XSOAR_Layouts_from_5.5_to_6.0.mp4 
</video>
