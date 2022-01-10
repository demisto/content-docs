---
id: domain-extraction
title: Domain Extraction
---

The Cortex XSOAR Domain indicator type is built using regex and a formatting script.
In this documentation, we will elaborate on the Domain indicator components and what output you should expect when extracting indicators of type Domain.

## Domain Extraction Components

There are two components when extracting Domain indicators:
Regular Expression
Formatting script

### Regular Expression

When text is given, a Domain regex will try to catch a valid Domain based on the following characteristics:
- A Domain with ASCII and non-ASCII characters
- An Escaped and Unescaped Domains

The regex can extract Domains from one of the following:
- Explicit Domain
- URL
- Email Address

### Formatting Script

After extracting the Domain using regex, an ‘ExtractDomainAndFQDNFromUrlAndEmail’ formatting script iterates on each given Domain and does the following:

1. Replaces "[.]" with ".".
	
	For example:
 
	`www[.]evil.com --> www.evil.com`

2. Validate the Top-Level-Domain to avoid file extensions false positives.
	
	Excludes ‘.zip’ Top-Level-Domain by default.

3. Returns the formatted Domain.

## Common Domain Structures

The following are some of the most common Domain structures that Cortex XSOAR supports:

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
