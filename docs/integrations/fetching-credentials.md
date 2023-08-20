---
id: fetching-credentials
title: Fetching Credentials
---

As seen [here](https://xsoar.pan.dev/docs/reference/articles/managing-credentials), it is possible to integrate with 3rd party credential 
vaults for Cortex XSOAR to use when authenticating with integrations. This article provides an example of such vault integration.

## Requirements

In order to fetch credentials to the Cortex XSOAR credentials store, the vault integration needs to be able to retrieve credential objects 
in the format of a username and password (key:value).

## Implementation

### isFetchCredentials Parameter
  
For this example we are going to look at the HashiCorp Vault integration. The first thing you need to do is add a boolean parameter with the name:
`isFetchCredentials`(You can give it a different display name). When this parameter is set to true, Cortex XSOAR will fetch credentials from the vault integration.

It would look like something like this: ![image](/doc_imgs/integrations/53886096-eae09600-4027-11e9-8c2d-a46078c3dcc4.png)  
![image](/doc_imgs/integrations/53886311-69d5ce80-4028-11e9-9755-08585fecff34.png)

### fetch-credentials Command

When Cortex XSOAR tries to fetch credentials from vault integrations, it will call a command called `fetch-credentials`.
This is where you should implement the credentials retrieving logic:
```python
if demisto.command() == 'fetch-credentials':
   fetch_credentials()
```

### Creating credentials objects

In the `fetch_credentials` function, you should retrieve the credentials from the vault and create new JSON objects in the format:
```json
{
  "user": "username",
  "password": "password",
  "name": "name"
}
```
In the end you should have a credentials list that contains the above objects:
```json
[
  {
    "user": "username_foo",
    "password": "password_foo",
    "name": "name_foo"
  },
  {
    "user": "username_bar",
    "password": "password_bar",
    "name": "name_bar"
  }
]
```
When you're done creating the credentials objects, send them to the credentials store by using:
```python
demisto.credentials(credentials)
```

### Logic
There are two scenarios that should be supported in `fetch-credentials` command:

#### 1. Fetch all credentials:
In order to have all relevant credentials from a vault integration visible and usable in other integrations, the `fetch-credentials` command will need to support the logic of pulling multiple credentials.
The best practice is to create a dedicated parameter in the vault integration which will allow the user to specify which credentials should be pulled.
Assuming this parameter is called `credential_names`:
```python
params: dict = demisto.params()
credentials_str = params.get('credential_names')
credentials_names_from_configuration = argToList(credentials_str)  # argToList is a wrapper to safely execute the str.split() function
credentials = []
for credentials_name in credentials_names_from_configuration:
    credentials.append(get_credentials(credentials_name))

demisto.credentials(credentials)
```

If everything went well you should be able to see the credentials in the Cortex XSOAR credentials store:
![image](/doc_imgs/integrations/53886981-f339d080-4029-11e9-9d27-a76b85d2d025.png)

Note that these credentials cannot be edited or deleted, they reflect what's in the vault. You can stop fetching credentials by unticking the 
`Fetch Credentials` checkbox in the integration settings.

#### 2. Fetch a specific set of credentials:
A user may choose to configure another integration using a set of credentials fetched by a vault integration: 

![image](/doc_imgs/integrations/choose_credentials.png)

Since XSOAR does not store the credentials in its DB, each time these credentials are used in the new configured integration, Cortex XSOAR
will query the vault integration for it.
In order to extract the specific credentials name use the `identifier` argument stored in `demisto.args()` this way:
```python
args: dict = demisto.args()
credentials_name: str = args.get('identifier')
try:
    credentials: list = [get_credentials(credentials_name)]
except Exception as e:
    demisto.debug(f"Could not fetch credentials: {creds_name}. Error: {e}")
    credentials = []

demisto.credentials(credentials)
```
:::note Important Note
When working with a specific credentials name (the `identifier` key), it is important to **always** return a list containing up to **one** set of credentials. In other words, it is important to catch errors that are part of this flow, and instead of raising them, return an empty list. If no list or a list with more than one element will be returned, the `credentials` tab will fail to load.
:::

#### The two scenarios together:
```python
params: dict = demisto.params()
args: dict = demisto.args()
credentials_str = params.get('credential_names')
credentials_names_from_configuration = argToList(credentials_str)  # argToList is a wrapper to safely execute the str.split() function
credentials_name: str = args.get('identifier')
if credentials_name:
    try:
        credentials: list = [get_credentials(credentials_name)]
    except Exception as e:
        demisto.debug(f"Could not fetch credentials: {creds_name}. Error: {e}")
        credentials = []
else:
    credentials = []
    for credentials_name in credentials_names_from_configuration:
        credentials.append(get_credentials(credentials_name))

demisto.credentials(credentials)
```

## Troubleshooting
- In case of an error during the process, you can debug your code by adding a test command that calls the `fetch_credentials` function.
Make sure you send a credentials list in the right format and as a valid JSON.

- In order to save API calls every time a credential is used, XSOAR uses a short time caching mechanism for fetched credentials, thus, it can be a bit hard to debug the second scenario. 
In order to override the caching mechanism you can set the caching timeout to 0 by navigating to: `Settings > ABOUT > Troubleshooting` and setting the following configuration key: `vault.module.cache.expire` to 0.
It is important to remove this configuration once debugging is done.






