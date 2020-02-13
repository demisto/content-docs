---
id: become-a-tech-partner
title: Become a Technology Partner
---

_Intended Audience:_
Technical Alliances, Business Development, and Product Management Teams

Building Demisto integrations is easy and we welcome and encourage contributions from our customers and partners. If you are a Technology Partner and want to include your product among the Demisto supported integrations, there are a few requirements and steps that must be followed.

Understand all the benefits of becoming a Demisto Technology Partner [here](why-demisto)

# Requirements

As we aim to provide a smooth and seamless partner onboarding experience, we encourage you to review the following requirements and reach out to us for any doubts of clarification requests.

## Business requirements

While most of the work is technical, we have a few requirements on the business side:

- Identify and communicate your primary points of contact for business and technical/dev side (_Slack_ is our preferred channel of tech communications)
- Complete the Technical Partner Agreement (more details below)
- Support your integration with customers and enroll in TSA Net (see below)
- Provide our team with access to your product for our content testing purposes

## Technical requirements

If you are creating integrations for your products on Demisto, you will need a Python developer. While a great deal of automation content (Playbooks, Dashboards, Layouts, etc.), can be created for the platform without developers, building your own integration requires such a resource.

_At minimum you will need the following capabilities:_

- Intermediate knowledge of Python 3.x (including basic concepts of _linting_ and _unit testing_)
- A strong understanding of your product's capabilities
- A strong understanding of your product's APIs
- Access to your company's product and APIs
- An installed Demisto Platform (you can install it on-prem or cloud: we will provide the licenses)
- Access to GitHub
- _Optional_: basic knowledge of Docker, if you want to use your own libraries or pip modules

# Partner Onboarding Process

The following steps explain the process that you need to go through in order to become a Palo Alto Networks Technology Partner with Demisto, and start developing content and integrations that can be certified and deployed to customers globally. Please review the following with your team and work with your Demisto Technical Alliances contacts to get started.

## 1. Sign up as a Technology Partner

[Submit your application now!](https://start.paloaltonetworks.com/become-a-technology-partner) After your application is approved you’ll receive an email with a few resources to help you get started, and we'll reach out for a follow up.
<a class="button button--outline button--primary button--lg" href="https://start.paloaltonetworks.com/become-a-technology-partner" target="_blank">Sign Up Now</a>

## 2. Complete the technical partnership agreement

Prior to acceptance into the program, all partners must complete and sign our Technology Partner Program Agreement (TPA). You must identify in the TPA which of your product(s) you wish to have integrated with Demisto. Due to the large number of partners, we prefer to use our DocuSign to expedite the process. We'll reach out to arrange for signatures.
<a href="/assets/NextWaveTechnologyPartnerProgramAgreement.pdf" target="_blank" class="button button--outline button--primary button--lg">Download the partnership agreement here</a>

## 3. Identify the Use Cases

Once you're accepted in the program, we'll provide you access to a few resources, including our [Support Portal](https://support.demisto.com). We'll also reach out to schedule a 60 minute technical call to identify the use cases. We expect a representative of your technical team to be in the call. 
Typically the flow of the call is:
- General overview/demo of Demisto, its capabilities and integration requirements
- General overview/demo of your product(s)
- Open discussion on use cases

At the end of the call we will share a document template, already partially compiled, that outlines the scope of the integration. The document includes concepts such as:
- Use cases
- Commands/APIs used
- Input for commands
- Context output for commands
- Raw output for commands

We'll ask you to complete the document and submit back to us for review. We will be available for clarification and follow up conversations.


## 4. Build the Integration

Once the use cases document is approved, we will provide you with the Demisto licenses. We encourage you to identify the technical team and provide us their contacts so we can create accounts on our Support Portal and invite them in our Slack workspace. We will create a private Slack channel and invite your team as well as representatives of our engineering team.

We will also provide you a **Partner ID** that you will use during the GitHub submission process once the integration is complete.

We recommend your technical team review the docs on this site, and the following useful resources:
- Our [GitHub Content repository](https://github.com/demisto/content), and
- Demisto [Support Portal](https://support.demisto.com)
- [Demisto Platform Installation Guide](https://support.demisto.com/hc/en-us/sections/360001323614-Installing-Demisto)
- [Slack](https://www.demisto.com/community/) #demisto-integrations-help
- [GitHub](https://github.com/demisto/content/#demisto-platform---content-repository)
- [Demisto Concepts, and Terminology](https://support.demisto.com/hc/en-us/articles/360005126713-Demisto-Components-Concepts-and-Terminology)
- [Demisto Getting started video tutorial](https://youtu.be/bDntS6biazI)

Please reach out on Slack if you need any technical assistance or guidance. Follow the [Getting Started Guide](getting-started-guide) to understand all the requirements and components.

At a minimum, an integration consists in:
- The Python code that connects to your product(s)
- Metadata that defines inputs/outputs/descriptions/etc.
- A logo, appropriate, category, and all integration information defined
- Auto generated Integration documentation
- Documentation for customers on how to use the integration
- Python Unit test(s) for automated testing
- Ability to test the integration, build test playbooks, and use the integration from the CLI
- A couple of example playbooks to showcase how your your integration could be used

## 5. Provide our team with product access

As an automation platform, it shouldn’t surprise you that we’ve also automated our integration testing and deployment. We do nightly tests of each integration in order to confirm functionality and, in order to do this, we require access to your product and/or APIs. Preferably, the instance will have all data related to the integration use cases, so they can be tested. E.g. if one of the use cases is ingesting incidents to Demisto, the instance should have demo incidents. This access is not used for any other purpose.

Before submitting the integration, please work with the Palo Alto Networks BD Team to share access

## 6. Submit a GitHub pull request

Once you have completed development of your content or integration, please submit a *Pull Request* on our GitHub Content Repo. The title of the Pull Request must contain the *Partner ID* we provided earlier.

After the PR is submitted, it will require a review session with the development team. When the review of your integration is complete, check your code into our GitHub repository. Your build will added to be published to our global community. We release content updates every two weeks.

## 7. Join TSANet

To have their integrations approved and shipped with the Demisto Content, we require our partners to join the industry-standard support framework called TSANet in order to deliver outstanding support to our mutual customers. It’s free when you register under the Palo Alto Networks account, and it really streamlines the cross-company processes. [Sign Up For TSANet](https://paloaltonetworks-nextwave.connect.tsanet.org/).

## 8. Get the word out

Now that the integration is complete, you'll get the visibility you deserve! Our BD team will connect you to our Marketing team to work together on content, such as Solution Briefs, Blog posts, YouTube videos, etc.
