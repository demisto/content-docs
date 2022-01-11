---
title: SAML 2.0
description: You can authenticate your Demisto users using SAML 2.0 authentication and your organization`s as the identity provider.
---

Use the SAML 2.0 integration to configure single sign-on for your Demisto users, using your organization's identity provider (IdP).

If your IdP is Okta or ADFS refer to the relevant article.

* [SAML 2.0: Okta as IdP](https://xsoar.pan.dev/docs/reference/integrations/saml-20---okta-as-id-p)
* [SAML 2.0: ADFS as IdP](https://xsoar.pan.dev/docs/reference/integrations/saml-20---adfs-as-id-p)

### What is SAML 2.0?

This definition of SAML 2.0 is taken from the [SAML 2.0 page in Wikipedia](https://en.wikipedia.org/wiki/SAML_2.0).

Security Assertion Markup Language 2.0 (SAML 2.0) is a version of the SAML standard for  
exchanging authentication and authorization data between security domains. SAML 2.0 is an  
XML-based protocol that uses security tokens containing assertions to pass information  
about a principal (usually an end user) between a SAML authority, named an Identity  
Provider, and a SAML consumer, named a Service Provider. SAML 2.0 enables web-based  
authentication and authorization scenarios including cross-domain single sign-on (SSO),  
which helps reduce the administrative overhead of distributing multiple authentication  
tokens to the user.

### Configure SAML 2.0 with your IdP

When you configure SAML 2.0, you need to map several attributes from your IdP to Demisto fields. You need to populate the attribute fields in Demisto exactly as they appear in your IdP. For example, if the email attribute in your IdP is email.address, this is the value you need to provide in the Attribute to get email parameter in the SAML 2.0 integration in Demisto.

**IMPORTANT**: It is important that you provide values for all parameters. If you skip parameters, the Demisto user that is created will not contain important attributes and information, and will require you to manually assign a Demisto role to the user that is created.

| Attribute | Description |
| --- | --- |
| Name | A meaningful name for the integration instance. |
| Service Provider Entity ID | Also known as an ACS URL. This is the URL of your Demisto server, for example: https://yourcompany.yourdomain.com/saml |
| IdP metadata URL | URL of your organization's IdP metadata file. |
| IdP metadata file | Your organization's IdP metadata file . |
| IdP SSO URL | URL of the IdP application that corresponds to Demisto. |
| Attribute to get username | Attribute in your IdP for the user name. |
| Attribute to get email | Attribute in your IdP for the user's email address. |
| Attribute to get first name | Attribute in your IdP for the user's first name. |
| Attribute to get last name | Attribute in your IdP for the user's last name. |
| Attribute to get phone | Attribute in your IdP for the user's phone number. |
| Attribute to get groups | Attribute in your IdP for the groups of which the user is a member. |
| Groups delimiter | Groups list separator. |
| Default role | Role to assign to the user when they are not a member of any group. |
| RelayState | Only used by certain IdPs. If your IdP uses relay state, you need to supply the relay state. |
| Sign request and verify response signature | Method for the IdP to verify the user sign-in request using the IdP vendor certificate. |
| Identity Provider public certificate | Public certificate for your IdP . |
| Identity Provider private key | Private key for your IdP, in PEM format (required for single logout) . |
| Service Provider public certificate | Public certificate for the service provider. |
| Service Provider Private key (pem format) | Private certkeyificate for the service provider. |
| Do not validate server certificate (insecure) | whether to verify the server certificate or not. |
| Use system proxy settings | Wether to use proxy settings or not. |
| ADFS | Whether to use ADFS server. |
| Compress encode URL (ADFS) | Check mandatory for ADFS encoding. |
| Service Identifier (ADFS)| | The ADFS relay identifier which XSOAR will redirect the user for SSO first login. |
| Identity Provider Single Logout URL | URL that users are sent to after logging out of the SAML session. |
| Single Logout Service Endpoint | Logout service with which SAML communicates. |
| Do not map SAML groups to Demisto roles | SAML groups will not be mapped to Demisto roles |
| Single logout - specify Name ID Format | Wether to use the Name ID format. |
| Name ID | | Defines the name identifier formats supported by the identity provider. |
| Use this instance for external authentication only | By checking this box you are limiting this instance to authenticate external (non-XSOAR) users when they enter to answer a survey sent via a communication task.