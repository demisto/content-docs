/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
import useUserPreferencesContext from '@theme/hooks/useUserPreferencesContext';
import clsx from 'clsx';
import React, { Children, cloneElement, useState } from 'react';
import styles from './styles.module.css';

function isInViewport(element) {
  const {top, left, bottom, right} = element.getBoundingClientRect();
  const {innerHeight, innerWidth} = window;
  return top >= 0 && right <= innerWidth && bottom <= innerHeight && left >= 0;
}

const keys = {
  left: 37,
  right: 39,
};

function ContentPackTabs(props) {
  const {lazy, block, defaultValue, values, groupId, className, downloadUrl, premium} = props;
  const {tabGroupChoices, setTabGroupChoices} = useUserPreferencesContext();
  const [selectedValue, setSelectedValue] = useState(defaultValue);
  const children = Children.toArray(props.children);
  const tabRefs = [];

  if (groupId != null) {
    const relevantTabGroupChoice = tabGroupChoices[groupId];

    if (
      relevantTabGroupChoice != null &&
      relevantTabGroupChoice !== selectedValue &&
      values.some((value) => value.value === relevantTabGroupChoice)
    ) {
      setSelectedValue(relevantTabGroupChoice);
    }
  }

  const handleTabChange = (event) => {
    const selectedTab = event.currentTarget;
    const selectedTabIndex = tabRefs.indexOf(selectedTab);
    const selectedTabValue = values[selectedTabIndex].value;
    setSelectedValue(selectedTabValue);

    if (groupId != null) {
      setTabGroupChoices(groupId, selectedTabValue);
      setTimeout(() => {
        if (isInViewport(selectedTab)) {
          return;
        }

        selectedTab.scrollIntoView({
          block: 'center',
          behavior: 'smooth',
        });
        selectedTab.classList.add(styles.tabItemActive);
        setTimeout(
          () => selectedTab.classList.remove(styles.tabItemActive),
          2000,
        );
      }, 150);
    }
  };

  const handleKeydown = (event) => {
    let focusElement;

    switch (event.keyCode) {
      case keys.right: {
        const nextTab = tabRefs.indexOf(event.target) + 1;
        focusElement = tabRefs[nextTab] || tabRefs[0];
        break;
      }

      case keys.left: {
        const prevTab = tabRefs.indexOf(event.target) - 1;
        focusElement = tabRefs[prevTab] || tabRefs[tabRefs.length - 1];
        break;
      }

      default:
        break;
    }

    focusElement?.focus();
  };

  return (
    <div className="tabs-container">
      <ul
        role="tablist"
        aria-orientation="horizontal"
        className={clsx(
          'tabs',
          {
            'tabs--block': block,
          },
          className,
        )}>
        {values.map(({ value, label }) => (
          <li
            role="tab"
            tabIndex={selectedValue === value ? 0 : -1}
            aria-selected={selectedValue === value}
            className={clsx('tabs__item', styles.tabItem, {
              'tabs__item--active': selectedValue === value,
            })}
            key={value}
            ref={(tabControl) => tabRefs.push(tabControl)}
            onKeyDown={handleKeydown}
            onFocus={handleTabChange}
            onClick={handleTabChange}>
            {label}
          </li>
        ))}
        {(premium == "true") ? (null) : (
            <li className={clsx('tabs__item', styles.tabItem, styles.downloadTabItem, styles.noAnimation)}>
                <a className={clsx("button button--primary button--outline button--md" )}
                   href={downloadUrl}
                   target="_blank"
                   title="To ensure proper installation, automatically download all other content packs that are required by this pack. ">
                Download With Dependencies
                </a>
            </li>
        )}
      </ul>
      {lazy ? (
        cloneElement(
          children.filter(
            (tabItem) => tabItem.props.value === selectedValue,
          )[0],
          {
            className: 'margin-vert--md',
          },
        )
      ) : (
        <div className="margin-vert--md">
          {children.map((tabItem, i) =>
            cloneElement(tabItem, {
              key: i,
              hidden: tabItem.props.value !== selectedValue,
            }),
          )}
        </div>
      )}
    </div>
  );
}

export default ContentPackTabs;
