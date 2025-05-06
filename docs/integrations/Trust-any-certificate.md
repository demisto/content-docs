# Trust Any Certificate

## Overview

Disabling SSL verification by setting `verify=False` in `BaseClient` (or by enabling “Trust Any Certificate” in an integration) allows connecting to servers using less-secure SSL configurations. This bypasses standard HTTPS checks—skipping certificate validation, lowering OpenSSL’s security level, and permitting older ciphers and renegotiation modes.

## Usage

In your integration’s when constructing `BaseClient`, set `verify=False` to disable SSL checks and allow legacy ciphers:

```python
from CommonServerPython import BaseClient

client = BaseClient(
    base_url="https://api.example.com",
    verify=False
)
response = client._http_request(...)
```

## _http_request()

In the implementation of `_http_request`, the verify parameter is passed to the underlying HTTP request from the `BaseClient`:

```python
class BaseClient:
    ...
    def _http_request():
        ...
        res = self._session.request(..., verify=self._verify)
```

When `self._verify` is set to False, SSL certificate verification is disabled. This means the client will accept insecure certificates.

## Skip Certificate Verification

When `verify=False` is set, the following function is triggered to delete certificate environment variables.
This ensures that no extra CA bundles are loaded.
For requests versions earlier than 2.28, this step is necessary to fully disable certificate validation in addition to passing the `self._verify` to the session.request.

```python
def skip_cert_verification()
    for k in ('REQUESTS_CA_BUNDLE', 'CURL_CA_BUNDLE'):
        if k in os.environ:
            del os.environ[k]
```

## Python 3.10+ & Custom SSLAdapter

Python 3.10 increased OpenSSL’s default security level to 2, which rejects many older cipher suites and breaks connections to legacy servers.
To mitigate this, `BaseClient` mounts a custom SSL adapter when `verify=False`:

```python
if IS_PY3 and PY_VER_MINOR >= 10 and not verify:
    self._session.mount('https://', SSLAdapter(verify=verify))
```

## SSLAdapter

When `verify=False` on Python 3.10+, `SSLAdapter` creates a custom `ssl.SSLContext` that:

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

This configuration restores legacy ciphers (excluding null, MD5, DSS).
