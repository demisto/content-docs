---
id: about-context-standards
title: About Context Standards
---

Cortex XSOAR organizes incident data in a tree of objects called the *Incident Context*. Any integration commands or scripts that run, will add data into the context at a predefined location. This also applies to commands that run within playbook execution.

When building new integrations the entry context should be returned according to this standard in addition to the vendor specific context. 

The structure should be:

```json
  {
  "Object": {
    ...
  },
  "Vendor": {
    "Object": {
      ...
    }
  }

}

```

Some standard objects are [Mandatory](../mandatory-context-standards)  and enforced in the code, and some are our [Recommendations](../recommended-context-standards).

If there is no matching item in the standard, reach out to us to check if your addition merits an update or change of the standard. 




