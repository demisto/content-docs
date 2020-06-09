---
title: Connection issues troubleshooting guide
description: This article helps common troubleshooting issues with XSOAR integrations
---

# Connection issues troubleshooting guide
### When a customer has any connection errors try the following steps:
1. Check and uncheck the “insecure” checkbox
2. Check and uncheck the “proxy” checkbox
3. Try to isolate the problem, is it the integration instance server or the client?

    a. In case you have access from your local computer to the integration instance server, Try to generate the same request using curl or postman from your local computer (or customer’s computer)- if it fails: the integration instance server is probably down, could be instance issue.
    
    b. Try to do some curl from the XSOAR machine, for example: 
    ```
   curl https://httpbin.org/status/200  -vk
   ```
    and see if the returning status is 200

    c. Try to run some curl request via a docker container using 
    ```
   docker run -it demisto/netutils:1.0.0.6138 curl https://httpbin.org/status/200  -vk
   ```
   
    - If section c. fails and you suspect this is a proxy issue, try to run curl without proxy using 
    ```
   docker run -it demisto/netutils:1.0.0.6138 curl https://httpbin.org/status/200  -vk --noproxy "*"
   ```
   
    - If section b. worked and section c. failed: this could be a docker networking issue, see the following [link](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/5-5/cortex-xsoar-admin/docker/docker-hardening-guide/troubleshoot-docker-networking-issues) for guidance.
    - If section a. worked but sections b. and c. failed: This could possibly be an integration bug, open an issue with server log bundle and preferably a .pcap files of the commands attempts.
4. See if the customer’s firewall is blocking some packets during a command. Since some integrations has some internal redirection to different destination IPs. See this issue as an example

### Examples:
1. #### EWS v2 integration does not honor proxy settings with Engine:
    When proxy checkbox was unchecked AND engine was in use AND engine had proxy defined to connect to server, integration kept using proxy and fail requests.
    solved by setting the server config with 
    
    Key: `python.pass.extra.keys`
    
    Value: `--network=host`
2. #### VirusTotal Private API Issue:
    Client got the following exception `SSLError(SSLEOFError(8, u'EOF occurred in violation of protocol (_ssl.c:661)'),)`.
    
    solved by whitelisting a URL in the firewall.

