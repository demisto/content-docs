---
title: Active Directory Authentication
description: Authenticate using Active Directory.
---

This integration enables using your Active Directory user authentication settings in Cortex XSOAR. Users can log in to
 Cortex XSOAR with their Active Directory username and passwords, and their permissions in Cortex XSOAR is set according
  to the groups and mapping set in Active Directory.

This integration requires read access permission or higher.

### To set up the integration on Cortex XSOAR:

1.  Go to __Settings > INTEGRATIONS > Servers & Services__
2.  Locate the **Active Directory Authentication** integration.
3.  Click __Add instance__ to create and configure a new integration. You should configure the following settings:  
    - **Name**: A textual name for the integration instance.  
    - **Server IP**: The Active Directory server you are using.  
    - **Port**: The port being used.  
    - **Credentials and Password**: The username and password, or toggle to Credentials.  
    - **Base DN**: For example, DC=domain, DC=com.
    - **Default Domain**: The default domain being used to connect to Active Directory.  
    - **Security Type:** The security type you are using to connect to Active Directory such as none, SSL or TLS.  
    - **Do not validate server certificate**: Select to avoid server certification validation. You may want to do this in case Cortex XSOAR cannot validate the integration server certificate (due to missing CA certificate).  
    - **Auto populate groups**: Select this option to get Active Directory groups and add them as roles in Cortex XSOAR, by which
 Cortex XSOAR permissions are set.
    - **Full path for CA certificate of Active Directory server (type pem)**: Type the path to the server file system where the CA certificate of the LDAP is located. Add this if you use your own certificate.
     - **Single engine**: If relevant, select the engine that acts as a proxy to the server.  
    Engines are used when you need to access a remote network segments and there are network devices such as proxies, firewalls, etc. that prevent the Cortex XSOAR server from accessing the remote networks.  
    For more information about engines see:  
    [https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-admin/engines](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-2/cortex-xsoar-admin/engines)  
5.  Click **Test** to validate connection.  
    If you are experiencing issues with the service configuration, contact Cortex XSOAR support. 
6.  After completing the test successfully, click **Save & exit**.

### Use-Cases

Use Active Directory user authentication groups to set user roles in Demisto.

### Server Configurations

After you have successfully set up your integration, you may want to customize attributes such as `name`, `mail`, and `phone` fields as the user's AD attributes. You can change the following configurations, by selecting **Settings > ABOUT > Troubleshooting > Add Server Configuration**:

|Key| Description |
|--|--|
|`ad.login.name`| The value is the attribute `name` to take the `name` value from. Default is `name`.|
|`ad.login.mail`| The value is the attribute `mail` to take the `mail` value from. Default is `mail`.|
|`ad.login.phone`| The value is attribute `phone` to take the `phone` value from. Default is `telephoneNumber`.|
|`ad.login.phone.pull`| Set to `true` to fetch the phone number as well as other attributes. Default is `false`.| 
