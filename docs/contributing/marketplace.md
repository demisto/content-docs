---
id: marketplace
title: Contributing via Cortex XSOAR
---

Cortex XSOAR v6.0 introduces a Marketplace which is the central location for installing, exchanging, contributing, and managing all of your content, including playbooks, integrations, automations, fields, layouts, and more. For more information, you can read all about the [Marketplace](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/marketplace/marketplace-overview.html).

This article walks you through the process of contributing content from the Cortex XSOAR Server to the Marketplace. This flow is meant to ease and speed up the contribution process for individual contributors who are not fully familiar with GitHub and how the Pull Request process works. Technology Partners should not use this flow and submit their Packs via a [GitHub Pull Request](checklist#pull-request-checklist).  

## Submit a Contribution

1. Contribute your content entity from Cortex XSOAR. For more information, see [Contribute a Content Pack](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-1/cortex-xsoar-admin/marketplace/content-pack-contributions.html).

2. After you contribute the content entity a message displays explaining that your contribution is ready for review, and includes a link to a form you need to fill in to complete your contribution. You will receive an email with a link to the form.

3. Completing the form

   ### **Contribute a New Pack**  

      These instructions are only intended for creating a new pack. If you have a pack that you need to update, follow the instructions in the _Contribute to an Existing Pack_ section.
      
          1. Select "Create New Pack" from the "Select Contribution Mode" dropdown.
          2. Fill in additional details, such as, pack name, author, and description.
          3. Log in to your GitHub account so you can participate in the review process of the pull request that will be opened for your content pack.
          4. Sign the [Palo Alto Networks Contributor License Agreement](https://github.com/demisto/content/blob/master/docs/cla.pdf).

   ### **Contribute to an Existing Pack**
   You can contribute new entities or update existing entities for an existing pack.
   
         1. Select "Update Existing Pack" from the "Select Contribution Mode" dropdown.
         2. Select the pack that you wish to update from the "Select Existing Pack" dropdown.
         3. Log in to your GitHub account so you can participate in the review process of the pull request that will be opened for your content pack.
         4. Sign the [Palo Alto Networks Contributor License Agreement](https://github.com/demisto/content/blob/master/docs/cla.pdf).

   
	_Contribute an update to an existing content entity_: Duplicate the entity you want to update. For example, if you want to update the `AbuseIPDB` integration, you need to duplicate it  and save the duplicate with your changes as `AbuseIPDB_copy`.
	

4. After you submit the form you will be redirected to a page that informs you that your contribution was received and is being processed.  

5. A GitHub branch will be created in the [xsoar-contrib Content repository fork](https://github.com/xsoar-contrib/content) with the changes from your contribution.

6. You will receive an invitation to join the **xsoar-contrib** organization. Being a member of the organization enables the **xsoar-bot** to invite you to a GitHub team and grant you write permissions to the created branch.

7. The pull request is created and a reviewer is assigned.

    The documentation for new integration/script/playbook is automatically generated and contains the basic information of it.
    You will now need to review the documentation (README.md) and modify it according to XSOAR standards.
    The files to be reviewed will be listed at the pull request comment.
    See the [Documentation article](https://xsoar.pan.dev/docs/documentation/readme_file) for more information.

8. You can now modify the files changed in the pull request as part of the review process.


## Resubmit a Contribution

If you have already submitted your contribution and you would like to make changes to the submission, you can do so by resubmitting the content pack from XSOAR. The resubmission process is very similar to the initial submission, the difference being you update an existing pull request instead of creating one.
      
      1. Create or edit any content items that need to be included in your contribution.

      2. Go to **Marketplace** > **Contributions**, select your pack and press "Edit".

      3. Add or remove content items from the pack, as needed.

      4. Press **Save and Contribute** and complete the form as documented [above](#submit-a-content-pack).

         **Note**: Changing the pack name or the email of the contributor at this stage will result in creating a pull request on GitHub, rather than updating the existing one.

         In the form you may include notes describing the essence of the update, or an updated demo video link, which will be displayed in a comment on the pull request after the changes are successfully pushed to GitHub.

      5. Once the changes are pushed to your branch, you will receive a notification via email.


In addition, there are other ways to update a content pack that you contributed and is already on a GitHub pull request: you may either modify the files directly on the pull request, or close the pull request and create a new contribution that includes your changes.

 
## Known Limitations

1. Updating JavaScript integrations/scripts in an existing pack is not supported.
2. Resubmit changes to an existing content pack is not supported.
