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
  favicon: "img/demistofavicon.png",//square version
  organizationName: "Demisto", // Usually your GitHub org/user name.
  projectName: "content-docs", // Usually your repo name.
  themeConfig: {
    sidebarCollapsible: true,
    navbar: {
      title: "",
      logo: {
        alt: "Demisto for Developers",
        src: "img/demistopeelable.png"
      },

      links: [
        {
          to: "docs/why-demisto",
          label: "Why Demisto",
          position: "left"
        },
        { 
          to: "docs/get-started", 
          label: "Get Started", 
          position: "left" 
        },
        { 
          to: "docs/dev-guide", 
          label: "Develop", 
          position: "left" 
        },
        {
          href: "https://blog.demisto.com/topic/use-cases",
          label: "Use Cases",
          position: "left"
        },
        {
          href: "https://go.demisto.com/become-a-technology-partner",
          label: "Sign Up Now",
          position: "right"
        },
        {
          href: "http://github.com/demisto/content/",
          label: "GitHub",
          position: "right"
        },
        {
          href: "https://medium.com/palo-alto-networks-developer-blog",
          label: "Blog",
          position: "right"
        },
      ]
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [
            { to: "docs/why-demisto", label: "Why Demisto" },
            { to: "docs/get-started", label: "Get Started" },
            { to: "docs/dev-guide", label: "Develop" }
          ]
        },
        {
          title: "Social",
          items: [
            {
              label: "Blog",
              href: "https://medium.com/palo-alto-networks-developer-blog"
            }
          ]
        }
      ],
      logo: {
        alt: "PAN-OS® for Developers",
        src: "img/pandev.png",
        href: "https://pan.dev"
      },
      copyright: `Copyright © ${new Date().getFullYear()} Palo Alto Networks, Inc.`
    }
  },
  themes: ['@docusaurus/theme-live-codeblock'],
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          // editUrl:
          //   "https://github.com/PaloAltoNetworks/panos.pan.dev/tree/master/docs",
          routeBasePath: "docs",
          include: ["**/*.md", "**/*.mdx"], // Extensions to include.
          docLayoutComponent: "@theme/DocPage",
          docItemComponent: "@theme/DocItem",
          remarkPlugins: [],
          rehypePlugins: [],
          showLastUpdateAuthor: true,
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
