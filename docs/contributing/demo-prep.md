---
id: demo-prep
title: Contribution Demo Preparation
---

This document includes info on how to prepare for a demo and how it will be conducted.          
Please make sure you review it before the demo.


## Contribution Demo

A demo is the last stage of the contribution before it is merged into the [Content](https://github.com/demisto/content) internal repo.
In order to be prepared as much as possible and avoid post-demo change requests, make sure to go through the steps detailed in this document.

### General Notes
- The purpose of the demo is to make sure the contribution is up to Cortex XSOAR standards and to ensure that everything works as expected while providing a good UX. 
- The participants who will take part in the demo are the contributor, the PR reviewer, and based on the content of the PR, a security reviewer as well.
- The demo should take up to an hour (based on the PR size).

### Pre Demo
- Make sure the change requests from your code review are fully addressed and fixed.
- Prepare a Cortex XSOAR instance that has all the recent changes and has the most updated version of your pack. The demo will be performed in this environment.
### Demo Agenda and Workflow
The following may change given the scope and the size of the contribution.
- Product overview - short general explanation about the product.
- Overview of the use cases implemented in the pack - the use cases the customer will use the pack for.
- Overview of the integration commands implemented - which commands are implemented.
- Demo integration instance configuration:
  - Verify that it is clear how to retrieve required credentials.
  - Verify correct error handling - what happens when the credentials are wrong.
- Demo integration commands:
  - Verify that commands, arguments, and outputs (including descriptions) are according to standard:
    - [Python code conventions](https://xsoar.pan.dev/docs/integrations/code-conventions)
    - [Context and Outputs](https://xsoar.pan.dev/docs/integrations/context-and-outputs)
    - [Context Standards](https://xsoar.pan.dev/docs/integrations/context-standards-about)
- Demo fetch incidents (if applicable) - verify that incidents are fetched and displayed correctly.
- Demo playbooks (if applicable).
- Review layout, incident and indicator type, incident and indicator fields, and classifiers (if applicable).
  - Verify layout is bound to incident / indicator type.
  - Verify incident / indicator fields are bound to incident / indicator types.
  - Verify classifier is bound to incident type.
  - Verify playbook is bound to an incident type.

### Post Demo
- If there were any changes requested during the demo by the reviewers, they must be fixed and committed.
- After all requested changes are made, the PR will be merged.

