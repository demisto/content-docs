---
id: get-started
title: The Process To Get Started
---

_Intended Audience:_
Technical Alliances, Business Development, and Product Management Teams

The following guide explains the process that you need to go through in order to get started developing content and integrations that can be certified and deployed to customers globally. Please review the following with your team to get started developing content and integrations for the Demisto platform.

## 1. Sign up as a content development partner

<a href="https://start.paloaltonetworks.com/become-a-technology-partner" target="_blank">Submit your application now!</a> After your application is approved you’ll receive an email with resources to help you get started. Once you receive it, we recommend you review the resources including the docs here, our GitHub repository, and Support Portal to assist you in content development.
<a class="button" href="https://start.paloaltonetworks.com/become-a-technology-partner" target="_blank">Sign Up Now</a>

## 2. Complete the technical partnership agreement

Prior to acceptance into the program, all partners must complete and sign our Technology Partner Program Agreement (TPA). You must identify in the TPA which of your product(s) you wish to have integrated with Demisto. We'll reach out to arrange for signatures. <a href="/NextWaveTechnologyPartnerProgramAgreement.pdf" target="_blank" class="button">Download the partnership agreement here</a>

## 3. Identify technical resources

If you are creating integrations for your products you will want a Python developer to be available. While a great deal of content can be created for the platform without developers, building your own integration requires a resource.

_At minimum you will need the following capabilities:_

- Knowledge of Python (preferred) or JavaScript (you don't need to be an expert)
- A strong understanding of your product's capabilities
- A strong understanding of your product's APIs
- Access to your company's product and APIs
- An installed Demisto Platform (on-prem or cloud)
- Access to GitHub
- Optional: Docker if you want to use your own libraries or pip modules

## 4. Get access to Demisto platform

After your Palo Alto Networks Technical Partner Agreement (TPA) is completed, a license and a download link will be generated with instructions on installation.

_Make sure you have access to:_

- [The Palto Alto Networks Demisto Platform Installation Guide](https://support.demisto.com/hc/en-us/sections/360001323614-Installing-Demisto) (Login Required)
- [Support Articles](https://support.demisto.com)
- [Slack](https://www.demisto.com/community/) #demisto-integrations-help
- [GitHub](https://github.com/demisto/content/#demisto-platform---content-repository)

## 5. Get familiar with terminology and key concepts

Check out the following video to jump start you on building an integration. Then watch some videos on youtube and in our Support Portal.

- Youtube channel: https://www.youtube.com/channel/UCPZSycGbjGoIcTF6kudEilw
- Watch the following tutorial:

<iframe width="424" height="238" src="https://www.youtube.com/embed/bDntS6biazI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  
The platform has many different features and functionality components so we recommend reading about the different aspects of the terminology and concepts.

Read about the [Platform Architecture](https://www.demisto.com/demisto-enterprise-under-the-hood/)

_NOTE: Requires support center login access_

[Demisto Concepts, and Terminology](https://support.demisto.com/hc/en-us/articles/360005126713-Demisto-Components-Concepts-and-Terminology)

## 6. Create use cases

Document the use cases for your content or integration. We suggest you include the following information as part of the documentation:

- Use cases
- Commands used
- Input for commands
- Context output for commands
- Raw output for commands

## 7. Build your content or integration

Build away! Please reach out on Slack if you need any technical assistance or guidance. You’ll also create a sample playbook or two to demonstrate actions and showcase your solution.

- Full documentation for writing an integration in Demisto can be found in the Demisto Content GitHub repository: https://github.com/demisto/content
- The integration should be written in Python. If communication with your product API requires some third-party libraries, then python is a more convenient language to use.
- Documentation about the contribution process that can be found in our repository https://github.com/demisto/content/blob/master/CONTRIBUTING.md.

## 8. Create a test playbook

Build a test playbook that tests out a use case (or more) for the integration. To check out sample playbooks, go to the ‘Playbooks’ tab from within the Demisto product or access the GitHub library.

Why create a test playbook? [See examples](https://github.com/demisto/content/tree/master/Playbooks)

- When we build our content packages, we automate the testing of the integrations.
- The test playbooks enable our team to review the command input and outputs.
- Test playbooks help determine additional use cases for your products.

## 9. Document your content or integration

Documentation for the integration can be generated automatically by using this script located in [GitHub](https://github.com/demisto/content/blob/master/docs/integration_documentation/README.MD), then fill in the blanks such as overview. The documentation will appear in Support articles.

## 10. Joint review

Once you’re done testing and developing your integration, <a href="mailto:mchase@paloaltonetworks.com">email us</a> or join the <a href="https://www.demisto.com/community/" target="_blank">Demisto Community</a>. Send a note to #demisto-integrations-help channel so our team can do a quick review session with you to see what you’ve built.

## 11. Submit a GitHub pull request

Once you have completed development of your content or integration, it will require a review session with the development team. When the review of your integration is complete, check your code into our GitHub repository. Your build will added to be published to our global community. We release content updates every two weeks.

- Read the documentation for the contribution process: https://github.com/demisto/content/blob/master/CONTRIBUTING.md.
- Open a pull request and submit yaml files for any content, integrations and the sample playbooks for validation.
- Minimum Requirements:
  - Defined Use Cases
  - For integrations, auto documentation must be generated
  - A test playbook for the product integration that shows that it works
  - All inputs, outputs, and parameters must be defined and documented in the integration
  - A logo, appropriate, category, and all integration information defined
  - Ability to test the integration, build test playbooks, and use the integration from the CLI
  - Documentation for customers on how to use the integration

## 12. Provide our team with product access

As an automation platform, it shouldn’t surprise you that we’ve also automated our integration testing and deployment. We do nightly tests of each integration in order to confirm functionality and, in order to do this, we require access to your product and/or APIs. Preferably, the instance will have all data related to the integration use cases, so they can be tested. E.g. if one of the use cases is ingesting incidents to Demisto, the instance should have demo incidents. This access is not used for any other purpose.

- Work with the Palo Alto Networks BD Team to share access
- Work with the Dev team to make sure they have access to your products for testing the content and integration

## 13. Join TSANet

We require our partners to join the industry-standard support framework called TSANet in order to deliver outstanding support to our mutual customers. It’s free when you register under the Palo Alto Networks account, and it really streamlines the cross-company processes. <a href="https://paloaltonetworks.tsanet.org" target="_blank">Sign Up For TSANet</a>
