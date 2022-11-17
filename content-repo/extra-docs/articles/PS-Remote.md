---
id: Powershell_Remoting_-_Configuration
title: Powershell Remoting - Configuration
description: Overview of how to configure your Windows environment and XSOAR for the PowerShell Remoting integration. 
---

PowerShell Remoting is a built-in feature in Windows hosts that enables connecting to hosts remotely in order to execute scripts and PowerShell commands. By using PowerShell Remoting, the SOC analyst or incident responder is able to connect to the Windows host in order to perform various tasks such as gathering data, remediating the host, move files to and from the host to XSOAR, and much more.
## Pack Workflow
Follow the instructions in this article to configure your Windows environment and the PowerShell Remoting integration.

After configuring the integration you will be able to perform various tasks on Windows hosts, including running PowerShell commands and scripts, as well as gather forensic data.

## In This Pack
The PowerShell Remoting content pack includes the following content item.
### Integrations
The [PowerShell Remoting](https://xsoar.pan.dev/docs/reference/integrations/power-shell-remoting) integration.

## Before You Start
Disclaimer: The integration was created and tested on Windows Server 2016 with PowerShell version 5.1.14393.3866. This article provides configuration instructions for this environment. Your required configuration may vary if using a different Windows Server version. Keep in mind that WinRM is entirely a Microsoft feature. We highly recommend you perform all actions listed here on test/staging environments prior to implementing on production environments. Also it's important to note that WinRM has security implications to consider as described [here](https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/winrmsecurity?view=powershell-7.1). 

The integration in its current version works with HTTP using NTLM authentication or HTTPS using basic authentication. PowerShell remoting does encrypt the session even on HTTP; however, the initial connection is unencrypted. If you decide to use basic authentication keep in mind it isn`t considered a secure authentication method; however, since the whole session is encrypted via SSL this compensates for the less secure authentication method.

### Network Settings
Your XSOAR server will require access on ports 5985,5986 TCP
to the hosts on which you want to run the integration. Take into consideration both the network firewall and the localhost firewall. If using the Windows firewall, make sure to create a relevant Group Policy Object (GPO) to allow traffic on the relevant ports. The configuration of the Windows firewall GPO is not in the scope of this article. The same goes for other local host firewall agents. For WinRM over HTTPS, open port 5986 TCP.

### Permissions
The user who will execute the PowerShell remote commands on the endpoint will require local admin credentials. Potentially more granular permissions can be applied; however, this was not tested and therefore not in the scope of this article. For basic authentication make sure to use a local user and not a domain user.


### Domain Settings
For a Windows 2016 environment Active Directory domain, perform the following.

On your 2016 Domain Controller, create a new OU (Organizational Unit) and move the computer accounts you wish to enable Powershell Remoting on to the new OU. 
1. Open the Active Directory Users and Computers tool. 
2. Right-click the domain, and select **New** > **Organizational Unit**.

For example:
 !["Organizational Unit"](https://raw.githubusercontent.com/demisto/content-docs/1b625fbf790242cfc36ac079e1c3f5e027015d19/docs/doc_imgs/reference/PowershellRemoting/1-OU.JPG "Organizational Unit")

3. Drag and drop the computer account to the new OU.
 !["Organizational Unit"](https://raw.githubusercontent.com/demisto/content-docs/bdf04770e31fc2f821053bfeea7353893480e318/docs/doc_imgs/reference/PowershellRemoting/2-OU.JPG "Organizational Unit")

Keep in mind that you can also use an existing OU. In this article we recommend creating a new OU for testing purposes.
### GPO settings
1. Create a new GPO.
   1. Open the Group Policy Management tool. 
   2. Right-click the OU for which you want to apply the GPO (where the relevant computer accounts are located) and select **Create GPO in this domain and Link it here**.
!["Group Policy Management tool"](https://raw.githubusercontent.com/demisto/content-docs/bdf04770e31fc2f821053bfeea7353893480e318/docs/doc_imgs/reference/PowershellRemoting/3-gpo.JPG "Group Policy Management tool")

   3. Provide a name for the new GPO and click **OK**.
 !["Group Policy Management Object"](https://raw.githubusercontent.com/demisto/content-docs/bdf04770e31fc2f821053bfeea7353893480e318/docs/doc_imgs/reference/PowershellRemoting/4-gpo.JPG "Group Policy Management Object")

    4. Right-click the new GPO and click **Edit**.
 !["Group Policy Management Object"](https://raw.githubusercontent.com/demisto/content-docs/057a6ef277e847775b6ee401d757a15088f97618/docs/doc_imgs/reference/PowershellRemoting/4_1-gpo.jpg "Group Policy Management Object")
 
2. Enable PowerShell Remote

   1. Navigate to **Computer Configuration** > **Policies** > **Administrative Templates** > **Windows Components** >**Windows Remote Management (WinRM)** > **WinRM Service**.
   2. Select **Allow remote server management through WinRM**.
   3. Click **Edit policy setting**.
   4. Select **Enabled**.
   4. Provide the IP or the XSOAR server. * is also a valid option but keep in mind that this will allow any address to initiate a WinRM connection to the affected hosts. 
   5. Click **OK**.
   
   This setting will enable Powershell remoting to the relevant hosts.
 !["Allow remote server management"](https://raw.githubusercontent.com/demisto/content-docs/057a6ef277e847775b6ee401d757a15088f97618/docs/doc_imgs/reference/PowershellRemoting/5-gpo.JPG "Allow remote server management")

3.  Allow Basic Authentication. 
Configure this setting only if you want to use Basic authentication and not Negotiate.

    1. Navigate to **Computer Configuration** > **Policies** > **Administrative Templates** > **Windows Components** >**Windows Remote Management (WinRM)** > **WinRM Service**.
    2. Select **Allow Basic Authentication**.
    3. Click **Edit policy setting**.
    3. Select **Enabled**.
    5. Click **OK**.
!["Allow basic Authentication"](https://raw.githubusercontent.com/demisto/content-docs/057a6ef277e847775b6ee401d757a15088f97618/docs/doc_imgs/reference/PowershellRemoting/6-gpo.JPG "Allow basic Authentication")

4. Configure the WinRM service.

   1. Navigate to **Computer Configuration** > **Policies** > **Windows Settings** > **Security Settings** >**System Services**.
   
   2. Select **Windows Remote Management (WS-Management)**.

   !["WinRM service"](https://raw.githubusercontent.com/demisto/content-docs/de30769a3caa7d8d880563ff613857c7486fbcbf/docs/doc_imgs/reference/PowershellRemoting/7-gpo.JPG "WinRM service")

   3. Select **Define this policy setting**.
    
   4. Select **Automatic** for the service startup mode. This setting will ensure that the WinRM service will be started automatically on the relevant hosts.

   5. Click ***OK**.

!["WinRM service startup"](https://raw.githubusercontent.com/demisto/content-docs/de30769a3caa7d8d880563ff613857c7486fbcbf/docs/doc_imgs/reference/PowershellRemoting/8-gpo.JPG "WinRM service startup")

### Workgroup settings
It is possible to configure the Powershell Remoting to work in a workgroup (non-domain) environment. The network settings and configuration are the same as described in the [Domain Settings](#domain-settings) section. To configure the host within the workgroup to accept PowerShell remote connections:

1. For the host on which to enable PowerShell remoting, open the Powershell command prompt as an administrator and type **Enable-PSRemoting**.

!["Enable-PSRemoting"](https://raw.githubusercontent.com/demisto/content-docs/de30769a3caa7d8d880563ff613857c7486fbcbf/docs/doc_imgs/reference/PowershellRemoting/14-workgroup.JPG "Enable-PSRemoting")
2. From the Administrative command line run the command **winrm set winrm/config/client @{TrustedHosts="*"}**.
!["Trusted hosts"](https://raw.githubusercontent.com/demisto/content-docs/057a6ef277e847775b6ee401d757a15088f97618/docs/doc_imgs/reference/PowershellRemoting/15-workgroup.JPG "Trusted hosts")


## Integration Configuration

Once the GPO has been applied or the workgroup settings are in effect, configure the integration instance settings and validate if the integration is working.

To configure the integration, provide the following settings.

| Field | Description|
| --- | ---|
| Domain | Provide the DNS domain name (suffix). For example, winrm.local. This allows the integration commands to work for hostnames so the user won't have to supply the FQDN of hosts when running the integration commands. |
| DNS | Provide the IP address of the DNS server to provide name resolution. Make sure your XSOAR machine has access to the DNS server on port 53. |
| Username | Provide the username that has proper administrative privileges on the relevant hosts. If you are using Basic Authentication, provide a local user on the hosts and not a domain user. |
| Password | Provide the password for the username provided. |
| Test Hostname | This optional parameter tests if the integration can perform a connection to a the specified hostname. |
| Use SSL | This option enables the PS remote session to be encrypted with SSL. In order to configure your environment to use SSL, see [Configure WinRM over HTTPS For a Domain Environment](#configure-winrm-over-https-for-a-domain-environment). Currently, SSL only works with basic authentication. |
| Authentication Type | This option selects the authentication method used by the integration. Valid options are Basic which currently requires SSL and Negotiate which currently does not support SSL.|

## Testing the Integration
When you click **Test** in the integration settings, it will perform the following on the host specified in the Test Hostname parameter.
* Attempt to resolve the hostname specified.
* Attempt to test connectivity via ports 5985 or 5986 (if SSL is enabled).
* Attempt to open a PowerShell Remote session to the host.

If the test fails, an error message will describe at which point an error occurred. Review the [Troubleshooting](#troubleshooting) section for further assistance.

## Troubleshooting
- [Host Troubleshooting](#host-troubleshooting)
- [XSOAR Troubleshooting](#xsoar-troubleshooting)
- [Name Resolution Troubleshooting](#name-resolution-troubleshooting)
- [Network Connectivity Troubleshooting](#network-connectivity-troubleshooting)
- [Authentication Troubleshooting](#authentication-troubleshooting)
- [Incidents Injestions Delays](#incidents-injestions-delays)

### Host Troubleshooting
A common issues with regards to working with WinRM is that the network connectivity is not properly configured. 

To test network connectivity, check if the host is listening on the relevant port.
For example, log in to one of the hosts and run the following from the command prompt:

**netstat -na 1 | find "5985"**

or

**netstat -na 1 | find "5986"**

The result should show that the host is listening on the port.
!["Netstat"](https://raw.githubusercontent.com/demisto/content-docs/de30769a3caa7d8d880563ff613857c7486fbcbf/docs/doc_imgs/reference/PowershellRemoting/9-trouble.JPG "Netstat")

If the host is not listening on the port, make sure the host actually received the GPO that was previously configured.

From the command line run: 
**gpresult /r -scope computer**
!["gpresult"](https://raw.githubusercontent.com/demisto/content-docs/de30769a3caa7d8d880563ff613857c7486fbcbf/docs/doc_imgs/reference/PowershellRemoting/10-trouble.JPG "gpresult")
The GPO you created should appear under COMPUTER SETTINGS and the Applied Group Policy Objects.
!["Applied GPO"](https://raw.githubusercontent.com/demisto/content-docs/de30769a3caa7d8d880563ff613857c7486fbcbf/docs/doc_imgs/reference/PowershellRemoting/10-trouble.JPG "Applied GPO")

If the GPO does not appear, make sure that the computer account is in the correct OU. If not, make sure to move the computer account to the correct OU. Regardless if the computer account is in the OU, from the hosts command line run the **gpupdate /force** command.
!["Gpupdate /force"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/11-trouble.JPG "Gpupdate /force")

The result should show that the computer policy updated successfully.

Keep in mind that port 5985 is for HTTP and port 5986 is for HTTPS. In order to configure HTTPS follow the configuration provided in the [Configure GPO](#configure-gpo) section in the [Appendix](#appendix).

### XSOAR Troubleshooting
If when you click **Test** in the integration settings no network connection is available or the host is not resolved or the username/password permissions are not working, the relevant errors will be displayed. Resolve the issue as needed.

### Name Resolution Troubleshooting
If you receive the following error in the integration test, make sure that you provided a valid DNS server address in the integration settings and that the DNS server has a relevant DNS record for the host you want to resolve.
Also make sure your XSOAR has network access on port 53 to the DNS server.
!["DNS resolve error"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/error1.jpg "DNS resolve error")
### Network Connectivity Troubleshooting
If you receive the following error in the integration test, verify you have network access to the tested host from XSOAR on ports 5985 or 5986 accordingly. Check the network or host firewall logs and adjust the rules accordingly.
!["Network access error"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/error2.jpg "Network access error")
### Authentication Troubleshooting
If you receive the following error in the integration test, check the provided username and password by attempting to connect to the tested host locally or via terminal services. Make sure that you are able to login with the provided credentials. If the login fails, verify that the username and password are correct or that the user has sufficient privileges on the host. If the password is wrong, reset it in the Active Directory.
!["Session error"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/error3.jpg "Session error")

If you are using Basic Authentication, make sure to provide a local user and not a domain user.
Another issue could be related to the Powershell remoting settings. Review the [Host Troubleshooting](#host-troubleshooting) section above accordingly.

### Incidents Injestions Delays
You might come across cases where your incidents are pulled into XSOAR with some delay, in such cases we recommend checking that the given username does not include the domain in it, this should solve the delay problems.

## WinRM Useful Commands
The following provides a list of useful WinRM commands.
| To... | Command |
| --- | --- |
| Get the WinRM configuration run on the host. | **winrm get winrm/config** | 
| Test the connection status run. | **Test-WSMan -ComputerName *The host name* -Authentication default -Credential *The username to connect with*** |
| Perform a connection. | **New-PSSession -ComputerName *The host name*** |
| Perform a connection with SSL. | **New-PSSession -ComputerName *The host name> -UseSSL*** |
| Check listener status. | **WinRM enumerate  winrm/config/listener** |
| Configure WinRM to use SSL. | **winrm quickconfig -transport:https** |
| Delete HTTP listener. | **winrm delete winrm/config/Listener?Address=*+Transport=HTTP** |
| Delete HTTPS listener. | **winrm delete winrm/config/Listener?Address=*+Transport=HTTPS** |


## Appendix

### Configure WinRM over HTTPS For a Domain Environment
To enable PowerShell remote over SSL perform the following.

#### Configure Certificate Services

1. Install a server with the Active Directory Certificate Services role with the Certification Authority sub-role. (This procedure is not covered by this article.) 


2. From your Active Directory Certificate Services server, open the Certification Authority tool.
!["CA settings"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/18-cert.JPG "CA settings")

3. Right-click **Certificate Templates** and select **Manage**.
!["CA settings"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/19-cert.JPG "CA settings")

4. Right-click **Web Server** and select **Duplicate Template**.
!["CA settings"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/20-cert.JPG "CA settings")

5. In the new template, click the **General** tab. Type the new template name (for example WinRM) and select the validity period for the certificate.
!["CA settings"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/21-cert.JPG "CA settings")

6. Click the **Subject Name** tab and select **Build from this Active Directory information**. For the Subject name format,  select **Common Name**. Under Include this information in alternate subject name, select **DNS name** and deselect **User principal name (UPN)**.
!["CA settings"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/22-cert.JPG "CA settings")

7. Click the **Security** tab and select the following permissions:
    - Read
    - Enroll
    - Autoenroll

!["CA settings"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/23-cert.JPG "CA settings")

8. Click **OK**. Your new template will now be saved.
8. In the Certification Authority console, click **Certificate Templates** > **New** > **Certificate Template to Issue**.
!["CA settings"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/24-cert.JPG "CA settings")

9. Select your new template and click **OK**.
!["CA settings"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/25-cert.JPG "CA settings")
#### Configure GPO
1. Open the GPMC (Group Policy Management Console).
2. Create and link a new GPO to your relevant OU.
!["Cert GPO"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/26-gpo.JPG "Cert GPO")

3. Edit the new GPO and navigate to **Computer Configuration** > **Policies** > **Windows Settings** > **Security Settings** > **Public Key Policies** > **Certificate Services Client - Auto-Enrollment**.
!["Cert GPO"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/27-gpo.JPG "Cert GPO")

4. Under Configuration Model, select **Enabled** and click the checkbox for **Update Certificates that use certificate templates**. 
!["Cert GPO"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/28-gpo.JPG "Cert GPO")

5. Click **OK**.

6. Review the Certification Authority and make sure a certificate was issued for your host.
!["Issued certificates"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/29-cert.JPG "Issued certificates")

7. On the host on which you want to configure WinRM with HTTPS, open a command prompt as an administrator and type **winrm quickconfig -transport:https**.
!["Administrator"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/13-workgroup.JPG "Administrator")
!["Configure HTTPS"](https://raw.githubusercontent.com/demisto/content-docs/e017a13b2b37d1107c6cce33cb788163f716230a/docs/doc_imgs/reference/PowershellRemoting/30-ssl.JPG "Configure HTTPS")

Since Microsoft doesn't currently have a GPO to set up the HTTPS listener, it is possible to create a login script that contains this command. Creation of a login script and deploying it via GPO is not covered in this article.

#### Configure a Non-CA Environment 
If you do not have a Certificate Authority in your environment it is possible to use self signed certificates. The configuration self signed certificates is not in the scope of this article.
