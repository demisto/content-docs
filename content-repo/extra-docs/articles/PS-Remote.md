---
title: Powershell Remoting - Configuration
description: Overview of how to configure your Windows enviornment and XSOAR for the Powershell Remoting integration. 
---

Powershell Remoting is a built in capability in Windows hosts that enables to connect remotley and in order to execute scripts and Poweshell commands. By using Powershell Remoting the SOC analyst or incident resopnder will be able to connect to the windows host in oder to perform various tasks such as gathering data, remediating the host, move files to and from the host to XSOAR and much more.
## Pack Workflow
Follow this article to configure your Windows enviornment and the integration.

After configuring the integration you will be able to perform various tasks on Windows hosts. Including running Powershell commands and script as well as gather forensic data.

## In This Pack
The Powershell Remoting content pack includes.
### Integrations
The Powershell Remoting integration.

## Before You Start
### Disclaimer
The integration was created and tested on Windows 2016 win server with Powershell version 5.1.14393.3866. Configuration may vary to different windows server versions. Keep in mind that WinRM is entirely a Microsoft feature. We provide this manual “as is”. We highly recommend to perform all actions listed here on test/staging environments prior to implementing on production environments. Also it's important to notice that WinRM has security implications to consider as described [here](https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/winrmsecurity?view=powershell-7.1). The integration in its current version works with HTTP using NTLM authentication or HTTPS using basic authentication. PS remoting does encrypt the session event on HTTP however the initial connection is unencrypted while basic authentication is not considered a secure authentication method but since the whole session is encrypted via SSL this compensates for the less secure authentication method.

### Network Settings
Your XSOAR server will require access or ports 5985,5986 TCP
to the hosts to which you want to run the integration on. Take into consideration both the network firewall and the localhost firewall. In case of using the Windows firewall make sure to create a relevant GPO to allow traffic on the relevant ports. The configuration of the windows FW GPO is not in the scope of this article. Same goes for other local host FW agents. For WinRM over HTTPS open port 5986 TCP.

### Permissions
The user that will be used in order to execute the PS remote commands on the endpoint will require local admin credentials. Potentially more granular permissions can be applied however this was not tested and therefore not in the scope of this article.


### Domain Settings
For Windows 2016 env Active Directory domain perform the following

On your 2016 Domain controller create a new OU (Organizational Unit) and move the computer accounts to the new OU. 
To do so, open the Active DIrectory Users and Computers tool. Right Click on the Domain, select New and Organizational Unit.

For example

Now Drag and drop the computer account to the new OU.
Keep in mind that you can also use an existing OU. In this article we recommend creating a new OU for testing purposes.
GPO settings
Open the Group Policy Management tool. Right click on the OU for which you want to apply the GPO (where the relevant computer accounts are located) and select Create GPO in this domain and link it here.
Enable PS Remote

 
From Computer Configuration > Administrative Templates > Windows Remote Management (WinRM) > WinRM Service
Select Allow remote server management through WinRM
Select Enabled
Provide the IP or the XSOAR server, * is also a valid option but keep in mind that this will allow any address to initiate a WinRM connection to the affected hosts. This setting will enable Powershell remoting to the relevant hosts.

### Allow basic Authentication
Configure this setting only if you are interested in using Basic authentication and not Negotiate.
From Computer Configuration > Administrative Templates > Windows Remote Management (WinRM) > WinRM Service
Select Allow Basic Authentication
Select Enabled


### WinRM service

From Computer Configuration > Policies > Windows Settings > Security Settings > System Services
Select Windows Remote Management (WS-Management)

Select Define this Policy and Automatic service startup mode. This setting will ensure that the WinRM service will be started up automatically on the relevant hosts.

### Workgroup settings
It is possible to configure the integration to work in a workgroup (non domain) environment. Network settings and configuration are the same as described in the previous relevant section. To configure the host within the workgroup to accept PS remote connections perform the following settings. For the host that you wish to enable PS remoting. Open the Powershell command prompt as an administrator as an administrator and type Enable-PSRemoting.


## Pack Configurations
### Integration Configuration

Once the GPO has been applied and the settings are in effect. We can configure the integration instance settings and validate if the integration is working.

To configure the integration provide the following settings

### Domain:
Provide the DNS domain name For example winrm.local. This will allow the integration commands to work for hostnames and not just FQDN.

### DNS:
Provide the IP address of the DNS server to provide name resolution.

### Username:
Provide the Username with proper administrative privileges on the relevant hosts. If your are using Basic Authentication provide a local user and not a domain user.

### Password:
Provide the password for the user name.

### Test Hostname:
This optional parameter tests if the integration can perform a connection to a the specified host.

