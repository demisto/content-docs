---
id: getting-started-guide
title: Getting Started Guide
---

This guide will provide you with some pointers to jumpstart your development journey. After reading it, you’ll have a great background for creating content and integrations for the Cortex XSOAR platform.

## Prerequisites to start development

Please make sure you have completed the following before proceeding:

1. Python 3.x programming experience (intermediate level)
2. A copy of the Cortex XSOAR Platform (if you are not a Partner, you can obtain the Community Edition [here](https://start.paloaltonetworks.com/sign-up-for-demisto-free-edition)
3. Access to our [Support Portal](https://docs.paloaltonetworks.com)
4. Access to the Palo Alto Networks [DFIR Slack Community](https://start.paloaltonetworks.com/join-our-slack-community) and join the *#demisto-integrations-help* channel
5. API or SDK access to your product or solution.  

If you are a Technology Partner, make sure that you also:

1. Read the [Become a Technology Partner](../partners/become-a-tech-partner) page and sign up
2. Complete the Technical Partnership Agreement
3. Work with your Business Development contacts to make sure your use cases has been validated

If you have trouble with any of these items, please contact us via Slack or [email](mailto:info@demisto.com).

## Setting up & installing Cortex XSOAR

*Note: Requires Support Center login access.*

If you need to install Cortex XSOAR, please read the following Support Center article:

<a href="https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/installation.html" target="_blank">Installing Cortex XSOAR</a>

## Learning the Cortex XSOAR platform

The platform comes with a rich set of features and functionality that allow for a high degree of customization, so we recommend that you familiarize yourself with the different aspects of the platform as listed below.

*Note: Requires Support Center login access*

[Cortex XSOAR Concepts, and Terminology](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/cortex-xsoar-overview/cortex-xsoar-concepts)

* [The Cortex XSOAR CLI](https://support.demisto.com/hc/en-us/articles/115002333194-The-CLI-Command-Line-) - Think of this like an operating system CLI that is built into the product, and connects to every tool that you need. It allows the user to test and run integration commands, run automations, and more. 
* [Incidents](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/cortex-xsoar-overview/cortex-xsoar-concepts#h_571910869151527515268695) - From third party systems, email, etc., or created manually. Its the combination of a ticket and real time data. 
* [Integrations](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/cortex-xsoar-overview/cortex-xsoar-concepts#h_401233651221527515275882) - Product integrations (or apps) are mechanisms through which security orchestration platforms communicate with other products. These integrations can be executed through REST APIs, webhooks, and other techniques. An integration can be unidirectional or bidirectional, with the latter allowing both products to execute cross-console actions.
* [Playbooks](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/cortex-xsoar-overview/cortex-xsoar-concepts#h_17615621281527515282557) -  Playbooks (or runbooks) are task-based graphical workflows that help visualize processes across security products. These playbooks can be fully automated, fully manual, or anywhere in between.
* [Automations](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/cortex-xsoar-overview/cortex-xsoar-concepts#h_471741284321527515376864) - Single purpose automations that generally manipulate data in the system, or used to wrap multiple integrations, or develop single purpose tools that are not complete products. Maybe you have some library that is not a full product that you want to utilize, automations are a good use for this. 
* [Playground](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/cortex-xsoar-overview/cortex-xsoar-concepts#h_638814023411527515421050) - The place you go in order to test integration commands, automations, and other tools from the Cortex XSOAR CLI. 
* [The Cortex XSOAR Context](https://xsoar.pan.dev/docs/integrations/context-and-outputs) - All of the above are tied together by way of something called the Cortex XSOAR Context. Every incident and playbook has a place to store data called the Context. The context stores the results from every integration command and every automation script that is run. It is a JSON storage for each incident. Whether you run an integration command from the CLI or from a playbook task, the output result is stored into the JSON context in the incident or the playground. Simply put, if you have a command like ``` !whois query="cnn.com" ``` it would return the data and store the results into the context.  
* [Indicators](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/cortex-xsoar-overview/cortex-xsoar-concepts#h_812388463361527515415520) - Indicators are any type of data that you want to match using regular expressions, or add to the system. Indicators can be assigned certain integration commands, and automations in order to determine reputation, take action, enrich, the list goes on here. 
* Try the product walkthroughs. You can access these by clicking the ‘Ask DBot’ icon on the bottom-right of the Cortex XSOAR console screen.

## Development Guidelines

Please read the following guidelines. Following these guidelines will maximize the chances for a fast, easy and effective review process for everyone involved. If something is not clear, please don't hesitate to reach out to us via GitHub, [Slack](http://go.demisto.com/join-our-slack-community), or [email](mailto:info@demisto.com)

* Setup a development environment by following the [Dev Setup Guide](dev-setup).
* Use the [Content Pack format](packs-format) to add your contribution.
* Use [Integration and Script Directory Structure](package-dir) for all Python code based entities. If working on existing code, beyond trivial changes, we require converting to this structure as it allows running linting, unit tests and provides a clearer review process.
* Make sure to read and follow [code conventions](code-conventions).
* Run and verify that the various linters we support pass as detailed [here](linting).
* For Scripts/Integrations written in Python, make sure to create unit tests as documented [here](unit-testing)
* Create a test playbook as documented [here](testing). **Note**: for simple Scripts that have unit tests, a test playbook is optional.
* Validate that our validation hooks pass. If you used `.hooks/bootstrap` as documented in the [Dev Setup Guide]
(dev-setup) the validation hook will run automatically upon commit. You can also run the validation hooks manually by
 running `.hooks/pre-commit`. If you want to validate specific files please use the demisto-sdk commands [validate](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/validate/README.md)
  or [lint](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/lint/README.md) 
* Document your integration as detailed [here](integration-docs).
* Document your changes in a relevant release notes file as detailed [here](release-notes)

At this point you should be ready to submit a Pull Request! Check out our [Contributing Checklist](../contributing/checklist), and for more details, refer to our [Contributing](https://github.com/demisto/content/blob/master/CONTRIBUTING.md) page on GitHub.

**Note**: if you are a technology partner, make sure you have reviewed the use cases with your Business Development contacts and that you have a *Partner ID* to associate your Pull Request to.
