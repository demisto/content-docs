---
title: Microsoft Integrations - Authentication
description: Authentication method for Microsoft Graph and Azure integrations in Cortex XSOAR.
---

Microsoft integrations (Graph and Azure) in Cortex XSOAR use Azure Active Directory applications to authenticate with Microsoft APIs. These integrations use OAuth 2.0 and OpenID Connect standard-compliant authentication services, which use an **Application** to sign-in or delegate authentication. 
For more information, see the [Microsoft identity platform overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview).

There are 2 application authentication methods available: 

1.  Cortex XSOAR Application
2.  Self-Deployed Application

## Cortex XSOAR Application
In this method, you give consent to the Cortex XSOAR application to access your data.
Depending on the integration, this requires either admin consent to [get access without a user](https://docs.microsoft.com/en-us/graph/auth-v2-service) or user consent to [get access on behalf of a user](https://docs.microsoft.com/en-us/graph/auth-v2-user).
**Note**: This method requires that you give consent to all permissions requested by the application.

To start the authentication process, go to the integration's detailed instructions:

1.  Navigate to __Settings > Integration > Servers & Services__.
2.  Search for wanted Microsoft integration, e.g. `Microsoft Defender Advanced Threat Protection`.
3.  Click __Add instance__.
4.  Click on the question mark on the top right.

    <img width="300" src="../../../docs/doc_imgs/tutorials/tut-microsoft-auth-guide/instance_detailed_instructions.png" align="middle"></img>

5.  Follow the link to our authentication service to initiate the authorization flow.

## Self Deployed Application
To use a self-configured Azure application, you need to add a new Azure App Registration in the Azure Portal. 

The application must have the required permissions for the relevant APIs, which are documented in the integration documentation, for example see [Microsoft Defender Advanced Threat Protection required permissions](https://xsoar.pan.dev/docs/reference/integrations/microsoft-defender-advanced-threat-protection#required-permissions).

To add the registration, refer to the [Microsoft documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)

The Tenant ID, Client ID, and Client secret are required for the integration. 

When you configure the integration in Cortex XSOAR, enter those parameters in the appropriate fields:

* ID - Client ID
* Token - Tenant ID
* Key - Client Secret

In addition, make sure to select the ***Use a self-deployed Azure Application*** checkbox in the integration instance configuration.