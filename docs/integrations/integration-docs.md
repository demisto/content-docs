---
id: integration-docs
title: Integration Documentation
---

Documentation is a critical step that assists customers who may use your integration by providing insight into how the integration is supposed to work. From creating custom playbooks, to providing background information to assist in debugging, it is important to ensure that the documentation explains every aspect of the integration. Documentation is maintained as `README.md` per integration/automation/playbook and made available for customers as part of the [reference docs](https://xsoar.pan.dev/docs/reference/index) of the Cortex XSOAR Developer Hub.

**Note:** The documentation must conform to the [Integration Doc Format](doc-structure).


## Creating Documentation
Within Cortex XSOAR, exists the ability to generate documentation for your integration. First verify that the DocumentationAutomation script exists in your content by navigating to the **Automation** tab in Cortex XSOAR.

First, take the YAML file of your integration and upload it to the War Room. Please note the entry ID as you will need it in the next step.

To use the DocumentationAutomation script, navigate to the War Room and execute the command:
 ```
!DocumentationAutomation entryID="the_entry_id_of_the_uploaded_yml_integration"
```
You may choose to include the other arguments depending on what you may need.

Once the command has been executed, you will see the documentation html in the War Room as a new entry and a copy of it as a file entry. Review the generated document.

Where there is missing information, be sure to fill out the document completely. It is advised to include use-cases, screenshots, and examples of the context. 

## Documentation _must_ be generated if:
1.  If the integration is new then you are required to create new documentation.
2.  If the integration is existing but missing documentation then please create new documentation.
3.  If the integration is existing and some of the integration has changed. For example, a new command was added, context was changed, or anything else; please update the documentation.


## Using commands parameter
To automatically generate example output (human readable and context), you should create a text file containing command examples, one per line. The command examples should appear the same way they would as in the CLI in Cortex XSOAR, for example `!url url=8.8.8.8`.
Commands will be executed one at a time, in the order in which they appear in the file. If there are duplicates of a command included in the text file, only the output of the command's first execution  will be included in the generated documentation output.

Example for commands file:
```
!ip ip=8.8.8.8
!domain domain=demisto.com
```

![ScreenRecording2019-09-22at16241](../doc_imgs/integrations/65404184-313ced00-dde0-11e9-9257-e61e2943fd75.gif)


## Documentation Examples

* [Microsoft Graph Groups](https://github.com/demisto/content/blob/master/Integrations/MicrosoftGraphGroups/README.md): Shows how the commands and examples should be presented.
* [Slack v2](https://github.com/demisto/content/blob/master/Packs/Slack/Integrations/Slack/README.md): Shows an example of the troubleshooting section.

Example Images: 

![image](../doc_imgs/integrations/40935346-7ca3b24a-6840-11e8-8540-b00677cd6657.png)
![image](../doc_imgs/integrations/40935354-8406dcc4-6840-11e8-9b0c-b0a9c4bd8a99.png)


## Posting Documentation
The documentation should be posted in the integration/automation script directory as a `README.md` file. If the integration/automation is not in the [Directory Structure](package-dir), name the documentation file the same as the yml file without the `.yml` extension and with an ending of: `_README.md`. For example: [integration-mcafeeDam_README.md](https://github.com/demisto/content/blob/master/Integrations/integration-mcafeeDam_README.md).

## Documentation Deployment
Once the PR with the documentation README file is merged in to master, it will trigger an update to the Cortex XSOAR Developer Hub. When the deployment is complete the documentation will be available at the [reference docs section](https://xsoar.pan.dev/docs/reference/index). If you wish to preview how the documentation looks at the Developer Hub, before merging to master, you can create a PR at the [content-docs repo](https://github.com/demisto/content-docs) with the same branch name as the PR you are working on in the [content repo](https://github.com/demisto/content-docs). Mention in the PR that it is related to a PR from the content repo. Your PR in the content-docs repo will include a preview link in the GitHub Checks section from `deploy/netlify`. You can perform a dummy white space change for the PR that will re-trigger the build and create a new preview. Example screenshot for preview link:

<img src="../doc_imgs/integrations/doc-preview-check.png" width="500" ></img>

## Notes
We use [MDX](https://mdxjs.com/) for the Markdown generation. MDX is a superset of standard Markdown, but it requires that any html used in the document must be jsx complaint. Meaning all html tags need to contain a closing tag. For example don't use: `<br>`, use: `<br/>`. Additionally, html entities `< >`, not in code blocks, need to be encoded. Use `&lt;` and `&gt;` to encode.
