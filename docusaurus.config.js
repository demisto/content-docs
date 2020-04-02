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
  favicon: "img/Cortex-XSOAR-product-green.svg", //square version
  organizationName: "Cortex XSOAR", // Usually your GitHub org/user name.
  projectName: "content-docs", // Usually your repo name.
  themeConfig: {
    prism: {
      theme: require("prism-react-renderer/themes/github"),
      darkTheme: require("prism-react-renderer/themes/oceanicNext")
    },
    algolia: {
      apiKey: process.env.ALGOLIA_APIKEY,
      indexName: process.env.ALGOLIA_INDEX,
      algoliaOptions: {} // Optional, if provided by Algolia
    },
    sidebarCollapsible: true,
    navbar: {
      title: "",
      logo: {
        alt: "Cortex for Developers",
        src: "img/Cortex_XSoar_logos_RGB_Cortex-Ng-Soar-Horizontal.svg",
        srcDark: "img/Cortex_XSoar_logos_RGB_Cortex-Ng-Soar-Horizontal-KO.svg"
      },
      links: [
        {
          to: "docs/welcome",
          label: "Developer Docs",
          position: "left"
        },
        {
          to: "docs/tutorials/tut-setup-dev",
          label: "Tutorials",
          position: "left"
        },
        {
          to: "docs/reference/index",
          label: "Reference",
          position: "left"
        },
        {
          label: "Partners",
          items: [
            { to: "docs/partners/why-demisto", label: "Why Cortex XSOAR?" },
            {
              to: "docs/partners/become-a-tech-partner",
              label: "Become a Partner"
            },
            {
              to: "docs/partners/partner-owned-integration",
              label: "Partner Owned Integration"
            },
            {
              to: "docs/partners/development-partners",
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
          href: "http://github.com/demisto/content/",
          label: "GitHub",
          position: "right"
        },
        {
          href: "https://blog.demisto.com/",
          label: "Blog",
          position: "right"
        }
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
              label: "Cortex",
              logo: "/img/cortexfavicon.png"
            },
          ],
          position: "right"
        }
      ]
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [
            { to: "docs/integrations/getting-started-guide", label: "Development Guide" },
            { to: "docs/partners/why-demisto", label: "Why become a Partner?" },
            {
              to: "docs/partners/become-a-tech-partner",
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
        src: "img/PANW_Parent_Brand_Primary_Logo_RGB_KO.svg",
        href: "https://pan.dev"
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
