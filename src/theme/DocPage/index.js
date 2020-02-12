/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import renderRoutes from "@docusaurus/renderRoutes";
import { matchPath } from "@docusaurus/router";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { MDXProvider } from "@mdx-js/react";
import DocSidebar from "@theme/DocSidebar";
import Layout from "@theme/Layout";
import MDXComponents from "@theme/MDXComponents";
import NotFound from "@theme/NotFound";
import React, { useEffect, useRef, useState } from "react";
import styles from "./styles.module.css";

function matchingRouteExist(routes, pathname) {
  return routes.some(route => matchPath(pathname, route));
}

function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    if (typeof document !== "undefined") {
      try {
        const item = window.localStorage.getItem(key);
        return item ? JSON.parse(item) : initialValue;
      } catch (error) {
        console.log(error);
        return initialValue;
      }
    }
  });

  const setValue = value => {
    try {
      const valueToStore =
        value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      if (typeof document !== "undefined") {
        window.localStorage.setItem(key, JSON.stringify(valueToStore));
      }
    } catch (error) {
      console.log(error);
    }
  };

  return [storedValue, setValue];
}

const useResize = myRef => {
  const [sidebarWidth, setSidebarWidth] = useState(0);
  const handleResize = () => {
    if (myRef.current.getBoundingClientRect().height > 0) {
      setSidebarWidth(myRef.current.offsetWidth - 1);
    } else {
      setSidebarWidth(0);
    }
  };
  if (typeof document !== "undefined") {
    useEffect(() => {
      handleResize();
      window.addEventListener("resize", handleResize);

      return () => {
        window.removeEventListener("resize", handleResize);
      };
    }, [myRef.current]);
  }

  return { sidebarWidth };
};

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
  const sidebarRef = useRef();
  const { sidebarWidth } = useResize(sidebarRef);
  const [activeTabIndex, setActiveTabIndex] = useLocalStorage(null);

  if (!matchingRouteExist(route.routes, location.pathname)) {
    return <NotFound {...props} />;
  }

  return (
    <Layout version={version}>
      <div
        className="row row--no-gutters"
        style={{ paddingLeft: sidebarWidth }}
      >
        {options.map((menuItem, i) => (
          <a
            className={
              "button button--outline button--secondary button--md " +
              (activeTabIndex === i ? "button--active" : "")
            }
            style={{
              borderRadius: "5px 5px 0 0",
              borderColor: "var(--ifm-contents-border-color)",
              borderWidth: "1px",
              borderStyle: "solid",
              borderBottom: "none",
              padding:
                "calc( var(--ifm-button-padding-vertical) * .70 ) calc( var(--ifm-button-padding-horizontal) * .70 )"
            }}
            href={menuItem.to}
            onClick={() => setActiveTabIndex(i)}
            key={i}
          >
            {menuItem.label}
          </a>
        ))}
      </div>

      <div className={styles.docPage}>
        {sidebar && (
          <div className={styles.docSidebarContainer} ref={sidebarRef}>
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
