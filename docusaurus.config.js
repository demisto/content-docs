/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
const visit = require("unist-util-visit");
const path = require("path");

const globby = require("globby");

function genMetaData() {
  let marketplace = [];
  const packs = globby.sync(["./index", "!./index/index.json"], {
    absolute: false,
    objectMode: true,
    deep: 1,
    onlyDirectories: true,
  });
  packs.map((pack) => {
    const meta = globby.sync([`${pack.path}/metadata.json`], {
      absolute: true,
      objectMode: true,
      deep: 1,
    });
    let metadata = require(meta[0].path);
    marketplace.push(metadata);
  });
  if (process.env.MAX_PACKS) {
    console.log(`limiting packs to ${process.env.MAX_PACKS}`);
    return marketplace.slice(0, process.env.MAX_PACKS);
  }
  return marketplace;
}

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
      apiKey: "f5dfbee43cfa4c5024b10045c6d91461",
      indexName: "demisto",
      algoliaOptions: {
        typoTolerance: false,
        hitsPerPage: 1000,
        filters: "type:lvl1 OR type:content",
      }, // Optional, if provided by Algolia
    },
    sidebarCollapsible: true,
    navbar: {
      title: "",
      logo: {
        alt: "Cortex XSOAR for Developers (Formerly Demisto)",
        src: "/img/Cortex_XSoar_logos_RGB_Cortex-Ng-Soar-Horizontal.svg",
        srcDark: "/img/Cortex_XSoar_logos_RGB_Cortex-Ng-Soar-Horizontal-KO.svg",
      },
      items: [
        {
          to: "/docs/welcome",
          label: "Developer Docs",
          position: "left",
        },
        {
          to: "/docs/reference/articles-index",
          label: "Articles",
          position: "left",
        },
        {
          to: "/docs/reference/index",
          label: "Reference",
          position: "left",
        },
        {
          to: "/marketplace",
          label: "Marketplace",
          position: "left",
        },
        {
          label: "Partners",
          items: [
            { to: "/docs/partners/why-xsoar", label: "Why Cortex XSOAR?" },
            {
              to: "docs/partners/become-a-tech-partner",
              label: "Become a Partner",
            },
            {
              to: "/docs/partners/marketplace",
              label: "Marketplace",
            },
            {
              to: "/docs/partners/adopt",
              label: "Adopt-a-Pack",
            },
            {
              to: "/docs/partners/certification",
              label: "Pack Certification",
            },
            {
              to: "/docs/partners/office-hours",
              label: "Office Hours",
            },
            {
              to: "/docs/partners/development-partners",
              label: "Development Partners",
            },
            {
              to:
                "https://start.paloaltonetworks.com/become-a-technology-partner",
              label: "Sign Up Now",
            },
          ],
          position: "right",
        },
        {
          href: "https://blog.demisto.com/",
          label: "Blog",
          position: "right",
        },
        {
          href: "http://github.com/demisto/content/",
          position: "right",
          className: "header-github-link",
          "aria-label": "GitHub repository",
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
              label: "Become a Technology Partner",
            },
          ],
        },
        {
          title: "Social",
          items: [
            {
              label: "Blog",
              href: "https://blog.demisto.com/",
            },
          ],
        },
      ],
      logo: {
        alt: "Palo Alto Networks for Developers",
        src: "/img/PANW_Parent_Brand_Primary_Logo_RGB_KO.svg",
        // href: "https://pan.dev"
      },
      copyright: `Copyright © ${new Date().getFullYear()} Palo Alto Networks, Inc.`,
    },
    announcementBar: {
      id: "github_star",
      content:
        '⭐️ If you like Cortex XSOAR Content, give it a star on <a target="_blank" rel="noopener noreferrer" href="https://github.com/demisto/content">GitHub</a>! ⭐',
      backgroundColor: "#fafbfc",
      textColor: "#091E42",
    },
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
          showLastUpdateTime: true,
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
        sitemap: {
          cacheTime: 600 * 1000, // 600 sec - cache purge period
          changefreq: "weekly",
          priority: 0.5,
        },
      },
    ],
  ],
  customFields: {
    sites: [
      {
        label: "Products",
        items: [
          {
            href: "https://panos.pan.dev",
            label: "PAN-OS",
            logo: "/img/strata_favicon.png",
          },
          {
            href: "https://cortex.pan.dev",
            label: "Cortex Data Lake",
            logo: "/img/cortexfavicon.png",
          },
          {
            href: "https://xsoar.pan.dev",
            label: "Cortex XSOAR",
            logo: "/img/Cortex-XSOAR-product-green.svg",
          },
        ],
        position: "products",
      },
    ],
    marketplace: genMetaData(),
  },
  stylesheets: [
    {
      href: "https://use.fontawesome.com/releases/v5.15.0/css/all.css",
      type: "text/css",
      rel: "stylesheet",
    },
  ],
  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",
  onDuplicateRoutes: "warn",
};
