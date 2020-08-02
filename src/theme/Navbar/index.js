/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import Link from "@docusaurus/Link";
import useBaseUrl from "@docusaurus/useBaseUrl";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import useHideableNavbar from "@theme/hooks/useHideableNavbar";
import useLockBodyScroll from "@theme/hooks/useLockBodyScroll";
import useLogo from "@theme/hooks/useLogo";
import useThemeContext from "@theme/hooks/useThemeContext";
import useWindowSize, { windowSizes } from "@theme/hooks/useWindowSize";
import SearchBar from "@theme/SearchBar";
import Toggle from "@theme/Toggle";
import clsx from "clsx";
import React, { useCallback, useEffect, useState } from "react";
import styles from "./styles.module.css";

// retrocompatible with v1
const DefaultNavItemPosition = "right";

function NavLink({
  activeBasePath,
  activeBaseRegex,
  to,
  href,
  label,
  activeclassname = "navbar__link--active",
  prependBaseUrlToHref,
  ...props
}) {
  const toUrl = useBaseUrl(to);
  const activeBaseUrl = useBaseUrl(activeBasePath);
  const normalizedHref = useBaseUrl(href, { forcePrependBaseUrl: true });

  return (
    <Link
      {...(href
        ? {
            target: "_blank",
            rel: "noopener noreferrer",
            href: prependBaseUrlToHref ? normalizedHref : href,
          }
        : {
            isNavLink: true,
            activeclassname,
            to: toUrl,
            ...(activeBasePath || activeBaseRegex
              ? {
                  isActive: (_match, location) =>
                    activeBaseRegex
                      ? new RegExp(activeBaseRegex).test(location.pathname)
                      : location.pathname.startsWith(activeBaseUrl),
                }
              : null),
          })}
      {...props}
    >
      {label}
    </Link>
  );
}

function SiteLink({
  activeBasePath,
  activeBaseRegex,
  to,
  href,
  label,
  logo,
  activeclassname = "navbar__link--active",
  prependBaseUrlToHref,
  ...props
}) {
  const toUrl = useBaseUrl(to);
  const activeBaseUrl = useBaseUrl(activeBasePath);
  const normalizedHref = useBaseUrl(href, { forcePrependBaseUrl: true });

  return (
    <Link
      {...(href
        ? {
            target: "_self",
            rel: "noopener noreferrer",
            href: prependBaseUrlToHref ? normalizedHref : href,
          }
        : {
            isNavLink: true,
            activeclassname,
            to: toUrl,
            ...(activeBasePath || activeBaseRegex
              ? {
                  isActive: (_match, location) =>
                    activeBaseRegex
                      ? new RegExp(activeBaseRegex).test(location.pathname)
                      : location.pathname.startsWith(activeBaseUrl),
                }
              : null),
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

function NavItem({
  items,
  position = DefaultNavItemPosition,
  className,
  ...props
}) {
  const navLinkClassNames = (extraClassName, isDropdownItem = false) =>
    clsx(
      {
        "navbar__item navbar__link": !isDropdownItem,
        dropdown__link: isDropdownItem,
      },
      extraClassName
    );

  if (!items) {
    return <NavLink className={navLinkClassNames(className)} {...props} />;
  }

  return (
    <div
      className={clsx("navbar__item", "dropdown", "dropdown--hoverable", {
        "dropdown--left": position === "left",
        "dropdown--right": position === "right",
      })}
    >
      <NavLink
        className={navLinkClassNames(className)}
        {...props}
        onClick={(e) => e.preventDefault()}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            e.target.parentNode.classList.toggle("dropdown--show");
          }
        }}
      >
        {props.label}
      </NavLink>
      <ul className="dropdown__menu">
        {items.map(
          ({ className: childItemClassName, ...childItemProps }, i) => (
            <li key={i}>
              <NavLink
                activeclassname="dropdown__link--active"
                className={navLinkClassNames(childItemClassName, true)}
                {...childItemProps}
              />
            </li>
          )
        )}
      </ul>
    </div>
  );
}

function SiteItem({
  items,
  position = DefaultNavItemPosition,
  className,
  ...props
}) {
  const navLinkClassNames = (extraClassName, isDropdownItem = false) =>
    clsx(
      {
        "navbar__item navbar__link": !isDropdownItem,
        dropdown__link: isDropdownItem,
      },
      extraClassName
    );

  if (!items) {
    return <NavLink className={navLinkClassNames(className)} {...props} />;
  }

  return (
    <div
      className={clsx("navbar__item", "dropdown", "dropdown--hoverable", {
        "dropdown--right": position === "right",
        "dropdown--left": position === "products",
      })}
    >
      <NavLink
        className={navLinkClassNames(className)}
        {...props}
        onClick={(e) => e.preventDefault()}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            e.target.parentNode.classList.toggle("dropdown--show");
          }
        }}
      >
        {props.label}
      </NavLink>
      <ul className="dropdown__menu">
        {items.map(
          ({ className: childItemClassName, ...childItemProps }, i) => (
            <li key={i}>
              <SiteLink
                activeclassname="dropdown__link--active"
                className={navLinkClassNames(childItemClassName, true)}
                {...childItemProps}
              />
            </li>
          )
        )}
      </ul>
    </div>
  );
}

