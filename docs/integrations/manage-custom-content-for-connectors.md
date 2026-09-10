---
id: manage-custom-content-for-connectors
title: Manage custom content for connectors
description: Learn how Cortex XSIAM manages custom content for connectors, including viewing source code and duplicating sub-capabilities (integrations) using the demisto-sdk.
---

:::note
This topic applies to the following Cortex products: **Cortex XSIAM**, **Cortex XDR**, **Cortex Cloud**, **Cortex AgentiX**, and **Cortex Data Security**. It does not apply to standalone Cortex XSOAR deployments.
:::

Cortex XSIAM is transitioning to a unified connector experience that consolidates all vendor security capabilities, including log ingestion, automation, and threat intelligence, into a single entry in the catalog. Within a connector, these individual services are referred to as sub-capabilities (integrations).

---

## Availability

The method for managing custom content depends on your onboarding date and the implementation status of the specific vendor:

- **New customers (onboarded after July 26, 2026):** All services in the catalog follow the unified connector experience and require external management for custom content.
- **Existing customers (onboarded before July 26, 2026):** You may see a mix of legacy integrations and unified connectors. The product UI will automatically direct you to the external workflow for sub-capabilities (integrations) that have been transitioned to the unified experience.

---

## Duplicate and view source code

The method for managing source code depends on whether the service is currently part of a unified connector.

- **Legacy integrations:** For services not yet transitioned to the unified experience, you can continue to use the **Duplicate** and **View Source** options directly within the product UI. Upon duplication, the item transitions to a custom content status, and you can modify the source code using the built-in editor.
- **Connector sub-capabilities (integrations):** For vendors using the unified connector experience, the built-in UI editor is not supported. To view the source code of a sub-capability (integration), you can do so directly in **GitHub**. To duplicate a sub-capability (integration) and upload it as custom content, you must perform a manual flow using the `demisto-sdk`.

---

## External management workflow

When you select **Duplicate** or **View Source** for a sub-capability (integration) on the **Data Sources & Integrations** page, Cortex XSIAM provides the names of all the collector's sub-capabilities (integrations) so you can select the one relevant to you. You will need this name to locate the relevant files in the official repository.

### Option 1: View Source in GitHub

If you only need to review the code without making changes:

