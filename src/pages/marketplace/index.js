/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import { translate } from "@docusaurus/Translate";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import IconArrow from "@theme/IconArrow";
import Layout from "@theme/Layout";
import clsx from "clsx";
import queryString from "query-string";
import React, { useCallback, useEffect, useState } from "react";
import { useMediaQuery } from "react-responsive";
import { useLocation } from "react-router-dom";
import Button from "../../theme/Button";
import MarketplaceSidebar from "../../theme/MarketplaceSidebar";
import styles from "./styles.module.css";

const TITLE = "🛍️";
const DESCRIPTION = "Palo Alto Networks XSOAR Marketplace";

function capitalizeFirstLetter(string) {
  if (typeof string === "string") {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
}

function Marketplace() {
  const location = useLocation();
  const params = queryString.parse(location.search);
  const isBreakpoint = useMediaQuery({ query: "(max-width: 1321px)" });
  const { siteConfig } = useDocusaurusContext();
  const [hiddenSidebarContainer, setHiddenSidebarContainer] = useState(false);
  const [hiddenSidebar, setHiddenSidebar] = useState(false);
  const toggleSidebar = useCallback(() => {
    if (hiddenSidebar) {
      setHiddenSidebar(false);
    }
    setHiddenSidebarContainer(!hiddenSidebarContainer);
  }, [hiddenSidebar]);
  const marketplace = siteConfig.customFields.marketplace;
  const [showNew, setShowNew] = useState(false);
  const [showFeatured, setShowFeatured] = useState(false);
  const [price, setPrice] = useState(false);
  const [support, setSupport] = useState(false);
  const [author, setAuthor] = useState(false);
  const [useCase, setUseCase] = useState(false);
  const [integration, setIntegration] = useState(false);
  const [category, setCategory] = useState(false);
  const [value, setValue] = useState("");

  // Parse URL query params
  useEffect(() => {
    if (!showNew && params.new) setShowNew(params.new);
    if (!showFeatured && params.featured) setShowNew(params.featured);
    if (!price && params.price) setPrice(params.price);
    if (!support && params.support) setSupport(params.support);
    if (!author && params.vendor) setAuthor(params.vendor);
    if (!useCase && params.useCase) setUseCase(params.useCase);
    if (!integration && params.integration) setIntegration(params.integration);
    if (!category && params.category) setCategory(params.category);
    if (!value && params.q) setValue(params.q);
  }, []);

  const filters = {
    ...((price == "free" && { price: 0 }) ||
      (price == "premium" && { premium: true })),
    ...(author && { author: author }),
    ...(useCase && { useCases: useCase }),
    ...(integration && { integrations: integration }),
    ...(category && { categories: category }),
    ...(support && { support: support }),
    ...(showNew && { new: showNew }),
    ...(showFeatured && { featured: showFeatured }),
  };

  const preFilteredPacks = marketplace.filter((pack) => {
    for (var key in filters) {
      if (key == "useCases" && pack[key].includes(useCase)) return true;

      if (key == "categories" && pack[key].includes(category)) return true;

      if (key == "integrations") {
        var match = false;
        pack[key].map((i) => {
          if (i.name == integration) {
            match = true;
          }
        });
        if (match) {
          return true;
        }
      }

      if (
        key == "new" &&
        (new Date() - new Date(pack.created)) / (1000 * 60 * 60 * 24) < 30
      ) {
        return true;
      }
      if (key == "featured" && pack.featured == "true") return true;

      if (pack[key] === undefined || pack[key] != filters[key]) return false;
    }
    return true;
  });

  // Keyword input filter
  const filteredPacks = preFilteredPacks.filter((pack) => {
    if (!value) return true;
    if (
      pack.name.toLowerCase().includes(value.toLowerCase()) ||
      pack.description.toLowerCase().includes(value.toLowerCase())
    ) {
      return true;
    }
  });

  const totalFilteredPacks = filteredPacks.length;

  // Generate author options
  function generateAuthors() {
    const dictionary = {};
    const uniqueAuthors = new Set(
      filteredPacks.map((pack) => {
        dictionary[pack.author] = {
          name: pack.author,
          count: dictionary[pack.author]
            ? dictionary[pack.author]["count"] + 1
            : 1,
        };
        return pack.author;
      })
    );
    let authors = [];
    uniqueAuthors.forEach((author) => {
      authors.push({
        label: dictionary[author]
          ? `${author} (${dictionary[author]["count"]})`
          : author,
        value: author,
      });
    });
    return authors;
  }

  // Generate use case options
  function generateUseCases() {
    const dictionary = {};
    let useCases = [];
    let combinedUseCases = [];
    filteredPacks.map((pack) => {
      combinedUseCases.push(pack.useCases);
    });
    const flattenedUseCases = () => {
      var flat = [];
      for (var i = 0; i < combinedUseCases.length; i++) {
        flat = flat.concat(combinedUseCases[i]);
      }
      return flat;
    };
    const allUseCases = flattenedUseCases();
    allUseCases.map((useCase) => {
      dictionary[useCase] = {
        name: useCase,
        count: dictionary[useCase] ? dictionary[useCase]["count"] + 1 : 1,
      };
    });
    const uniqueUseCases = new Set(allUseCases);
    uniqueUseCases.forEach((useCase) => {
      useCases.push({
        label: dictionary[useCase]
          ? `${useCase} (${dictionary[useCase]["count"]})`
          : useCase,
        value: useCase,
      });
    });
    return useCases;
  }

  // Generate integrations
  function generateIntegrations() {
    const dictionary = {};
    let integrations = [];
    let allIntegrations = [];
    filteredPacks.map((pack) => {
      pack.integrations.map((i) => {
        allIntegrations.push(i.name);
      });
    });
    allIntegrations.map((i) => {
      dictionary[i] = {
        name: i,
        count: dictionary[i] ? dictionary[i]["count"] + 1 : 1,
      };
    });
    const uniqueIntegrations = new Set(allIntegrations);
    uniqueIntegrations.forEach((i) => {
      integrations.push({
        label: dictionary[i] ? `${i} (${dictionary[i]["count"]})` : i,
        value: i,
      });
    });
    return integrations;
  }

  // Generate category options
  function generateCategories() {
    const dictionary = {};
    let categories = [];
    let combinedCategories = [];
    filteredPacks.map((pack) => {
      combinedCategories.push(pack.categories);
    });
    const flattenedCategories = () => {
      var flat = [];
      for (var i = 0; i < combinedCategories.length; i++) {
        flat = flat.concat(combinedCategories[i]);
      }
      return flat;
    };
    const allCategories = flattenedCategories();
    allCategories.map((category) => {
      dictionary[category] = {
        name: category,
        count: dictionary[category] ? dictionary[category]["count"] + 1 : 1,
      };
    });
    const uniqueCategories = new Set(allCategories);
    uniqueCategories.forEach((category) => {
      categories.push({
        label: dictionary[category]
          ? `${category} (${dictionary[category]["count"]})`
          : category,
        value: category,
      });
    });
    return categories;
  }

  // Generate price options
  function generatePrices() {
    const dictionary = {};
    var prices = [];
    const costs = filteredPacks.map((pack) => {
      if (pack.price === undefined) {
        return false;
      }
      if (pack.price === 0) {
        dictionary["free"] = {
          name: "free",
          count: dictionary["free"] ? dictionary["free"]["count"] + 1 : 1,
        };
        return "Free";
      }
      if (pack.price > 0) {
        dictionary["premium"] = {
          name: "premium",
          count: dictionary["premium"] ? dictionary["premium"]["count"] + 1 : 1,
        };
        return "Premium";
      }
    });
    const uniqueCosts = new Set(costs);
    uniqueCosts.forEach((cost) => {
      prices.push({
        label: dictionary[cost.toLowerCase()]
          ? `${cost} (${dictionary[cost.toLowerCase()]["count"]})`
          : cost,
        value: cost.toLowerCase(),
      });
    });
    return prices;
  }

  // Generate support options
  function generateSupports() {
    const dictionary = {};
    var supports = [];
    const allSupports = filteredPacks.map((pack) => {
      if (pack.support === undefined) return false;
      dictionary[pack.support] = {
        name: pack.support,
        count: dictionary[pack.support]
          ? dictionary[pack.support]["count"] + 1
          : 1,
      };
      return pack.support;
    });
    const uniqueSupports = new Set(allSupports);
    uniqueSupports.forEach((support) => {
      if (support === "xsoar") {
        supports.push({
          label: dictionary[support]
            ? `Cortex ${support.toUpperCase()} (${
                dictionary[support]["count"]
              })`
            : `Cortex ${support.toUpperCase()}`,
          value: support,
        });
      } else {
        supports.push({
          label: dictionary[support]
            ? `${capitalizeFirstLetter(support)} (${
                dictionary[support]["count"]
              })`
            : `${capitalizeFirstLetter(support)}`,
          value: support,
        });
      }
    });
    return supports;
  }

  return (
    <Layout
      title={TITLE}
      description={DESCRIPTION}
      wrapperClassName="main-docs-wrapper"
    >
      <div
        className={clsx(styles.docSidebarContainer, {
          [styles.docSidebarContainerHidden]: hiddenSidebarContainer,
        })}
        onTransitionEnd={(e) => {
          if (!e.currentTarget.classList.contains(styles.docSidebarContainer)) {
            return;
          }

          if (hiddenSidebarContainer) {
            setHiddenSidebar(true);
          }
        }}
        role="complementary"
      >
        <MarketplaceSidebar
          sidebar={[
            {
              type: "checkbox",
              label: "New",
              action: setShowNew,
              state: showNew,
            },
            // {
            //   type: "checkbox",
            //   label: "Featured",
            //   action: setShowFeatured,
            //   state: showFeatured,
            // },
            {
              type: "select",
              label: "Published By",
              action: setSupport,
              options: generateSupports(),
              state: support,
            },
            {
              type: "select",
              label: "Price",
              action: setPrice,
              options: generatePrices(),
              state: price,
            },
            {
              type: "select",
              label: "Vendor",
              action: setAuthor,
              options: generateAuthors(),
              state: author,
            },
            {
              type: "select",
              label: "Use Cases",
              action: setUseCase,
              options: generateUseCases(),
              state: useCase,
            },
            {
              type: "select",
              label: "Integrations",
              action: setIntegration,
              options: generateIntegrations(),
              state: integration,
            },
            {
              type: "select",
              label: "Categories",
              action: setCategory,
              options: generateCategories(),
              state: category,
            },
          ]}
          path="/marketplace/"
          sidebarCollapsible={
            siteConfig.themeConfig?.sidebarCollapsible ?? true
          }
          onCollapse={toggleSidebar}
          isHidden={hiddenSidebar}
          search={setValue}
          totalPacks={marketplace.length}
          totalFilteredPacks={totalFilteredPacks}
        />

        {hiddenSidebar && (
          <div
            className={styles.collapsedDocSidebar}
            title={translate({
              id: "theme.docs.sidebar.expandButtonTitle",
              message: "Expand sidebar",
              description:
                "The ARIA label and title attribute for expand button of doc sidebar",
            })}
            aria-label={translate({
              id: "theme.docs.sidebar.expandButtonAriaLabel",
              message: "Expand sidebar",
              description:
                "The ARIA label and title attribute for expand button of doc sidebar",
            })}
            tabIndex={0}
            role="button"
            onKeyDown={toggleSidebar}
            onClick={toggleSidebar}
          >
            <IconArrow className={styles.expandSidebarButtonIcon} />
          </div>
        )}
      </div>

      <main
        className={clsx(styles.docMainContainer, {
          [styles.docMainContainerEnhanced]: hiddenSidebarContainer,
        })}
      >
        <div
          className={clsx("container padding-vert--lg", styles.docItemWrapper, {
            [styles.docItemWrapperEnhanced]: hiddenSidebarContainer,
          })}
        >
          <div className="row">
            {filteredPacks.map((pack) => (
              <div
                key={pack.id}
                className={
                  isBreakpoint
                    ? "col col--6 margin-bottom--lg"
                    : "col col--3 margin-bottom--lg"
                }
              >
                <Button
                  className={clsx(styles.article)}
                  variant="plain"
                  href={`/marketplace/details/${pack.id
                    .replace(/-|\s/g, "")
                    .replace(".", "")}`}
                  target="_self"
                  uppercase={false}
                  newTab={false}
                >
                  <div className={clsx("card shadow--md", styles.contentPack)}>
                    {pack.certification == "certified" ? (
                      <>
                        <div className="certifiedBadge"></div>
                        <i className="certified" title="Certified"></i>
                      </>
                    ) : (
                      <>
                        <div className="demistoBadge"></div>
                        <i className="demisto" title="By Cortex XSOAR"></i>
                      </>
                    )}
                    <div className="card__body">
                      <div className="avatar">
                        <div className="avatar__intro margin-left--none">
                          <h4
                            className={clsx(
                              "avatar__name",
                              "text text--primary",
                              styles.packName,
                              styles.ellipsis
                            )}
                            title={pack.name}
                          >
                            {pack.name}
                          </h4>
                          <small
                            className={clsx(
                              "avatar__subtitle",
                              styles.packHeader,
                              styles.ellipsis
                            )}
                          >
                            {new Date(pack.updated).toLocaleString("en-US", {
                              year: "numeric",
                              month: "long",
                              day: "numeric",
                            })}
                            <span className={clsx(styles.packAuthor)}>
                              By: {pack.author}
                            </span>
                          </small>
                          <small
                            className={clsx(
                              "avatar__subtitle",
                              styles.packDescription
                            )}
                          >
                            {pack.description}
                          </small>
                        </div>
                      </div>
                    </div>
                    <div className="card__footer">
                      <div className={clsx("row", styles.integrations)}>
                        {pack.integrations.length > 3
                          ? pack.integrations.slice(0, 3).map((integration) => {
                              return (
                                <div
                                  className={styles.integrationImageContainer}
                                  key={integration.name}
                                >
                                  <img
                                    className={clsx(styles.integrationImage)}
                                    src={`https://storage.googleapis.com/marketplace-dist/${integration.imagePath}`}
                                    alt={integration.name}
                                    title={integration.name}
                                  />
                                </div>
                              );
                            })
                          : pack.integrations.map((integration) => {
                              return (
                                <div
                                  className={styles.integrationImageContainer}
                                  key={integration.name}
                                >
                                  <img
                                    className={styles.integrationImage}
                                    src={`https://storage.googleapis.com/marketplace-dist/${integration.imagePath}`}
                                    alt={integration.name}
                                    title={integration.name}
                                  />
                                </div>
                              );
                            })}
                      </div>
                      <div className={clsx("row", styles.footer)}>
                        <span className={clsx(styles.downloads)}>
                          {pack.downloads < 100 && "<100 installs"}
                          {pack.downloads > 100 &&
                            pack.downloads < 1000 &&
                            `${pack.downloads} installs`}
                          {pack.downloads > 1000 && "1K+ installs"}
                          {pack.price == 0 ? (
                            <span className={clsx(styles.free)}>FREE</span>
                          ) : (
                            <span className={clsx(styles.cost)}>
                              {pack.price}
                            </span>
                          )}
                        </span>
                      </div>
                    </div>
                  </div>
                </Button>
              </div>
            ))}
          </div>
        </div>
      </main>
    </Layout>
  );
}

export default Marketplace;
