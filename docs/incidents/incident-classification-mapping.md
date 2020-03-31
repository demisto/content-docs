---
id: incident-classification-mapping
title: Classification and Mapping
---
The classification and mapping feature enables you to take the events and event information that Cortex XSOAR ingests from integrations or REST API, and classify the event as a type of Cortex XSOAR incident. For example, Cortex might generate alerts from Traps which you would classify according to the information in those either as dedicated Traps incident types or maybe Authentication or Malware. You might have EWS configured to ingest both phishing and malware alerts which you would want to classify to their respective incident types based on some information in the event. By classifying the events differently, you have more control of the incident type and allowing you to run multiple playbooks for the events coming from one source. 

Once you classify the incident, you can map the fields from the 3rd party integration to the fields that you defined in the incident layout.
Any fields that you do not map, are automatically mapped to Cortex XSOAR labels. While this information can still be accessed, it is always easier to work with fields. 

To get the most benefit out of classification and mapping, make sure that you understand which information will be ingested from the events so you can set up the fields and incident types accordingly. 

## Classification
Classification determines the type of incident that is created for events ingested from a specific integration.  
You can classify events in one of two ways:
* When defining an integration - Select the incident type that is created. When this is configured, it becomes the default incident type. If you do not classify the event through classification and mapping, it will be set as what you have defined here. For information about defining the incident type within the integration settings, see [XSOAR Dev Hub](https://xsoar.pan.dev/docs/reference).
* By setting a classification key - Use the classification engine to determine the incident type. This overrides whatever you configured in the integration settings.

## Classify using a classification key

When an integration fetches incidents, it populates the rawJSON object in the incident object. The rawJSON object contains all of the attributes for the event. For example, source, when the event was created, the priority that was designated by the integration, and more. When classifying the event, you will want to select an attribute that can determine what the event type is.

1. Open the Classification & Mapping window for the Integrations instance: 

- In **Settings** -> **Integrations** -> **Servers & Services** click **Mapping** next to the integration instance.
- In **Settings** -> **Integrations** -> **Classifications & Mapping** select the integration instance from the drop-down menu.

2. Click **Set up a classification rule** to open the Classification wizard.

3. Load event data using one of the following options: 

  - Pull from *integratioName* - Cortex XSOAR fetches events from the instance (alerts, notifications etc.)
  - Upload JSON file - Upload a file containing the rawJSON object from the integration. The file must be uploaded in JSON format.  
  - Skip getting samples - Map the attributes without event data. This is not recommended.

4. Set the classification key.

   The event attributes are presented on the right side of the screen. Click on the attribute by which you want to classify the incidents. You can navigate between the fetched events to view all of the attributes in the other events and to ensure that you are selecting a viable attribute. In our example, below, we are classifying by the description attribute. 

   You can use filters and transformers to make the selection more exact. For more information, see [INSERT LINK TO filters and transformers doc]

5. Click **Done**.

   Once you select the attribute, the unique values for the attribute that you have selected from the fetched events appear under the **Unmapped Values** section on the left side of the screen.

6. Drag an unmapped value to the Values to Identify column for the incident type to which you want to classify. Any unmapped values that you do not classify, an incident type as defined in the integration will be created. 

   **Note:** You can map multiple values to an incident type, but you cannot map an unmapped value to multiple incident types.

## Map event attributes to fields

You should map event attributes to the incident fields so the information is indexed. By default, attributes are not mapped to any fields. They are only available in the incident.labels of the incident. 

1. Click Edit Mapping in the incident type. 

2. In the Mapping Wizard, in the left pane click **Choose data path**.

3. Click the event attribute to which you want to map. You can further manipulate the field using filters and transformers. For more information, see [INSERT LINK TO filters and transformers doc].

4. Click **Done**.