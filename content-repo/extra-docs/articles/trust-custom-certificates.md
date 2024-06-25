---
id: trust-custom-certificates
title: Configure Server and Integrations to Trust Custom Certificates
description: Setup the Server and JS/Native Integrations to Trust Custom Certificates.
---
:::note
This article is relevant only for Cortex XSOAR 6 server or engines and Cortex XSOAR 8 cloud or on-prem engines.
:::

Server initiated communication (for example, downloading a pack from the Marketplace), Javascript integrations, and native integrations use the built-in set of CA-signed certificates of the host machine to validate TLS communication. If you use an engine, the engine also uses CA-signed certificates. You can add custom trusted certificates to the host built-in set.
For Python Docker integrations, you need to create a certificate file that includes the custom certificates and configure Cortex XSOAR to use it. For more information for configuring Cortex XSOAR 6, see [Configure Python Docker Integrations to Trust Custom Certificates](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/6.12/Cortex-XSOAR-Administrator-Guide/Configure-Python-Docker-Integrations-to-Trust-Custom-Certificates). For more information for configuring Cortex XSOAR 8 cloud see [Configure Docker Integrations to Trust Custom Certificates](https://docs-cortex.paloaltonetworks.com/r/Cortex-XSOAR/8/Cortex-XSOAR-Administrator-Guide/Configure-Docker-Integrations-to-Trust-Custom-Certificates).
 
1. Add the certificate to the machine’s trusted ROOT CA Bundle. The location of the CA Bundle depends on the version of the operating system and the operating configuration.
  Examples of certificate bundle paths:  

  "/etc/ssl/certs/ca-certificates.crt", // Debian/Ubuntu/Gentoo etc.  
  "/etc/pki/tls/certs/ca-bundle.crt", // Fedora/RHEL 6  
  "/etc/ssl/ca-bundle.pem", // OpenSUSE  
  "/etc/pki/tls/cacert.pem", // OpenELEC  
  "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem", // CentOS/RHEL 7  
  "/etc/ssl/cert.pem", // Alpine Linux

  Examples of certificate bundle directories:  

  "/etc/ssl/certs", // SLES10/SLES11, https://golang.org/issue/12139  
  "/etc/pki/tls/certs", // Fedora/RHEL

2. Restart the server.

3. Restart the engine (if applicable).
