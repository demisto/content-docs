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
              <div className="col col--12">
                <div class="card shadow--md">
                  <div class="card__header">
                    <h2>Featured Content</h2>
                    <description>
                      These articles will get you up to speed quickly
                    </description>
                  </div>
                  <div class="card__body">
                  <Link href={useBaseUrl("docs/concepts/faq")}>FAQ</Link>
                    <br/>
                    <Link href={useBaseUrl("docs/tutorials/getting-started/tut-setup-dev")}>Getting Started Tutorial</Link>
                    <br/><br/><br/><br/>
                  </div>
                  <div class="card__footer">
                  </div>
                </div>
              </div>
            </div>
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
                    <Link href={useBaseUrl("docs/concepts/use-cases")}>Use Cases</Link>
                    <br/>
                    <Link href={useBaseUrl("docs/concepts/design-best-practices")}>Design</Link>
                    <br/>
                    <Link href={useBaseUrl("docs/concepts/faq")}>FAQ</Link>
                    <br/><br/><br/><br/>
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
                    <description>Dive into details and learn how to do stuff with Demisto</description>
                  </div>
                  <div class="card__body">
                    <Link href={useBaseUrl("docs/howtos#integrations")}>Integrations</Link>
                    <br/>
                    <Link href={useBaseUrl("docs/howtos#playbooks")}>Playbooks</Link>
                    <br/>
                    <Link href={useBaseUrl("docs/howtos#scripts")}>Scripts</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/howtos#incidents-fields--layouts")}>Incidents, Fields  Layouts</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/howtos#dashboards--widgets")}>Dashboards  Widgets</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/howtos#contributing")}>Contributing</Link>
                    <br/>
                  </div>
                  <div class="card__footer">
                    <Link
                      className={classnames(
                        "button button--primary",
                        styles.docs
                      )}
                      href={useBaseUrl("docs/howtos")}
                    >
                      How-Tos
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
                     Detailed instructions to learn step-by-step
                    </description>
                  </div>
                  <div class="card__body">
                    <Link href={useBaseUrl("docs/tutorials#getting-started")}>Getting Started</Link>
                    <br/>
                    <Link href={useBaseUrl("docs/tutorials#integrations")}>Integrations</Link>
                    <br/>
                    <Link href={useBaseUrl("docs/tutorials#playbooks")}>Playbooks</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/tutorials#scripts")}>Scripts</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/tutorials#incidents-fields--layouts")}>Incidents, Fields  Layouts</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/tutorials#dashboards--widgets")}>Dashboards  Widgets</Link> (<i>coming soon</i>)
                    <br/>
                  </div>
                  <div class="card__footer">
                    <Link
                      className={classnames(
                        "button button--primary",
                        styles.docs
                      )}
                      href={useBaseUrl("docs/tutorials")}
                    >Tutorials</Link>
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
                    <Link href={useBaseUrl("docs/reference#integrations")}>Integrations</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/reference#playbooks")}>Playbooks</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/reference#scripts")}>Scripts</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/reference#demisto-rest-api")}>Rest API</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/reference#code")}>Demisto SDK</Link> (<i>coming soon</i>)
                    <br/>
                    <Link href={useBaseUrl("docs/reference#demisto-sdk")}>Helper Functions</Link> (<i>coming soon</i>)
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
