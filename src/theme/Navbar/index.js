/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import Head from "@docusaurus/Head";
import Link from "@docusaurus/Link";
import useBaseUrl from "@docusaurus/useBaseUrl";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import useTheme from "@theme/hooks/useTheme";
import SearchBar from "@theme/SearchBar";
import Toggle from "@theme/Toggle";
import classnames from "classnames";
import React, { useCallback, useState } from "react";
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

function NavMenu(props) {
  return (
    <div className="navbar__item dropdown dropdown--hoverable">
      <a className="navbar__link">{props.label} &#9662;</a>
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

function Navbar() {
  const context = useDocusaurusContext();
  const [sidebarShown, setSidebarShown] = useState(false);
  const [menuShown, setMenuShown] = useState({});
  const [isSearchBarExpanded, setIsSearchBarExpanded] = useState(false);
  const [theme, setTheme] = useTheme();
  const { siteConfig = {} } = context;
  const { baseUrl, themeConfig = {} } = siteConfig;
  const { navbar = {}, disableDarkMode = false } = themeConfig;
  const { title, logo = {}, links = [], menus = [] } = navbar;

  const showSidebar = useCallback(() => {
    setSidebarShown(true);
  }, [setSidebarShown]);
  const hideSidebar = useCallback(() => {
    setSidebarShown(false);
  }, [setSidebarShown]);

  const toggleMenu = id => {
    setMenuShown(menuShown => {
      return { ...menuShown, [id]: !menuShown[id] };
    });
  };

  const onToggleChange = useCallback(
    e => setTheme(e.target.checked ? "dark" : ""),
    [setTheme]
  );

  const logoUrl = useBaseUrl(logo.src);
  return (
    <>
      <Head>
        {/* TODO: Do not assume that it is in english language */}
        <html lang="en" data-theme={theme} />
      </Head>
      <nav
        className={classnames("navbar", "navbar--light", "navbar--fixed-top", {
          "navbar-sidebar--show": sidebarShown
        })}
      >
        <div className="navbar__inner">
          <div className="navbar__items">
            <div
              aria-label="Navigation bar toggle"
              className="navbar__toggle"
              role="button"
              tabIndex={0}
              onClick={showSidebar}
              onKeyDown={showSidebar}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="30"
                height="30"
                viewBox="0 0 30 30"
                role="img"
                focusable="false"
              >
                <title>Menu</title>
                <path
                  stroke="currentColor"
                  strokeLinecap="round"
                  strokeMiterlimit="10"
                  strokeWidth="2"
                  d="M4 7h22M4 15h22M4 23h22"
                />
              </svg>
            </div>
            <Link className="navbar__brand" to={baseUrl}>
              {logo != null && (
                <img className="navbar__logo" src={logoUrl} alt={logo.alt} />
              )}
              {title != null && (
                <strong
                  className={isSearchBarExpanded ? styles.hideLogoText : ""}
                >
                  {title}
                </strong>
              )}
            </Link>
            {menus
              .filter(menuItem => menuItem.position !== "right")
              .map((menuItem, i) => (
                <NavMenu {...menuItem} key={i} />
              ))}
            {links
              .filter(linkItem => linkItem.position !== "right")
              .map((linkItem, i) => (
                <NavLink {...linkItem} key={i} />
              ))}
          </div>
          <div className="navbar__items navbar__items--right">
            {menus
              .filter(menuItem => menuItem.position === "right")
              .map((menuItem, i) => (
                <NavMenu {...menuItem} key={i} />
              ))}
            {links
              .filter(linkItem => linkItem.position === "right")
              .map((linkItem, i) => (
                <NavLink {...linkItem} key={i} />
              ))}
            {!disableDarkMode && (
              <Toggle
                className={styles.displayOnlyInLargeViewport}
                aria-label="Dark mode toggle"
                checked={theme === "dark"}
                onChange={onToggleChange}
              />
            )}
            <SearchBar
              handleSearchBarToggle={setIsSearchBarExpanded}
              isSearchBarExpanded={isSearchBarExpanded}
            />
          </div>
        </div>
        <div
          role="presentation"
          className="navbar-sidebar__backdrop"
          onClick={() => {
            setSidebarShown(false);
          }}
        />
        <div className="navbar-sidebar">
          <div className="navbar-sidebar__brand">
            <Link className="navbar__brand" onClick={hideSidebar} to={baseUrl}>
              {logo != null && (
                <img className="navbar__logo" src={logoUrl} alt={logo.alt} />
              )}
              {title != null && <strong>{title}</strong>}
            </Link>
            {!disableDarkMode && sidebarShown && (
              <Toggle
                aria-label="Dark mode toggle in sidebar"
                checked={theme === "dark"}
                onChange={onToggleChange}
              />
            )}
          </div>
          <div className="navbar-sidebar__items">
            <div className="menu">
              <ul className="menu__list">
                {menus.map((menuItem, i) => {
                  var className = menuShown[i]
                    ? "menu__list-item"
                    : "menu__list-item menu__list-item--collapsed";

                  return (
                    <li className={className} key={i}>
                      <a
                        className="menu__link menu__link--sublist"
                        onClick={() => toggleMenu(i)}
                      >
                        {menuItem.label}
                      </a>
                      <ul className="menu__list">
                        {menuItem.items.map((item, i) => (
                          <li className="menu__list-item" key={i}>
                            <NavLink
                              className="menu__link"
                              {...item}
                              onClick={hideSidebar}
                            />
                          </li>
                        ))}
                      </ul>
                    </li>
                  );
                })}
                {links.map((linkItem, i) => (
                  <li className="menu__list-item" key={i}>
                    <NavLink
                      className="menu__link"
                      {...linkItem}
                      onClick={hideSidebar}
                    />
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </nav>
    </>
  );
}

export default Navbar;
