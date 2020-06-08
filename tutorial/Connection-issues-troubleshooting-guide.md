# Connection issues troubleshooting guide
### When a customer has any connection errors try the following steps:
1. Check and uncheck the “insecure” checkbox
2. Check and uncheck the “proxy” checkbox
3. Try to isolate the problem, is it the server or the client?

    a. Try to generate the same request using curl or postman from your local computer (or customer’s computer)- if it fails: server is probably down, could be instance issue.
    
    b. Try to do some curl from the demisto machine, for example: 
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
   
    - If section b. worked and section c. failed: this could be a docker networking issue, see the following link for guidance.
    - If section a. worked but sections b. and c. failed: This could possibly be an integration bug, open an issue with server log bundle and preferably a .pcap files of the commands attempts.
4. See if the customer’s firewall is blocking some packets during a command. Since some integrations has some internal redirections to different destination IPs. See this issue as an example

### Examples:
1. [EWS v2 integration does not honor proxy settings with Engine](https://github.com/demisto/etc/issues/24900) - solved by setting the server config with Key: python.pass.extra.keys Value: --network=host
2. [VirusTotal Private API Issue](https://github.com/demisto/etc/issues/23626) - solved by whitelisting a URL in the firewall.

