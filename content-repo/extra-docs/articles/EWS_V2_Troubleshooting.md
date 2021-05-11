---
id: EWS_V2_Troubleshooting
title: EWS V2 Troubleshooting  
description: The following provides EWS V2 troubleshooting steps to perform before contacting Cortex XSOAR customer support for help.
---


Exchange Web Services (EWS) provides the functionality to enable client applications to communicate with the Exchange server. EWS provides access to much of the same data that is made available through Microsoft OfficeOutlook.

For information on the EWS V2 integration, see [EWS v2](https://xsoar.pan.dev/docs/reference/integrations/ews-v2).


## Docker Issues
The following are possible Docker issues that may occur. If you are not running Docker, you will not be able to run any Office 365 compliance search commands (ews-o365-*).

- [Not Running Docker](#not-running-docker)
- [How to Install Docker](#how-to-install-docker)

### Not Running Docker 

To run Office 365 non-compliance search commands without running Docker, install the following python packages:
- asn1crypto==0.24.0
- cached-property==1.4.2
- certifi==2018.4.16
- cffi==1.11.5
- chardet==3.0.4
- cryptography==2.3.1
- defusedxml==0.5.0
- dnspython==1.15.0
- enum34==1.1.6
- exchangelib==1.12.0
- future==0.16.0
- idna==2.6
- ipaddress==1.0.22
- isodate==0.6.0
- lxml==4.2.1
- ntlm-auth==1.1.0
- pycparser==2.18
- Pygments==2.2.0
- pykerberos==1.2.1
- python-dateutil==2.7.3
- pytz==2018.4
- requests==2.18.4
- requests-kerberos==0.12.0
- requests-ntlm==1.1.0
- six==1.11.0
- tzlocal==1.5.1
- urllib3==1.22
- virtualenv==15.0.3



### How to Install Docker 
1. If Cortex XSOAR is installed on Red Hat (RHEL), install Docker CE on RHEL.
   1. Run ***sudo yum-config-manager --enable rhel-7-server-extras-rpms***.
   2. Download the following rpms:
      - http://mirror.centos.org/centos/7/extras/x86_64/Packages/container-selinux-2.119.2-1.911c772.el7_8.noarch.rpm
      - http://mirror.centos.org/centos/7/extras/x86_64/Packages/pigz-2.3.3-1.el7.centos.x86_64.rpm
      - https://download.docker.com/linux/centos/7/x86_64/stable/Packages/docker-ce-18.03.1.ce-1.el7.centos.x86_64.rpm (This is the Docker installation rpm.)
   3. Install the rpms one by one in the above order. The installation command is
       ***sudo yum install -y &lt;rpm_filename&gt;.rpm***.
   4. Run ***sudo usermod -aG docker demisto***.
2. Get the latest Demisto Docker images by running ***docker pull demisto/py-ews:2.0***. If this command fails, refer to https://support.demisto.com/hc/en-us/articles/360001649634-Docker-Image-Air-Gapped-Installation.
3. Verify that you can Docker curl to the EWS server.
   1. Run the demisto/py-ews:2.0 Docker image:

      ***docker run -it demisto/py-ews:2.0 bash***
   2. From inside the Docker container, run:

      ***curl -v https://&lt;Server&gt;/EWS/Exchange.asmx/***
3. If Docker cannot curl to the EWS server, restart the Docker service.
4. If the issue is not resolved, contact Cortex XSOAR customer support.

## Instance Test Failed
The following are common EWS V2 error messages indicating that the instance test failed. To fix the problem, perform the applicable troubleshooting steps.
- [Import error: No module named ExchangeLib](#import-error-no-module-named-exchangelib)
- [Max timeout reached](#max-timeout-reached)
- [Got unauthorized from the server](#got-unauthorized-from-the-server)
- [No such folder](#no-such-folder)
- [Got timeout from the server](#got-timeout-from-the-server)

If your instance failed and none of these error messages appear, contact Cortex XSOAR customer support.

### Import error: No module named ExchangeLib
If this error occurs, follow the instructions in [How to Install Docker](#how-to-install-docker).

### Max timeout reached
1. Locate the status code in the logs.
   1. Download the server logs.
   2. Open the *server.log* file (or *d1.log* when using engine).
   3. Search for *Max timeout reached*.
   4. Go to the last (or second last) result.
   5. Locate the line:

      *RateLimitError: Max timeout reached (gave up after X seconds. URL Y returned status code Z)*
    2. If the status code is *401*, continue. Otherwise, contact Cortex XSOAR customer support.     
2. If the status code is *401*,
   1. Check the exchange server version.
      - For Office 365, the version should be 2016.
      - For the On-premise Exchange Server, check with your IT Administrator. (For server version 2010, check the service pack as well).
   2. Verify the user credentials.
      1. Check that the user is not locked.
      2. Try to log in to Outlook Web Access with the user credentials.
      3. Re-enter the password in the integration configuration field.
   3. Verify the authentication method.
      - For Office 365, the authentication method should be *Basic*.
      - For On-Premise Exchange Server, the authentication method should be *NTLM*.

         **Note:** 
         - Configure the authentication method even if SAML is being used.
         - Check if Digest authentication is required. 
   4. Run the instance test again.
   5. If the error still occurs, contact Cortex XSOAR customer support.

### Got unauthorized from the server
1. Verify your credentials.
2. Run the instance test again.
3. If the integration test still fails, contact Cortex XSOAR customer support.

### No such folder
1. Find the desired folder’s name by running

   ***!ews-find-folder target-mailbox=&lt;target mailbox&gt;***

2. If the target mailbox folders are shown in a right-to-left-language, copy and paste the folder name(s) directly from the output into the *Name of the folder from which to fetch incidents* field. (The reason for this is RTL languages in Exchange have invisible characters, so simply typing their names in the folder path won’t work. You must copy and paste each filename in the path from the output of !ews-find-folders.)
2. Verify that the user in the *Authentication* field has access to the target mailbox and the folder.
4. Run the instance test again.
3. If the error still occurs, contact Cortex XSOAR customer support.


### Got timeout from the server
1. Check if the proxy is needed.
   - For Exchange URL or Server IP address: Write only the IP address (without “https://” or “/ews/exchange.asmx”).
   - For Proxy: Check or uncheck as needed.
4. Run the instance test again.
3. If the error still occurs, contact Cortex XSOAR customer support.


## Instance Test is Successful but Error Occurs
The following are examples of error messages that may occur even if the instance test is successful:
- Python script failed due to timeout - see [Docker Issues](#docker-issues)
- [No such folder](#no-such-folder)


## Problem Fetching Incidents
1. Synchronize the clock of the Cortex XSOAR server. Use NTP to synchronize the server’s clock with an NTP server.
2. If Cortex XSOAR is installed on CentOS, update the CentOS packages by running the following commands and restart the server.
   - ***sudo yum check-update***
   - ***sudo yum update***
3. Update the Docker service and restart it.
4. In the integration settings, 
   1. Click *Reset the "last run" timestamp*.
   2. Click *Reset Now*.
5. If the error still occurs, contact Cortex XSOAR customer support.






