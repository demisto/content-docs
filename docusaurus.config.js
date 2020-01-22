/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

module.exports = {
  title: "Demisto",
  tagline: "Developers - Palo Alto Networks",
  url: "https://demisto.pan.dev",
  baseUrl: "/",
  favicon: "img/demistofavicon.png", //square version
  organizationName: "Demisto", // Usually your GitHub org/user name.
  projectName: "content-docs", // Usually your repo name.
  themeConfig: {
    algolia: {
      apiKey: process.env.ALGOLIA_APIKEY,
      appId: process.env.ALGOLIA_APPID,
      indexName: process.env.ALGOLIA_INDEX
    },
    sidebarCollapsible: true,
    navbar: {
      title: "",
      logo: {
        alt: "Demisto for Developers",
        src: "img/demistopeelable.png"
      },
      menus: [
        {
          label: "Concepts",
          items: [
            { to: "docs/getting-started-guide", label: "Overview" },
            { to: "docs/restapi_qs", label: "Architecture" },
            { to: "docs/pandevice_qs", label: "Integrations" },
            { to: "docs/panpython_qs", label: "Scripts" },
            { to: "docs/pango_qs", label: "Playbooks" },
            { to: "docs/terraform_qs", label: "Context Data" },
            { to: "docs/ansible_qs", label: "Classification & Mapping" },
            { to: "docs/cloudtemplates_qs", label: "Demisto Transform Language" },
            { to: "docs/cloudtemplates_qs", label: "Docker" },
          ],
          position: "left"
        },
        {
          label: "Tasks",
          items: [
            { to: "docs/xmlapi_qs", label: "Build Playbooks" },
            { to: "docs/restapi_qs", label: "Create and Configure Integrations" },
            { to: "docs/pandevice_qs", label: "Create Documentation" },
          ],
          position: "left"
        },
        {
          label: "Tutorials",
          items: [
            { to: "docs/xmlapi_qs", label: "Create an Integration" },
            { to: "docs/restapi_qs", label: "Create a Scipt" },
            { to: "docs/pandevice_qs", label: "Create a Phishing Playbook" },
          ],
          position: "left"
        },
        {
          label: "Reference",
          items: [
            { to: "docs/xmlapi_qs", label: "Integrations" },
            { to: "docs/restapi_qs", label: "Playbooks" },
            { to: "docs/pandevice_qs", label: "Scripts" },
            { to: "docs/restapi_qs", label: "REST API" },
            { to: "docs/pandevice_qs", label: "Demisto SDK" },
          ],
          position: "left"
        }
      ],
      links: [
        {
          href: "docs/become-a-tech-partner",
          label: "Partnerships",
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
      ]
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [
            { to: "docs/getting-started-guide", label: "Development Guide" },
            { to: "docs/why-demisto", label: "Why become a Partner?" },
            { to: "docs/become-a-tech-partner", label: "Become a Technology Partner" }
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
        src: "img/pandev.png"
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
  ]
};
