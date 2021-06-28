
## Phishing Campaign

A phishing campaign is a collection of phishing incidents that originate from the same attacker or that are part of the same organized attack launched against multiple users.
Since phishing campaigns are actually a number of phishing incidents that are similar to each other, it's important to detect them, create the links between them and look at them as a whole rather than spend time investigating each incident separately.

Phishing Campaigns in XSOAR are detected and managed through the Phishing Campaign Content Pack.

### How It Works

The Phishing Campaign pack contains the `FindEmailCampaign` script.
The script interates over existing, previous phishing incidents and by using machine-learning to inspect different parameters in the phishing incidents, it is able to detect similar phishing incidents. The incidents may be deemed similar if elements like, but not limited to, the email body, subject or sender are similar (they do not need to be identical).
The script outputs the data about all the incidents that were found to be part of the campaign to the context, as well as sets summarized information about the campaign in incident fields.

The script can be customized to meet different criteria if your email information is mapped into different fields, if your incident type has a different name or if the similarity by which incidents are searched is too lenient or too strict.

The script can be run to detect phishing campaigns, but in order to fully utilize the pack to detect and manage campaigns, the `Find & Detect Phishing Campaigns` playbook should be used. 

The playbook uses the `FindEmailCampaigns` script to detect phishing campaigns. If incidents belonging to a campaign were detected, the playbook checks whether the incidents are already linked to a Phishing Campaign incident or not. If they are, then the currently investigated incident is also added to that campaign. If not, then a new Phishing Campaign incident will be created - and all similar incidents will be linked to it.

Additionally, the playbook takes the context and incident fields set by the `FindEmailCampaign` script, and updates the Phishing Campaign incident with that data so that it contains the most up to date information about the phishing incidents.

Finally, the playbook marks all the similar Phishing incidents as incidents belonging to the detected Phishing Campaign incident. It edits their context by adding the **PartOfCampaign** context key to it:

