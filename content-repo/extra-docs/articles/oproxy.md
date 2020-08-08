---
title: OProxy
description: Service for OAUTH2 authentication with 3rd party vendors to integrate with.
---

OProxy is a service that is developed and maintained by Cortex XSOAR on Google Cloud. It is used to facilitate in performing an OAUTH2 authentication flow with a 3rd-party vendor (e.g., Microsoft). 

In the authorization flow, the user grants permission for Cortex XSOAR application to access to the relevant data for running the required API queries.

Usually, three parameters are stored encrypted in the Oproxy database:

    1. Identifier (UUID)
    2. Key
    3. Token
    
After the authentication is completed successfully, these parameters are returned by Oproxy to the user to insert in the integration instance configuration.
The integration can then use the parameters to communicate securely with Oproxy and obtain the required credentials for making API queries.


