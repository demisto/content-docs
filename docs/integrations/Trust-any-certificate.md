# Trust Any Certificate
This document explains how and what happens when SSL verification is disabled in integrations.
This includes the following:

1. Skipping the certificate validation.
2. Reducing the security level of OpenSSL
3. Allowing more cipher for TLS handshake.
4. Disable hostname checks.
5. Allow old TLS renegotiation.

## Usage

In your integration’s when constructing `BaseClient`, set `verify=False` to disable SSL checks and allow legacy ciphers:

```python
from CommonServerPython import BaseClient

client = BaseClient(
    base_url="https://api.example.com",
    verify=False  # disable SSL checks and allow legacy ciphers
)
response = client._http_request(...)
```

## Skip Certificate Verification

The following function enabled when `verify=False`, which deletes the certificate environment variables so requests skip certificate validation.
It ensures that no extra certificate files are loaded.
```python

def skip_cert_verification()
    # removes any custom CA bundle overrides
    for k in ('REQUESTS_CA_BUNDLE', 'CURL_CA_BUNDLE'):
        if k in os.environ:
            del os.environ[k]
```

## Python 3.10+ & Custom SSLAdapter

Python 3.10 increased OpenSSL’s default security level to **2**, rejecting many older cipher suites and causing handshake failures against legacy servers. We detect and mount a custom adapter inside the BaseClient Constructor:

```python
if IS_PY3 and PY_VER_MINOR >= 10 and not verify:
    self._session.mount('https://', SSLAdapter(verify=verify))
```

## What `SSLAdapter` Does

When verify=False on Python 3.10+, `SSLAdapter` creates a custom `ssl.SSLContext` that:

1. **Disables hostname checks:**  
   ```python
    if not verify and IS_PY3:
        self.context.check_hostname = False
    ```

2. **Enabling Legacy TLS Renegotiation:**
 
    ```python
    if not verify and ssl.OPENSSL_VERSION_INFO >= (3, 0, 0):
        self.context.options |= ssl.OP_LEGACY_SERVER_CONNECT
    ```
   The OP_LEGACY_SERVER_CONNECT flag (0x4) tells OpenSSL to allow old‐style TLS renegotiation. Relevant when a server doesn’t support the secure‐renegotiation extension (RFC 5746).


3. **Lowers OpenSSL security level to 1 & Enables a cipher list**  
   ```python
   CIPHERS_STRING = (
       '@SECLEVEL=1:'
       'ECDHE+AESGCM:'
       'ECDHE+CHACHA20:'
       'DHE+AESGCM:'
       'DHE+CHACHA20:'
       'ECDH+AESGCM:'
       'DH+AESGCM:'
       'ECDH+AES:'
       'DH+AES:'
       'RSA+AESGCM:'
       'RSA+AES:'
       '!aNULL:'
       '!eNULL:'
       '!MD5:'
       '!DSS'
   )
   context = create_urllib3_context(ciphers=CIPHERS_STRING)
   ```

This configuration restores legacy ciphers (excluding null, MD5, DSS, etc.).
