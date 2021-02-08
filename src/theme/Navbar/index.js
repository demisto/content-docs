/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
import Link from "@docusaurus/Link";
import { useThemeConfig } from "@docusaurus/theme-common";
import useBaseUrl from "@docusaurus/useBaseUrl";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import useHideableNavbar from "@theme/hooks/useHideableNavbar";
import useLockBodyScroll from "@theme/hooks/useLockBodyScroll";
import useThemeContext from "@theme/hooks/useThemeContext";
import useWindowSize, { windowSizes } from "@theme/hooks/useWindowSize";
import IconMenu from "@theme/IconMenu";
import Logo from "@theme/Logo";
import NavbarItem from "@theme/NavbarItem";
import SearchBar from "@theme/SearchBar";
import Toggle from "@theme/Toggle";
import clsx from "clsx";
import React, { useCallback, useEffect, useState } from "react";
import styles from "./styles.module.css"; // retrocompatible with v1

const DefaultNavItemPosition = "right"; // If split links by left/right
// if position is unspecified, fallback to right (as v1)

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

function splitNavItemsByPosition(items) {
  const leftItems = items.filter(
    (item) => (item.position ?? DefaultNavItemPosition) === "left"
  );
  const rightItems = items.filter(
    (item) => (item.position ?? DefaultNavItemPosition) === "right"
  );
  const productItems = items.filter(
    (item) => (item.position ?? DefaultNavItemPosition) === "products"
  );
  return {
    leftItems,
    rightItems,
    productItems,
  };
}

function Navbar() {
  const {
    siteConfig: {
      customFields: { sites = [] },
    },
  } = useDocusaurusContext();
  const {
    navbar: { items, hideOnScroll, style },
    colorMode: { disableSwitch: disableColorModeSwitch },
  } = useThemeConfig();
  const [sidebarShown, setSidebarShown] = useState(false);
  const [isSearchBarExpanded, setIsSearchBarExpanded] = useState(false);
  const { isDarkTheme, setLightTheme, setDarkTheme } = useThemeContext();
  const { navbarRef, isNavbarVisible } = useHideableNavbar(hideOnScroll);
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
  const allItems = items.concat(sites);
  const { leftItems, rightItems, productItems } = splitNavItemsByPosition(
    allItems
  );
  return (
    <nav
      ref={navbarRef}
      className={clsx("navbar", "navbar--fixed-top", {
        "navbar--dark": style === "dark",
        "navbar--primary": style === "primary",
        "navbar-sidebar--show": sidebarShown,
        [styles.navbarHideable]: hideOnScroll,
        [styles.navbarHidden]: !isNavbarVisible,
      })}
    >
      <div className="navbar__inner">
        <div className="navbar__items">
          {items != null && items.length !== 0 && (
            <div
              aria-label="Navigation bar toggle"
              className="navbar__toggle"
              role="button"
              tabIndex={0}
              onClick={showSidebar}
              onKeyDown={showSidebar}
            >
              <IconMenu />
            </div>
          )}
          <Logo
            className="navbar__brand"
            imageClassName="navbar__logo"
            titleClassName={clsx("navbar__title", {
              [styles.hideLogoText]: isSearchBarExpanded,
            })}
          />
          {leftItems.map((item, i) => (
            <NavbarItem {...item} key={i} />
          ))}
        </div>
        <div className="navbar__items navbar__items--right">
          {productItems.map((linkItem, i) => (
            <SiteItem {...linkItem} key={i} />
          ))}
          {rightItems.map((item, i) => (
            <NavbarItem {...item} key={i} />
          ))}
          {!disableColorModeSwitch && (
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
          <Logo
            className="navbar__brand"
            imageClassName="navbar__logo"
            titleClassName="navbar__title"
            onClick={hideSidebar}
          />
          {!disableColorModeSwitch && sidebarShown && (
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
              {items.map((item, i) => (
                <NavbarItem mobile {...item} onClick={hideSidebar} key={i} />
              ))}
            </ul>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
