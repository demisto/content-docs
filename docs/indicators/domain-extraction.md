---
id: domain-extraction
title: Domain Extraction
---

The Cortex XSOAR domain indicator type is built using regular expression and a formatting script.
The following describes the domain extraction components and what output you should expect when extracting indicators of type domain.

## Domain Extraction Components

There are two components when extracting domain indicators:
- Regular expression
- Formatting script

### Regular Expression

When text is given, a domain regular expression will try to catch a valid domain based on the following characteristics:
- A domain with ASCII and non-ASCII characters.
- Escaped and unescaped domains.

The regular expression can extract domains from one of the following:
- Explicit domain.
- URL.
- Email address.

### Formatting Script

After extracting the domain using a regular expression, an **ExtractDomainAndFQDNFromUrlAndEmail** formatting script iterates on each given domain and does the following:

1. Replaces "[.]" with ".".
	
	For example:
 
	`www[.]evil.com --> www.evil.com`

2. Validate the Top-Level-Domain to avoid file extension false positives.
	
	Excludes ‘.zip’ Top-Level-Domain by default.

3. Returns the formatted domain.

## Common Domain Structures

The following are some of the most common domain structures that Cortex XSOAR supports:

- `test.com`
- `www.test.com`
- `xn--t1e2s3t4.com`
- `www.xn--t1e2s3t4.com`
- `www.test.co.uk`
- `test.co.uk`
- `subtest.test.com`
- `www.test.test.com`
- `ötest.com`
- `testö.com`
- `www.testö.com`
- `www.teöst.com`

For more information about indicator extraction, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/manage-indicators/auto-extract-indicators).