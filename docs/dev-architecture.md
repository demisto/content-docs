---
id: dev-architecture
title: Architecture Basics 
---


*Intended Audience: Technical Staff, Developers, Content and Integration Authors*

## Platform Architecture

- Read about the architecture here
  - https://www.demisto.com/demisto-enterprise-under-the-hood/

- Architecture Diagram

![alt text](assets/Architecture-infographics.png "Architecture")  

- General Architecture Components
  - Installer is a self contained binary executable that runs on most linux operating systems
  - Core Server
	- Written in the go programming language
    - Uses React all built on REST API and Websockets
    - Supports multiple Authentication schemes
    - Supports RBAC with users and roles
    - Components can be installed on single server or distributed deployment
  - Storage Engine and Database 
	- Bleve and Scorch 
  - Components 
	- Integrations - Bring your own integration (BYOI) We have over 300 integrations with a lot of security tools. Integrations connect to third party api's using python or javascript. They can be built directly in the product with a built in IDE or externally using pycharm. Integrations support multiple different abilities based on the type of product supported. 
    - Automations - Single purpose scripts written in either python or javascript. For instance think like whois, dig, and other command line tools. 
    - Docker Containers - Integrations and Automations run inside docker containers. 
	- Engines - Can be deployed and distributed to run either integrations or automations and act as either a proxy to different corporate or cloud environments, or as load balancers and for a variety of segmentation purposes. 
    - D2 Agents - These are tied specifically to specific incidents within the platform and are used in situations to connect to an endpoint and run specific commands. 
---