function MobileNavItem({ items, position: _position, className, ...props }) {
  // Need to destructure position from props so that it doesn't get passed on.
  const navLinkClassNames = (extraClassName, isSubList = false) =>
    clsx(
      "menu__link",
      {
        "menu__link--sublist no_dropdown": isSubList,
      },
      extraClassName
    );

  if (!items) {
    return (
      <li className="menu__list-item">
        <NavLink className={navLinkClassNames(className)} {...props} />
      </li>
    );
  }

  return (
    <li className="menu__list-item">
      <NavLink className={navLinkClassNames(className, true)} {...props}>
        {props.label}
      </NavLink>
      <ul className="menu__list">
        {items.map(
          ({ className: childItemClassName, ...childItemProps }, i) => (
            <li className="menu__list-item" key={i}>
              <NavLink
                activeClassName="menu__link--active"
                className={navLinkClassNames(childItemClassName)}
                {...childItemProps}
                onClick={props.onClick}
              />
            </li>
          )
        )}
      </ul>
    </li>
  );
}

function MobileSiteItem({ items, position: _position, className, ...props }) {
  // Need to destructure position from props so that it doesn't get passed on.
  const navLinkClassNames = (extraClassName, isSubList = false) =>
    clsx(
      "menu__link no_dropdown",
      {
        "menu__link--sublist": isSubList,
      },
      extraClassName
    );

  if (!items) {
    return (
      <li className="menu__list-item">
        <NavLink className={navLinkClassNames(className)} {...props} />
      </li>
    );
  }

  return (
    <li className="menu__list-item">
      <NavLink className={navLinkClassNames(className, true)} {...props}>
        {props.label}
      </NavLink>
      <ul className="menu__list">
        {items.map(
          ({ className: childItemClassName, ...childItemProps }, i) => (
            <li className="menu__list-item" key={i}>
              <SiteLink
                activeClassName="menu__link--active"
                className={navLinkClassNames(childItemClassName)}
                {...childItemProps}
                onClick={props.onClick}
              />
            </li>
          )
        )}
      </ul>
    </li>
  );
}

// If split links by left/right
// if position is unspecified, fallback to right (as v1)
function splitLinks(links) {
  const leftLinks = links.filter(
    (linkItem) => (linkItem.position ?? DefaultNavItemPosition) === "left"
  );
  const rightLinks = links.filter(
    (linkItem) => (linkItem.position ?? DefaultNavItemPosition) === "right"
  );
  const productLinks = links.filter(
    (linkItem) => (linkItem.position ?? DefaultNavItemPosition) === "products"
  );
  return {
    leftLinks,
    rightLinks,
    productLinks,
  };
}

function Navbar() {
  const {
    siteConfig: {
      themeConfig: {
        navbar: { title, links = [], sites = [], hideOnScroll = false } = {},
        disableDarkMode = false,
      },
    },
    isClient,
  } = useDocusaurusContext();
  const [sidebarShown, setSidebarShown] = useState(false);
  const [isSearchBarExpanded, setIsSearchBarExpanded] = useState(false);

  const { isDarkTheme, setLightTheme, setDarkTheme } = useThemeContext();
  const { navbarRef, isNavbarVisible } = useHideableNavbar(hideOnScroll);
  const { logoLink, logoLinkProps, logoImageUrl, logoAlt } = useLogo();

  useLockBodyScroll(sidebarShown);

  const showSidebar = useCallback(() => {
    setSidebarShown(true);
  }, [setSidebarShown]);
  const hideSidebar = useCallback(() => {
    setSidebarShown(false);
  }, [setSidebarShown]);

  const onToggleChange = useCallback(
    (e) => (e.target.checked ? setDarkTheme() : setLightTheme()),
    [setLightTheme, setDarkTheme]
  );

  const windowSize = useWindowSize();

  useEffect(() => {
    if (windowSize === windowSizes.desktop) {
      setSidebarShown(false);
    }
  }, [windowSize]);

  const allLinks = links.concat(sites);
  const { leftLinks, rightLinks, productLinks } = splitLinks(allLinks);

  return (
    <nav
      ref={navbarRef}
      className={clsx("navbar", "navbar--light", "navbar--fixed-top", {
        "navbar-sidebar--show": sidebarShown,
        [styles.navbarHideable]: hideOnScroll,
        [styles.navbarHidden]: !isNavbarVisible,
      })}
    >
      <div className="navbar__inner">
        <div className="navbar__items">
          {links != null && links.length !== 0 && (
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
          )}
          <Link className="navbar__brand" to={logoLink} {...logoLinkProps}>
            {logoImageUrl != null && (
              <img
                key={isClient}
                className="navbar__logo"
                src={logoImageUrl}
                alt={logoAlt}
              />
            )}
            {title != null && (
              <strong
                className={clsx("navbar__title", {
                  [styles.hideLogoText]: isSearchBarExpanded,
                })}
              >
                {title}
              </strong>
            )}
          </Link>
          {leftLinks.map((linkItem, i) => (
            <NavItem {...linkItem} key={i} />
          ))}
        </div>
        <div className="navbar__items navbar__items--right">
          {productLinks.map((linkItem, i) => (
            <SiteItem {...linkItem} key={i} />
          ))}
          {rightLinks.map((linkItem, i) => (
            <NavItem {...linkItem} key={i} />
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
            {...logoLinkProps}
          >
            {logoImageUrl != null && (
              <img
                key={isClient}
                className="navbar__logo"
                src={logoImageUrl}
                alt={logoAlt}
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
              {sites.map((linkItem, i) => (
                <MobileSiteItem {...linkItem} onClick={hideSidebar} key={i} />
              ))}
              {links.map((linkItem, i) => (
                <MobileNavItem {...linkItem} onClick={hideSidebar} key={i} />
              ))}
            </ul>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;