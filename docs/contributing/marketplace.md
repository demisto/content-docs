---
id: marketplace
title: Contributing via Cortex XSOAR
---

Cortex XSOAR v6.0 introduces a Marketplace which is the central location for installing, exchanging, contributing, and managing all of your content, including playbooks, integrations, automations, fields, layouts, and more. For more information, you can read all about the [Marketplace](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/marketplace/marketplace-overview.html).

This article walks you through the process of contributing content from the Cortex XSOAR Server to the Marketplace. This flow is meant to ease and speed up the contribution process for individual contributors who are not fully familiar with GitHub and how the Pull Request process works. Technology Partners should not use this flow and submit their Packs via a [GitHub Pull Request](checklist#pull-request-checklist).  

## Submit a Content Pack

1. Contribute your content pack from Cortex XSOAR. For more information, see [Contribute a Content Pack](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/marketplace/content-pack-contributions.html).

2. After you contribute the content pack a message displays explaining that your contribution is ready for review, and includes a link to a form you need to fill in to complete your contribution. You will receive an email with a link to the form.

3. Completing the form

   1. **Create a New Pack**  

          These instructions are only intended for creating a new pack. If you have a pack that you need to update, follow the instructions in the _Update an Existing Pack_ section.

          1. Fill in additional details, such as, pack name, author, and description.
          2. Log in to your GitHub account so you can participate in the review process of the pull request that will be opened for your content pack.
          3. Sign the [Palo Alto Networks Contributor License Agreement](https://github.com/demisto/content/blob/master/docs/cla.pdf).

   2. **Update an Existing Pack**

          If your contribution is an update to an existing pack, complete the following steps. (See _[Notes](#notes)_ for more information regarding updating an existing pack.) 

          1. Select _Update Existing Pack_ from the _Select Contribution Mode_ dropdown.
          2. Select the pack that you wish to update from the _Select Existing Pack_ dropdown.
          3. Log in to your GitHub account so you can participate in the review process of the pull request that will be opened for your content pack.
          4. Sign the [Palo Alto Networks Contributor License Agreement](https://github.com/demisto/content/blob/master/docs/cla.pdf).


4. After you submit the form you will be redirected to a page that informs you that your pack was received and is being processed.  

5. A GitHub branch will be created in the [xsoar-contrib Content repository fork](https://github.com/xsoar-contrib/content) with the changes from your contribution.

6. You will receive an invitation to join the **xsoar-contrib** organization. Being a member of the organization enables the **xsoar-bot** to invite you to a GitHub team and grant you write permissions to the created branch.
(Each contributor can only modify files in content packs that they contributed).

7. The pull request is created and a reviewer is assigned.

    The documentation for new integration/script/playbook is automatically generated and contains the basic information of it.
    You will now need to review the documentation (README.md) and modify it according to XSOAR standards.
    The files to be reviewed will be listed at the pull request comment.
    See the [Documentation article](https://xsoar.pan.dev/docs/documentation/readme_file) for more information.

8. You can now modify the files changed in the pull request as part of the review process.


### Notes

1. There are two options for updating a content pack that you contributed and which is already in the GitHub pull request process, you will need to either modify the files directly in the pull request created in GitHub directly or close the pull request and create a new contribution including your changes.
2. The contribution mode selection dropdown will only appear if content items that were part of your contribution were detected as originating from existing sources (for example, you created a new automation in the UI by clicking "Duplicate Automation").
3. When updating an existing pack, the pack options are determined and populated by the content items included in your contribution. For example, if you were to duplicate the `AbuseIPDB` integration and save the duplicate with your changes as `AbuseIPDB_copy`. **Note**: the default name applied to duplicated content appends `_copy` to the original name. This is important because it indicates to us that this most likely contains a modification to existing content. In our example, the pack to which the `AbuseIPDB` integration belongs, `AbuseIPDB`, will appear as an option in the dropdown for updating content.


## Resubmit a Content Pack

If you have already submitted your contribution and you would like to make changes to the submission, you can do so as follows:

1. Create or edit any content items need to be included in your contribution.

2. Go to **Marketplace** > **Contributions**, select your pack and press "Edit".

3. Add or remove content items from the pack, if needed.

4. Press **Save and Contribute** and complete the form as documented [above](#submit-a-content-pack).
 
   **Note**: Changing the pack name or the email of the contributor at this stage will result creating a new pull request on GitHub, rather than updating the existing one.
   
   In the form you may include notes describing the essence of the update, or an updated demo video link, which will be displayed in a comment on the pull request after the changes are successfully pushed to GitHub.

5. Once the changes are pushed to your branch, you will receive an notification via email.
