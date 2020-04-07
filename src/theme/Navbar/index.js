/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import React, {useCallback, useState} from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import isInternalUrl from '@docusaurus/isInternalUrl';

import SearchBar from '@theme/SearchBar';
import Toggle from '@theme/Toggle';

import classnames from 'classnames';

import useThemeContext from '@theme/hooks/useThemeContext';
import useHideableNavbar from '@theme/hooks/useHideableNavbar';
import useLockBodyScroll from '@theme/hooks/useLockBodyScroll';

import styles from './styles.module.css';

function NavLink({activeBasePath, to, href, label, position, ...props}) {
  const toUrl = useBaseUrl(to);
  const activeBaseUrl = useBaseUrl(activeBasePath);

  return (
    <Link
      className="navbar__item navbar__link"
      {...(href
        ? {
            target: '_blank',
            rel: 'noopener noreferrer',
            href,
          }
        : {
            activeClassName: 'navbar__link--active',
            to: toUrl,
            ...(activeBasePath
              ? {
                  isActive: (_match, location) =>
                    location.pathname.startsWith(activeBaseUrl),
                }
              : null),
          })}
      {...props}>
      {label}
    </Link>
  );
}

function SiteLink({
  activeBasePath,
  to,
  href,
  label,
  position,
  logo,
  ...props
}) {
  const toUrl = useBaseUrl(to);
  const activeBaseUrl = useBaseUrl(activeBasePath);

  return (
    <Link
      className="navbar__item navbar__link"
      {...(href
        ? {
            target: "_self",
            rel: "noopener noreferrer",
            href
          }
        : {
            activeClassName: "navbar__link--active",
            to: toUrl,
            ...(activeBasePath
              ? {
                  isActive: (_match, location) =>
                    location.pathname.startsWith(activeBaseUrl)
                }
              : null)
          })}
      {...props}
    >
      <span>
        <div className="avatar">
          <img className="avatar__photo avatar__photo--sm" src={logo} />
          <div className="avatar__intro">
            <h5 className="avatar__name">{label}</h5>
          </div>
        </div>
      </span>
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

function SiteMenu(props) {
  return (
    <div className="navbar__item dropdown dropdown--hoverable">
      <a className="navbar__link">{props.label}</a>
      <ul className="dropdown__menu">
        {props.items.map((linkItem, i) => (
          <li key={i}>
            <SiteLink {...linkItem} key={i} />
          </li>
        ))}
      </ul>
    </div>
  );
}

function Navbar() {
  const {siteConfig = {}, isClient} = useDocusaurusContext();
  const {baseUrl, themeConfig = {}} = siteConfig;
  const {navbar = {}, disableDarkMode = false} = themeConfig;
  const {
    title, 
    logo = {}, 
    links = [], 
    menus = [],
    sites = [],
    hideOnScroll = false
  } = navbar;

  const [sidebarShown, setSidebarShown] = useState(false);
  const [isSearchBarExpanded, setIsSearchBarExpanded] = useState(false);
  const [menuShown, setMenuShown] = useState({});
  const [siteMenuShown, setSiteMenuShown] = useState({});
  const {isDarkTheme, setLightTheme, setDarkTheme} = useThemeContext();
  const {navbarRef, isNavbarVisible} = useHideableNavbar(hideOnScroll);

  useLockBodyScroll(sidebarShown);

  const showSidebar = useCallback(() => {
    setSidebarShown(true);
  }, [setSidebarShown]);
  const hideSidebar = useCallback(() => {
    setSidebarShown(false);
  }, [setSidebarShown]);

  const onToggleChange = useCallback(
    e => (e.target.checked ? setDarkTheme() : setLightTheme()),
    [setLightTheme, setDarkTheme],
  );

  const logoLink = logo.href || baseUrl;
  let logoLinkProps = {};

  if (logo.target) {
    logoLinkProps = {target: logo.target};
  } else if (!isInternalUrl(logoLink)) {
    logoLinkProps = {
      rel: 'noopener noreferrer',
      target: '_blank',
    };
  }

  const logoSrc = logo.srcDark && isDarkTheme ? logo.srcDark : logo.src;
  const logoImageUrl = useBaseUrl(logoSrc);

  return (
    <nav
      ref={navbarRef}
      className={classnames('navbar', 'navbar--light', 'navbar--fixed-top', {
        'navbar-sidebar--show': sidebarShown,
        [styles.navbarHideable]: hideOnScroll,
        [styles.navbarHidden]: !isNavbarVisible,
      })}>
      <div className="navbar__inner">
        <div className="navbar__items">
          <div
            aria-label="Navigation bar toggle"
            className="navbar__toggle"
            role="button"
            tabIndex={0}
            onClick={showSidebar}
            onKeyDown={showSidebar}>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="30"
              height="30"
              viewBox="0 0 30 30"
              role="img"
              focusable="false">
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
          <Link className="navbar__brand" to={logoLink} {...logoLinkProps}>
            {logo != null && (
              <img
                key={isClient}
                className="navbar__logo"
                src={logoImageUrl}
                alt={logo.alt}
              />
            )}
            {title != null && (
              <strong
                className={classnames('navbar__title', {
                  [styles.hideLogoText]: isSearchBarExpanded,
                })}>
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
            .filter(linkItem => linkItem.position !== 'right')
            .map((linkItem, i) => (
              <NavLink {...linkItem} key={i} />
            ))}
            {sites
            .filter(siteItem => siteItem.position !== "right")
            .map((siteItem, i) => (
              <SiteMenu {...siteItem} key={i} />
            ))}
        </div>
        <div className="navbar__items navbar__items--right">
          {menus
            .filter(menuItem => menuItem.position === "right")
            .map((menuItem, i) => (
              <NavMenu {...menuItem} key={i} />
            ))}
          {links
            .filter(linkItem => linkItem.position === 'right')
            .map((linkItem, i) => (
              <NavLink {...linkItem} key={i} />
            ))}
          {sites
            .filter(siteItem => siteItem.position === "right")
            .map((siteItem, i) => (
              <SiteMenu {...siteItem} key={i} />
            ))}
          {!disableDarkMode && (
            <Toggle
              className={styles.displayOnlyInLargeViewport}
              aria-label="Dark mode toggle"
              checked={isDarkTheme}
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
        onClick={hideSidebar}
      />
      <div className="navbar-sidebar">
        <div className="navbar-sidebar__brand">
          <Link
            className="navbar__brand"
            onClick={hideSidebar}
            to={logoLink}
            {...logoLinkProps}>
            {logo != null && (
              <img
                key={isClient}
                className="navbar__logo"
                src={logoImageUrl}
                alt={logo.alt}
              />
            )}
            {title != null && (
              <strong className="navbar__title">{title}</strong>
            )}
          </Link>
          {!disableDarkMode && sidebarShown && (
            <Toggle
              aria-label="Dark mode toggle in sidebar"
              checked={isDarkTheme}
              onChange={onToggleChange}
            />
          )}
        </div>
        <div className="navbar-sidebar__items">
          <div className="menu">
            <ul className="menu__list">
            {menus.map((menuItem, i) => {
                var className = menuShown[i]
                var className = siteMenuShown[i]
                  ? "menu__list-item"
                  : "menu__list-item menu__list-item--collapsed";

                return (
                  <li className={className} key={i}>
                    <a
                      className="menu__link menu__link--sublist"
                      onClick={() => toggleMenu(i)}
                      onClick={() => toggleSiteMenu(i)}
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
              {menus.map((menuItem, i) => {
                var className = menuShown[i]
                var className = siteMenuShown[i]
                  ? "menu__list-item"
                  : "menu__list-item menu__list-item--collapsed";

                return (
                  <li className={className} key={i}>
                    <a
                      className="menu__link menu__link--sublist"
                      onClick={() => toggleMenu(i)}
                      onClick={() => toggleSiteMenu(i)}
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
            </ul>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
