---
id: cosign-signature
title: Cosign Signature Guide
slug: cosign-signature
tags: [cosign, signature, security, supply-chain, integrations, docker]
---

# Cosign Signature Guide

## Overview

[Cosign](https://github.com/sigstore/cosign) is a tool from the [Sigstore](https://www.sigstore.dev/) project used to verify signatures for container images. Verifying image signatures lets you confirm that a Cortex XSOAR/XSIAM Docker image is authentic and has not been tampered with.

Cosign **replaces Docker Content Trust (DCT)** for signing our images. DCT (based on Notary v1) is deprecated, and Cosign provides a modern, OCI-native signing workflow going forward.

This guide covers how to verify Cortex XSOAR/XSIAM Docker images with Cosign.

## What Is Changing

- Our images are now signed with **Cosign** instead of Docker Content Trust (DCT).
- During a grace period, every image is **dual-signed** with both DCT and Cosign, so you can verify with either mechanism.
- **DCT is retired on Dec 8, 2026.** After that date, verify with Cosign only.

If you rely on `docker trust inspect` / `DOCKER_CONTENT_TRUST=1` today, switch to `cosign verify` before the retirement date.

`docker trust` -> `cosign` mapping:

| Task | DCT (legacy) | Cosign (new) |
| --- | --- | --- |
| Verify at pull | `DOCKER_CONTENT_TRUST=1 docker pull` | `cosign verify --key cosign.pub ...` |
| Inspect signatures | `docker trust inspect <image>` | `cosign tree <image>` / `cosign verify ...` |

## Prerequisites

- **cosign binary** installed in your environment:

  ```bash
  COSIGN_VERSION=v2.4.1
  curl -sSfL "https://github.com/sigstore/cosign/releases/download/${COSIGN_VERSION}/cosign-linux-amd64" \
    -o /usr/local/bin/cosign
  chmod +x /usr/local/bin/cosign
  cosign version
  ```

  > Both cosign **v2** and **v3** work for verification.

- **The Cosign public key** (`cosign.pub`). This is all you need to verify; it is not secret.

## Getting the Public Key

`--key cosign.pub` is a **file path**: cosign reads a file named `cosign.pub` in the directory you run the command from. If that file is missing you get `open cosign.pub: no such file or directory`, so save the key first.

Create `cosign.pub` with the published key (run all later commands from the same directory, or pass the full path to the file):

```bash
cat > cosign.pub <<'EOF'
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEH1arbOyIQuZLdy8bF5ss2LHCDB9M
DlUs3beCk/90l2LQyOLWSLEAHsCTv43LxKhhOn+Cqvot8rpjBFrb7UEj7g==
-----END PUBLIC KEY-----
EOF
```

Confirm it loaded:

```bash
cosign public-key --key cosign.pub   # re-prints the same PEM if the file is valid
```

## Verifying Signatures

The signature lives in a sibling `<org>/sig-<image>` repo, so point cosign at it
with `COSIGN_REPOSITORY`, and pass `--insecure-ignore-tlog=true` because our
images are signed without a public transparency log entry:

```bash
# Verify a Docker Hub image (signature in demisto/sig-python3):
COSIGN_REPOSITORY=demisto/sig-python3 \
  cosign verify --key cosign.pub --insecure-ignore-tlog=true \
  demisto/python3:<version>

# Verify by digest (unambiguous, matches how it was signed):
COSIGN_REPOSITORY=demisto/sig-python3 \
  cosign verify --key cosign.pub --insecure-ignore-tlog=true \
  demisto/python3@sha256:<digest>
```

During the dual-sign window you can also confirm the legacy DCT signature:

```bash
DOCKER_CONTENT_TRUST=1 docker pull demisto/python3:<version>
```

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| `open cosign.pub: no such file or directory` | `--key cosign.pub` points at a file that is not in the current directory. | Save the key as shown in [Getting the Public Key](#getting-the-public-key), or pass the full path (e.g. `--key /path/to/cosign.pub`). |
| `no matching signatures` on verify | Verifying against the image repo instead of the signature repo. | Set `COSIGN_REPOSITORY=<org>/sig-<image>` to match where the signature is stored. |
| Verify fails looking for a transparency-log entry | Images are signed without a public transparency log entry. | Add `--insecure-ignore-tlog=true` to `cosign verify`. |
| `--tlog-upload=false is not supported with --signing-config` | cosign **v3** changed defaults. | This only affects signing, not verification. Verification works on both v2 and v3. |