1. Copy the **Integration Name** provided for the sub-capability (integration) on the **Data Sources & Integrations** page in Cortex XSIAM.
2. Navigate to the official [Cortex Content GitHub Repository](https://github.com/demisto/content).
3. Search for the integration folder under the `Packs/` directory using the name you copied (such as, `Packs/<PackName>/Integrations/<IntegrationName>/`).
4. Review the YAML and Python/PowerShell files directly in the repository.

### Option 2: Duplicate and modify via the SDK

To modify an existing sub-capability (integration) and upload it as custom content, you must use the SDK.

#### Prerequisites

Before starting, ensure you have:

1. **[Python 3.10 or higher](https://www.python.org/downloads/)** installed on your workstation.
2. **[Git](https://git-scm.com/downloads)** installed and configured with access to GitHub.
3. **Cortex XSIAM tenant credentials** (Instance Administrator privileges required).

---

#### Step 1: Install or update demisto-sdk

The custom upload flow requires `demisto-sdk` version **1.40.0 or higher**.

Run the following command to install or upgrade:

```bash
pip install --upgrade demisto-sdk
```

Verify the version and confirm the command is available:

```bash
demisto-sdk upload-custom-integration --version
```

:::note
For full installation instructions and system requirements, see the [Demisto-SDK Installation Guide](https://cortex-docs.paloaltonetworks.com/demisto-sdk-development-guide/demisto-sdk-guide/install-demisto-sdk).
:::

---

#### Step 2: Clone or sync the content repository

:::note Planning to contribute back to the official repository?
If you intend to submit your changes as a pull request to `demisto/content`, you should **fork** the repository first instead of cloning it directly. See the [Contributing Guide](../contributing/contributing) for the full fork-based contribution workflow.
:::

Clone the official [`demisto/content`](https://github.com/demisto/content) repository locally.

**Option A: SSH** *(recommended for local uploads only)*

```bash
git clone git@github.com:demisto/content.git
```

**Option B: HTTPS**

```bash
git clone https://github.com/demisto/content.git
```

:::note
If you already have a local copy, ensure it is up to date before proceeding:

```bash
git checkout master
git pull origin master --rebase
```
:::

---

#### Step 3: Configure environment variables

To allow `demisto-sdk` to authenticate with your platform instance, create a `.env` file in the root directory of your cloned content repository (`content/.env`).

**How to obtain credentials from the Cortex XSIAM UI:**

1. Log in to Cortex XSIAM.
2. Navigate to **Settings → Configurations** → search for **API Keys**.
3. **API URL** (`DEMISTO_BASE_URL`): Click **Copy API URL** in the top right corner.
4. **API Key** (`DEMISTO_API_KEY`):
   - Click **New Key** (top right corner).
   - Set **Key Type** to `Standard`.
   - Set **Role** to `Instance Administrator`.
   - Click **Generate** and copy the key immediately from the window.
5. **Auth ID** (`XSIAM_AUTH_ID`):
   - Close the key window to view the API Keys table.
   - Locate the row for your newly created API key.
   - Copy the numerical ID in the **ID** column (such as, `4`).

**Populate `content/.env`**

Add your credentials to `content/.env`:

```bash
DEMISTO_BASE_URL=https://api-your-tenant-url.xdr.us.paloaltonetworks.com
DEMISTO_API_KEY=your_copied_api_key_here
XSIAM_AUTH_ID=your_key_id_number_here
```

---

#### Step 4: Duplicate and update YAML

1. **Locate the sub-capability (integration)**: Find the directory you want to duplicate under the Packs directory (such as, `Packs/<PackName>/Integrations/<IntegrationName>/`).
2. **Add the `_copy` marker**: Open the integration's `.yml` file in your favorite IDE (such as, VS Code) and update both the `commonfields.id` and `name` fields to include the `_copy` marker.

:::note
If either field is missing this marker, the upload command will block execution to prevent tenant corruption.

Updating the `display` field with the `_copy` marker is not mandatory, but it is recommended. Doing so makes it easier to distinguish your custom duplicate from the original sub-capability (integration) in the Cortex XSIAM UI.
:::

:::warning Critical System ID Conflict Risk
If you upload a custom sub-capability (integration) whose ID matches an official system integration's ID, any subsequent attempt to update or install the system pack containing that integration will **fail with a platform system error**. The `_copy` marker suffix is required to protect your instance.
:::

For example:

```yaml
# BEFORE
commonfields:
  id: PolarSecurity
name: Polar Security
display: Polar Security

# AFTER (Required Duplication Convention)
commonfields:
  id: PolarSecurity_copy
name: Polar Security_copy
display: Polar Security_copy
```

---

#### Step 5: Upload the custom sub-capability (integration)

Run the `upload-custom-integration` command, passing the path to your modified directory or direct YAML file.

**Recommended (upload using directory path)**

```bash
demisto-sdk upload-custom-integration -i 'Packs/MyPack/Integrations/MyIntegration'
```

**Alternative (upload using direct YAML file)**

```bash
demisto-sdk upload-custom-integration -i 'Packs/MyPack/Integrations/MyIntegration/MyIntegration.yml'
```

**Expected command output:**

```text
Running Demisto-SDK CLI
Uploading Packs/MyPack/Integrations/MyIntegration/MyIntegration.yml to https://api-your-tenant...
UPLOAD SUMMARY:

SUCCESSFUL UPLOADS:
┌───────────────────┬─────────────┬──────────────┬──────────────┐
│ NAME              │ TYPE        │ PACK NAME    │ PACK VERSION │
├───────────────────┼─────────────┼──────────────┼──────────────┤
│ MyIntegration.yml │ Integration │ My Pack      │ 1.0.0        │
└───────────────────┴─────────────┴──────────────┴──────────────┘
```

---

#### Step 6: Verify in Cortex XSIAM

1. Log in to Cortex XSIAM.
2. Navigate to **Settings → Data Sources & Integrations → Add New**.
3. Locate your sub-capability (integration); it will display a **Custom** badge.
4. Click **Add** to configure and use your custom duplicate.

---

## Troubleshooting & FAQ

### Error: Missing `_copy` Marker

If you see an error like the one below, the SDK has blocked the upload to prevent ID conflicts:

```text
Invalid value:
  Integration field(s) missing the '_copy' marker:
    commonfields.id = 'MyIntegration' and name = 'MyIntegration'
```

**Fix**: Open your YAML file and append `_copy` to both `commonfields.id` and `name`.

---

### Bypassing Validation (`--force-id`)

:::warning
Using `--force-id` is strongly discouraged. Only use this flag if you are an advanced administrator explicitly maintaining custom IDs outside standard system pack boundaries.

Before using this flag, verify ALL of the following:
1. Your chosen ID is completely unique and does NOT match the original integration ID.
2. Your chosen ID does NOT match any integration ID published on the Marketplace.
:::

If you must upload without the `_copy` marker, pass the `--force-id` flag:

```bash
demisto-sdk upload-custom-integration -i <path> --force-id
```

This will log a high-visibility CLI warning before proceeding:

```text
[WARNING] Uploading custom content without the '_copy' marker risks conflicting with official system pack IDs... Proceeding because --force-id was explicitly set.
```
