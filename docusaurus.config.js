/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
const visit = require("unist-util-visit");
const fs = require("fs");
const marketplace = JSON.parse(fs.readFileSync("./index.json"));

const remarkPlugin = () => {
  const transformer = (root) => {
    visit(root, "link", (node) => {
      if (!node.url) {
        console.log("empty link", node);
        node.url = "#";
      }
    });

    visit(root, "image", (node) => {
      if (!node.url) {
        console.log("empty image", node);
        node.url = "/img/placeholder.png";
      }
    });
  };
  return transformer;
};

module.exports = {
  title: "Cortex XSOAR",
  tagline: "Developers - Palo Alto Networks",
  url: "https://xsoar.pan.dev",
  baseUrl: "/",
  favicon: "/img/cortexfavicon.png", //square version
  organizationName: "Demisto", // Usually your GitHub org/user name.
  projectName: "content-docs", // Usually your repo name.
  themeConfig: {
    algolia: {
      apiKey: "74349c31456061cb5e9cb8e9d9992b89",
      appId: "HRXQIDA6WM",
      indexName: "demisto",
      algoliaOptions: { typoTolerance: false, hitsPerPage: 1000, filters: 'type:lvl1 OR type:content' } // Optional, if provided by Algolia
    },
    sidebarCollapsible: true,
    navbar: {
      title: "",
      logo: {
        alt: "Cortex XSOAR for Developers (Formerly Demisto)",
        src: "/img/Cortex_XSoar_logos_RGB_Cortex-Ng-Soar-Horizontal.svg",
        srcDark: "/img/Cortex_XSoar_logos_RGB_Cortex-Ng-Soar-Horizontal-KO.svg"
      },
      items: [
        {
          to: "/docs/welcome",
          label: "Developer Docs",
          position: "left",
          activeBaseRegex:
            "docs(/welcome|/index|/concepts|/contributing|/dashboards|/doc_imgs|/documentation|/incidents|/integrations|/packs|/playbooks|/scripts|/tutorials)"
        },
        {
          to: "/docs/reference/articles",
          label: "Articles",
          position: "left",
          activeBaseRegex: "docs/reference/articles"
        },
        {
          to: "/docs/reference/index",
          label: "Reference",
          position: "left",
          activeBaseRegex: "docs/reference/(index|api|integrations|playbooks|releases|scripts)"
        },
        {
          to: "https://cortex.marketplace.pan.dev/marketplace",
          label: "Marketplace",
          position: "left",
          target: '_self'
        },
        {
          label: "Products",
          items: [
            {
              href: "https://panos.pan.dev",
              label: "PAN-OS",
              className: "panosItem",
              target: "_self"
            },
            {
              href: "https://cortex.pan.dev",
              label: "Cortex Data Lake",
              className: "cortexItem",
              target: "_self"
            },
            {
              href: "https://xsoar.pan.dev",
              label: "Cortex XSOAR",
              className: "xsoarItem",
              target: "_self"
            },
            {
              href: "https://prisma.pan.dev",
              label: "Prisma",
              className: "prismaItem",
              target: "_self"
            },
          ],
          position: "right"
        },
        {
          label: "Partners",
          to: "docs/partners/why-xsoar",
          activeBaseRegex: "docs/partners",
          items: [
            { to: "/docs/partners/why-xsoar", label: "Why Cortex XSOAR?" },
            {
              to: "docs/partners/become-a-tech-partner",
              label: "Become a Partner"
            },
            {
              to: "/docs/partners/premium-packs",
              label: "Premium Packs"
            },
            {
              to: "/docs/partners/private-offer",
              label: "Private Offer"
            },
            {
              to: "/docs/partners/adopt",
              label: "Adopt-a-Pack"
            },
            {
              to: "/docs/partners/certification",
              label: "Pack Certification"
            },
            {
              to: "/docs/partners/office-hours",
              label: "Office Hours"
            },
            {
              to: "/docs/partners/development-partners",
              label: "Development Partners"
            },
            {
              to:
                "https://technologypartners.paloaltonetworks.com/English/register_email.aspx",
              label: "Sign Up Now"
            },
          ],
          position: "right"
        },
        {
          href: "https://www.paloaltonetworks.com/blog/security-operations/",
          label: "Blog",
          position: "right"
        },
        {
          href: "http://github.com/demisto/content/",
          position: "right",
          className: "header-github-link",
          "aria-label": "GitHub repository"
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [
            { to: "/docs/welcome", label: "Developer Docs" },
            {
              to: "/docs/partners/become-a-tech-partner",
              label: "Become a Technology Partner"
            }
          ],
        },
        {
          title: "Social",
          items: [
            {
              label: "Blog",
              href: "https://blog.demisto.com/"
            }
          ],
        },
      ],
      logo: {
        alt: "Palo Alto Networks for Developers",
        src: "/img/PANW_Parent_Brand_Primary_Logo_RGB_KO.svg"
        // href: "https://pan.dev"
      },
      copyright: `Copyright © ${new Date().getFullYear()} Palo Alto Networks, Inc.`
    },
    announcementBar: {
      id: 'github_star',
      content:
        '⭐️ If you like Cortex XSOAR Content, give it a star on <a target="_blank" rel="noopener noreferrer" href="https://github.com/demisto/content">GitHub</a>! ⭐',
      backgroundColor: '#fafbfc',
      textColor: '#091E42',
    }
  },
  themes: ["@docusaurus/theme-live-codeblock"],
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          editUrl: "https://github.com/demisto/content-docs/tree/master",
          routeBasePath: "docs",
          include: ["**/*.md", "**/*.mdx"], // Extensions to include.
          docLayoutComponent: "@theme/DocPage",
          docItemComponent: "@theme/DocItem",
          beforeDefaultRemarkPlugins: [remarkPlugin],
          remarkPlugins: [],
          rehypePlugins: [],
          showLastUpdateAuthor: false,
          showLastUpdateTime: true
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css")
        },
        sitemap: {
          changefreq: "weekly",
          priority: 0.5
        },
      },
    ],
  ],
  customFields: {
    marketplace: marketplace
  },
  stylesheets: [
    {
      href: "https://use.fontawesome.com/releases/v5.15.0/css/all.css",
      type: "text/css",
      rel: "stylesheet"
    },
  ],
  plugins: [
    [
      require.resolve("./docusaurus-plugin-gtm/index.js"),
      {
        gtm: "GTM-KWZSPLM", //GTM-XXXXXX
      },
    ]
  ],
  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",
  onDuplicateRoutes: "warn"
};
