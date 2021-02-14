---
title: Active Directory Authentication
description: Authenticate using Active Directory.
---

This integration enables using your Active Directory user authentication settings in Demisto. Users can log in to
 Demisto with their Active Directory username and passwords, and their permissions in Demisto will be set according
  to the groups and mapping set in Active Directory.

This integration requires the Read Access permission or higher.

### To set up the integration on Demisto:

1.  Go to __Settings > Integrations > Servers & Services__
2.  Locate the Active Directory Authentication integration by searching for it using the search box on the top of the page.
3.  Click __Add instance__ to create and configure a new integration. You should configure the following Active
 Directory and Demisto-specific settings:  
    **Name**: A textual name for the integration instance.  
    **Server IP**: The Active Directory server you are using.  
    **Port**: The port being used.  
    **Credentials and Password**: The username and password, or toggle to Credentials.  
    **Base DN** (e.g. DC=domain,DC=com):
    **Default Domain**: The default domain being used to connect to Active Directory.  
    **Security Type:** The security type you are using to connect to Active Directory such as none, SSL or TLS.  
    **Do not validate server certificate**: Select to avoid server certification validation. You may want to do this in case Demisto cannot validate the integration server certificate (due to missing CA certificate)  
    **Use system proxy settings**: Select whether to communicate via the system proxy server or not.  
    **Demisto engine**: If relevant, select the engine that acts as a proxy to the server.  
    Engines are used when you need to access a remote network segments and there are network devices such as proxies, firewalls, etc. that prevent the Demisto server from accessing the remote networks.  
    For more information on Demisto engines see:  
    [https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/engines](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/engines)  
    Require users to enter additional password: Select whether you’d like an additional step where users are required to authenticate themselves with a password.
4.  Press the ‘Test’ button to validate connection.  
    If you are experiencing issues with the service configuration, please contact Demisto support at [support@demisto.com](mailto:support@demisto.com)
5.  Auto populate groups mark this option to get Active Directory groups and add them as Roles in Demisto, by which
 Demisto permissions are set.
6.  After completing the test successfully, press the ‘Done’ button.

### Use-Cases

Use Active Directory user authentication groups to set user roles in Demisto.