/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import React, {useState, useCallback} from 'react';
import classnames from 'classnames';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import useLockBodyScroll from '@theme/hooks/useLockBodyScroll';
import Link from '@docusaurus/Link';
import isInternalUrl from '@docusaurus/isInternalUrl';

import styles from './styles.module.css';

const MOBILE_TOGGLE_SIZE = 24;

function DocSidebarItem({item, onItemClick, collapsible}) {
  const {items, href, label, type} = item;
  const [collapsed, setCollapsed] = useState(item.collapsed);
  const [prevCollapsedProp, setPreviousCollapsedProp] = useState(null);

  // If the collapsing state from props changed, probably a navigation event
  // occurred. Overwrite the component's collapsed state with the props'
  // collapsed value.
  if (item.collapsed !== prevCollapsedProp) {
    setPreviousCollapsedProp(item.collapsed);
    setCollapsed(item.collapsed);
  }

  const handleItemClick = useCallback(e => {
    e.preventDefault();
    setCollapsed(state => !state);
  });

  switch (type) {
    case 'category':
      return (
        items.length > 0 && (
          <li
            className={classnames('menu__list-item', {
              'menu__list-item--collapsed': collapsed,
            })}
            key={label}>
            <a
              className={classnames('menu__link', {
                'menu__link--sublist': collapsible,
                'menu__link--active': collapsible && !item.collapsed,
              })}
              href="#!"
              onClick={collapsible ? handleItemClick : undefined}>
              {label}
            </a>
            <ul className="menu__list">
              {items.map(childItem => (
                <DocSidebarItem
                  key={childItem.label}
                  item={childItem}
                  onItemClick={onItemClick}
                  collapsible={collapsible}
                />
              ))}
            </ul>
          </li>
        )
      );

    case 'link':
    default:
      return (
        <li className="menu__list-item" key={label}>
          <Link
            className="menu__link"
            to={href}
            {...(isInternalUrl(href)
              ? {
                  activeClassName: 'menu__link--active',
                  exact: true,
                  onClick: onItemClick,
                }
              : {
                  target: '_blank',
                  rel: 'noreferrer noopener',
                })}>
            {label}
          </Link>
        </li>
      );
  }
}

// Calculate the category collapsing state when a page navigation occurs.
// We want to automatically expand the categories which contains the current page.
function mutateSidebarCollapsingState(item, path, level) {
  const {items, href, type} = item;
  switch (type) {
    case 'category': {
      const anyChildItemsActive =
        items
          .map(childItem => mutateSidebarCollapsingState(childItem, path, level+1))
          .filter(val => val).length > 0;
      // eslint-disable-next-line no-param-reassign
      item.collapsed = !anyChildItemsActive && level > 0;
      return anyChildItemsActive;
    }

    case 'link':
    default:
      return href === path;
  }
}

function DocSidebar(props) {
  const [showResponsiveSidebar, setShowResponsiveSidebar] = useState(false);
  const {
    siteConfig: {themeConfig: {navbar: {title, logo = {}} = {}}} = {},
  } = useDocusaurusContext();
  const logoUrl = useBaseUrl(logo.src);

  const {
    docsSidebars,
    path,
    sidebar: currentSidebar,
    sidebarCollapsible,
  } = props;

  useLockBodyScroll(showResponsiveSidebar);

  if (!currentSidebar) {
    return null;
  }

  const sidebarData = docsSidebars[currentSidebar];

  if (!sidebarData) {
    throw new Error(
      `Cannot find the sidebar "${currentSidebar}" in the sidebar config!`,
    );
  }

  if (sidebarCollapsible) {
    sidebarData.forEach(sidebarItem =>
      mutateSidebarCollapsingState(sidebarItem, path, 0),
    );
  }

  return (
    <div className={styles.sidebar}>
      <div className={styles.sidebarLogo}>
        {logo != null && <img src={logoUrl} alt={logo.alt} />}
        {title != null && <strong>{title}</strong>}
      </div>
      <div
        className={classnames('menu', 'menu--responsive', styles.menu, {
          'menu--show': showResponsiveSidebar,
        })}>
        <button
          aria-label={showResponsiveSidebar ? 'Close Menu' : 'Open Menu'}
          className="button button--secondary button--sm menu__button"
          type="button"
          onClick={() => {
            setShowResponsiveSidebar(!showResponsiveSidebar);
          }}>
          {showResponsiveSidebar ? (
            <span
              className={classnames(
                styles.sidebarMenuIcon,
                styles.sidebarMenuCloseIcon,
              )}>
              &times;
            </span>
          ) : (
            <svg
              className={styles.sidebarMenuIcon}
              xmlns="http://www.w3.org/2000/svg"
              height={MOBILE_TOGGLE_SIZE}
              width={MOBILE_TOGGLE_SIZE}
              viewBox="0 0 32 32"
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
          )}
        </button>
        <ul className="menu__list">
          {sidebarData.map(item => (
            <DocSidebarItem
              key={item.label}
              item={item}
              onItemClick={() => {
                setShowResponsiveSidebar(false);
              }}
              collapsible={sidebarCollapsible}
            />
          ))}
        </ul>
      </div>
    </div>
  );
}

export default DocSidebar;
