---
id: tut-design
title: Contribution Design
---

The design phase is extremely important when building content for Cortex XSOAR that you wish to contribute and make available to all the customer through the Marketplace. While many developers prefer to jump right into the coding phase, there is lot of value in stopping to think about what you want to achieve and how. There are several best practices that you should consider and, by following this tutorial, you should be able to design your contribution in a way that can be reviewed accepted quickly and easily by the XSOAR Content team.

## Before you start

Before starting to design, make sure you understand the Cortex XSOAR [concepts](../concepts/concepts) and you become familiar with the different components that constitute a Contribution (Integrations, Playbooks, etc.). Also please read and understand the [contribution](../contributing/contributing) process.

## Design Steps

The tutorial will cover the following topics:
- Use cases
- Contribution scope
- Design Document
- Integration Design
- Playbook Design

Once all the above steps are completed, the coding part will be trivial. Let's get started.

## Use Cases

We are grateful that you decided to spend time and effort to contribute to Cortex XSOAR. At first, it's important to understand what you want to achieve with your contribution. We recommend to start thinking about User Stories, to determine what would constitute a successful outcome of your effort.

Cortex XSOAR is a solution that SOCs use to reduce manual activity by providing automation via playbooks and integrations with multiple third party APIs. The flexibility of the product is such as there isn't a specific script but, in very general terms, often we see the following phases of an incident lifecycle:

1. Incident creation: a new incident is created in Cortex XSOAR because something happened. Incidents can be fetched by Cortex XSOAR from external APIs, or pushed to it using REST APIs or emails. Incidents can be classified to existing out of the box types, or new types and related fields can be defined. Custom layouts can also be created to allow the SOC analyst to focus on the most relevant information.

2. Incident data enrichment: following the creation of an incident, there is usually an enrichment phase where additional data is automatically collected from multiple sources (reputation, directories, DBs, etc.) to provide the analyst with all the necessary context to make decisions on priority and impact.

3. Incident response: once all the data is collected, it's time to handle the incident response. This could be as simple as closing it (in case it has been determined that is a false positive), to very rich and complex playbooks that include several automated (or semi-automated) remediation steps across the entire IT infrastructure, such as blocking, quarantining, notifying people, collecting even more data, forensics analysis, reporting, etc. The number of actions available out of the box through Cortex XSOAR via Integrations is huge, and more can be added through contributions. Everything that can be automated is a huge help for the SOC team.

With this in mind, you could start thinking about how your contribution should look like:
 - Do you want to create an end-to-end use case that includes all of the phases above?
 - Do you want Cortex XSOAR to consume Incidents from a new product?
 - Do you want to provide enrichment from a data or reputation source that isn't already available in content?
 - Do you want to automatically fetch IOCs from a third party platform into Cortex XSOAR?
 - Do you want to map a third party product API into Cortex XSOAR, so that actions can be automated?
 - Do you want to create Playbooks that automate an Incident Response workflow across multiple security products?
 - Are there manual tasks in your products or Security department where users spend a lot of time on and could be automated? 

Providing the answers to these questions is a great starting point to define use cases. A few examples:
-  The SOC team wants to include a new source of Incidents in Cortex XSOAR from a security product that is currently not supported by the Marketplace. This could be already achieved through a SIEM, but a direct integration will make it easier to consume and provide a better UX to the analysts.
- The SOC team wants Cortex XSOAR to automatically provide reputation information about IOCs from a Threat Intelligence source that is currently not supported by Cortex XSOAR.
- The SOC team wants to integrate to an existing IT solution (i.e. a CMDB, Instant Messaging platform or Database) to automatically exchange data between with Cortex XSOAR.
- The SOC team wants to automatically trigger actions on a third party security product that is currently not available in the Cortex XSOAR Marketplace.


If you are a third-party security vendor and want to integrate your product, [here](../concepts/use-cases) are some common Use Cases across different product categories that you could use as a starting point. However, don't limit your imagination to what is there, as your product has unique capabilities that could be exposed through Cortex XSOAR  to provide lots of value to our joint customers.

Another important recommendation about this design phase, is not to necessarily focus on APIs when designing the use cases. Think about the outcomes and write them down first, then look at your APIs to understand if they can be achieved or if there are any gaps. During our design sessions with technology partners, we often found them deciding to implement new APIs in their platforms to improve the level of automation that customers could achieve.

