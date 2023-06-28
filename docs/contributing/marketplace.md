---
id: marketplace
title: Contributing Through Cortex XSOAR Marketplace
---

Marketplace is the central location for installing, exchanging, contributing, and managing all of your content, including playbooks, integrations, automations, fields, layouts, and more. For more information, you can read all about the [Marketplace](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/6.11/Cortex-XSOAR-Administrator-Guide/Marketplace-Overview).

This article walks you through the process of contributing content from the Cortex XSOAR Server to the Marketplace. This flow is meant to ease and speed up the contribution process for individual contributors who are not fully familiar with GitHub and how the Pull Request process works. Technology Partners should not use this flow and submit their Packs via a [GitHub Pull Request](checklist#pull-request-checklist).  

## Submit a Content Pack

1. Contribute your content pack from Cortex XSOAR. For more information, see [Contribute a Content Pack](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/6.11/Cortex-XSOAR-Administrator-Guide/Content-Pack-Contributions).

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
          5. Given a version number MAJOR.MINOR.REVISION, select _Update Type_:
                 1. **Revision** when you make backwards compatible bug fixes.
                 2. **Minor** when you add functionality in a backwards compatible manner.
                 3. **Major** when you make incompatible API changes or revamping the pack by adding to it a lot of new backwards compatible functionality.
                 4. **Documentation** when only documentation files were updated.

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


## Resubmit a Content Pack

If you have already submitted your contribution and you would like to make changes to the submission, you can do so by resubmitting the content pack from XSOAR. The resubmission process is very similar to the initial submission, the difference being you update an existing pull request instead of creating one.

1. Create or edit any content items need to be included in your contribution.

2. Go to **Marketplace** > **Contributions**, select your pack and click **Edit**.

3. Add or remove content items from the pack, as needed.

4. Click **Save and Contribute** and complete the form as documented [above](#submit-a-content-pack).
 
   **Note**: Changing the pack name or the email of the contributor at this stage will result in creating a pull request on GitHub, rather than updating the existing one.
   
   In the form you may include notes describing the essence of the update, or an updated demo video link, which will be displayed in a comment on the pull request after the changes are successfully pushed to GitHub.

5. Once the changes are pushed to your branch, you will receive an notification via email.


## Notes

* In addition to the resubmission option described above, there are other ways to update a content pack that you contributed and is already on a GitHub pull request: you may either modify the files directly on the pull request, or close the pull request and create a new contribution that includes your changes (not recommended).

* The contribution mode selection dropdown will only appear if content items that were part of your contribution were detected as originating from existing sources (for example, you created a new automation in the UI by clicking "Duplicate Automation").

## Known Limitations

* Updating JavaScript integrations/scripts in an existing pack is not supported.
