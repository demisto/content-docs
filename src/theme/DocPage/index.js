/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import Link from "@docusaurus/Link";
import renderRoutes from "@docusaurus/renderRoutes";
import { matchPath } from "@docusaurus/router";
import useBaseUrl from "@docusaurus/useBaseUrl";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { MDXProvider } from "@mdx-js/react";
import DocSidebar from "@theme/DocSidebar";
import Layout from "@theme/Layout";
import MDXComponents from "@theme/MDXComponents";
import NotFound from "@theme/NotFound";
import React from "react";
import styles from "./styles.module.css";

function matchingRouteExist(routes, pathname) {
  return routes.some(route => matchPath(pathname, route));
}

function DocPage(props) {
  const { route, docsMetadata, location } = props;
  const { permalinkToSidebar, docsSidebars, version } = docsMetadata;
  const sidebar = permalinkToSidebar[location.pathname.replace(/\/$/, "")];
  const {
    siteConfig: { themeConfig = {} } = {},
    siteConfig: { customFields = {} } = {}
  } = useDocusaurusContext();
  const { sidebarCollapsible = true } = themeConfig;
  const { docbar = {} } = customFields;
  const { options = [] } = docbar;

  if (!matchingRouteExist(route.routes, location.pathname)) {
    return <NotFound {...props} />;
  }

  return (
    <Layout version={version}>
      <div className={styles.docPage}>
        {sidebar && (
          <div className={styles.docSidebarContainer}>
            <DocSidebar
              docsSidebars={docsSidebars}
              location={location}
              sidebar={sidebar}
              sidebarCollapsible={sidebarCollapsible}
            />
          </div>
        )}
        <main className={styles.docMainContainer}>
          <div
            className="row row--no-gutters"
            style={{
              position: "sticky",
              top: "60px",
              zIndex: 1,
              backgroundColor: "var(--ifm-background-color)"
            }}
          >
            {options.map((menuItem, i) => (
              <Link
                className={
                  "button button--outline button--secondary button--md " +
                  (typeof window !== "undefined" &&
                  window.location.pathname.split("/")[2] ==
                    useBaseUrl(menuItem.to).split("/")[2]
                    ? "button--active--tab shadow--lw"
                    : "")
                }
                style={{
                  borderRadius: "0 0 0 0",
                  borderColor: "var(--ifm-contents-border-color)",
                  borderWidth: "0",
                  padding:
                    "calc( var(--ifm-button-padding-vertical) * 1.5  ) calc( var(--ifm-button-padding-horizontal) * .65 )"
                }}
                key={i}
                to={useBaseUrl(menuItem.to)}
              >
                {menuItem.label}
              </Link>
            ))}
          </div>
          <MDXProvider components={MDXComponents}>
            {renderRoutes(route.routes)}
          </MDXProvider>
        </main>
      </div>
    </Layout>
  );
}

export default DocPage;
