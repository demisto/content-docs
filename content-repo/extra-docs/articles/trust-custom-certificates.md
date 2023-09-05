---
id: trust-custom-certificates
title: Configure Server and Integrations to Trust Custom Certificates
description: Setup the Server and JS/Native Integrations to Trust Custom Certificates.
---

Server initiated communication (for example, downloading a pack from the marketplace), Javascript integrations, and native integrations use the built-in set of CA-Signed certificates of the host machine to validate TLS communication. If you are using an engine, the engine also uses CA-Signed certificates. You can add custom trusted certificates to the host built-in set. (In addition, you will need to [configure Python Docker integrations to trust custom certificates](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-9/cortex-xsoar-admin/docker/configure-python-docker-integrations-to-trust-custom-certificates.html).)
 
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
