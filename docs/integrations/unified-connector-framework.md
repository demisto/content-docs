---
id: unified-connector-framework
title: Understanding the unified connector framework and automatic updates
description: Learn how the unified connector framework changes content categories, version management, and update behavior across the applicable Cortex products.
---

:::note
This framework applies to the following Cortex products: **Cortex XSIAM**, **Cortex XDR**, **Cortex Cloud**, **Cortex AgentiX**, and **Cortex Data Security**. It does not apply to standalone Cortex XSOAR deployments.
:::

For applicable Cortex products, Palo Alto Networks is evolving the integration infrastructure with the Unified Connector framework. This framework transitions the products from fragmented, manual version management to a streamlined, unified onboarding experience with automatic background updates.

---

## Content categories

To help you manage your security ecosystem, the applicable Cortex products now distinguish between two categories of content:

### 1. Connector-Ready capabilities

Items labeled as **Connector-Ready** are part of the new framework. These core integration layers, now referred to as sub-capabilities, are built directly into the unified connector and are force-updated silently in the background. You no longer need to manually manage versions for these items.

<ul className="bullet-list">
<li><strong>Update method:</strong> Forced (Silent).</li>
<li><strong>Included types:</strong> Sub-capability (integration) code, parsing rules, data model rules, fields, and mappings.</li>
<li><strong>Visibility:</strong> These items are displayed within the connector's side-panel.</li>
</ul>

### 2. Marketplace Legacy content

Items labeled as **Marketplace Legacy** are standalone integrations and high-level content that remain in the content pack. These must be managed and updated manually via Marketplace.

<ul className="bullet-list">
<li><strong>Update method:</strong> Manual (Marketplace).</li>
<li><strong>Included types:</strong> Playbooks, scripts, dashboards, layouts, and jobs.</li>
</ul>

---

## Transitioning to unified connectors

For applicable Cortex products, the configuration workflow and update behavior depend on your onboarding date and the specific connector you are enabling.

### New customers (onboarded after July 26, 2026)

As a new customer, you will see the updated connector experience across the entire catalog.

<ul className="bullet-list">
<li><strong>Automatic force-updates:</strong> All connectors in your tenant will shift to the automatic force-update model automatically.</li>
<li><strong>Background updates:</strong> Core sub-capabilities (integrations) are updated silently in the background without requiring user intervention.</li>
</ul>

### Existing customers (onboarded before July 26, 2026)

As an existing customer, you have immediate access to a subset of the unified catalog, specifically specialized SaaS remediation connectors (such as G-Suite, Salesforce, and Microsoft 365).

<ul className="bullet-list">
<li><strong>Manual update support:</strong> You will continue to manage updates manually for most integrations until those specific services are transitioned to the unified connector framework for your tenant.</li>
<li><strong>Manual conversion:</strong> If you have existing standalone instances for services that are now available as connectors, you may need to perform a manual conversion process if your related content packs are not at the latest version.</li>
</ul>

---

## Important considerations

<ul className="bullet-list">
<li><strong>Integration visibility:</strong> Once you convert an integration to a connector, the legacy integration card will no longer appear in your catalog, and the service will appear as a sub-capability (integration) within the connector.</li>
<li><strong>Dev-prod sync:</strong> For customers using a Dev/Prod setup, it is highly recommended to perform updates and conversions in your Test tenant first, push them to your repository, and then pull them into your Production tenant to ensure parity.</li>
</ul>

---

## Related resources

For product-specific configuration guides and comprehensive catalogs, refer to the documentation portal:

<ul className="bullet-list">
<li><a href="https://cortex-docs.paloaltonetworks.com/cortex-xsiam/configure-cortex-xsiam/cortex-xsiam-data-sources">Cortex XSIAM Data Sources and Connectors</a></li>
<li><a href="https://cortex-docs.paloaltonetworks.com/cortex-xdr-5.x/configure-cortex-xdr/cortex-xdr-data-sources">Cortex XDR Data Sources and Connectors</a></li>
<li><a href="https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/what-are-cortex-cloud-data-sources">Cortex Cloud Data Source and Connectors (Posture Management)</a></li>
<li><a href="https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/what-are-cortex-cloud-data-sources">Cortex Cloud Data Sources and Connectors (Runtime Security)</a></li>
<li><a href="https://cortex-docs.paloaltonetworks.com/cortex-agentix/configure-cortex-agentix/cortex-agentix-data-sources-and-connectors">Cortex AgentiX Data Sources and Connectors</a></li>
<li><a href="https://cortex-docs.paloaltonetworks.com/data-security-documentation/cortex-data-security-data-sources-and-connectors/what-are-cortex-data-security-data-sources-and-connectors">Cortex Data Security Data Sources and Connectors</a></li>
</ul>
