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
* When defining an integration - Select the incident type that is created. When this is configured, it becomes the default incident type. If you do not classify the event through classification and mapping, it will be set as what you have defined here. For information about defining the incident type within the integration settings, see [Integration Configuration](../integrations/yaml-file#configuration).
* By setting a classification key - Use the classification engine to determine the incident type. This overrides whatever you configured in the integration settings.

## Classify using a classification key

When an integration fetches incidents, it populates the rawJSON object in the incident object. The rawJSON object contains all of the attributes for the event. For example, source, when the event was created, the priority that was designated by the integration, and more. When classifying the event, you will want to select an attribute that can determine what the event type is.

1. Open the Classification & Mapping window for the Integrations instance: 

- In **Settings** -> **Integrations** -> **Servers & Services** click **Mapping** next to the integration instance.
- In **Settings** -> **Integrations** -> **Classifications & Mapping** select the integration instance from the drop-down menu.

2. Click **Set up a classification rule** to open the Classification wizard.

3. Load event data using one of the following options: 

  - Pull from *integrationName* - Cortex XSOAR fetches events from the instance (alerts, notifications etc.)
  - Upload JSON file - Upload a file containing the rawJSON object from the integration. The file must be uploaded in JSON format.  
  - Skip getting samples - Map the attributes without event data. This is not recommended.

4. Set the classification key.

   The event attributes are presented on the right side of the screen. Click on the attribute by which you want to classify the incidents. You can navigate between the fetched events to view all of the attributes in the other events and to ensure that you are selecting a viable attribute. In our example, below, we are classifying by the description attribute. 

   You can use filters and transformers to make the selection more exact.

5. Click **Done**.

   Once you select the attribute, the unique values for the attribute that you have selected from the fetched events appear under the **Unmapped Values** section on the left side of the screen.

6. Drag an unmapped value to the Values to Identify column for the incident type to which you want to classify. Any unmapped values that you do not classify, an incident type as defined in the integration will be created. 

   **Note:** You can map multiple values to an incident type, but you cannot map an unmapped value to multiple incident types.

## Map event attributes to fields

You should map event attributes to the incident fields so the information is indexed. By default, attributes are not mapped to any fields. They are only available in the incident.labels of the incident. 

1. Click Edit Mapping in the incident type. 

2. In the Mapping Wizard, in the left pane click **Choose data path**.

3. Click the event attribute to which you want to map. You can further manipulate the field using filters and transformers.

4. Click **Done**.

## Classifier & Mapper files structure

Classifier and mapper files structure differs before and after Cortex XSOAR version 6.0.

#### Up to Cortex XSOAR version 6.0

The classifier & mapper should be represented in one file, as exported from Cortex XSOAR, with addition of the field `toVersion: 5.9.9`.

The file should be named `classifier-<PACK-NAME>_5_9_9.json`, e.g. `classifier-CortexXDR_5_9_9.json`

#### Cortex XSOAR version 6.0 and above

Cortex XSOAR version 6.0 introduces an improved classification & mapping experience, which includes a mirroring functionality by allowing to map outgoing incidents.

:::note note
You can set default classifier and/or mapper for an integration by populating the following keys in the integration YAML file with the classifier and/or mapper IDs:
* For default classifier: `defaultclassifier`
* For default incoming mapper: `defaultmapperin`
* For default outgoing mapper: `defaultmapperout`
:::

Classifier file:
 - Filename: `classifier-<PACK-NAME>.json`, e.g. `classifier-CortexXDR.json`
 - File contents:
 ```jsonc
 {
	"name": string,                 // Usually is <PACK-NAME> - Classifier
	"type": "classification",
	"id": string,                   // Usually is <PACK-NAME>
	"description": string,          // Short description of the classifier
	"defaultIncidentType": string,  // Default incident type to classify by
	"keyTypeMap": object,           // Incident type mapping as generated in Cortex XSOAR
	"transformer": object,          // Incident type transformer as generated in Cortex XSOAR
	"version": -1,
	"fromVersion": "6.0.0"
  }
 ```
 
 For example:
  ```json 
 {
	"name": "Cortex XDR - Classifier",
	"type": "classification",
	"id": "Cortex XDR - IR",
	"description": "Classifies Cortex XDR incidents.",
	"defaultIncidentType": "",
	"keyTypeMap": {
		"PortScan": "Cortex XDR Port Scan",
		"XDR Incident": "Cortex XDR Incident"
	},
	"transformer": {
		"complex": {
			"accessor": "",
			"filters": [],
			"root": "description",
			"transformers": [
				{
					"args": {
						"dt": {
							"isContext": false,
							"value": {
								"complex": null,
								"simple": ".=val \u0026\u0026 val.toLowerCase().indexOf(\"port scan\") \u003e -1 ? \"PortScan\" : \"XDR Incident\""
							}
						}
					},
					"operator": "DT"
				}
			]
		},
		"simple": ""
	},
	"version": -1,
	"fromVersion": "6.0.0"
  }
 ```
 
 Incoming mapper file:
 - Filename: `classifier-mapper-incoming-<PACK-NAME>.json`, e.g. `classifier-mapper-incoming--CortexXDR.json`
 - File contents:
  ```jsonc
 {
    "name": string,             // Usually is <PACK-NAME> - Incoming Mapper
    "type": "mapping-incoming",
    "id": string,               // Usually is <PACK-NAME>-mapper
    "description": string,      // Short description of the incoming mapper
	"mapping": {},              // Fields mapping as generated in Cortex XSOAR
	"version": -1,
	"fromVersion": "6.0.0"
  }
 ```
 
 For example:
 ```json
 {
    "name": "Cortex XDR - Incoming Mapper",
    "type": "mapping-incoming",
    "id": "Cortex XDR - IR-mapper",
    "description": "Maps incoming Cortex XDR incidents fields.",
	"defaultIncidentType": "",
	"mapping": {
		"Cortex XDR Incident": {
			"dontMapEventToLabels": false,
			"internalMapping": {
				"XDR Alert Count": {
					"complex": null,
					"simple": "alert_count"
				},
				"XDR Assigned User Email": {
					"complex": null,
					"simple": "assigned_user_mail"
				},
				"XDR Assigned User Pretty Name": {
					"complex": null,
					"simple": "assigned_user_pretty_name"
				},
				"XDR Description": {
					"complex": null,
					"simple": "description"
				},
				"XDR Detection Time": {
					"complex": {
						"accessor": "",
						"filters": [],
						"root": "detection_time",
						"transformers": [
							{
								"args": {},
								"operator": "TimeStampToDate"
							}
						]
					},
					"simple": ""
				},
				"XDR High Severity Alert Count": {
					"complex": null,
					"simple": "high_severity_alert_count"
				},
				"XDR Host Count": {
					"complex": null,
					"simple": "host_count"
				},
				"XDR Incident ID": {
					"complex": null,
					"simple": "incident_id"
				},
				"XDR Low Severity Alert Count": {
					"complex": null,
					"simple": "low_severity_alert_count"
				},
				"XDR Medium Severity Alert Count": {
					"complex": null,
					"simple": "med_severity_alert_count"
				},
				"XDR Notes": {
					"complex": null,
					"simple": "notes"
				},
				"XDR Resolve Comment": {
					"complex": null,
					"simple": "resolve_comment"
				},
				"XDR Severity": {
					"complex": null,
					"simple": "severity"
				},
				"XDR Status": {
					"complex": null,
					"simple": "status"
				},
				"XDR URL": {
					"complex": null,
					"simple": "xdr_url"
				},
				"XDR User Count": {
					"complex": null,
					"simple": "user_count"
				},
				"occurred": {
					"complex": {
						"accessor": "",
						"filters": [],
						"root": "creation_time",
						"transformers": [
							{
								"args": {},
								"operator": "TimeStampToDate"
							}
						]
					},
					"simple": ""
				},
				"severity": {
					"complex": null,
					"simple": "severity"
				}
			}
		},
		"Cortex XDR Port Scan": {
			"dontMapEventToLabels": false,
			"internalMapping": {
				"XDR Alert Count": {
					"complex": null,
					"simple": "alert_count"
				},
				"XDR Assigned User Email": {
					"complex": null,
					"simple": "assigned_user_mail"
				},
				"XDR Assigned User Pretty Name": {
					"complex": null,
					"simple": "assigned_user_pretty_name"
				},
				"XDR Description": {
					"complex": null,
					"simple": "description"
				},
				"XDR Detection Time": {
					"complex": {
						"accessor": "",
						"filters": [],
						"root": "detection_time",
						"transformers": [
							{
								"args": {},
								"operator": "TimeStampToDate"
							}
						]
					},
					"simple": ""
				},
				"XDR High Severity Alert Count": {
					"complex": null,
					"simple": "high_severity_alert_count"
				},
				"XDR Host Count": {
					"complex": null,
					"simple": "host_count"
				},
				"XDR Incident ID": {
					"complex": null,
					"simple": "incident_id"
				},
				"XDR Low Severity Alert Count": {
					"complex": null,
					"simple": "low_severity_alert_count"
				},
				"XDR Medium Severity Alert Count": {
					"complex": null,
					"simple": "med_severity_alert_count"
				},
				"XDR Notes": {
					"complex": null,
					"simple": "notes"
				},
				"XDR Resolve Comment": {
					"complex": null,
					"simple": "resolve_comment"
				},
				"XDR Severity": {
					"complex": null,
					"simple": "severity"
				},
				"XDR Status": {
					"complex": null,
					"simple": "status"
				},
				"XDR URL": {
					"complex": null,
					"simple": "xdr_url"
				},
				"XDR User Count": {
					"complex": null,
					"simple": "user_count"
				},
				"occurred": {
					"complex": {
						"accessor": "",
						"filters": [],
						"root": "creation_time",
						"transformers": [
							{
								"args": {},
								"operator": "TimeStampToDate"
							}
						]
					},
					"simple": ""
				},
				"severity": {
					"complex": null,
					"simple": "severity"
				}
			}
		},
		"CortextXDRIncident": {
			"dontMapEventToLabels": false,
			"internalMapping": {
				"XDR Severity": {
					"complex": null,
					"simple": "severity"
				}
			}
		}
	},
	"version": -1,
	"fromVersion": "6.0.0"
  }
 ```

For more information about incident classification and mapping, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/incidents/classification-and-mapping).