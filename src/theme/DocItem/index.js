/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
import Head from "@docusaurus/Head";
import Link from "@docusaurus/Link";
import { useTitleFormatter } from "@docusaurus/theme-common/internal";
import useBaseUrl from "@docusaurus/useBaseUrl";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import DocPaginator from "@theme/DocPaginator";
import useDocVersionSuggestions from "@theme/DocVersionBanner";
import {
  useActivePlugin,
  useActiveVersion,
  useVersions,
} from "@docusaurus/plugin-content-docs/client";
import IconEdit from "@theme/Icon/Edit";
import TOC from "@theme/TOC";
import classnames from "classnames";
import clsx from "clsx";
import React from "react";
import styles from "./styles.module.css";

function DocItem(props) {
  const { siteConfig } = useDocusaurusContext();
  const { url: siteUrl } = siteConfig;
  const { content: DocContent } = props;
  const {
    metadata,
    frontMatter: {
      image: metaImage,
      keywords,
      hide_title: hideTitle,
      hide_table_of_contents: hideTableOfContents,
    },
  } = DocContent;
  const {
    description,
    title,
    permalink,
    editUrl,
    lastUpdatedAt,
    lastUpdatedBy,
    source,
  } = metadata;

  const issueTitle = `Issue with "${title}" in ${source}`;
  //IMPORTANT NOTE: if changing the body, note that the defacto max url length is 2000 chars for IE
  const issueBody = `
<!-- 
Thank you for taking the time to help us improve our documentation! Please describe the problem and a suggested fix below and we'll get back to you as soon as we can.
-->

## Describe the problem

* Page: [${title}](${siteConfig.url}${permalink})
* Source: ${editUrl}

<!--- Is this a typo, stale information, request for improvement, inaccuracy? -->
<!--- Clearly and concisely describe the problem with the documentation -->


## Screenshots
<!-- If applicable, add screenshots to help explain your problem. -->

## Environment
 - OS: [e.g. Windows]
 - Browser: [e.g. chrome, safari, firefox..]
 - Browser Version:

## Suggested fix

<!--- If possible, help us by offering a suggested fix to the problem. If you know the fix, you may also submit a PR to fix the issue if you like! -->

`;
  const issueUrl = `https://github.com/demisto/content-docs/issues/new?labels=documentation&body=${encodeURIComponent(
    issueBody
  )}&title=${encodeURIComponent(issueTitle)}`;
  const { pluginId } = useActivePlugin({
    failfast: true,
  });
  const versions = useVersions(pluginId);
  const version = useActiveVersion(pluginId); // If site is not versioned or only one version is included
  // we don't show the version badge
  // See https://github.com/facebook/docusaurus/issues/3362

  const showVersionBadge = versions.length > 1;
  const metaTitle = useTitleFormatter(title);
  const metaImageUrl = useBaseUrl(metaImage, {
    absolute: true,
  });
  return (
    <>
      <Head>
        <title>{metaTitle}</title>
        <meta property="og:title" content={metaTitle} />
        {description && <meta name="description" content={description} />}
        {description && (
          <meta property="og:description" content={description} />
        )}
        {keywords && keywords.length && (
          <meta name="keywords" content={keywords.join(",")} />
        )}
        {metaImage && <meta property="og:image" content={metaImageUrl} />}
        {metaImage && <meta name="twitter:image" content={metaImageUrl} />}
        {metaImage && (
          <meta name="twitter:image:alt" content={`Image for ${title}`} />
        )}
        {permalink && <meta property="og:url" content={siteUrl + permalink} />}
        {permalink && <link rel="canonical" href={siteUrl + permalink} />}
      </Head>

      <div className="row">
        <div
          className={clsx("col", {
            [styles.docItemCol]: !hideTableOfContents,
          })}
        >
          <useDocVersionSuggestions />
          <div className={styles.docItemContainer}>
            <article>
              {showVersionBadge && (
                <div>
                  <span className="badge badge--secondary">
                    Version: {version.label}
                  </span>
                </div>
              )}
              {!hideTitle && (
                <header>
                  <h1 className={styles.docTitle}>{title}</h1>
                </header>
              )}
              <div className="markdown">
                <DocContent />
              </div>
            </article>
            {(editUrl || lastUpdatedAt || lastUpdatedBy || issueUrl) && (
              <div className="margin-vert--xl">
                <div className="row">
                  <div className="col">
                    {editUrl && (
                      <a
                        href={editUrl}
                        target="_blank"
                        rel="noreferrer noopener"
                      >
                        <IconEdit />
                        Edit this page
                      </a>
                    )}
                  </div>
                  {(lastUpdatedAt || lastUpdatedBy) && (
                    <div className="col text--right">
                      <em>
                        <small>
                          Last updated{" "}
                          {lastUpdatedAt && (
                            <>
                              on{" "}
                              <time
                                dateTime={new Date(
                                  lastUpdatedAt * 1000
                                ).toISOString()}
                                className={styles.docLastUpdatedAt}
                              >
                                {new Date(
                                  lastUpdatedAt * 1000
                                ).toLocaleDateString()}
                              </time>
                              {lastUpdatedBy && " "}
                            </>
                          )}
                          {lastUpdatedBy && (
                            <>
                              by <strong>{lastUpdatedBy}</strong>
                            </>
                          )}
                          {process.env.NODE_ENV === "development" && (
                            <div>
                              <small>
                                {" "}
                                (Simulated during dev for better perf)
                              </small>
                            </div>
                          )}
                        </small>
                      </em>
                    </div>
                  )}
                </div>
                <div className="row">
                  <div className="col text--right">
                    <Link
                      className={classnames(
                        "button button--outline button--primary button--md"
                      )}
                      href={issueUrl}
                      target="_blank"
                    >
                      Report an Issue
                    </Link>
                  </div>
                </div>
              </div>
            )}
            <div className="margin-vert--lg">
              <DocPaginator metadata={metadata} />
            </div>
          </div>
        </div>
        {!hideTableOfContents && DocContent.toc && (
          <div className="col col--3">
            <TOC toc={DocContent.toc} />
          </div>
        )}
      </div>
    </>
  );
}

export default DocItem;
