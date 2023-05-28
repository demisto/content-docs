---
id: getting-started-guide
title: Getting Started Guide
---

This guide will provide you with some pointers to jumpstart your development journey. After reading it, you’ll have a great background for creating content for the Cortex XSOAR platform.  
If you have trouble with any of these items, please reach out for help over at our [Slack](https://start.paloaltonetworks.com/join-our-slack-community) on the `#demisto-developers` channel or.  
If you're a Technology Partner (or interested in becoming one), you can also contact us via the [Cortex XSOAR Alliance Email](mailto:soar.alliances@paloaltonetworks.com).
 
## Prerequisites and Resources
Cortex XSOAR is a powerful platform with a rich set of features and customizations.
Because of that, we recommend to go over the following resources before you start developing custom content:
1. Read and understand [Cortex XSOAR Concepts](../concepts/concepts).
2. Go over the [FAQ](../concepts/faq).
3. Register to the [Learning Center](http://education.paloaltonetworks.com/learningcenter) and go through the [Product Training section](../partners/become-a-tech-partner#3-take-required-training).
4. For server-related (non-content) documentations, refer to the [Cortex XSOAR Product Documentation Page](https://docs.paloaltonetworks.com/cortex/cortex-xsoar.html).
5. Access the Palo Alto Networks [DFIR Slack Community](https://start.paloaltonetworks.com/join-our-slack-community) and join the *#demisto-developers* channel.
6. Sign up to the [Developer Newsletter](https://start.paloaltonetworks.com/cortex-xsoar-developer-newsletter.html) to receive technical updates on developing and contributing.
7. If you plan to publish your content to the [Cortex XSOAR Marketplace](https://cortex.marketplace.pan.dev/marketplace) for other customers to use, read about the [Contribution](../contributing/contributing).
8. Obtain and install a copy of Cortex XSOAR. If you are not a partner, you can obtain the Community Edition [here](https://start.paloaltonetworks.com/sign-up-for-demisto-free-edition) for free. Installation instructions are available [here](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/installation.html).
9. If you are integrating with an external API, make sure you have API or SDK access to the product or solution you want to integrate with for testing purposes.

### Technology Partners
If you are or want to become a Technology Partner, we also recommend you to:
1. Read the [Become a Technology Partner](../partners/become-a-tech-partner) article, and follow the steps mentioned there to become a partner.
2. Work with the Cortex XSOAR Alliances Team ([email](mailto:soar.alliances@paloaltonetworks.com)) to make sure your use cases have been validated.

## Development Environment
:::tip
If you want to share your work the Cortex XSOAR Marketplace and make it available to other clients and users in the community
(either as a partner-supported, or a community-supported pack), refer to the [contribution](../contributing/contributing) article.
:::

### demisto-sdk
Whether you are using the XSOAR IDE or a full development environment, we have an official SDK that can help you with your development process.  
It can be used to upload, download and run code on XSOAR directly from your operating system shell.  
For more information, refer to the [demisto-sdk](../concepts/demisto-sdk) article.


### Basic XSOAR Environment
For creating / modifying content that's for personal use, or for a community contribution,
the basic [XSOAR IDE](../concepts/xsoar-ide) can be sufficient, and doesn't require setting up a special development environment.


### Full Development Environment
When making a large amount of changes, or developing new content, we recommend using a fully-fledged IDE like *Visual Studio Code* or *PyCharm* .  
For a tutorial on how to set up a full development environment, refer to the [Development Environment](../concepts/dev-setup) guide.

:::tip
If you are using *Visual Studio Code* as your IDE, we recommend you to install the [Cortex XSOAR extension](https://marketplace.visualstudio.com/items?itemName=CortexXSOARext.xsoar).  
For more information, refer to the [Visual Studio Code extension](vscode-extension) article.
:::