![image](https://user-images.githubusercontent.com/43602124/123551791-e5b92f00-d77b-11eb-9923-0968691a93fb.png)

This context key is then used by a dynamic section in the Phishing incidents which tells the analyst that the incident is part of a bigger campaign, and provides a quick link to the related campaign:

![image](https://user-images.githubusercontent.com/43602124/123551826-0a150b80-d77c-11eb-91ed-3325016d6935.png)


### Configuration

The way that you'll use the pack to detect and manage phishing campaigns is customizable all through the inputs of the `Detect & Manage Phishing Campaigns` playbook.
All of the playbook inputs are there to customize the execution of the `FindEmailCampaign` script, except for the first input - `AutomaticallyLinkIncidents` - which we recommend stays "True" to ensure that campaign detection and linkage is correct.

You may leave the following configurations with their default value, or change them according to your needs:
- `incidentTypeFieldName` - The **name** of the **incident field** in which the incident type is stored. Default is "type". Change this arguement only if you're using a custom field for specifying the incident type.
- `incidentTypes` - A comma-separatetd list of incident types by which to filter phishing incidents. Specify "None" to search through all incident types. By default - the value is Phishing because OOTB our phishing incidents have the Phishing incident type.
- `existingIncidentsLookback` - The date from which to search for similar phishing incidents. Date format is the same as in the incidents query page. For example: "3 days ago" or "2019-01-01T00:00:00 +0200".
- `query` - Additional text by which to query incidents to find similar phishing incidents. This uses the same lanaguage used to query incidents in the UI.
- `limit` - The maximum number of incidents to fetch. This determines how many incidents can be checked for similarity at the time of execution.
- `emailSubject` - The **name** of the **incident field** that contains the email subject. By default this will be "emailsubject" (because the email subject is stored under ${incident.emailsubject}).
- `emailBody` - The **name** of the **incident field** that contains the email body.
- `emailBodyHTML` - The **name** of the **incident field** that contains the HTML version of the email body.
- `emailFrom` - The **name* of the **incident field** that contains the email sender.
- `statusScope` - Whether to search similar incidents in closed incidents, non closed incidents or all incidents.
- `threshold` - Threshold to consider incident as similar. The range of values is 0-1. If needed, make small adjustments and continue to evaluate the right value for you. We recommend leaving this at the default value of 0.8.
- `maxIncidentsToReturn` The maximum number of incidents to display as part of a campaign. If a campaign includes a higher number of incidents, the results will contain only this amount of incidents.
- `minIncidentsForCampaign` - The minimum number of similar incidents to consider as a campaign. E.g., if you specify 10, but only 9 similar incidents are found - the script will not find them as part of a campaign.
- `minUniqueRecipients` - The minimum number of unique recipients of similar phishing incidents to consider as a campaign.
- `fieldsToDisplay` - A comma-seperated list of incident fields of the phishing incidents that are part of the campaign - to set in the context and to display in the markdown fields set by the script. An example of a possible value is "emailclassification,closereason". The list of fields specified here is the list of fields that will be output to the context for each phishing incident, and the same fields that will be displayed when looking at the Phishing Campaign incident to manage the campaign.
**Note* - removing the "emailfrom", "recipients" or "severity" fields from this list will affect dynamic sections displayed in the Phishing Campaign layout and render them useless.
**Note** - the fields referred to in this input are **incident fields**, not **context fields**. However, "Recipients" is a context field and is the only field which is not an incident-field and can still be displayed about the phishing incidents.

**Note:** the filters are applied to the incidents in the following order from left to right:
limit > lookBack > threshold. Meaning: if limit is 30, then only 30 incidents will be checked for similarity to begin with.

### Campaign Overview & Management

After the `Detect & Manage Phishing Campaigns` runs and finds a phishing camapaign, the Phishing incident will continue its investigation as usual. However, the analyst will already be able to view the incident as part of a campaign and take actions from another incident - the Phishing Campaign incident.

The Phishing Campaign incident gives the analyst an overview of the different elements of the campaign in the Campaign OVerview tab in its layout:
![image](https://user-images.githubusercontent.com/43602124/123633144-8281d800-d821-11eb-885e-980984a1af19.png)

The campaign summary displays aggregated information about the phishing incidents that make up the campaign.
The number of phishing incidents in which every detail of the campaign was observed is included in parenthesis.
Under the summary is a short version of what the campaign email looks like.
On the right side, there are dynamic sections showing important key information about the campaign incidents. 
**Note:** if any of the dynamic sections is empty, it's because context is missing, which is a result of running the `FindEmailCampaign` without all the necessary `fieldsToDisplay`, or without setting the context to the `Phishing Campaign` incident. This should work OOTB if the `Detect & Manage Phishing Campaigns` playbook is used.

Scrolling down, there are 2 lists of mutual indicators from the Phishing incidents that make up the campaign, and the Phishing incidents that are linked to the Phishing Campaign:
![image](https://user-images.githubusercontent.com/43602124/123635925-ec4fb100-d824-11eb-9599-1428c65a377b.png)

Another tab in the layout of the Phishing Campaign incident is the Campaign Management:
![image](https://user-images.githubusercontent.com/43602124/123636568-b232df00-d825-11eb-825f-5d95ba366152.png)

The management tab allows the analyst to take batch actions with ease.
The Phishing incidents are displayed at the top, and the columns shown are the same incident fields chosen in the `Detect & Manage Phishing Campaign` playbook's `fieldToDisplay` input - so the analyst can choose what they want to see about the related incidents.
Below that, in the "Incident Actions" section, the related incidents can be linked (happens automatically in the playbook by default), unlinked, closed and reopened.
Additionally, under the Notify Recipients section, the analyst can select incidents and the recipients from those incidents will be auto-populated to the "Campaign Email To" field. Then, the analyst can write an email and send it to the recipients directly from the layout.
