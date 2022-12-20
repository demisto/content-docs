---
id: sla
title: Contribution SLA
---

This is a Service Level Agreement (SLA) between the contributor and the Cortex XSOAR Content team. This document identifies the services required and the expected level of services.

#### There are three options for contributing content to the Cortex XSOAR marketplace:

   1. Contribute from the Cortex XSOAR UI - for more information please see [Contributing through the Marketplace](../contributing/marketplace).
   
   2. Contribute through a GitHub Pull Request on the public [XSOAR Content Repository](https://github.com/demisto/content) - for more information please see [Contributing docs](../contributing/contributing#how-to-contribute).

   3. Contribute through a private GitHub repository: this is required if you are providing a **Premium** (aka Paid) Content Pack - for more information please see [here](../packs/premium_packs).
   

In each of the above options, the review phase will begin with the **opening of the GitHub Pull Request** containing your content changes.

#### Once your PR is open, the XSOAR content team commits to the following:

   1. A reviewer will be assigned to your PR within an **hour** after opening it.
   
   2. Your reviewer will publish his initial response to your changes within **5 business days**.
   
   3. If requested, after the needed changes were done, and a corresponding message in the pull request was posted - your reviewer will respond within **3 business days**. Note, you might have a couple of such fixes rounds, the above holds for each of them.
   
   4. Your reviewer will be available for any questions during the review process - you can contact him on the PR itself or on slack (DFIR community).
   
   5. Once your PR is approved and merged by your reviewer, an **internal PR** including your changes will be opened within an **hour**.
    The internal PR allows us to run our internal validity and security checks on your final code. 
   
   6. Once the **internal PR is merged** your changes will be published in the XSOAR marketplace within **3 business days**.



#### In order for the contribution process to be successful, the XSOAR content team requires the contributors the following:

   1. Provide the XSOAR content team with as much information as possible about the changes you made or about the new content you created.
        * If you contributed through the XSOAR UI, please provide this information in your **UI contribution form**.
        * If you contributed through a GitHub Pull Request, please add this information in the PR body (fill in the template). 
   
   2. If you contributed through a GitHub Pull Request make sure to register your contribution by filling out the **contribution registration form**, and sign the **CLA** ([Contributor License Agreement](https://github.com/demisto/content/blob/master/docs/cla.pdf)).
      **The review process won't start if those forms remain unfilled**.
      
      Links to the Contribution registration form and to the CLA will appear on your PR:
      
      ![contribution-registration-form](/doc_imgs/contributing/contribution-registration-form.png)
      
      ![CLA](/doc_imgs/contributing/failed_CLA.png)
      
      
   3. Providing the XSOAR content team with a recorded demo session that demonstrates your changes is much appreciated and will speed up the review process.
        * If you contributed through the XSOAR UI, please provide a link to the recorded session in the redirected UI contribution form.
        * If you contributed through a GitHub Pull Request, please provide it in the **contribution registration form**.
   
   4. Please check the status of the build of your PR once it is completed - If the build includes errors, please try to solve them - for more information about the build process please see [the-build-process](../contributing/conventions#the-build-process).
   
   5. During the review process monitor your PR - your reviewer will add comments to the Pull Request, asking questions and requesting changes. In order to establish a decent review process for your contribution, you are kindly asked to respond to the reviewer's code review and apply the required changes within **14 days**.
      **Stale Pull Requests might be closed**.
    
   6. In some cases, your reviewer will ask you to schedule a meeting to see an interactive demo. Make sure you have a working installation of Cortex XSOAR with your most recent pack version (including all review comments) fully configured. Check out our [Contribution Demo Page](../contributing/demo-prep) for more details.
   
   
 
While the XSOAR content team strives to merge and publish your changes as quickly as possible, the duration of the review process depends on many factors such as the level of support of the edited content pack, the amount and complexity of your changes, and various validations and security tests.
Please understand and be patient.

