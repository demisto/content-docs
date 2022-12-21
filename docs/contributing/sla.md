---
id: sla
title: Contribution SLA
---

This is a Service Level Agreement (SLA) between the contributor (the Contributor) and the Cortex XSOAR (XSOAR) Content team. This document identifies the services required and the expected level of services.

#### Options for contributing content to the Cortex XSOAR Marketplace:

   1. Contribute from the Cortex XSOAR UI - for more information, see [Contributing through the Marketplace](../contributing/marketplace).
   
   2. Contribute through a GitHub Pull Request on the public [XSOAR Content Repository](https://github.com/demisto/content) - for more information, see [Contributing docs](../contributing/contributing#how-to-contribute).

   3. Contribute through a private GitHub repository: this is required if you are providing a **Premium** (Paid) Content Pack - for more information, see [Premium packs](../packs/premium_packs).
   

In each of the above options, the review phase begins with the **opening of the GitHub Pull Request** containing your content changes.

#### XSOAR content team commitments
Once your PR is open, the XSOAR content team commits to the following:
   1. After opening the PR, a reviewer will be assigned to your PR within an **hour**.
   
   2. Your reviewer will publish the initial response to your changes within **5 business days**.
   
   3. If you are asked to make changes, you need to make those changes, and add a corresponding message in the pull request. Your reviewer will respond within **3 business days**. Note: You might have a few rounds of fixes. These commitments are the same for each round.
   
   4. Your reviewer will be available for any questions during the review process - you can contact them on the PR itself or on slack ([DFIR Slack Community](https://start.paloaltonetworks.com/join-our-slack-community)).
   
   5. Once your PR is approved and merged by your reviewer, an **internal PR** including your changes will be opened within an **hour**.
    The internal PR allows us to run our internal validity and security checks on your final code. 
   
   6. Once the **internal PR is merged**, your changes will be published in the Cortex XSOAR Marketplace within **3 business days**.



#### The Contributor Commitments:

For the contribution process to be successful, the XSOAR content team requires the Contributors to do the following:
   1. Provide the XSOAR content team with as much information as possible about the changes made or about the new content you created.
        * If you contributed through the XSOAR UI, you need to provide this information in your **UI contribution form**.
        * If you contributed through a GitHub Pull Request, add this information in the PR body (fill in the template). 
   
   2. If you contributed through a GitHub Pull Request you need to register your contribution by filling out the **contribution registration form**, and sign the **CLA** ([Contributor License Agreement](https://github.com/demisto/content/blob/master/docs/cla.pdf)).
      **The review process won't start if those forms remain unfilled**.
      
      Links to the Contribution registration form and to the CLA will appear on your PR:
      
      ![contribution-registration-form](/doc_imgs/contributing/contribution-registration-form.png)
      
      ![CLA](/doc_imgs/contributing/failed_CLA.png)
      
      
   3. Providing the XSOAR content team with a recorded demo session that demonstrates your changes is much appreciated and will speed up the review process.
        * If you contributed through the XSOAR UI, provide a link to the recorded session in your **UI contribution form**.
        * If you contributed through a GitHub Pull Request, provide it in the **contribution registration form**.
   
   4. Please check the status of the build of your PR once it is completed. If the build includes errors, please try to solve them - for more information about the build process, see [the-build-process](../contributing/conventions#the-build-process).
   
   5. During the review process monitor your PR. Your reviewer will add comments to the PR, asking questions and requesting changes. To establish a decent review process for your contribution, you are kindly asked to respond to the reviewer's code review and apply the required changes within **14 days**.
      **Stale Pull Requests might be closed**.
    
   6. In some cases, your reviewer will ask you to schedule a meeting to see an interactive demo. Ensure you have a working installation of Cortex XSOAR with your most recent content pack version (including all review changes) fully configured. Check out our [Contribution Demo Page](../contributing/demo-prep) for more details.
   
   
 
While the XSOAR content team strives to merge and publish your changes as quickly as possible, the duration of the review process depends on many factors such as the level of support of the edited content pack, the amount and complexity of your changes, and various validations and security tests.
Please understand and be patient.

