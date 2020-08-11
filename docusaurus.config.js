/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

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
      apiKey: "f5dfbee43cfa4c5024b10045c6d91461",
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
      links: [
        {
          to: "/docs/welcome",
          label: "Developer Docs",
          position: "left"
        },
        {
          to: "/docs/tutorials/tut-setup-dev",
          label: "Tutorials",
          position: "left"
        },
        {
          to: "/docs/reference/index",
          label: "Reference",
          position: "left"
        },
        {
          label: "Partners",
          items: [
            { to: "/docs/partners/why-xsoar", label: "Why Cortex XSOAR?" },
            {
              to: "docs/partners/become-a-tech-partner",
              label: "Become a Partner"
            },
            {
              to: "/docs/partners/certiification",
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
              to: "https://start.paloaltonetworks.com/become-a-technology-partner",
              label: "Sign Up Now"
            }
          ],
          position: "right"
        },
        {
          href: "https://blog.demisto.com/",
          label: "Blog",
          position: "right"
        },
        {
          href: "http://github.com/demisto/content/",
          position: "right",
          className: "header-github-link",
          "aria-label": "GitHub repository",
        },
      ],
      sites: [
        {
          label: "Products",
          items: [
            {
              href: "https://panos.pan.dev",
              label: "PAN-OS",
              logo: "/img/strata_favicon.png"
            },
            {
              href: "https://cortex.pan.dev",
              label: "Cortex Data Lake",
              logo: "/img/cortexfavicon.png"
            },
            {
              href: "https://xsoar.pan.dev",
              label: "Cortex XSOAR",
              logo: "/img/Cortex-XSOAR-product-green.svg"
            }
          ],
          position: "products"
        }
      ]
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
          ]
        },
        {
          title: "Social",
          items: [
            {
              label: "Blog",
              href: "https://blog.demisto.com/"
            }
          ]
        }
      ],
      logo: {
        alt: "Palo Alto Networks for Developers",
        src: "/img/PANW_Parent_Brand_Primary_Logo_RGB_KO.svg"
        // href: "https://pan.dev"
      },
      copyright: `Copyright © ${new Date().getFullYear()} Palo Alto Networks, Inc.`
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
          remarkPlugins: [],
          rehypePlugins: [],
          showLastUpdateAuthor: false,
          showLastUpdateTime: true
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css")
        }
      }
    ]
  ],
  plugins: [
    "@docusaurus/plugin-sitemap",
    {
      cacheTime: 600 * 1000, // 600 sec - cache purge period
      changefreq: "weekly",
      priority: 0.5
    }
  ],
  customFields: {}
};