### Use SSL
This option enables the PS remote session to be encrypted with SSL. In order to configure your env to use SSL review the relevant section in the appendix. Currently SSL only works with basic authentication.

### Authentication Type
This option selects the authentication method used by the integration. Valid options are Basic which currently requires SSL and Negotiate which currently does not support SSL.
Testing the integration
The test button will perform the following. Test network connectivity to the host supplied as the test hostname and attempt to open a PSremote session to the specified host.

## Testing the Pack
## Troubleshooting
### Host Troubleshooting
One of the common issues with regards to working with WinRM is that the network connectivity was not properly configured. In order to test network connectivity we can check is the host is listening on the relevant port
For example logon to one of the hosts and run from the command prompt.
netstat -na 1 | find "5985"
The result should show that the host is listening on the port

In case the host is not listening on the port make sure the host actually received the GPO we previously configured.
From the command line run
gpresult /r -scope computer
The result should show under Computer settings and the Applied Group Policy Objects the GPO you created should appear as applied.


In case the GPO does not appear as applied make sure that the computer account is in the correct OU. If not make sure to move the computer account to the correct OU. Regardless if the computer account is in the OU, run from the hosts command line the command gpupdate /force


The result should show that the computer policy updated successfully.

## XSOAR Troubleshooting
First of all we provide in the integration settings the test option. From the integration settings provide all the relevant inputs and click on Test
In case no network connection is available or the host is not resolved or the username/password permissions are not working the following error will be displayed.

### Network connectivity
Another issue could be network connectivity from the XSOAR to the host. We can troubleshoot this by logging in to the XSOAR CLI and test connectivity by running the following command. sudo tcpdump -i any 'port 5985' This will display the traffic sent to the host. You can also see the raw traffic by running the command sudo tcpdump -i any -nnAs0 port 5985

In case you are not able to get a network connection to the host from XSOAR check the network or host firewall logs and adjust the rules accordingly.

### Authentication
Check the provided username and password by attempting to connect to the tested host locally or via Terminal services. Make sure that you are able to login with the provided credentials. If the login fails verify the username and password or that the user has sufficient privileges on the host. If the password is wrong, reset it in Active Directory.

In case you are using Basic Authentication make sure to provide a local user and not a domain user.

## WinRM Commands Useful Commands
For getting the WinRM configuration run on the host winrm get winrm/config

To test the connection status run Test-WSMan -ComputerName <The host name> -Authentication default -Credential <The username to connect with>

Perform a connection. Enter-PSSession -ComputerName <The host name>

Perform a connection with SSL. Enter-PSSession -ComputerName <The host name> -UseSSL

Check listener status. WinRM e winrm/config/listener

Configure WinRM to use SSL winrm quickconfig -transport:https

Delete HTTP listener winrm delete winrm/config/Listener?Address=*+Transport=HTTP

Delete HTTPS listener winrm delete winrm/config/Listener?Address=*+Transport=HTTPS

## Appendix

Open a command prompt as an administrator and run the command winrm set winrm/config/client @{TrustedHosts="*"}
### Configure WinRM over HTTPS For a Domain Environment
In order to enable PS remote over SSL perform the following
Certificate Services

Install a server with the Active Directory Certificate Services role with the Certification Authority sub role (this won't be covered by this article).


From your Active Directory Certificate Services server open the Certification Authority tool.


Right click on Certificate Templates and manage


Right click the Web Server template and select Duplicate Template

In the new template click on the General tab. Provide the new template name (for example WinRM). Select the validity period for the certificate.


Click on the Subject Name tab. Select Build from this Active Directory information. For Subject name format select Common Name. Under Include this information in alternate subject name select DNS name and deselect User principal name (UPN).

Click on the Security tab. Select the following permissions, Read, Enroll, Autoenroll. Click on OK. Your new template is now saved.

In the Certification Authority console click on Certificate Templates and New and Certificate Template to Issue

Select your new template and click OK.

### GPO
Open the GPMC (Group Policy Management Console) Create and link a new GPO to your relevant OU.

Edit the new GPO and navigate to Computer Configuration > Policies > Windows Settings > Security Settings > Public Key Policies > Certificate Services Client - Auto-Enrollment.

Under Configuration Model select enabled and click the checkbox for Update Certificates that use certificate templates

Review the Certification Authority and make sure a certificate was issued for your host

On the host you wish to configure WinRM with HTTPS open a command prompt as an administrator and type winrm quickconfig -transport:https

Since Microsoft doesn't currently have a GPO to set up the HTTPS listener it's possible to create a logon script that contains this command in it. Creation of logon script and deploying it via GPO is not covered in this article.
