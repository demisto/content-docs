---
title: Troubleshooting Guide
description: Common troubleshooting steps for XSOAR on-prem, XSOAR SaaS, and XSIAM.
---

This guide provides common troubleshooting steps. When reporting an issue to Cortex XSOAR Support, always include all information obtained from running the following troubleshooting steps.

## Troubleshooting tools

### Debugging

#### Debug Mode

Cortex XSOAR (Server 5.0+) supports running Python integration commands and automation scripts in `debug-mode` from the Cortex XSOAR CLI. When a command is run in `debug-mode` a log file of the command execution will be created and attached to the war room. When encountering an issue which is related to an integration or an automation, make sure to reproduce the command with `debug-mode` and inspect the generated log file. The `debug-mode` log file will contain information not available in the Server logs and can provide additional insights regarding the root cause of the issue. Additionally, some integrations have specific code to include extra debug info when run in `debug-mode`.

:::caution Important Note
The debug mode feature prints extended data from an integrations configuration and settings which may include sensitive information. Before sharing the generated log files, make sure sensitive information has been removed.
:::

##### Run a command in `debug-mode`

In the Cortex XSOAR CLI run the command with all arguments that cause the issue and append the following argument: `debug-mode=true`. For example:

```
!ad-search filter="(cn=Guest)" debug-mode=true
```

Screenshot of running a command with `debug-mode=true` and the resulting log file (`ad-search.log`):
![debug-mode-example](../../../docs/doc_imgs/reference/debug-mode-example.png)

#### Test Integration Module in `debug-mode`

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

**Note:** 
- If the instance name contains spaces, replace the space with an underscore (`_`).
- The "Do not use by default" checkbox should be unchecked on the integration instance you are testing.

Screenshot of running a `test-module` command with `debug-mode=true` and the resulting log file (`test-module.log`):

![test-module-debug](../../../docs/doc_imgs/reference/test-module-debug.png)

#### Fetch Incidents in `debug-mode`

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

#### Integration Debug Logs

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

### Reverting a Pack to a Previous Version

