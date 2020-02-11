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
import classnames from "classnames";
import React from "react";
import styles from "./styles.module.css";

function NavLink({ to, href, label, position, ...props }) {
  const toUrl = useBaseUrl(to);
  return (
    <Link
      className="navbar__item navbar__link"
      {...(href
        ? {
            target: "_blank",
            rel: "noopener noreferrer",
            href
          }
        : {
            activeClassName: "navbar__link--active",
            to: toUrl
          })}
      {...props}
    >
      {label}
    </Link>
  );
}

function DocBar(props) {
  return (
    <div className="navbar__item dropdown dropdown--hoverable">
      <a className="navbar__link">{props.label}</a>
      <ul className="dropdown__menu">
        {props.items.map((linkItem, i) => (
          <li key={i}>
            <NavLink {...linkItem} key={i} />
          </li>
        ))}
      </ul>
    </div>
  );
}

function matchingRouteExist(routes, pathname) {
  return routes.some(route => matchPath(pathname, route));
}

function DocPage(props) {
  const { route, docsMetadata, location } = props;
  const { permalinkToSidebar, docsSidebars, version } = docsMetadata;
  const sidebar = permalinkToSidebar[location.pathname.replace(/\/$/, "")];
  const { siteConfig: { themeConfig = {} } = {} } = useDocusaurusContext();
  const { sidebarCollapsible = true, docbar = {} } = themeConfig;
  const { menus = [] } = docbar;

  if (!matchingRouteExist(route.routes, location.pathname)) {
    return <NotFound {...props} />;
  }

  return (
    <Layout version={version}>
      <nav id="doc-navbar" className={classnames("navbar", "navbar--light")}>
        <div className="navbar__inner">
          <div
            className={classnames("navbar__items", "docbar")}
            style={{ paddingLeft: "15%" }}
          >
            {menus.map((menuItem, i) => (
              <DocBar
                {...menuItem}
                key={i}
                style={{ display: "flex !important" }}
              />
            ))}
          </div>
        </div>
      </nav>
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
          <MDXProvider components={MDXComponents}>
            {renderRoutes(route.routes)}
          </MDXProvider>
        </main>
      </div>
    </Layout>
  );
}

export default DocPage;
