# Trust Any Certificate

## Overview

Enabling “Trust Any Certificate” in an integration disables certificate validation and uses less-hardened SSL standards.

## Code usage

When constructing the `BaseClient` in your integrations, set `verify=False` to disable SSL checks and allow legacy ciphers:

```python
from CommonServerPython import BaseClient

client = BaseClient(
    base_url="https://api.example.com",
    verify=False
)
response = client._http_request(...)
```

## How it works

### _http_request()

In the implementation of `_http_request`, the verify parameter is passed to the underlying HTTP request from the `BaseClient`:

```python
class BaseClient:
    ...
    def _http_request():
        ...
        res = self._session.request(..., verify=self._verify)
```

When `self._verify` is set to False, SSL certificate verification is disabled. This means the client will accept insecure certificates.

### Skip Certificate Verification

When `verify=False` is set, the following function is triggered to delete certificate environment variables.
This ensures that no extra CA bundles are loaded.
For requests versions earlier than 2.28, this step is necessary to fully disable certificate validation in addition to passing the `self._verify` to the session.request.

```python
def skip_cert_verification()
    for k in ('REQUESTS_CA_BUNDLE', 'CURL_CA_BUNDLE'):
        if k in os.environ:
            del os.environ[k]
```

### Python 3.10+ & Custom SSLAdapter

Python 3.10 increased OpenSSL’s default security level to 2, which rejects many older cipher suites and breaks connections to legacy servers ([see CPython PR #25778](https://github.com/python/cpython/pull/25778)).
To mitigate this, `BaseClient` mounts a custom SSL adapter when `verify=False`:

```python
if IS_PY3 and PY_VER_MINOR >= 10 and not verify:
    self._session.mount('https://', SSLAdapter(verify=verify))
```

### SSLAdapter

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

   The OP_LEGACY_SERVER_CONNECT flag tells OpenSSL to allow legacy TLS renegotiation. Relevant when a server doesn’t support the secure‐renegotiation extension (RFC 5746).

3. **Lowers OpenSSL security level to 1 & Enables a [cipher list](https://github.com/demisto/content/blob/e3807159cae86ac30ecbb3c51ec82dbac7512d3d/Packs/Base/Scripts/CommonServerPython/CommonServerPython.py#L9127)**  

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