If you encounter an issue after upgrading a Pack, you can revert to a previous version by going to *Installed Content Packs* -> *Pack Name* -> *Version History* and choosing *Revert to this version*. Sample screenshot:
![Revert to version](https://user-images.githubusercontent.com/1395797/106351932-0faf1800-62e8-11eb-9433-5c80c632cf33.png)

### Troubleshoot pack

[The pack](https://cortex.marketplace.pan.dev/marketplace/details/Troubleshoot/) contains multiple automatons and playbook to run in the UI to help you troubleshoot and find various issues.

## General troubleshooting

This section contains steps that are suggested to do for all kind of issues regardless of what mechanism they relate to.

### Check for recent pack updates

When an error occurs in one of your packs, try to find out if a recent update took place in the pack related to the error. You can go check the version history under Marketplace > installed content packs >  choose the specific pack having the issue.
Try to review the version history to find whether there was a change related to your field or error.
Alternatively, you can revert the pack to the last version you were using and see if the problem still occur.
If it does - then it’s likely that there’s an issue with the configuration (point to the configuration troubleshooting page) or there’s a specific edge case that didn’t occur before.
If it doesn’t, then there might be some issues with the integration configuration (point to the configuration troubleshooting page)
If no recent updates were done to the pack (or recent updates were done but there’s an even newer version), it is recommended to try and update the pack version to the latest version as there might be some fixes that came out lately.

### Reconfigure to reauthenticate

Since some integrations execute authentication flows as a part of the integration configuration and the test-module execution. It’s recommended to try and configure a new instance when facing issues.

### Check whether the issue is wider

First thing you should do when facing an error with some integration, is to test whether other integrations are working or not. If they do, then it’s recommended to try and go over the other general steps, or alternatively, try and classify what the issue is related to and check specific issues troubleshooting (link to the TOC).
If similar errors seem to occur with other integration then there might be some issues with the tenant itself. If you’re  using Xsoar 6, then these issues might be Network issues and it’s recommended to go over the following troubleshooting steps (link to the network troubleshooting section)

### Retry

Some errors may be temporary errors. it is always recommended to wait a few minutes and then try to repeat what you did before to ensure it wasn't a temporary issue.

## Integration/Playbook/Script errors

### Can the issue be identified from the error? What type of error are you seeing?

#### Docker error

Docker timeout: A timeout error indicates a run that exceeded the default timeout configured for the docker container. This could be handled 
Make sure Docker/Podman is installed on your machine (on-prem) 

#### API error

Check the error received and try to see if it explains the issue. It could be related to missing permission, authentication, or API-specific issue.
Permissions: Compare the permissions required by the integration in Cortex to what the user has configured in his 3rd party product. If the integration does not mention specific permissions, check the 3rd party API.
Authentication: Re-check authentication parameters (credentials, IDs, etc), and try to re-configure them. Some integrations require different authentication flow, make sure to check the integration docs and verify you have covered the correct flow.

#### Common HTTP codes

401/403: Usually means that authentication failed. See the authentication section and Permissions sections above.
429: RAte limit means that too many requests were issued by the user to the server.
500: Internal server error usually implies the server was unable to process the request, make sure integration-specific parameters are entered correctly and are well formatted.
Python error
Sometimes you will be able to see a traceback that indicates a syntax error. In such cases it’s best to open a ticket that points to the exact error and this kind of tickets are usually handled within 3-5 days.

#### Network error

Note that this part is only relevant for XSOAR on-rem.
Examples of common errors indicating that there probably is a networking issue:
* `[Errno -2] Name does not resolve`
* `[Errno 110] Operation timed out`
* `Failed to establish a new connection: [Errno -3] Try again`
* `dial tcp: lookup ****: no such host`
* `connect: operation timed out`
* `connect: connection refused`
* `ERR_CONNECTION_REFUSED`


When troubleshooting networking issues, it is important to first understand what type of networking the integration or automation is using. Cortex XSOAR integrations and automations can be classified into two main types regarding their networking use:

##### Host Based Networking

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

##### Docker Based Networking

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



##### Read Timeout
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


##### TLS/SSL Troubleshooting

Examples of common errors indicating that there is an issue with trusting a TLS/SSL networking connection:

* `SSLCertVerificationError`
* `SSL_CERTIFICATE_VERIFY_FAILED`
* `SSL: CERTIFICATE_VERIFY_FAILED`
* `SSLError: certificate verify failed`

These errors are usually as a result of a server using an untrusted certificate or a proxy (might be transparent) that is doing TLS/SSL termination. 

**Notes**

* Most integrations provide a configuration option of *Trust any certificate*, which will cause the integration to ignore TLS/SSL certificate validation errors. You can use this option to test the connection and verify that in fact the issue is certificate related.
* To trust custom certificates in Cortex XSOAR server or engines, follow the following [instructions](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-0/cortex-xsoar-admin/docker/configure-python-docker-integrations-to-trust-custom-certificates).

##### CertificatesTroubleshoot Automation
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

### Playbooks issues

#### Failing to obtain value from previous task

Make sure the data type is configured as "From Previous Tasks" rather than "As value".

#### Not seeing any task outputs

New playbooks are set to quiet-mode by default. Make sure to unquiet them.

## Fetch issues

### Fetch History

It is possible to observe the results of the last **fetch-incidents**/**fetch-indicators**/**fetch-events** runs using the Fetch History modal. To view the modal, click the button with the history icon next to the Integration Instance settings.
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

#### Server Configurations (for XSOAR on-prem)

| Key | Description | Default Value |
| --- | --- | --- |
| **fetch.history.size** | The amount of records stored for every instance. | 20 |
| **fetch.history.enabled** | Whether or not the feature is enabled. | true |

#### Check the fetch history for the following

##### Temporary error from the API

Sometimes fetch mechanism can encounter temporary issues when calling the API, such issues will usually appear once or twice before getting back to fetch normally and will contain the 500 (internal server) error.

##### Params collision

In some integrations, there are params that can’t be configured together and will throw an error if they do. The error should appear in the fetch history and should be informative about which two params can’t be configured together.

##### Error from the API related to malformed params

Sometimes an error can come up from the API informing us that there was an issue with the params passed as part of the request, this error usually occurs in integrations where there’s a free-text filter param that might be malformed, double check all params are correct and ensure the error message doesn’t point to such issue.

##### getting 429 (rate limit) error

Some APIs have a rate limiter in their system configured to a certain value that might be reached. when getting 429 try to increase the fetch interval as it will result less calls in a certain amount of time, and raise the limit as it usually affect the number of calls due to the data being fetched in less time.

### Debugging Fetch incidents

1. In case of a recurring issue with a fetching instance, follow [these steps](https://xsoar.pan.dev/docs/reference/articles/troubleshooting-guide#fetch-incidents-in-debug-mode) to produce a debug log of a single fetch run.

2. If the issue does not reproduce consistently:

   - [Set the log level](https://xsoar.pan.dev/docs/reference/articles/troubleshooting-guide#integration-debug-logs) of the specific instance for more convenient tracking of the fetch logs over time.
   - Keep track on the [Fetch History](https://xsoar.pan.dev/docs/reference/articles/troubleshooting-guide#fetch-history) of this instance. Consider temporarily setting the **fetch.history.size** server configuration to store more records.

### Events mismatch

In some cases there might be some discrepancy between the events being shown in the UI compare to the events being shown in the 3rd party app.
In such cases it’s recommended to do the following:
Re-check the timezones of the events in the query - sometimes the time appears in the event in the UI is different than the one in the 3rd party due to time zone differences, ensure the times point to the same TZ.
Double check for any filter params in the configurations - sometimes the integration configuration will contain filter params - an open text filter, drop down to a specific field optional values, etc.. if you see events missing in the UI, double check those events doesn’t match the existing filters in the integration configuration page. In particular, make sure the filter does not point to past time.
Make sure suspicious missing events cannot be found using ID.

### Delay in the fetch/ingestion

in case you’re having aggregated delays between the fetched events and the real time events. Try to increase the limit parameter up to the its maximum (usually documented), ensure the fetch interval is set to the lowest, and in some integrations, the fetch attempts to fetch from multiple endpoints/entities. In that case, try to separate the integration instance into several instances each fetching from one endpoint/entity to maximize the productivity.
If you’re still having delays, try to get an estimation of the average amount per day and see if that amount co-op with the amount you manage to retrieve in a given minute. Sometimes the fetch mechanism can’t fully co-op with the peak times of the day but can make up for that during the quiet hours.

## Mirroring issues

### In what mirroring direction does the error occur?

When configuring mirroring instance you can choose between incoming, outgoing, or both mirroring direction.

If the issue occur with outgoing mirroring, then the issue is either the change is not detected in XSOAR/XSIAM side, or it is not received on the other side. To ensure the issue is not related to the connection with the othe side, most integrations has a manual command that does the same (update incident fields in the remote) if the integration you’re using has some command, try to run it and see if it trigger chanes in the remote.
Also, in some integrations, like Microsoft for example, writing to the remote require more permissions, try to make sure your instance has all the required permissions to write to the remote.
To ensure the issue is not with the modification mechanism, try to run update-remote-system command from the specific incident’s war room. You can also add the debug-mode=true to try and get extra information about the issue (error, response code).

If the issue occur with incoming mirroring, then there’s either an issue with connecting to the remote and retrieving the information from or there are issues with the mapper and updating the incident. 
To ensure the issue is not related to the remote, try to run `get-remote-data` command from the specific incident’s war room. You can also add the debug-mode=true to try and get extra information about the issue (error, response code).
To ensure the issue is not related to the mapper, double check that the mapper is indeed configured and contains the expected field.

### The case occur only using a custom mapper/field

Double check the mapper and field, ensure they are mapped correctly, you can use this guide for further assistance: https://xsoar.pan.dev/docs/integrations/mirroring_integration

### Does it only occur for a specific field

Try to double check the field is mapped correctly in the mapper tab (show how to get there), ensure the right field in the response is mapped to the right field in the mapper.

### Ensure all the parameters are correct

Ensure all the parameters are configured as expected, the instance is indeed a fetching instance, the incident expected to be mirrored indeed came from that specific instnace, the mirroring direction is configured, in case other fields such as tags or closing parameters also exist, ensure they’re marked if expected to be working.

## CI/CD issues

There are currently no known recurring CI/CD issues. Most CI/CD issues are related to the sdk section (add link).
For more information about setting up and developing CI/CD enviorenment: https://xsoar.pan.dev/docs/reference/packs/content-management

## VS code extension issues

### Try to classify whether the issue is related to VS code or demisto-sdk

When there’s an error related to vs code, the error will usually pop up at the bottom-right of the screen and will be informative. Try to follow the error and solution.
When there’s an error related to the demisto-sdk, the issue will usually appear in the terminal with traceback to demisto-sdk code. To ensure the issue is with demisto-sdk, you can try and manually execute the command from the terminal and see if the issue still occur.
For more information about how to troubleshoot the SDK refer to (link to the sdk)
For more information about the VS Code extension, refer to the official docs: https://xsoar.pan.dev/docs/concepts/vscode-extension

### Setup integration/script environment fails

Is docker set up correctly? Make sure docker is up and running, make sure that Allow the default docker socker to be used (required password) is enabled in Docker advanced settings.
If docker is up and running and the issue still occur, try to clean up the docker (https://docs.docker.com/engine/manage-resources/pruning/) or sign in to docker (https://www.docker.com/blog/seamless-sign-in-with-docker-desktop-4-4-2/)  to avoid rate limit (https://docs.docker.com/docker-hub/usage/#:~:text=Pull%20rates%20limits%20are%20based,to%205000%20pulls%20per%20day.)
Ensure the command was triggered on the integration / script itself by right click the code file > choosing setup integration/script environment (can add photo)
In this case a message saying "Please run this from an
integration or script directory". will pop up.

## TIM issues

### Missing indicators in the threat intel page

Sometimes indicators that were fetched cannot be seen in the threat intel page, if you encounter such an issue, double-check the exclusion list and ensure the indicator is not a part of the list (* add photos)

### A mismatch between the number of fetched indicators and the number of new indicators in the threat intel page

Sometimes some of the fetched indicators are already known to the system. In that case, the existing indicator will be modified rather than recreated. You can double-check the number of new / omitted/modified indicators in the logs (add the exact line to search).

### Failing to obtain indicators from 3rd party application using Taxii server

Ensure the issue is not related to the 3rd party, attempt to obtain the indicators using postman to make sure the searched URL is indeed correct.

### Failing to connect to the ‘Generic export indicators’ service

Make sure the Xsoar IP (add a link to the list) is whitelisted in the customer’s firewall.

### Getting 500 (internal server error) when attempting to connect to ‘Generic export indicators’

Double-check that the user & password configured are correct, incorrect credentials may throw 500 error. Also, note that the password is case-sensitive.

### Connecting to ‘Generic export indicators’ takes a lot of time

Double check the parameters, if the ‘Use Legacy Queries’ parameter is checked and not needed, make sure to uncheck it. If the issue still persists, try to raise the ‘XSOAR Indicator Page Size’ parameter.

## XQL issues

### Dataset discrepancy

Failing to save modeling / parsing rules - when attempting to edit modeling / parsing rules from the UI, may sometimes lead to dataset mismatches leading to an error msg informing that there were error to an unrelated data set (i.e. editing pack 'X' modeling rules can cause an error message claiming there're errors with data set of pack 'Y') In such cases, the marketplace can also be affected and you may encounter errors when attempting to download packs.
As a short-term solution, remove the pack related to the dataset mentioned in the error message so your tenant would un-stuck.
As a long-term solution, contact our Siem developers team via our support to inform them about the datasets mismatch.

## Demisto-sdk issues

### Try to make sure it's a bug

SDK commands does not include all kind of functionalities. Sometimes what seems to be a bug is actually a feature request. Double check the documentation using `demisto-sdk <command-name> --help` to ensure there's indeed something that doesn't work.

### Make sure you're up to date

As demisto-sdk is a developers tool variously used, it's being updated very often (at least twice a month) and a lot of bugs are being fixed as part of these releases.
When encountering an error, check that you're running on the latest update and there's no newer version.
To update to a specific version run

```bash
pip install demisto-sdk==x.y.z
```

To update to the latest version run

```bash
pip install demisto-sdk --upgrade
```

### Make sure the environment is configured correctly

Make sure all condition are met in "Prerequisite" section in [Install Demisto SDK|https://docs-cortex.paloaltonetworks.com/r/1/Demisto-SDK-Guide/Install-Demisto-SDK].
Make sure all condition are met in [Environment variables setup|https://docs-cortex.paloaltonetworks.com/r/1/Demisto-SDK-Guide/Environment-variables-setup].
For more information, refer to the [official demisto-sdk docs.|https://docs-cortex.paloaltonetworks.com/r/1/Demisto-SDK-Guide]
