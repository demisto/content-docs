---
title: SAML 2.0
description: Authenticate your Cortex XSOAR users using SAML 2.0 authentication with your organization`s identity provider.
---

Use the SAML 2.0 integration to configure single sign-on for Cortex XSOAR users, using your organization's identity provider (IdP).

If your IdP is Okta or ADFS, refer to the relevant article.

* [SAML 2.0: Okta as IdP](https://xsoar.pan.dev/docs/reference/integrations/saml-20---okta-as-id-p)
* [SAML 2.0: ADFS as IdP](https://xsoar.pan.dev/docs/reference/integrations/saml-20---adfs-as-id-p)

### What is SAML 2.0?

According to the [SAML 2.0 page in Wikipedia](https://en.wikipedia.org/wiki/SAML_2.0):

Security Assertion Markup Language 2.0 (SAML 2.0) is a version of the SAML standard for  
exchanging authentication and authorization data between security domains. SAML 2.0 is an  
XML-based protocol that uses security tokens containing assertions to pass information  
about a principal (usually an end user) between a SAML authority, named an Identity  
Provider, and a SAML consumer, named a Service Provider. SAML 2.0 enables web-based  
authentication and authorization scenarios including cross-domain single sign-on (SSO),  
which helps reduce the administrative overhead of distributing multiple authentication  
tokens to the user.

### Configure SAML 2.0 with your IdP

When configuring SAML 2.0, you need to map several attributes from your IdP to Cortex XSOAR fields. The attribute fields must be populated in Cortex XSOAR exactly as they appear in your IdP. For example, if the email attribute in your IdP is email.address, you need to provide this value in the attribute to get the email parameter in the SAML 2.0 integration in Cortex XSOAR.

**IMPORTANT**: You need to provide values for all parameters. If you skip parameters, the Cortex XSOAR user you create will not contain important attributes and information, and will require you to manually assign a Cortex XSOAR role to the user.

| Attribute | Description |
| --- | --- |
| Name | A meaningful name for the integration instance. |
| Service Provider Entity ID | Also known as an ACS URL. This is the URL of your Cortex XSOAR server, for example: https://yourcompany.yourdomain.com/saml |
| IdP metadata URL | URL of your organization's IdP metadata file. |
| IdP metadata file | Your organization's IdP metadata file. |
| IdP SSO URL | URL of the IdP application that corresponds to Cortex XSOAR. |
| Attribute to get username | Attribute in your IdP for the user name. |
| Attribute to get email | Attribute in your IdP for the user email address. |
| Attribute to get first name | Attribute in your IdP for the user first name. |
| Attribute to get last name | Attribute in your IdP for the user last name. |
| Attribute to get phone | Attribute in your IdP for the user phone number. |
| Attribute to get groups | Attribute in your IdP for the groups in which the user is a member. |
| Groups delimiter | Groups list separator. |
| Default role | Role to assign to the user when they are not a member of any group. |
| RelayState | For IdPs using relay state, you need to supply the relay state. |
| Sign request and verify response signature | Method for the IdP to verify the user sign-in request using the IdP vendor certificate. |
| Identity Provider public certificate | Public certificate for your IdP. |
| Identity Provider private key | Private key for your IdP in PEM format in PKCS#1 type (required for single logout). |
| Service Provider public certificate | Public certificate for the service provider. |
| Service Provider Private key (pem format) | Private certificate key for the service provider in PKCS#1 type. |
| Do not validate server certificate (insecure) | Whether to verify the server certificate. |
| Use system proxy settings | Whether to use proxy settings. |
| ADFS | Whether to use the ADFS server. |
| Compress encode URL (ADFS) | Check mandatory for ADFS encoding. |
| Service Identifier (ADFS) | The ADFS relay identifier to which Cortex XSOAR redirects the user for SSO first login. |
| Identity Provider Single Logout URL | URL that users are sent to after logging out of the SAML session. |
| Single Logout Service Endpoint | Logout service with which SAML communicates. |
| Do not map SAML groups to Demisto roles | SAML groups will not be mapped to Cortex XSOAR roles. |
| Single logout - specify Name ID Format | Whether to use the Name ID format. |
| Name ID | Defines the name identifier formats supported by the identity provider. |
| Use this instance for external authentication only | Limits this instance to authenticate external (non-Cortex XSOAR) users when they answer a survey sent via a communication task. |
