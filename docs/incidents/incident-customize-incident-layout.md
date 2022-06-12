---
id: incident-customize-incident-layout
title: Convert Layout Files from Cortex XSOAR 5.5
---

Prior to Cortex XSOAR 6.0, each incident layout tab, when exported, was a separate file. From Cortex 6.0 and later, all [incident layout](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/incidents/customize-incident-view-layouts/customize-incident-layouts) tabs can be exported as a single file containing the complete incident layout.

Note: For the layout to be associated with incident/indicator type, the layout ID should be populated in the `layout` attribute in the incident/indicator type JSON file.

Example of 6.0 schema:

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
 
 
### Demo Video: How to convert Layout files to Cortex XSOAR version 6.0 and above
  
 <video controls>
    <source src="https://github.com/demisto/content-assets/raw/9f10fd6817ad98aff05e604f5d9068428a7e8ed3/Assets/xsoar.pan.dev/Convert_XSOAR_Layouts_from_5.5_to_6.0.mp4"
            type="video/mp4"/>
    Sorry, your browser doesn't support embedded videos. You can download the video at: https://github.com/demisto/content-assets/blob/9f10fd6817ad98aff05e604f5d9068428a7e8ed3/Assets/xsoar.pan.dev/Convert_XSOAR_Layouts_from_5.5_to_6.0.mp4 
</video>
