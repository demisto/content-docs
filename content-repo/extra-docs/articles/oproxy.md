---
title: Oproxy
description: Service for OAUTH2 authentication with 3rd party vendors to integrate with.
---

Oproxy is a close-source service which was developed and maintained by Cortex XSOAR on Google Cloud.

It is used for OAUTH2 authentication with 3rd party vendors (e.g. Microsoft), which is required in order to integrate with them.

In the authorization flow, the user grants permission for Cortex XSOAR application to access to the relevant data for running the required API queries.

Usually, three parameters are stored encrypted in Oproxy database:

    1. Identifier (UUID)
    2. Key
    3. Token
    
These parameters are returned by Oproxy to the user, after the authentication is completed successfully, to insert in the integration instance configuration.
The integration can then use them, to communicate securely with Oproxy and obtain the required credentials for making API queries.


