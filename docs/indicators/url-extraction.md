---
id: url-extraction
title: URL Extraction
---


The Cortex XSOAR URL indicator type is built using regular expression and a formatting script.
The following describes the URL extraction components and what output you should expect when extracting indicators of type URL.

## URL Extraction Components

There are two components when extracting URL indicators:
- Regular expression
- Formatting script

### Regular Expression

When text is given, a URL regular expression will try to catch a valid URL based on the following characteristics:
- A URL prefixed by one of the following protocols:
   - http
   - https
   - ftp
   - ftps
   - hxxp (defanged hxxp)
   - hxxps (defanged hxxps)
- A URL with ASCII or non-ASCII characters
- Escaped and unescaped URLs
- URL with or without query parameters

### Formatting Script

After extracting the URL using regular expression, a  **FormatURL** formatting script iterates on each given URL and does the following:

1. If the URL is prefixed by a URL defense system, Proofpoint or ATP, the script extracts the redirected URL and continues with steps 3-6 for the original and extracted redirected URL.
2. If the URL is NOT prefixed by a URL defense system, Proofpoint or ATP, the script checks if the first query parameter is a *redirected URL* query parameter by checking if the first parameter value starts with *http* or *https*.

   The following is an example of such a query parameter: 
   
   `https://www.good.site/index.html?redirectURL=https://evil.com/mal.html`

   If such a query parameter exists, the script extracts the redirected URL and performs steps 3-6 both for the given URL and the one extracted from the query parameter.

3. Replaces "[.]" with "." .
   
   For example:

   `https://www[.]evil.com → https://www.evil.com`

4. Decodes the URL.

   For example: 

   `https://www.test.com%2F%21%40 → https://www.test.com/!@`

5. Converts obfuscated characters.

   For example:

   `hxxp → http`

   `hxxps → https`

6. Returns the formatted URL.

## Common URL Structures

The following are some of the most common URL structures that Cortex XSOAR supports:

- `http://öevil.tld/`

- `https://evilö.tld/evil.html`

- `www.evilö.tld/evil.aspx`

- `https://www.evöl.tld/`

- `www.evil.tld/resource`

- `http://xn--e1v2i3l4.tld/evilagain.aspx`

- `https://www.xn--e1v2i3l4.tld`

- `hxxps://www.xn--e1v2i3l4.tld`

- `hxxp://www.xn--e1v2i3l4.tld`

- `www.evil.tld:443/path/to/resource.html`
  
- `https://1.2.3.4/path/to/resource.html`

- `1.2.3.4/path`

- `1.2.3.4/path/to/resource.html`

- `http://1.2.3.4:8080/`

- `http://1.2.3.4:8080/resource.html`

- `http://☺.evil.tld/`

- `http://1.2.3.4`

- `ftp://foo.bar/resource`

- `ftps://foo.bar/resource`

For more information about indicator extraction, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/manage-indicators/auto-extract-indicators).