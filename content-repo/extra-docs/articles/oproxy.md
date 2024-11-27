---
title: OProxy
description: Service for OAuth2 authentication with 3rd party vendors.
---

OProxy is a service that is developed and maintained by Cortex XSOAR on Google Cloud. It is used to facilitate in performing an OAuth2 authentication flow with a 3rd-party vendor (e.g., Microsoft).

The 2 main functions of the OProxy service is to provide Cortex XSOAR Integrations the following:
* A dedicated *Application* to be used as part of the OAuth2 authentication process.
* A well known redirect URI to be used as part of the authorization flow (usually configured as part of the *Application* settings).

## High Level Authorization Flow
1. User accesses an OProxy url to start the authorization flow (for example: https://oproxy.demisto.ninja/ms-graph-mail-listener).
2. User is prompted to authenticate to the 3rd Party Service and grant the requested permissions for the OProxy *Application*.
3. OProxy service registers the grant.
4. **Configuration Settings** (usually: *ID*, *Token* and *Key*) are returned to the user's browser.
5. User copies the **Configuration Settings** to the Integration instance configuration.
6. The Integration then may use the copied **Configuration Settings** to either communicate directly with the 3rd party service (such as in the case of the Slack Integration) or request from OProxy an authentication token to be used to communicate directly with the 3rd party service (such as in the case of MS Graph Integrations).

## Obtaining an Access Token from OProxy

In cases that the 3rd party service uses temporary access tokens the Integration will fetch via OProxy periodically an access token which it will use to authenticate and communicate directly with the 3rd party service. There is need to obtain the Access Token via Oproxy, as Oproxy controls the *Application* configuration data (usually client id and client secret) needed as part of the request for an Access Token. 

The integration will use the **Configuration Settings** obtained during the authorization flow. The **Configuration Settings** includes the following parameters:

1. **ID**: A unique UUID used by OProxy to identify the **Configuration Settings**. The ID is used for lookup from OProxy's database the relevant data associated with the specific settings.
2. **Token**: Data needed to generate access tokens. OProxy does not persist this data on its end. The **Token** is passed to the Integration for storage. It stores a secure hash of the **Token** which is used to verify the **Token** value when an *Access Token Request* comes in. For example in MS Graph Integrations using the delegated auth flow, this will be the [refresh token](https://docs.microsoft.com/en-us/graph/auth-v2-user#5-use-the-refresh-token-to-get-a-new-access-token) used for generating access tokens. In MS Graph Integrations using the [admin consent](https://docs.microsoft.com/en-us/graph/auth-v2-service#4-get-an-access-token) flow, this will be the tenant GUID. 
3. **Key**: A unique random encryption key used for a second layer of encryption for sending the configuration **Token** from the Integration to OProxy. The **Key** is stored by OProxy and the Integration.

### Access Token Request (Integration -> OProxy)
To request an *Access Token*, the Integration sends a json POST request to the OProxy https endpoint. The json object will contain the following fields:
* `app_name`: A name identifying the Integration. Allows a single OProxy https endpoint to support multiple integrations.
* `registration_id`: The **Configuration Settings ID**
* `encrypted_token`: The **Configuration Settings Token** encrypted with the **Configuration Settings Key** using the following algorithm: 
  ```
  nonce = <12 bytes secure random>
  encrypted_token = BASE64(nonce + AESGCM(nonce, key, <TIMESTAMP in EPOCH SECONDS>:<Configuration Settings Token>))
  ```
  The source code of the encryption algorithm can be viewed [here](https://github.com/demisto/content/blob/master/Packs/ApiModules/Scripts/MicrosoftApiModule/MicrosoftApiModule.py) (see the `get_encrypted` function).
* `scope`: Permission scope of the requested access token. 

### Access Token Response (Oproxy -> Integration)
When Oproxy receives an Access Token Request is will perform the following steps:
*  Use `registration_id` to lookup the **Configuration Settings Key** and the **Token Hash**.
*  Decrypt the `encrypted_token` value to obtain the **Configuration Settings Token** and encryption timestamp.
*  Verify the timestamp is within an accepted time range. If not, deny the request.
*  Verify the **Token Hash** for the decrypted **Token**. If not, deny the request.
*  Use the decrypted **Token** together with the OProxy application settings (client id and client secret) to request a new **Access Token**. If communicating with a 3rd party service which supports refresh tokens, include in the request an argument asking for a new refresh token.
*  Return a json response containing the following fields:
   *  `access_token`: the Access Token obtained from the 3rd party service.
   *  `refresh_token`: the Refresh Token obtained from the 3rd party service (if relevant). The Refresh Token should be used as the **Token** data in further requests from the Integration to Oproxy.
   *  `expires_in`: expiration of the Access Token in seconds.

### Notes
The credentials created for the following integrations are valid for a single instance only: **AzureSentinel**, **AzureLogAnalytics**, **MicrosoftGraphListener**.