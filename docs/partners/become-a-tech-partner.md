---
id: become-a-tech-partner
title: Become an XSOAR Partner
---

_Intended Audience:_
Technical Alliances, Business Development, and Product Management Teams

Building Cortex XSOAR integrations is easy and we welcome and encourage contributions from our customers and partners. If you are a Technology Partner and want to include your product among the Cortex XSOAR supported integrations, there are a few requirements and steps that must be followed.

Understand all the [benefits](why-xsoar) of becoming a Cortex XSOAR Technology Partner. 

# Requirements

As we aim to provide a smooth and seamless partner onboarding experience, we encourage you to review the following requirements and reach out to us for any doubts of clarification requests.

## Business requirements

While most of the work is technical, we have a few requirements on the business side:

- Identify and communicate your primary points of contact for business and technical/dev side (_Slack_ is our preferred channel of tech communications)
- Complete the Technical Partner Agreement (more details below)
- Support your integration with customers and enroll in TSANet (see below)
- Provide our team with access to your product for our content testing purposes

## Technical requirements

If you are creating integrations for your products on Cortex XSOAR, you will need a Python developer. While a great deal of automation content (Playbooks, Dashboards, Layouts, etc.), can be created for the platform without developers, building your own integration requires such a resource.

_At minimum you will need the following capabilities:_

- Intermediate knowledge of Python 3.x (including basic concepts of _linting_ and _unit testing_)
- A strong understanding of your product's capabilities
- A strong understanding of your product's APIs
- Access to your company's product and APIs
- An installed Cortex XSOAR Platform (you can install it on-prem or cloud: we will provide the licenses)
- Access to GitHub
- _Optional_: basic knowledge of Docker, if you want to use your own libraries or pip modules

# XSOAR Partner Onboarding Process

The following steps explain the process that you need to go through in order to become a Palo Alto Networks Technology Partner with Cortex XSOAR, and start developing content and integrations that can be certified and deployed to customers globally. Please review the following with your team and work with your Cortex XSOAR <a href="mailto:soar.alliances@paloaltonetworks.com">Partner Success Team</a> to get started.

## 1. Sign up as an XSOAR Technology Partner

Submit your application now! After your application is approved you’ll receive an email with a few resources to help you get started, and we'll reach out for a follow up.
<a class="button button--outline button--primary button--lg" href="https://technologypartners.paloaltonetworks.com/English/register_email.aspx" target="_blank">Sign Up Now</a>

## 2. Complete the Technical Partnership Agreement

Prior to acceptance into the program, all partners must complete and sign our Technology Partner Program Agreement (TPA). You must identify in the TPA which of your product(s) you wish to have integrated with Cortex XSOAR. Due to the large number of partners, we prefer to use our DocuSign to expedite the process. We'll reach out to arrange for signatures.

## 3. Take Required Training

We require our Partners to take training classes at the Palo Alto Networks Beacon Learning Center prior to beginning development. 

1. [Cortex XSOAR: Analyst Training](https://beacon.paloaltonetworks.com/student/path/642715-cortex-xsoar-analyst-training?sid=31172842&sid_i=2) (3hrs)

1. [Cortex XSOAR: SOAR Engineer Training](https://beacon.paloaltonetworks.com/student/collection/666206/path/741516) (3hrs)

Create a free account with your business email address and search by title to enroll instantly. (Note: you must use your business email to ensure accurate reporting and tracking.)

Additional optional video resources include:
- [Recorded videos](office-hours) from previous office hours
- [Cortex XSOAR IT Administrator Training](https://beacon.paloaltonetworks.com/student/collection/666206/path/715595)


## 4. Identify and Document 

Once you're accepted in the program, we'll provide you links to a few resources, including our [Support Portal](https://docs.paloaltonetworks.com/). We'll also share a document template, already partially compiled, that outlines the scope of the integration. The document includes concepts such as:
- Use cases
- Commands/APIs used
- Input for commands
- Context output for commands
- Raw output for commands

We'll ask you to complete the document and submit back to us for review prior to starting to build. We will be available for clarification and follow up conversations.


## 5. Build the Integration

Once the use cases document is approved, we will provide you with the Cortex XSOAR licenses. We encourage you to identify the technical team and provide us their contacts so we can create accounts and invite them to our Slack workspace. 

We will also provide you a **Partner ID** that you will use during the GitHub submission process once the integration is complete.

We recommend your technical team review the docs on this site, and the following useful resources:
- Our [GitHub Content repository](https://github.com/demisto/content)
- Cortex XSOAR [Documentation](https://docs.paloaltonetworks.com/cortex/cortex-xsoar.html)
- Cortex XSOAR [Installation Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/installation.html)
- Our [Slack channel](https://start.paloaltonetworks.com/join-our-slack-community) #demisto-developers
- Cortex XSOAR [Concepts, and Terminology](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/cortex-xsoar-overview/cortex-xsoar-concepts)
- Cortex XSOAR [integration video tutorial](https://youtu.be/bDntS6biazI)

Please reach out on Slack if you need any technical assistance or guidance. Follow the [Getting Started Guide](../concepts/getting-started-guide) to understand all the requirements and components.

At a minimum, an integration consists in:
- The Python code that connects to your product(s)
- Metadata that defines inputs/outputs/descriptions/etc.
- A logo, appropriate, category, and all integration information defined
- Auto generated Integration documentation
- Documentation for customers on how to use the integration
- Python Unit test(s) for automated testing
- Ability to test the integration, build test playbooks, and use the integration from the CLI
- A couple of example playbooks to showcase how your your integration could be used

Here is an example of a timeline that shows a full development cycle for a pack

![Edi - Frame 1 (6)](https://user-images.githubusercontent.com/85438368/163706901-0de0171f-df61-4b4f-851b-dca35f8b827e.jpg)
![Edi - Frame 2 (2)](https://user-images.githubusercontent.com/85438368/163706921-f6edc411-8370-45d1-ac30-e9d41b65c6ac.jpg)


## 6. Submit a GitHub Pull Request

Once you have completed development of your content or integration, please [submit a Pull Request](/docs/contributing/contributing) on our GitHub Content Repo. You will be required to fill in a contribution form that includes details like your *Partner ID* and some other details.

After the PR is submitted, our development team will conduct a review. When the review of your integration is complete, your build will added to be published to our global community. We release content twice daily to Marketplace customers, and every two weeks for legacy customers.

## 7. Get the Word Out

Now that the integration is complete, you'll get the visibility you deserve! The Partner Success Team will connect you to our Marketing team to work together on content, such as Solution Briefs, Blog posts, YouTube videos, etc.

---

Partners who wish to contribute paid packs must follow a few [additional onboarding steps](/docs/partners/premium-packs-process). 
