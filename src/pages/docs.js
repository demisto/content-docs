/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import Link from "@docusaurus/Link";
import useBaseUrl from "@docusaurus/useBaseUrl";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import classnames from "classnames";
import React, { useRef } from "react";
import ScrollUpButton from "react-scroll-up-button";
import styles from "./styles.module.css";

function Docs() {
  const context = useDocusaurusContext();
  const { siteConfig = {} } = context;
  const scrollToRef = ref => ref.current.scrollIntoView({ behavior: "smooth" });
  const vertificalsRef = useRef(null);
  const toolsRef = useRef(null);
  const scrollToVerticals = () => scrollToRef(vertificalsRef);
  const scrollToTools = () => scrollToRef(toolsRef);
  return (
    <Layout
      title={`${siteConfig.themeConfig.navbar.title}`}
      description="All things related to automation and development with Demisto"
    >
      <main>
        <section className={styles.features} ref={vertificalsRef}>
          <div className="container">
            <h1>Demisto documentation</h1>
            <h4>
              Demisto's security orchestration and automation enables
              standardized, automated, and coordinated response across your
              security product stack. Playbooks powered by thousands of security
              actions make scalable, accelerated incident response a reality.
              Learn the ins and out of Demisto's development platform so you
              can begin create content and integrations.
            </h4>
            <div className="row">
              <div className="col col--6">
                <div class="card shadow--md">
                  <div class="card__header">
                    <h2>Learn the Concepts</h2>
                    <description>
                      Learn the core fundamentals to get started developing with
                      Demisto
                    </description>
                  </div>
                  <div class="card__body">
                    <Link
                      href={useBaseUrl("docs/concepts/getting-started-guide")}
                    >
                      Getting Started Guide
                    </Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/concepts/dev-setups")}>
                      Architecture
                    </Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/concepts/use-cases")}>
                      Use Cases
                    </Link>
                    <br></br>
                    <Link
                      href={useBaseUrl("docs/concepts/design-best-practices")}
                    >
                      Design
                    </Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/concepts/dev-setup")}>
                      Dev Environment & SDK
                    </Link>
                    <br></br>
                    <Link
                      href={useBaseUrl("docs/concepts/design-best-practicess")}
                    >
                      Best Practices
                    </Link>
                    <br></br>
                  </div>
                  <div class="card__footer">
                    <Link
                      className={classnames(
                        "button button--primary",
                        styles.docs
                      )}
                      href={useBaseUrl("docs/concepts")}
                    >
                      Concepts
                    </Link>
                  </div>
                </div>
              </div>
              <div className="col col--6">
                <div class="card shadow--md">
                  <div class="card__header">
                    <h2>How-Tos</h2>
                    <description>Dive into details</description>
                  </div>
                  <div class="card__body">
                    <Link href={useBaseUrl("docs/howtos/code-conventions")}>
                      Integrations
                    </Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/howtos/")}>Playbooks</Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/howtos/")}>Scripts</Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/howtos")}>
                      Incidents, Fields and Layouts
                    </Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/howtos")}>
                      Dashboards and Widgets
                    </Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/howtos")}>
                      Contribution Process
                    </Link>
                    <br></br>
                  </div>
                  <div class="card__footer">
                    <Link
                      className={classnames(
                        "button button--primary",
                        styles.docs
                      )}
                      href={useBaseUrl("docs/howtos")}
                    >
                      How-To
                    </Link>
                  </div>
                </div>
              </div>
            </div>
            <div className="row">
              <div className="col col--6">
                <div class="card shadow--md">
                  <div class="card__header">
                    <h2>Tutorials</h2>
                    <description>
                      Step-by-step detailed instructions
                    </description>
                  </div>
                  <div class="card__body">
                    <Link href={useBaseUrl("docs/tutorials/code-conventions")}>
                      Getting Started
                    </Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/tutorials/")}>Design</Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/tutorials/")}>
                      Integrations
                    </Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/tutorials/")}>Use Cases</Link>
                  </div>
                  <div class="card__footer">
                    <Link
                      className={classnames(
                        "button button--primary",
                        styles.docs
                      )}
                      href={useBaseUrl("docs/tutorials")}
                    >
                      Tutorials
                    </Link>
                  </div>
                </div>
              </div>
              <div className="col col--6">
                <div class="card shadow--md">
                  <div class="card__header">
                    <h2>Reference</h2>
                    <description>Reference Guides</description>
                  </div>
                  <div class="card__body">
                    <Link href={useBaseUrl("docs/reference")}>
                      Integrations
                    </Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/reference")}>Playbooks</Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/reference")}>Scripts</Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/reference")}>Rest API</Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/reference")}>
                      Helper Functions
                    </Link>
                    <br></br>
                    <Link href={useBaseUrl("docs/reference")}>Demisto SDK</Link>
                  </div>
                  <div class="card__footer">
                    <Link
                      className={classnames(
                        "button button--primary",
                        styles.docs
                      )}
                      href={useBaseUrl("docs/reference")}
                    >
                      Reference
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}

export default Docs;
