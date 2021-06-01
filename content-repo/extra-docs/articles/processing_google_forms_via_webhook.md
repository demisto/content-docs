---
id: google-forms-cortex-xsoar
title: Processing your Google Form responses in Cortex XSOAR via webhook
description: Connecting Google Forms with Cortex XSOAR.
---

Imagine you have a Google form for some purpose, and you want to run some logic with different services upon form submission.
As you might know, Google provides an IDE to run some code that is bounded to the form. This service is called [Google Apps Script](https://developers.google.com/apps-script).
But combining various kinds of services can be frustrating. You can use Cortex XSOAR to make this process a lot easier.

For instance, see the following architecture:

<img src="../../../docs/doc_imgs/reference/google-forms-cortex-xsoar.png" width="700"></img>

### To implement the above flow, do the following things:

1. Create a Google form that will provide the information you need.

2. In Cortex XSOAR, create an incident type that represents the Google form use case. Add a layout, mapper, classifier, etc...

3. Create a designated playbook to run when the incident is created.

4. Download the [Generic Webhook Pack](https://xsoar.pan.dev/docs/reference/integrations/generic-webhook) and configure an instance of the integration. For example, you can call the instance: *GenericWebhookForm*.

5. Create a Google Apps Script for the selected form. See [Creating a project from Google Docs, Sheets, or Forms](https://developers.google.com/apps-script/guides/projects#creating_a_project_from_google_docs_sheets_or_forms) for more information.

6. Add the `https://www.googleapis.com/auth/script.external_request` scope to your *appsscript.json* file. See [this](https://developers.google.com/apps-script/concepts/scopes) for more information.

7. Add the following generic code to a file in a script editor. (Replace the username, password, and URL with the values from the Generic Webhook integration):
  ```
   function atFormSubmit(e) {
    var formResponse = e.response;
    var itemResponses = formResponse.getItemResponses();
    var formData = {};
    for (var i = 0; i < itemResponses.length; i++) {
      var itemResponse = itemResponses[i];
      var key = itemResponse.getItem().getTitle();
      var value = itemResponse.getResponse();
      formData[key] = value;
      Logger.log('Response to the question "%s" was "%s"', key, value);
    }
    sendPostRequestToXSOAR(formData);
  }
  function sendPostRequestToXSOAR(formData) {
    var body = {name: "New response to the form $FORM_NAME", raw_json: formData};
    var username = $USERNAME;
    var password = $PASSWORD;
    var url = $URL;
    var params = {
      method: "POST",
      payload: JSON.stringify(body),
      validateHttpsCertificates: false,
      muteHttpExceptions: true,
      contentType: "application/json",
      headers: {"Authorization": "Basic " + Utilities.base64Encode(username + ":" + password)}
    };
    var response = UrlFetchApp.fetch(url, params);
    Logger.log('Response code "%s": ', response.getResponseCode());
    Logger.log('Response content "%s": ', response.getContentText());
  }
  ```

  8. Add an [on Submit trigger](https://developers.google.com/apps-script/guides/triggers) to the context of the form and choose the *atFormSubmit* function to run when the form is submitted.
  9. You can debug your work in the [Executions Feature](https://developers.google.com/apps-script/guides/v8-runtime?hl=en#view_executions).

That's it, now every form submission will be reflected and managed by your playbook in Contex XSOAR.