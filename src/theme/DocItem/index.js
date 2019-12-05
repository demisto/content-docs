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
import DocPaginator from "@theme/DocPaginator";
import useTOCHighlight from "@theme/hooks/useTOCHighlight";
import classnames from "classnames";
import React from "react";
import styles from "./styles.module.css";

const LINK_CLASS_NAME = "contents__link";
const ACTIVE_LINK_CLASS_NAME = "contents__link--active";
const TOP_OFFSET = 100;

function Headings({ headings, isChild }) {
  useTOCHighlight(LINK_CLASS_NAME, ACTIVE_LINK_CLASS_NAME, TOP_OFFSET);

  if (!headings.length) return null;
  return (
    <ul className={isChild ? "" : "contents contents__left-border"}>
      {headings.map(heading => (
        <li key={heading.id}>
          <a href={`#${heading.id}`} className={LINK_CLASS_NAME}>
            {heading.value}
          </a>
          <Headings isChild headings={heading.children} />
        </li>
      ))}
    </ul>
  );
}

function DocItem(props) {
  const { siteConfig = {} } = useDocusaurusContext();
  const { url: siteUrl } = siteConfig;
  const { metadata, content: DocContent } = props;
  const {
    description,
    title,
    permalink,
    image: metaImage,
    editUrl,
    lastUpdatedAt,
    lastUpdatedBy,
    keywords,
    source
  } = metadata;
  const issueTitle = `Issue with "${title}" in ${source}`;
  const issueUrl = `https://github.com/demisto/content-docs/issues/new?labels=documentation&template=developer-documentation-issue.md&title=${issueTitle}`;
  const metaImageUrl = siteUrl + useBaseUrl(metaImage);

  return (
    <div>
      <Head>
        {title && <title>{title}</title>}
        {description && <meta name="description" content={description} />}
        {description && (
          <meta property="og:description" content={description} />
        )}
        {keywords && keywords.length && (
          <meta name="keywords" content={keywords.join(",")} />
        )}
        {metaImage && <meta property="og:image" content={metaImageUrl} />}
        {metaImage && <meta property="twitter:image" content={metaImageUrl} />}
        {metaImage && (
          <meta name="twitter:image:alt" content={`Image for ${title}`} />
        )}
        {permalink && <meta property="og:url" content={siteUrl + permalink} />}
      </Head>
      <div className="padding-vert--lg">
        <div className="container">
          <div className="row">
            <div className="col">
              <div className={styles.docItemContainer}>
                {!metadata.hide_title && (
                  <header>
                    <h1 className={styles.docTitle}>{metadata.title}</h1>
                  </header>
                )}
                <article>
                  <div className="markdown">
                    <DocContent />
                  </div>
                </article>
                {(editUrl || lastUpdatedAt || lastUpdatedBy) && (
                  <div className="margin-vert--xl">
                    <div className="row">
                      <div className="col">
                        {editUrl && (
                          <a
                            href={editUrl}
                            target="_blank"
                            rel="noreferrer noopener"
                          >
                            <svg
                              fill="currentColor"
                              height="1.2em"
                              width="1.2em"
                              preserveAspectRatio="xMidYMid meet"
                              viewBox="0 0 40 40"
                              style={{
                                marginRight: "0.3em",
                                verticalAlign: "sub"
                              }}
                            >
                              <g>
                                <path d="m34.5 11.7l-3 3.1-6.3-6.3 3.1-3q0.5-0.5 1.2-0.5t1.1 0.5l3.9 3.9q0.5 0.4 0.5 1.1t-0.5 1.2z m-29.5 17.1l18.4-18.5 6.3 6.3-18.4 18.4h-6.3v-6.2z" />
                              </g>
                            </svg>
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
                                  <strong>
                                    {new Date(
                                      lastUpdatedAt * 1000
                                    ).toLocaleDateString()}
                                  </strong>
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
                      )}
                    </div>
                  </div>
                )}
                <div className="margin-vert--lg">
                  <DocPaginator metadata={metadata} />
                </div>
              </div>
            </div>
            {DocContent.rightToc && (
              <div className="col col--3">
                <div className={styles.tableOfContents}>
                  <Headings headings={DocContent.rightToc} />
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default DocItem;
