---
id: getting-started-guide
title: Getting Started Guide
---

This guide will provide you with some pointers to jumpstart your development journey.  
After reading it, you’ll have a starting point for creating new content for the Cortex XSOAR platform.  

If you have any questions or need support, feel free to reach out to us on the `#demisto-developers` channel on our [Slack DFIR Community](https://start.paloaltonetworks.com/join-our-slack-community).  

If you're a Technology Partner (or interested in becoming one), you can contact us via the [Cortex XSOAR Alliance Email](mailto:soar.alliances@paloaltonetworks.com).
 
## Prerequisites and Resources
Cortex XSOAR is a powerful platform with a rich set of features and customizations.  
Because of that, we recommend following these steps, and reading the aforementioned resources before creating custom content:
1. Understand the [Cortex XSOAR Concepts](../concepts/concepts).
2. Read the [FAQ](../concepts/faq).
3. Register to the [Learning Center](http://education.paloaltonetworks.com/learningcenter), and go through the [Product Training section of "Become an XSOAR Partner"](../partners/become-a-tech-partner#3-take-required-training).
4. For Cortex XSOAR server (non-content) documentation, refer to the [Cortex XSOAR Product Documentation Page](https://docs.paloaltonetworks.com/cortex/cortex-xsoar.html).
5. Join the [Palo Alto Networks DFIR Slack community](https://start.paloaltonetworks.com/join-our-slack-community), and join the *#demisto-developers* channel.
6. If you consider publishing your content to [Cortex XSOAR Marketplace](https://cortex.marketplace.pan.dev/marketplace), read the [contribution article](../contributing/contributing) for additional info.
7. Obtain and install a copy of Cortex XSOAR.  
    If you are not a partner, you can obtain the Community Edition from [here](https://start.paloaltonetworks.com/sign-up-for-demisto-free-edition) for free.  
    Installation instructions are available [here](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/6.11/Cortex-XSOAR-Installation-Guide/Overview).
8. If you are integrating with an external API, make sure you have API or SDK access to the product or solution you want to integrate with for testing purposes.
9. Sign up to the [Developer Newsletter](https://start.paloaltonetworks.com/cortex-xsoar-developer-newsletter.html) to receive technical updates on developing and contributing.

### Technology Partners
To become a Technology Partner, read the "[Become a Technology Partner](../partners/become-a-tech-partner)" article, and contact our Cortex XSOAR Alliances Team ([soar.alliances@paloaltonetworks.com](mailto:soar.alliances@paloaltonetworks.com)) to make sure your use cases have been validated.

## Development Environment
### Demisto SDK
Whether you are using the built-in Cortex XSOAR IDE, or a full development environment, we have an official SDK that will help you with your development process.  
The SDK is a command-line tool that can be used to upload, download, lint, validate and run code on Cortex XSOAR (or XSIAM) directly from your command line.  

For more information, refer to the [demisto-sdk](../concepts/demisto-sdk) article.


### Basic XSOAR Environment
For creating / modifying content that's for personal use, or for a community contribution,
the basic [Cortex XSOAR IDE](../concepts/xsoar-ide) can be sufficient, and doesn't require setting up a special development environment.


### Full Development Environment
When making a large amount of changes, or developing new content, we recommend using a fully-fledged IDE like *Visual Studio Code* or *PyCharm* .  
For a tutorial on how to set up a full development environment, refer to the [Development Environment](../concepts/dev-setup) guide.

:::tip
If you are using *Visual Studio Code* as your IDE, we have an official [Cortex XSOAR extension](https://marketplace.visualstudio.com/items?itemName=CortexXSOARext.xsoar) that will help you in your development process.  

For more information, refer to the [Visual Studio Code extension](vscode-extension) article.
:::