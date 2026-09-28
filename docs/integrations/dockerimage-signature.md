---
id: dockerimage-signature
title: Docker Image Signature Guide
slug: dockerimage-signature
tags: [cosign, signature, security, supply-chain, integrations, docker]
---

# Docker Image Signature

## Overview

[Cosign](https://github.com/sigstore/cosign) is a [Sigstore](https://www.sigstore.dev/) tool that verifies container image signatures. Verifying these signatures ensures that the Docker images running Cortex XSOAR/XSIAM and platform content such as content packs (connectors), integrations (capabilities), and scripts are authentic and untampered with.

:::info

This guide explains how to use Cosign to verify Docker images running Cortex XSOAR/XSIAM and platform content items.

## Transition to Cosign  

Cosign replaces the deprecated Docker Content Trust (based on Notary v1) with a modern, OCI-native image signing workflow.

> **Important**:  
>  
> Support for Docker Content Trust (DCT) ends on December 8, 2026.
- Current state: All images are currently dual-signed with both DCT and Cosign to allow for a seamless transition.
- The change: After the December 8 deadline, we will stop signing images with DCT and move exclusively to Cosign.

If your system relies on `docker trust inspect` / `DOCKER_CONTENT_TRUST=1` today, switch to `cosign verify` before the retirement date.

| Task | DCT (legacy) | Cosign (new) |
| --- | --- | --- |
| Verify at pull | `DOCKER_CONTENT_TRUST=1 docker pull` | `cosign verify --key cosign.pub ...` |
| Inspect signatures | `docker trust inspect <image>` | `cosign tree <image>` / `cosign verify ...` |

## Prerequisite

Ensure **cosign binary** is installed in your environment.

  On macOS (or any environment with [Homebrew](https://brew.sh/)):

  ```bash
  brew install cosign
  cosign version
  ```

  On Linux, download the release binary directly:

  ```bash
  COSIGN_VERSION=v2.4.1
  curl -sSfL "https://github.com/sigstore/cosign/releases/download/${COSIGN_VERSION}/cosign-linux-amd64" \
    -o /usr/local/bin/cosign
  chmod +x /usr/local/bin/cosign
  cosign version
  ```

  > **Note**:  
  >  
  > Both cosign **v2** and **v3** work for verification. For other platforms and installation methods, see the [cosign installation docs](https://docs.sigstore.dev/cosign/system_config/installation/).


## Get the Public Key
  
The Cosign public key (`cosign.pub`) is all you need to verify, it is not secret.
> **Note**:  
>  
> `--key cosign.pub` is a file path. Cosign reads a file named `cosign.pub` in the directory where the command is run from. If that file is missing, the error `open cosign.pub: no such file or directory` is returned, so save the key first.

Create `cosign.pub` with the published key (run all later commands from the same directory, or pass the full path to the file):

{/*
Maintainer note (not rendered on the site):
The public key below is the public half of the Cosign signing key stored in GCP KMS:
  gcpkms://projects/xdr-cloud-hsm-prod-eu-01/locations/global/keyRings/cortex-xdr-software/cryptoKeys/cosign-signing-key/cryptoKeyVersions/1
If the signing key is rotated (a new cryptoKeyVersion), re-export the public key and
update the PEM block below, e.g.:
  cosign public-key --key gcpkms://projects/xdr-cloud-hsm-prod-eu-01/locations/global/keyRings/cortex-xdr-software/cryptoKeys/cosign-signing-key/cryptoKeyVersions/<N>
*/}

```bash
cat > cosign.pub <<'EOF'
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEH1arbOyIQuZLdy8bF5ss2LHCDB9M
DlUs3beCk/90l2LQyOLWSLEAHsCTv43LxKhhOn+Cqvot8rpjBFrb7UEj7g==
-----END PUBLIC KEY-----
EOF
```

Confirm the file was saved correctly:

```bash
cat cosign.pub   # prints the PEM block saved above
```

## Verify the Image Signature

To verify an image signature with Cosign:

1. Make sure `cosign.pub` is saved in the current directory (see [Get the Public Key](#get-the-public-key)).
2. Get the image tag to verify. Images are signed by tag, so verify using the image tag (`:<tag>`).
3. Set `COSIGN_REPOSITORY` to the sibling `<org>/sig-<image>` repository where the signature is stored (for example, the signature for `demisto/python3` is stored in `demisto/sig-python3`).
4. Run `cosign verify` with `--insecure-ignore-tlog=true`.

For example, to verify `demisto/python3` by tag:

```bash
COSIGN_REPOSITORY=demisto/sig-python3 \
  cosign verify --key cosign.pub --insecure-ignore-tlog=true \
  demisto/python3:<tag>
```

## Example Verification Script

For convenience, the ready-to-run wrapper [`utils/verify_signature.sh`](https://github.com/demisto/dockerfiles/blob/master/utils/verify_signature.sh) is available in the [demisto/dockerfiles](https://github.com/demisto/dockerfiles) repository. It derives the sibling `<org>/sig-<image>` signature repository automatically, so only the image reference is passed.

To use the script:

1. Make sure `cosign` is installed and on the PATH (see [Prerequisites](#prerequisites)).
2. Download the script and make it executable:

   ```bash
   curl -sSfL https://raw.githubusercontent.com/demisto/dockerfiles/master/utils/verify_signature.sh \
     -o verify_signature.sh
   chmod +x verify_signature.sh
   ```

3. Save `cosign.pub` in the same directory as the script (see [Getting the Public Key](#getting-the-public-key)), or set `PUBLIC_KEY=/path/to/cosign.pub` to point to it elsewhere.
4. Run the script with the image tag to verify:

   ```bash
   ./verify_signature.sh demisto/<image>:<tag>
   ```

## Troubleshooting

| Issue | Cause | Fix |
| --- | --- | --- |
| `open cosign.pub: no such file or directory` | `--key cosign.pub` points at a file that is not in the current directory. | Save the key as shown in [Getting the Public Key](#getting-the-public-key), or pass the full path (e.g. `--key /path/to/cosign.pub`). |
| `no matching signatures` on verify | Verifying against the image repository instead of the signature repository. | Set `COSIGN_REPOSITORY=<org>/sig-<image>` to match where the signature is stored. |
| Verify fails looking for a transparency-log entry | Images are signed without a public transparency log entry. | Add `--insecure-ignore-tlog=true` to `cosign verify`. |
