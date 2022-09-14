---
title: Troubleshooting Guide
description: Common troubleshooting steps for automations and integrations.
---

This guide provides common troubleshooting steps. When reporting an issue to Cortex XSOAR Support, always include all information obtained from running the following troubleshooting steps.

## Reverting a Pack to a Previous Version
If you encounter an issue after upgrading a Pack, you can revert to a previous version by going to *Installed Content Packs* -> *Pack Name* -> *Version History* and choosing *Revert to this version*. Sample screenshot:
![Revert to version](https://user-images.githubusercontent.com/1395797/106351932-0faf1800-62e8-11eb-9433-5c80c632cf33.png)



## Network Troubleshooting

Examples of common errors indicating that there probably is a networking issue:
* `[Errno -2] Name does not resolve`
* `[Errno 110] Operation timed out`
* `Failed to establish a new connection: [Errno -3] Try again`
* `dial tcp: lookup ****: no such host`
* `connect: operation timed out`
* `connect: connection refused`
* `ERR_CONNECTION_REFUSED`


When troubleshooting networking issues, it is important to first understand what type of networking the integration or automation is using. Cortex XSOAR integrations and automations can be classified into two main types regarding their networking use:

### Host Based Networking 
Integrations/automations running within the server/engine will use the networking stack provided by the host machine of the server/engine. Such integrations/automations include native integrations (part of the server binary) such as the `RemoteAccess` integration and JavaScript integrations such as `VirusTotal` and `http`. Native integrations can be identified by the fact that they are shipped as part of the server and not associated with a Content Pack. JavaScript integrations/automations can be identified by checking the integration/automation settings to see that the *Language Type* is **JavaScript**. JavaScript integrations/automations run within the Cortex XSOAR server/engine process using a JavaScript virtual environment and therefore use the same network stack as the server/engine. The source IP addresses for these integrations/automations are the same as used by the server/engine.


If the integration/automation is using HTTP-based communication, we recommend first testing locally using the `curl` utility to verify that it is possible to perform network communication with the HTTP endpoint. Run the `curl` command on the server or engine machine by logging in via SSH. Common `curl` command variants (`httpbin.org` is used as an example url):
```bash
# Run simple curl command with -v for verbose output:
curl -v https://httpbin.org/status/200

# Run with -k to trust any certificate in case you receive errors regarding certificates
curl -vk https://httpbin.org/status/200

# curl will use the machine env variables for proxy settings. If you wish to ignore the proxy settings run:
curl -vk --noproxy "*" https://httpbin.org/status/200

# Setting explicitly a proxy server to use by curl
curl -x http://192.168.0.1:8080 https://httpbin.org/status/200

# Passing an additional header as part of the curl request:
curl -v -H 'Accept: application/json' https://httpbin.org/headers

# In cases that the integration uses basic authentication, you can also easily test the credentials:
curl -v --user myuser:mypass https://httpbin.org//basic-auth/myuser/mypass
```

More info about `curl` is available at [Everything curl](https://ec.haxx.se/).

If you are not able to perform a basic `curl` request from the machine to the target HTTP endpoint, the issue is probably not a problem with the integration/automation but rather with the networking setup of the server/engine machine. Make sure to first resolve the networking issue so a basic `curl` command succeeds before continuing to test the integration/automation. Many times this resolves to a firewall, NAT or proxy issue. 

### Docker Based Networking
Docker Based integrations/automations are written in Python or Powershell. They can be identified by inspecting the integration/automation settings and under *Language type* will appear **Python** or **Powershell**. Docker creates its own networking, therefore the integrations/automations use a different networking stack from the Cortex XSOAR server/engine. The source IP addresses for these integrations/automations are different and provided according to the Docker networking configuration.

As with [Host Based Networking](#host-based-networking), for integrations/automations that use HTTP endpoints we recommend testing with `curl` from within a Docker container as a first step. This can be done by logging in to the server/engine machine via SSH and running the following command:
```bash
docker run -it --rm demisto/netutils:1.0.0.6138 curl <curl parameters>
```
For example:
```bash
# Run simple curl command with -v for verbose output:
docker run -it --rm demisto/netutils:1.0.0.6138 curl -v https://httpbin.org/status/200
```
For additional `curl` sample commands see the [Host Based Networking](#host-based-networking) section.

**Note**: You may need to run `docker` with `sudo` or login with root if your user doesn't have sufficient permissions to execute the `docker` command.

If running `curl` from within `docker` fails with networking errors, we recommend checking if the `curl` command succeeds or fails without `docker` by running the `curl` command directly on the host machine. If the `curl` command succeeds on the host machine and fails within Docker, you are probably experiencing a Docker networking issue due to how the Docker networking stack is configured. 

We recommend that you use the Docker networking stack because it provides networking isolation. Try to resolve the [Docker networking issue](https://success.docker.com/article/troubleshooting-container-networking) and consult the [Docker networking docs](https://docs.docker.com/network/). 

When running with Docker's networking stack continues to cause issues, there is an option to run Docker containers with host networking. In this mode, the container will share the host’s network stack and all interfaces from the host will be available to the container. The container’s hostname will match the hostname on the host system. You can test this mode by running a `curl` command via `docker` in the following form:
```bash
docker run -it --rm --network=host demisto/netutils:1.0.0.6138 curl -v https://httpbin.org/status/200
```

If running with `--network=host` succeeds, you can configure the server to use host networking for docker by adding the following advanced server configuration in Cortex XSOAR:

Key | Value
--- |  ----
`python.pass.extra.keys` | `--network=host`

It is also possible to configure only a specific docker image to use the host networking by stating `python.pass.extra.keys.<docker-image>` as the key. For example:

Key | Value
--- |  ----
`python.pass.extra.keys.demisto/smbprotocol` | `--network=host`


After you add the server configuration, run the `/reset_containers` command from the Cortex XSOAR CLI to reset all containers and to begin using the new configuration.

**Notes:**
* For multi-tenant deployments, you need to add this setting to each tenant.
* When using engines, you need to add this setting to each engine.



### Read Timeout
In case you encounter a *ReadTimeout* error, such as `ReadTimeout: HTTPSConnectionPool(host='www.google.com', port=443): Read timed out. (read timeout=10)`, it means that the server (or network) failed to deliver any data within 10 seconds. This might be due to a large response size.

Starting from Base Content Pack version 1.17.6, we support controlling the read timeout value via server advanced configuration, as follows:
* System wide

  Key | Value
  --- |  ----
  `python.pass.extra.keys` | `--env=REQUESTS_TIMEOUT=<TIMEOUT>`

* Per Integration

  Key | Value
  --- |  ----
  `python.pass.extra.keys` | `--env=REQUESTS_TIMEOUT.<INTEGRATION-ID>=<TIMEOUT>`

Examples: 

* Set the read timeout value to *120* seconds system wide, `--env=REQUESTS_TIMEOUT=120`
* Set the read timeout value to *75* seconds for the Palo Alto Networks WildFire v2 integration, `--env=REQUESTS_TIMEOUT.WildFire-v2=75`

**Note:** The `REQUESTS_TIMEOUT` settings only affects integrations which use the [BaseClient](https://xsoar.pan.dev/docs/integrations/code-conventions#client-class) class from CommonServerPython.


## TLS/SSL Troubleshooting

Examples of common errors indicating that there is an issue with trusting a TLS/SSL networking connection:

* `SSLCertVerificationError`
* `SSL_CERTIFICATE_VERIFY_FAILED`
* `SSL: CERTIFICATE_VERIFY_FAILED`
* `SSLError: certificate verify failed`

These errors are usually as a result of a server using an untrusted certificate or a proxy (might be transparent) that is doing TLS/SSL termination. 

**Notes**

* Most integrations provide a configuration option of *Trust any certificate*, which will cause the integration to ignore TLS/SSL certificate validation errors. You can use this option to test the connection and verify that in fact the issue is certificate related.
* To trust custom certificates in Cortex XSOAR server or engines, follow the following [instructions](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/docker/configure-python-docker-integrations-to-trust-custom-certificates).

### CertificatesTroubleshoot Automation
Use the [CertificatesTroubleshoot Automation](https://xsoar.pan.dev/docs/reference/scripts/certificates-troubleshoot) to retrieve and decode an endpoint certificate. Additionally, use it to retrieve, decode and validiate the custom certificates deployed in Docker containers. The automation is part of the [Troubleshoot Pack](https://xsoar.pan.dev/marketplace/details/Troubleshoot).

**Common reasons for TLS/SSL issues and resolutions**

* Endpoint certificate issues:
  * Expiration date - The certificate has a start and end date which is not valid anymore.

    * Identify: `Endpoint certificate` -> `General`-> `NotValidBefore/NotValidAfter`:

    ![image-20201018155224381](../../../docs/doc_imgs/reference/certificate-verification-expire-date.png)

    * Resolution: If the certificate expired, make sure to renew the certificate at the target endpoint.

  * Common name / Alt name -  A certificate signed only for a specific URI, For example, if the certificate is signed for `test.com` and the integration is accessing the endpoint using `test1.com` the certification validation will fail.

    * Identify: `Endpoint certificate` -> `Subject` -> `CommonName` and `certificate` -> `Extentions` -> `SubjectAlternativeName`:

      ![image-20201018160939173](../../../docs/doc_imgs/reference/certificate-verification-altnames.png)

      ![image-20201018160950403](../../../docs/doc_imgs/reference/certificate-verification-common-name.png)

    * Resolution: If the URI isn't matching the URI endpoint (Regex), try to access the endpoint with one of the alt names/common names. If the endpoint isn't accessible via trusted names, sign the certificate with the correct common name or apply an additional alt name.


## Fetch Incidents Troubleshooting
### Fetch History
In XSOAR Versions 6.8 and above, it is possible to observe the results of the last **fetch-incidents**/**fetch-indicators** runs using the Fetch History modal. To view the modal, click the button with the history icon next to the Integration Instance settings.
<img src="../../docs/doc_imgs/incidents/fetchhistory.gif"></img>

The following fields are stored for each record:

1. **Pulled At** - The date and time the fetch run was completed.
1. **Duration** - The length of time the fetch run took to complete.
1. **Last Run** - The contents of the last run object.
1. **Message** - Depending on the fetch run status, will be one of the following:
   - If successfully finished, how many Incidents/Indicators were pulled or dropped. If nothing was pulled or dropped, the message will be "Completed".
   - In case of an error, the error details.
   - In long-running integrations, the info/error message forwarded to `demisto.updateModuleHealth()`. The *is_error* boolean argument of this method determines the message type.
1. **Source IDs** - If available, displays the incident IDs as they appear in the 3rd-party product. The IDs are collected from incidents that contain the `dbotMirrorId` field.
   Note: the `dbotMirrorId` field should be determined at the integration level rather than the mapping level.

#### Server Configurations
| Key | Description | Default Value |
| --- | --- | --- |
| **fetch.history.size** | The amount of records stored for every instance. | 20 |
| **fetch.history.enabled** | Whether or not the feature is enabled. | true |

### Debugging
1. In case of a recurring issue with a fetching instance, follow [these steps](https://xsoar.pan.dev/docs/reference/articles/troubleshooting-guide#fetch-incidents-in-debug-mode) to produce a debug log of a single fetch run.

2. If the issue does not reproduce consistently:

   - [Set the log level](https://xsoar.pan.dev/docs/reference/articles/troubleshooting-guide#integration-debug-logs) of the specific instance for more convenient tracking of the fetch logs over time.
   - Keep track on the [Fetch History](https://xsoar.pan.dev/docs/reference/articles/troubleshooting-guide#fetch-history) of this instance. Consider temporarily setting the **fetch.history.size** server configuration to store more records.


## Debug Mode
Cortex XSOAR (Server 5.0+) supports running Python integration commands and automation scripts in `debug-mode` from the Cortex XSOAR CLI. When a command is run in `debug-mode` a log file of the command execution will be created and attached to the war room. When encountering an issue which is related to an integration or an automation, make sure to reproduce the command with `debug-mode` and inspect the generated log file. The `debug-mode` log file will contain information not available in the Server logs and can provide additional insights regarding the root cause of the issue. Additionally, some integrations have specific code to include extra debug info when run in `debug-mode`.

:::caution Important Note
The debug mode feature prints extended data from an integrations configuration and settings which may include sensitive information. Before sharing the generated log files, make sure sensitive information has been removed.
:::

### Run a command in `debug-mode`
In the Cortex XSOAR CLI run the command with all arguments that cause the issue and append the following argument: `debug-mode=true`. For example: 

```
!ad-search filter="(cn=Guest)" debug-mode=true
```

Screenshot of running a command with `debug-mode=true` and the resulting log file (`ad-search.log`):
![debug-mode-example](../../../docs/doc_imgs/reference/debug-mode-example.png)

### Test Integration Module in `debug-mode`
Starting with Cortex XSOAR 6.2 when you `Test` an integration module and it fails, you can download from the integration configuration dialog a `debug-mode` full report by following the link: **Run advanced test and download a full report**. Example screenshot:

![image](https://user-images.githubusercontent.com/1395797/169849803-56908773-0bb4-41b7-ae65-133454d51865.png)

If you require a `debug-mode` log when the `Test` from the integration configuration dialog succeeds, it is possible to run the test integration module command from the Cortex XSOAR CLI with `debug-mode=true`. This is done by issuing a command of the form:

```
!<instance_name>-test-module debug-mode=true
```

For example for an integration instance name of: `Cortex_XDR_instance_1` run the following from the CLI:

```
!Cortex_XDR_instance_1-test-module debug-mode=true
```


### Fetch Incidents in `debug-mode`
Starting with Cortex XSOAR 6.0 it is possible to run the fetch incidents command from the Cortex XSOAR CLI with `debug-mode=true`. This is done by issuing a command of the form:

```
!<instance_name>-fetch debug-mode=true
```

For example for an integration instance name of: `Cortex_XDR_instance_1` run the following from the CLI:

```
!Cortex_XDR_instance_1-fetch debug-mode=true
```

**Note:** if the instance name contains spaces, replace the space with an underscore (`_`).

Screenshot of running a `fetch` command with `debug-mode=true` and the resulting log file (`fetch-incidents.log`):
![fetch-incidents-debug](../../../docs/doc_imgs/reference/fetch-incidents-debug.png)

**Note:** 
- If the instance name contains spaces, replace the space with an underscore (`_`).
- The "Do not use by default" checkbox should be unchecked on the integration instance you are testing.

Screenshot of running a `test-module` command with `debug-mode=true` and the resulting log file (`test-module.log`):

![test-module-debug](../../../docs/doc_imgs/reference/test-module-debug.png)

## Integration Debug Logs
:::caution Important Note
The Integration Debug feature prints extended data from an integrations configuration and settings which may include sensitive information. Before sharing the generated **Integration-Instance** log files, make sure sensitive information has been removed.
:::
Starting with version 6.2, it is possible to create logs for an instance of an integration in order to get debug information for a specific instance over a period of time. 

This mode is especially useful for long running integrations such as EDL or TAXII-Server. It helps troubleshooting when it is not possible to run the desired command in `debug-mode` from the playground. Whether it is a long running integration, or the issue occurs from time to time such as with the ***fetch-incidents*** command.

For example, if you have an integration instance running the ***fetch-incidents*** command, and the integration misses some of the incidents, you may want to get debug level information for each ***fetch-incidents*** command (or any other command executed by this instance) even if the server log level is set to *Info*. If you move the server log level to *Debug*, the server log would contain a lot of irrelevant information for integration troubleshooting. For this reason, the *Log Level* configuration parameter was added to the integration configuration. 

There are three options for this parameter:
- Off
- Debug
- Verbose 

![Log Levels](../../../docs/doc_imgs/reference/log_level.png "Log Level")


In Debug mode, the server will run all the commands of this instance with a *Debug* log level and log the information in the **Integration-Instance** log.

In Verbose mode, additional information such as connections coming off device handling, the raw response, and all parameters and headers are logged in addition to the debug level information. 


For example, if an integration fails and the instance log level is *Debug*, the **Integration-Instance** log will contain the error stack trace. If the log level is *Verbose*, the **Integration-Instance** log will contain the error stack trace, but also a copy of the HTTP request, the parameters used in the integration, what the response was, etc.

By default, the *Log Level* configuration parameter is set to *Off*.

The **Integration-Instance.log** is located in  `/var/log/demisto/`.

These log level modes are only for the configured instance and do not affect the log for the entire server.

Note that the log level configuration for an integration instance may affect performance of the integration instance, therefore use this feature only for troubleshooting and set it to Off when you have the required information in the log.
