---
title: Remote Access
description: File transfer and execute commands via ssh, on remote machines.
---

This integration enables Demisto to access and run commands on a terminal in a remote location (via SSH). For example this could be used to connect to a remote machine and search for malicious files.

Can be used via the Demisto CLI or in a Playbook.

## Use SSH with a Custom Certificate
To use the Remote Access integration with a custom certificate you need to add custom credential and then add the certificate.

1. Navigate to Settings > Integrations > Credentials.
2. Click the New button.

| **Field** | **Description** |
| --- | --- |
| Credential Name |	A meaningful name for the credential that you will select when configuring the Remote Access integration |
| Username | Username of the user you are creating the credentials for |
| Workgroup | Workgroup the user is member of |
| Password | Password |
| Certificate | Custom certificate to use for these credentials |

3. When you configure the integration instance, make sure you select the credentials you created.

## Configure the Remote Access Integration on Demisto
1. Go to ‘Settings > Integrations > Servers & Services’
1. Locate the Remote Access integration by searching for it using the search box on the top of the page.
1. Click ‘Add instance’ to create and configure a new integration. You should configure the following Remote Access and Demisto-specific settings:
    
    **Name**: A textual name for the integration instance.
    
    **Default Hostname or IP Address**: The hostname or IP address of the Remote Access Make sure the URL is reachable with respect to IP address and port.

    **Credentials and Password**: Configure credentials in the Credentials section in Demisto, including a valid certificate. Ciphers: Specify the ciphers to use for the inception. To use more and one cipher divide between then with commas (,).
    The supported ciphers are: “aes128-ctr”, “aes192-ctr”, “aes256-ctr” and “aes128-gcm@openssh.com”, “arcfour256”, “arcfour128".

    **Interactive terminal mode (checkbox)**: When using this option Demisto cleans the response from the remote machine.

    **Terminal Type**: The terminal emulator program to use such as xterm (default), GNOME Terminal, Konsole, and Terminal.

    **Demisto engine**: If relevant, select the engine that acts as a proxy to the server.
    Engines are used when you need to access a remote network segments and there are network devices such as proxies, firewalls, etc. that prevent the Demisto server from accessing the remote networks.
    For more information on Demisto engines see [here](https://demisto.zendesk.com/hc/en-us/articles/226274727-Settings-Integrations-Engines)

    **Require users to enter additional password**: Select whether you’d like an additional step where users are required to authenticate themselves with a password.

4. Press the `Test` button to validate connection.
After completing the test successfully, press the `Done` button.

## Commands
* **copy-from** - Copy file from remote system to war room
* **copy-to** - Copy file from war room to remote system
* **ssh** - Run command on remote system with ssh