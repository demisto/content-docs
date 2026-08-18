---
id: custom-integration-duplication
title: Custom Integration Duplication & Manual Upload
description: Step-by-step guide for duplicating and uploading a custom integration using demisto-sdk upload-custom-integration.
---

When replacing traditional integrations with Connectors, the in-product **Duplicate** button in the platform user interface redirects users to perform a custom duplicate and upload flow.

This guide provides a step-by-step walkthrough for manually duplicating an existing integration from the official Content repository, updating its identifiers safely, and uploading it to your Cortex XSOAR or Cortex XSIAM platform tenant using the `demisto-sdk`.

---

:::warning Critical System ID Conflict Risk
If you upload a custom integration whose `id` matches an official system integration's `id`, any subsequent attempt to update or download the system pack containing that integration will **fail with a platform system error**.

To protect your instance, custom integrations **must** append the `_copy` marker suffix to both their **ID** and **Display Name** (e.g., `MyIntegration_copy`). The `demisto-sdk` CLI auto-enforces this convention before any upload.
:::

---

## Prerequisites

Before starting, ensure you have:

1. **Python 3.10 or higher** installed on your workstation.
2. **Git** installed and configured with access to GitHub.
3. **Cortex Platform Tenant Credentials** (Instance Administrator privileges required).

---

## Step 1: Install or Update `demisto-sdk`

The duplication upload flow requires `demisto-sdk` version **1.40.0 or higher**, which includes the dedicated `upload-custom-integration` safety command.

Open your terminal and run:

```bash
pip install --upgrade demisto-sdk
```

Verify your installed version and confirm the command is available:

```bash
demisto-sdk upload-custom-integration --help
```

---

## Step 2: Clone or Sync the Content Repository

Clone the official `demisto/content` repository locally (or update your existing copy):

**Option A: Clone via SSH**

```bash
git clone git@github.com:demisto/content.git
cd content
```

**Option B: Clone via HTTPS**

```bash
git clone https://github.com/demisto/content.git
cd content
```

If you already have a local copy, ensure it is up to date:

```bash
git checkout master
git pull origin master --rebase
```

---

## Step 3: Configure Environment Variables

To allow `demisto-sdk` to authenticate with your platform instance, create a `.env` file in the root directory of your cloned content repository (`content/.env`).

### How to Obtain Credentials from the Platform UI

1. Log in to your Cortex XSOAR / XSIAM platform instance.
2. Navigate to **Settings → Configurations** → search for **API Keys**.
3. **API URL** (`DEMISTO_BASE_URL`): Click **Copy API URL** in the top right corner.
4. **API Key** (`DEMISTO_API_KEY`):
   - Click **New Key** (top right corner).
   - Set **Key Type** to `Standard`.
   - Set **Role** to `Instance Administrator`.
   - Click **Generate** and copy the key immediately from the modal popup.
5. **Auth ID** (`XSIAM_AUTH_ID`):
   - Close the key modal to view the API Keys table.
   - Locate the row for your newly created API key.
   - Copy the numerical ID in the **ID** column (e.g., `4`).

### Populate `content/.env`

Add your credentials to `content/.env`:

```bash
DEMISTO_BASE_URL=https://api-your-tenant-url.xdr.us.paloaltonetworks.com/xsoar
DEMISTO_API_KEY=your_copied_api_key_here
XSIAM_AUTH_ID=your_key_id_number_here
```

---

## Step 4: Duplicate & Update Integration YAML

1. **Locate the Integration**: Find the integration folder you wish to duplicate inside `Packs/<PackName>/Integrations/<IntegrationName>/`.
2. **Create a Working Copy**: Copy the integration directory or YAML file to a new location or branch.
3. **Add the `_copy` Marker**: Open the integration's `.yml` file in an editor (e.g., VS Code) and update both the `commonfields.id` and `name` fields:

```yaml
# BEFORE
commonfields:
  id: PolarSecurity
name: Polar Security

# AFTER (Required Duplication Convention)
commonfields:
  id: PolarSecurity_copy
name: Polar Security_copy
```

:::note
Both `commonfields.id` and `name` must end with the `_copy` suffix. If either field is missing this marker, the upload command will block execution to prevent tenant corruption.
:::

---

## Step 5: Upload the Custom Integration

Run the `upload-custom-integration` command, passing the path to your modified YAML file or its parent directory:

**Recommended: Upload via Directory Path**

```bash
demisto-sdk upload-custom-integration -i Packs/PolarSecurity/Integrations/PolarSecurity_copy/
```

**Alternative: Upload via Direct YAML File**

```bash
demisto-sdk upload-custom-integration -i Packs/PolarSecurity/Integrations/PolarSecurity_copy/PolarSecurity_copy.yml
```

### Expected Command Output

```text
Running Demisto-SDK CLI
Uploading Packs/PolarSecurity/Integrations/PolarSecurity_copy/PolarSecurity_copy.yml to https://api-your-tenant...
UPLOAD SUMMARY:

SUCCESSFUL UPLOADS:
┌────────────────────────┼─────────────┼────────────────┼──────────────┐
│ NAME                   │ TYPE        │ PACK NAME      │ PACK VERSION │
├────────────────────────┼─────────────┼────────────────┼──────────────┤
│ PolarSecurity_copy.yml │ Integration │ Polar Security │ 1.0.0        │
└────────────────────────┴─────────────┴────────────────┴──────────────┘
```

---

## Step 6: Verify in Platform UI

1. Log in to your Cortex platform instance.
2. Navigate to **Settings → Integrations → Custom Integrations**.
3. Locate your integration (e.g., `Polar Security_copy`). It will display a **Custom** badge next to its title.
4. Click **Add Instance** to configure and use your custom duplicate.

---

## Troubleshooting & FAQ

### Error: Missing `_copy` Marker

If you see an error like this:

```text
Invalid value:
  Integration field(s) missing the '_copy' marker:
    commonfields.id = 'PolarSecurity' and name = 'PolarSecurity'
```

**Fix**: Open your YAML file and append `_copy` to both `commonfields.id` and `name`.

---

### Bypassing Validation (`--force-id`)

:::warning
Using `--force-id` is strongly discouraged. Only use this flag if you are an advanced administrator explicitly maintaining custom IDs outside standard system pack boundaries.
:::

If you must upload without the `_copy` marker, pass `--force-id`:

```bash
demisto-sdk upload-custom-integration -i <path/to/integration.yml> --force-id
```

This will log a high-visibility CLI warning and proceed with the upload:

```text
[WARNING] Uploading custom content without the '_copy' marker risks conflicting with official system pack IDs... Proceeding because --force-id was explicitly set.
```