## Contribution Scope

Now that you have an idea of what Use Cases you want to create, it's time to determine how they translate into a Cortex XSOAR contribution.

All contributions are grouped in [Content Packs](../concepts/concepts#content-packs): the first thing to understand is what you should create and add to your pack.

Depending on whether you are a Palo Alto Networks Technology Partner, an Individual Contributor, a Customer or an Enthusiast and depending on how you want your contribution to appear on the [Cortex XSOAR Marketplace](../partners/paid-packs), the thoroughness and complexity of your final product will be different.

This section summarizes some guidelines to get started.

### Playbooks

If you have an end-to-end use case in mind, most likely you are going to build one or more **Playbooks**. Start thinking about the process that you want to automate and enumerate the steps and the decisions that are part of it: those will become your playbook's tasks. Figure out if all these building blocks are already part of Cortex XSOAR by browsing the Marketplace.

You can have multiple Playbooks in the same Content Pack, as long as they are related to a similar end-to-end use case. If they are completely separate, consider splitting them in multiple Content Packs.

Playbooks can use sub-playbooks from the same Content Pack or others, with dependencies that can be set as mandatory or optional (Check the *Skip this branch if this automation/playbook is unavailable* option under the [Playbook Reference](../playbooks/playbooks-field-reference#advanced-fields)).

Cortex XSOAR already provides number of Generic Playbooks that can be used as sub-playbooks are described [here](../playbooks/playbooks-generic).

### Integrations

You will need to create an **Integration** if the answer is yes to any of the following questions:
- You have a use case in mind that requires communicating with a third party system or API, but there is no Integration available for it in the Cortex XSOAR Marketplace.
- You are a vendor and you want Cortex XSOAR to be able to interact with your product or retrieve indicators from your Threat Intel Feed. 

Think of Integrations as the building blocks that enable external communications and form the foundations of Playbooks.

While it's possible to have multiple integrations in a single Content Pack, we generally recommend to include only a single integration in each Content Pack (i.e. if you are building two integrations to interact with two different third party products, we recommend to create one Content Pack for each product).

### Classifiers, Mappers, Types, Fields and Layouts

If you are planning to create a new Integration that [fetches incidents](../integrations/fetching-incidents) from a third party system, it is recommended that you create a few additional items and add them to your Content Pack:
- **Incident Types**: Cortex XSOAR ships with a number of out of the box Incident Types, however it is recommended to create one or more Incident Types that are specific to the product you are creating incidents from. More [info](../incidents/incident-types).

- **Incident Fields**: Product-specific fields are important to create a data model that is relevant to the incident type you have created. More [info](../incidents/incident-fields). All of the incident fields should be associated only to the incident type you have created, and their name should be prefixed accordingly to indicate it.

- **Layouts**: As you create new Incident Types with dedicated Fields, it's a good practice to define layouts to visualize them in the Cortex XSOAR UI so that the right data is immediately visible to the analyst. More [info](../incidents/incident-customize-incident-layout).

- A **Classifier**, that is used to determine how an incoming incident retrieved by your integration is associated to a specific Incident type. More [info](../incidents/incident-classification-mapping).

- A **Mapper**: after the incoming incident is associated by the Classifier to an Incident Type, the Mapper determines how the raw data from the incoming incident JSON is mapped to the specific Incident Fields. More [info](../incidents/incident-classification-mapping#map-event-attributes-to-fields).

- **Playbooks**: we also recommend to create a Playbook, associated with the new Incident Type, that performs some minimal activity such as enrichment or additional triage of the incident. For example, check out the [Handle Hello World Alert](https://xsoar.pan.dev/docs/reference/playbooks/handle-hello-world-alert) playbook.

More details about the incident lifecycle in Cortex XSOAR are available [here](../incidents/incident-xsoar-incident-lifecycle).

**Note:** If you build an integration that retrieves **Indicators**  (see [feeds](../integrations/feeds)), similar considerations apply, except that most of the time out of the box Indicator Types suffice and you don't need custom ones.

### Automations (Scripts)

Scripts are used for different functions across Cortex XSOAR: the main difference from Integrations is that they work with data that is already within XSOAR and do not communicate with external APIs. Scripts are often used for transforming data, visualizing it, triggering playbooks when certain conditions happen, etc. 

Most of the times you don't need to consider Scripts at this stage of the design process: it will come up later as you progress with the development of your contribution.

### Dashboards & Widgets

If you want to visualize summarized and aggregated data about anything in Cortex XSOAR (Incidents, Indicators, etc.), you can also create custom Dashboards. Dashboards are collections of Widgets that can be also customized and shipped through Content Packs.

## Design Document

At this point you should be able to understand what components you are going to build (Integrations, Playbooks, etc.) and the level of thoroughness and quality you need to reach in order to achieve the level of certification you are aiming for.

No matter what you want to build and how you want to support, we always recommend to document your design.

For contributors that aim to be [Certified](../partners/certification), we require you to produce a Design Document following a specific template, while for everyone else it is optional but recommended. 

For more details, check the [Contribution Guidelines](../contributing/contributing) and verify the [Contribution Checklist](../contributing/checklist).

If you are a [Technology Partner](../partners/become-a-tech-partner) you should have already received an invite to edit a personalized template on Google Docs. Otherwise, you can clone our [Design Document Template](https://docs.google.com/document/d/183jIki5hAwADUL7L5PREtjDCZVKQOTmqypeomzSpBZI) and get started.

As a reference on how to properly fill a Design Document, check out the [Hello World Design Document](https://docs.google.com/document/d/1wETtBEKg37PHNU8tYeB56M1LE314ux086z3HFeF_cX0). Make sure you also look at the comments that provide useful guidelines.

## Integration Design

If your contribution includes an Integration, it is very important to follow the Design Best Practices summarized [here](../concepts/design-best-practices): in this tutorial we will walk you through many of those topics in more detail.

Integrations enable communications with third party APIs: in order to get them accepted in the Cortex XSOAR Marketplace, they must function correctly, be properly [documented](../documentation/readme_file) and perform well alongside the rest of the Content.

### Integration Design Questions

Start your integration design by knowing the answers to the following questions:
 - What Product/API are you integrating with?
 - Which product [category](../integrations/packs-format#pack_metadatajson) does it belong to?
 - What version(s) or the product you are going to support?
 - Does it support on-prem deployment or SaaS only?
 - How does the authentication work?
 - What version(s) of Cortex XSOAR are you going to support? We recommend 6.0 and above, but if you have existing customers running older versions you should consider that.
 - Does this integration fetch incidents? If so, what is the name of the entities in the source product (i.e. incidents, alerts, events, messages, warnings, logs) that will be mapped to Incidents in Cortex XSOAR? What is the lifecycle of such entities: are they static or they get updated over time?
 - How many new incidents could this product generate in a busy production environment (worst case scenario)?
 - Are you calling APIs that can take longer than 5-10s to respond?
 - Does the product provide any reputation on Indicators of Compromise (IOCs)?
 - Does the product provide feeds of IOCs? 

### Integration Parameters

Each integration has *parameters*, that are configured by the customers when they configure an instance on their Cortex XSOAR system.

The following parameter types are supported: Short Text, Long Text, Boolean, Encrypted, Single Select, Multi Select.

Even if XSOAR doesn't make any distinction, in this tutorial we group parameters in three categories.

#### Connection and Authentication Parameters

These parameters determine how Cortex XSOAR connects to the third party API. 

Usually there are at least two parameters:
 - **url**: the URL Cortex XSOAR should connect to. In case the API is SaaS only and the URL is the same for all customers and is never going to change over time, you can omit this parameter and store the URL directly in the code. Some SaaS products have different urls based on the tenant name, for example `customer1.my-test-saas-service.info` and `customer2.my-test-saas-service.info`: in this case we still recommend to use the full url here and not just the tenant name (i.e. have the clients input `customer1.my-test-saas-service.info` and not just `customer1`).

 - **api_key**: usually credentials are needed to authenticate to the API you want to interact with. Many times this is in the form of an API Key, a secure quantity that gets stored in Cortex XSOAR and used in somewhere in your code (i.e. to populate HTTP headers) to craft the requests. Sometimes APIs use different authentication parameters: [credentials](../reference/articles/managing-credentials), tokens, client_id and client_secret combination, and so on. Make sure you capture all the required parameters that will allow a machine-to-machine authentication between Cortex XSOAR and your API.
 
    **Note**: if you are using authentication mechanisms based on short-lived access tokens such as JSON Web Tokens (JWT) and long-lived refresh tokens, take a look at the [Integration Cache](../integrations/integration-cache) article.

Every integration also requires some additional parameters:
- **proxy**: boolean to determine whether to use the system proxy setting. You won't actually need to deal with proxy settings in your code, just set environment variables accordingly based on this boolean.

- **insecure**: boolean to determine whether to avoid verifying SSL certificates. This parameter, which by default is set to False, is important when customers deploy Cortex XSOAR on-prem behind proxies with self-signed certificates.


Integration parameters should be named using [snake_case](https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841).

#### Fetch Incidents Parameters

If your integration [fetches incidents](../integrations/fetching-incidents), you should define what type of entities in the third party product you are connecting to you are retrieving. Every product has its own nomenclature: they can be called Alerts, Incidents, etc: for the rest of this section we are going to assume they are called Alerts in the third party product, and they are mapped 1:1 to Cortex XSOAR incidents.

Many products are very verbose, and can potentially generate lots of alerts of different types, with different level of severity. Each alert could have a status (i.e. `open` or `resolved`) as well as attributes.

SOC analysts might be interested only in a subset of the incoming Alerts, so when they configure your integration in Cortex XSOAR, they expect to find Parameters that allow them to filter and determine what alerts are going to generate incidents or discarded.

Common filters for fetching incidents are:

 - **Maximum number of incidents per fetch** (parameter name must be: *max_fetch*): it's a good practice to limit the number of incidents you retrieve every time you fetch, in order to avoid overloading XSOAR by running lots of playbooks at the same time. Customers should be allowed to set this value as an integration parameter. Recommended default is 10 to 20, with a maximum 50.

 - **Severity**: many SOCs prefer to retrieve from third party systems only incident with specific severities, and do not import the lower severity ones. It's a common practice to let customers choose in the integration settings the severity of the incidents they want to retrieve (either using a multi-select, or a single-select where they specify the lowest severity level they are interested in).

 - **Type**: third party products typically generate different types of alerts/events/issues/incidents. Often SOCs are interested only in a specific subset of types they want to handle automatically through Cortex XSOAR. This integration setting should allow the end users to specify what types of alerts they are interested to fetch from the third party platform. If the types are of finite and known cardinality, we recommend to use a multi-select here: if they are not known up-front or change over time, we suggest to use a comma separated text input, with a link in the details to your product documentation where an up-to-date list of those types is presented.

 - **First Fetch** (parameter name mist be: *first_fetch*): when customers configure the integration for the first time, they are usually interested to retrieve incidents that happened in the past. This common setting is used to specify how long back in time they want to go to retrieve incidents the first time. You can check the [HelloWorld](https://github.com/demisto/content/blob/master/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.py) integration implementation code for more details.

If the API you are integrating with also supports a query interface using free-form text (i.e. a specific query language implemented in the product), you can also add another parameter (usually called **query**) that will give the users more freedom to generate incidents in XSOAR based on a specific query: this gives more freedom to the users and supports more advanced use cases for your integration.

There are additional required parameters for integrations that fetch incidents: you don't need to handle  them in your code, just make sure they are correctly defined in your integration yml file. The updated list is [here](https://github.com/demisto/demisto-sdk/blob/f407ffe9d632c45acce0ce0587efbf8ae89d6db8/demisto_sdk/commands/common/constants.py#L942).

#### Fetch Indicators Parameters

If your integration implements a [feed](../integrations/feeds), you should define some common parameters, that are used by XSOAR to control how the indicators are handled. You don't need to handle  them in your code, just make sure they are correctly defined in your integration yml file. The updated list is [here](https://github.com/demisto/demisto-sdk/blob/f407ffe9d632c45acce0ce0587efbf8ae89d6db8/demisto_sdk/commands/common/constants.py#L870). 

#### Other Parameters

Your product is unique, so are the parameters you might want to add to the integration. Besides connectivity and fetch parameters, you can add more as you see fit. The general rule of the thumb is to add parameters whenever you want the users to specify settings that are common across several integration commands.

A good example is a Threat Intel reputation threshold: imagine that you are creating an integration that asks for reputation about network assets (IP addresses, URLs and domains), using different commands (`!ip`, `!url` and `!domain`). Your API returns a score value between 0 and 100 to determine whether the asset is malicious: the higher the score is,  more likely the asset is bad. Cortex XSOAR reports whether an indicator is good or bad using the concept of [DBotScore](../integrations/dbot) with a discrete set of values: 0 means no reputation, 1  good, 2  suspicious and 3 bad. In order to map the score that your API returns (0-100) to a DBotScore, you typically define a threshold above which the asset is considered malicious. The value of the threshold is usually something that you provide as a default (say 60) but the end user should be able to override. And such threshold value should be common across all the different reputation commands (`!ip`, `!url` and `!domain`) of your integration. For such reasons, adding `threshold` as an additional Integration parameter is a good practice, so the users can set it once and don't have to specify it manually every time the invoke a reputation command. Note that you can still add an optional argument to each command to override the integartion parameter if you need to.

### Integration Commands

Besides fetching incidents or indicators, your integration is probably mapping some of your product APIs in commands that you want to expose to XSOAR.

Every command takes inputs (arguments) and returns outputs.

Commands names follow a naming convention that makes it easy for the users to understand what they do: `!vendor-action-object` using [kebab-case](https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841). For example, a command of an integration from vendor HelloWorld that performs an update action of an object of type alert, should be named: `!helloworld-update-alert`.

Integration commands are used in two ways inside Cortex XSOAR:
- In Playbooks: in this case commands become building blocks or tasks of playbooks.
- In the CLI: users can manually run commands within an incident using the XSOAR CLI by typing `!commandname` and specifying the arguments.

Customers typically use a combination of both: they use commands to automate processes through the playbooks and, when they are conducting investigations manually they run commands from the CLI to analyze the data.

It's very important to understand how arguments and outputs work and what are the design best practices.

#### Command Design

Commands should be as atomic as possible (i.e. each command should ideally run a single API call to your product): this will simplify the handling of conditions where some calls fail and other succeeds: whenever possible such logic should be implemented in Playbooks rather than integrations.

Make sure that commands run quickly and are non-blocking: a command should never take more than 2-3 seconds to run and return the information, or it would have significant performance impacts in XSOAR. **Avoid sleep() at all costs in your code**.

If you have commands that need to run for longer periods of time, we recommend two approaches:
- Make the commands asynchronous and implement a [Generic Polling](..//playbooks/generic-polling) mechanism. For example, if you need to run a search across your Endpoints, instead of having a single command that waits until the search is completed, you should implement three separate commands:
  - A command that triggers the search and returns immediately a job id as output (i.e. `!helloworld-start-scan`).
  - A command that checks the status of the job taking the job id as input (i.e. `!helloworld-scan-status`).
  - A command that retrieves the results of a job when it's complete, taking the job id as input (i.e. `helloworld-scan-results`).
  
  A good example to refer to is the [HelloWorld](https://github.com/demisto/content/blob/master/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.py) integration.

- Use [Long Running](../integrations/long-running) containers: this is suitable for services that need to keep a connection open for long time or need to open a listening TCP port. For example [Slack](https://github.com/demisto/content/tree/master/Packs/Slack/Integrations/Slack).

There are cases where you want to build commands that perform generic well-known actions that are common across several use cases, for example Reputation commands (i.e. commands that return enrichment and reputation information about indicators, such as IPs). For those scenarios, we have standardized ways to define command names, inputs and outputs that will make interoperability much easier. For more information, check out the docs about [Generic Commands](../integrations/generic-commands-about) and [DBotScore](../integrations/dbot).

#### Command Arguments

Arguments are the inputs of your integration commands. They can be mandatory or not, and can have default and predefined values. More details [here](../integrations/yaml-file#commands).

Command arguments should be named using [snake_case](https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841).

When you design your commands and their inputs, you should keep in mind how they are invoked: if a user, either manually or through a playbook, has to provide an input, where do they take that input data from? Something they know because it's obvious? Or the output of another command?

We also recommend to make the argument values consistent to what the user needs to provide in the user interface of the original product you are integrating with, not necessarily what the API requires. For example, if in the product UI  you have 3 options for an argument: `Low`, `Medium` and `High`, but the product API takes corresponding numbers (`1`, `2` and `3`), then your XSOAR integration's command argument should support `Low`, `Medium` and `High` and you should take care of converting them in numbers in your integration code: the user experience of integration should be consistent with what the user is most familiar with (see the [principle of least astonishment](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)).

Another important design rule is to avoid having the SOC analyst waste time and focus by switching across multiple consoles and retrieve data from many different places. If they need to provide an input value in an XSOAR command, there should be a way to get that information within XSOAR.

Let's clarify the concept with an example: imagine that you are designing a command that modifies an existing Firewall policy. For simplicity let's assume you have only two arguments: the id of the policy and the action (allow or deny). The latter argument is obvious: depending on what the user wants to do, they will set the value to `allow` or `deny` (you will use predefined values so the user can only choose between those). But what about the id of the policy? It's probably not something that they know right away: maybe they know the policy name, but you don't want them to switch context and log to a different console to find the id that corresponds to the name. So in this case, you should design your integration to make sure that there is another command that returns the list of all policies and shows their ids, or allows the user to retrieve the id from the name. This way they don't have to switch consoles.

#### Command Outputs

Every automation script and integration command returns several types of outputs:
 - Human Readable: this is shown to the user in the War Room and is typically formatted in a way that is understandable by the SOC analyst. The Human Readable data is usually a subset of the entire information returned by your command: typically you should show the most relevant data that is also present in the user interface of the product you are integrating with. The ordering is also important: make sure the most relevant fields (and the ones the user is most familiar with) are displayed in the leftmost columns.
 - Context Data: outputs are also saved in a structured way (JSON backed) within an incident, so they can be retrieved later as inputs of other tasks (either within Playbooks or from the CLI). More information [here](../concepts/concepts#context-data).
 - Additional outputs such as images or files.

When you design your outputs, you must make sure that the data is properly formatted for both human consumption and machine consumption. Here are some best practices:
 - Keep Human Readable information to the reasonable minimum (i.e. remove unnecessary data that is not relevant to a human analyst) and present it nicely (we recommend using [tableToMarkdown()](../integrations/code-conventions#tabletomarkdown) to automatically format lists into tables: the function also supports arguments that allow you to filter and order columns and make the column headers prettier). 
 - Keep Context Data well organized, which means:
   - Return data using a prefix, such as `VendorName.Entitytype`, for example if your Pack is called `HelloWorld` and you are returning a list of hosts, the prefix of the output should be `HelloWorld.Host`.
   - Use the [CommandResults](../integrations/code-conventions#commandresults) class to return data to make sure it's properly formatted, and use the `outputs_key_field` parameter to identify the primary keys.
   - Adhere to the [Standard Context](../integrations/context-standards-about).

[Here](../integrations/context-and-outputs) are some more details about Context and Outputs.

If you are returning files, it's important to understand the difference between `Files` and `InfoFiles`, as you should specify the right return type in your command output:
 - `Files` are potentially malicious files (i.e. attachments from potential phishing emails) that should be treated as such: they will be automatically enriched (by checking their reputation against configured Threat Intel sources) and detonated in Sandboxes. More [details](../integrations/context-standards-mandatory#file).
 - `InfoFiles` are not malicious by definitions: they can be reports, CSVs and other artifacts that your API is returning. They are not automatically enriched and detonated. More [details](../integrations/context-standards-mandatory#infofile).

### Additional Integration Considerations

In general, make sure you understand and follow our Code Conventions to dramatically simplify the implementation and the review process:
- [Python](../integrations/code-conventions)
- [PowerShell](../integrations/powershell-code)

#### Classification and Mapping

If your integration is fetching incidents, it's highly recommended to create at least a Custom Incident Type with corresponding Classifiers and Mappers, and add these to your Content Pack.

#### Docker Image

Integrations run in [Docker](../integrations/docker) containers on the XSOAR server and its engines. We provide generic images with recent Python and Powershell versions and a smalls set of libraries.

If you need to use additional libraries that are not part of the default images, check our [dockerfiles](https://github.com/demisto/dockerfiles) repository in GitHub to see if one of the existing images works for you.

If none works, you can create your own Docker image and contribute it by following the [instructions](https://github.com/demisto/dockerfiles/blob/master/README.md).

The docker image to use is specified in the Integration yml file.

#### Feed Integrations

Starting from version 5.5 of Cortex XSOAR, we provide the ability to build Feed Integrations, that are used to collect batches of Indicators from Threat Intel feeds. If you're planning to build such functionality, please check the [documentation](../integrations/feeds).

#### Integrations cache

If you need to store integration-specific data, such as tokens that have a specific duration (i.e. JWTs for authentication), you can use the [integration cache](../integrations/integration-cache) functionality.

#### Mirroring

Starting from version 6.0 of Cortex XSOAR, it is possible to bidirectionally synchronize incident updates among different systems, using the [Mirroring](../integrations/mirroring_integration) functionality. This allows to make sure that XSOAR incidents are always up-to-date with the remote system and, when a change occours on either side, the information is promptly updated without requiring to run a Playbook: this functionality enable analysts to use Cortex XSOAR as a single user interface to interact with multiple products.

### Integration Naming Conventions

When naming integrations, commands, arguments and outputs, please use the following naming conventions:
- **Integration Parameters**: Brief and clear names with [snake_case](https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841) (i.e. `min_severity`).

- **Command Names**: Explicit `!vendor-action-object` with [kebab-case](https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841) (i.e. `!helloworld-get-alert`).

- **Command Arguments**: Brief and clear names with [snake_case](https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841) (i.e. `alert_id`).

- **Command Outputs**: Explicit `Vendor.Object.data` with [PascalCase](https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841) for the Vendor and Object block (i.e. `HelloWorld.Alert.owner.name`).
After the Vendor and Object blocks just use the same format as your product's API, but make sure there are **no spaces or dots** in the key names, as dots are interpreted as object separators.
For example, XSOAR will correctly parse this:
    ```json
    {
      "HelloWorld": {
        "Alert": {
          "owner": {
              "name": "Francesco",
              "email": "francesco@cortex.local"
          }
        }
      }
    }
    ```
    as:
    ```
    HelloWorld.Alert.owner.name: "Francesco"
    HelloWorld.Alert.owner.email: "francesco@cortex.local"
    ```
    but will not correctly parse this:
    ```json
        {
      "HelloWorld": {
        "Alert": {
          "owner.name": "Francesco",
          "owner.email": "francesco@cortexl.local"
        }
      }
    }
    ```

## Playbook Design

Playbooks are a great solution to automate complex workflows using Cortex XSOAR no-code/low-code Playbook Editor.

You can assemble building blocks as tasks, that can be automated or manual, conditional statements and other playbooks (known as subplaybooks).

Automated tasks correspond to Automation Scripts or Integration Commands.

Check out the following guides:
- [Playbook Contribution Guide](../playbooks/playbook-contributions)
- [Playbook Conventions](../playbooks/playbook-conventions)
To avoid reinventing the wheel every time, we provide a number of out-of-the-box playbooks that can be included as subplaybooks to perform common tasks whenever possible. The up-to-date list of generic playbooks can be found [here](../playbooks/playbooks-generic)

### Playbook Triggers

Playbooks are triggered in three different ways:
- by incidents: determine what XSOAR Incident Types should trigger the playbook. Do they already exist or you need to create a new **Incident Type** as part of your contribution?

- by indicator query: you can trigger Playbooks based on a query on the indicator store. If so, determine what the query is (i.e. all IP indicators retrieved from a particular feed). Are there new **Indicator Types** that must be created as part of the contribution or the out of the box ones suffice?

- as a subplaybook: the playbook is meant to be invoked by a parent one. In this case you need to determine what [Inputs and Outputs](../playbooks/playbooks-inputs-outputs) you want your playbook to support and think about default values.

### Generic Polling

If you are building asynchronous tasks (i.e. starting a job and waiting for it to complete before returning the results), you should use the [Generic Polling](../playbooks/generic-polling) mechanism.

## Documentation

To make your content easy find in the Cortex XSOAR Marketplace and properly used by customers, it's really important to document it properly. Make sure to check the [Content Pack Documentation](../documentation/pack-docs) page to understand how.

Integrations, Scripts and Playbooks and their components (i.e. integration commands arguments and outputs) also have descriptions that show up within the product and in this site on the Reference section. We recommend to learn our [Documentation Best Practices](../documentation/documentation_tips) early on so you get familiar with them as you write your design document. 
