---
title: Syslog (Deprecated)
id: syslog
description: Syslog events logger. Automatically convert incoming logs to incidents.
---

:::caution Deprecated
Use the Syslog v2 integration instead.
:::

A Syslog server provides the ability to automatically open incidents from Syslog clients.  
This integration provides the ability to filter which logs are to be converted to incidents (or choose to convert all logs).

## Configure Syslog on Demisto

1.  Configure a syslog client to send it's logs to the Demisto server address.
2.  Make sure to note which port and protocol the client is communicating with.

### To set up the integration on Demisto:

1.  Go to ‘Settings > Integrations > Servers & Services’
2.  Locate ‘Syslog’ by searching for it using the search box on the top of the page.
3.  Click ‘Add instance’ to create and configure a new integration. You should configure the following settings:  
    **Name**: A textual name for the integration instance.  
    **IP address**: The hostname or IP address of the listening machine. In most cases localhost, 127.0.0.1, or 0.0.0.0 to listen on all addresses. We recommend that you do not change this.  
    **Port**: The port being used.  
    **Protocol**: The protocol to use.  
    **Format**: The incoming logs' format.  
    **Filters**: You can configure various filters as conditions for automatically opening incidents from incoming logs. Leave all filters empty to automatically open incidents from all incoming logs. For more information and examples on filtering.  
    **Log content field as a filter for incident creation (Regex)**: Content field to use as a filter.  
    **Log message field as a filter for incident creation (Regex)**: Message field to use as a filter.  
    **Log tag field as a filter for incident creation (Equal)**: Tag field to use as a filter.  
    **Log client field as a filter for incident creation (Equal)**: Client field to use as a filter.  
    **Log hostname field as a filer for incident creation**: Hostname field to use as a filter.  
    **Log TLS peer field as a filter for incident creation (Equal)**: TLS peer field to use as a filter.  
    **Log app name field as a filter for incident creation**: App name to use as a filter.  
    **Log process id field as a filter for incident creation (Equal)**: Process ID field to use as a filter.  
    **Log message id field as a filter for incident creation (Equal)**: Message ID field to use as a filter.  
    **Log structured data field as a filter for incident creation**: Structured data field to use as a filter.  
    **Log version field as a filter for incident creation (Greater than)**: Version field to use as a filter.  
    **Log severity field as a filter for incident creation (Greater than).**: Severity field to use as a filter.  
    **Log priority field as a filter for incident creation (Greater than)**: Priority field to use as a filter.  
    **Log facility field as a filter for incident creation (Greater than)**: Facility field to use as a filter.
4.  Click **Test** to validate the URLs, ports, and connections.

## Fetched incidents data:

Incidents will be fetched from the moment the integration is enabled.  
All Syslog logs can be converted to incidents, depending on the chosen filters.  
**Note**: This applies only to incoming logs from the moment the integration was enabled (previously received logs will not be converted).

## Top Use-cases:

The following are examples of the top use-cases for this integration.

*   A specific client writes to syslog with severity 10.  
    The filter will consist of the "hostname" or "client" fields in combination with the "severity" field.  
    Example: in the log `{content: "update failed", severity: 10, priority: 24, client: "127.0.0.1"}`  
    a suitable filter will be: `client: "127.0.0.1", severity: "9"`
    
*   A specific product crashes.  
    The filter will consist of a regular expression containing the specific error and the product name on the log's "message" or "content" field.  
    Example: in the log `{content: "The product ProductName has crashed with error 42.", severity: 20, priority: 32, client: "127.0.0.1"}`  
    a suitable filter will be: `content: "(ProductName).*(crash).*"`
    

## Commands:

This integration does not have any commands as it runs as a service, creating new incidents from chosen logs.

## Known Limitations

The condition for creating an incident from a log is currently a combination of all chosen filters.  
This means that only 1 complex filter can be used at a given time.  
For example, if the filter "hostname" is applied with the value "localhost" and the filter "priority" is applied with the value "20", only logs with the hostname "localhost" AND priority greater than 20 will be filtered. In other words, all the filters need to exist for a log to qualify as an incident.

## Troubleshooting

*   Make sure the client address is correct.
*   Make sure the client is writing to the correct address.
*   Make sure both the client and server are configured to use the same protocol.
*   Make sure the port is correct on both the client and the server and not in use by another process or Demisto instance.
*   In case of bind fails due to permission error, try a port greater than 1024.
*   In case no logs are received, try restarting the syslog service on the client machine (e.g. "service rsyslog restart" on Ubuntu).
*   In the case of partial logs, try using a different logs format.

## Additional information:

This integration was integrated and tested using Ubuntu Desktop v16 as a client, default rsyslog service, TCP/UDP, RFC3164 Format.