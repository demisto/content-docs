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

const features = [
  {
    title: <>What is Cortex XSOAR?</>,
    imageUrl: "img/undraw_pair_programming_njlp.svg",
    description: (
      <>
        Cortex XSOAR is the most comprehensive SOAR platform in the market today,
        orchestrating across hundreds of security products to help your SOC
        customers standardize and automate their processes for faster response
        times and increased team productivity. Read More or watch some videos
      </>
    ),
    button: (
      <div className={styles.buttons}>
        <Link
          className={classnames(
            "button button--outline button--primary button--md",
            styles.getStarted
          )}
          href="https://www.demisto.com/security-orchestration/"
        >
          Learn More
        </Link>
        <Link
          className={classnames(
            "button button--outline button--primary button--md",
            styles.getStarted
          )}
          href="https://www.youtube.com/channel/UCPZSycGbjGoIcTF6kudEilw"
        >
          Watch Videos
        </Link>
      </div>
    )
  },
  {
    title: <>Why Become a Partner?</>,
    imageUrl: "img/undraw_mind_map_cwng.svg",
    description: (
      <>
        Join our 300+ integrations network to increase your reach into some of
        the largest SOCs in the world. Access over 60,000 customers in 150+
        locations across multiple industries. See Why
      </>
    ),
    button: (
      <div className={styles.buttons}>
        <Link
          className={classnames(
            "button button--outline button--primary button--md",
            styles.getStarted
          )}
          href="/docs/why-demisto"
        >
          Learn More
        </Link>
      </div>
    )
  },
  {
    title: <>Cortex XSOAR Use Cases</>,
    imageUrl: "img/undraw_google_analytics_a57d.svg",
    description: (
      <>
        Learn about use cases relevant to your customers and create new
        scenarios that better integrate your product or services into the SOC
        incident response lifecycle. Read More
      </>
    ),
    button: (
      <div className={styles.buttons}>
        <Link
          className={classnames(
            "button button--outline button--primary button--md",
            styles.getStarted
          )}
          to="docs/use-cases"
        >
          Learn More
        </Link>
      </div>
    )
  }
];

function Feature({ imageUrl, title, description, button }) {
  const imgUrl = useBaseUrl(imageUrl);
  return (
    <div className={classnames("col col--4", styles.features)}>
      {imgUrl && (
        <div className="text--center">
          <img className={styles.featureImage} src={imgUrl} alt={title} />
        </div>
      )}
      <h3>{title}</h3>
      <p>{description}</p>
      {button}
    </div>
  );
}

function Home() {
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
      description="All things related to automation and development with Cortex XSOAR (formerly Demisto)"
    >
      <ScrollUpButton />

      <header
        className={classnames(
          "hero hero--primary heroTilted",
          styles.heroBanner
        )}
      >
        <div className="container">
          <div className={styles.hero}>
            <div className={styles.heroInner}>
              <h1 className={styles.heroProjectTagline}>
                <img
                  alt="Cortex XSOAR"
                  className={styles.heroLogo}
                  src={useBaseUrl("img/Cortex-XSOAR-black.svg")}
                />
                Automate the{" "}
                <span className={styles.heroProjectKeywords}>future</span> with{" "}
                <span className={styles.heroProjectKeywords}>Cortex XSOAR</span>{" "}
              </h1>
              <h3 className={styles.heroProjectDescription}>
                Develop new integrations, automations, playbooks, reports and
                more...
              </h3>
              <div className={styles.indexCtas}>
                <Link
                  className={classnames(
                    "button button--info button--secondary button--lg",
                    styles.headerButtons
                  )}
                  to="docs/partners/why-xsoar"
                >
                  Why Cortex XSOAR?
                </Link>
                <Link
                  className={classnames(
                    "button button--info button--secondary button--lg",
                    styles.headerButtons
                  )}
                  href="https://start.paloaltonetworks.com/become-a-technology-partner"
                >
                  Become a Partner
                </Link>
              </div>
            </div>
          </div>
        </div>
      </header>

      <main>
        {features && features.length && (
          <section className={styles.features} ref={vertificalsRef}>
            <div className="container">
              <div className="row">
                {features.map((props, idx) => (
                  <Feature key={idx} {...props} />
                ))}
              </div>
            </div>
          </section>
        )}
        <section className={styles.hero}>
          <div className="customer">
            <div className="customer-inner">
              Are you a Cortex XSOAR Customer or an Independent Developer?
              <Link to="docs/integrations/getting-started-guide"> Get Started Now!</Link>
              <br /> 
              Join <b>#demisto-integrations-help</b> on our <a href="https://start.paloaltonetworks.com/join-our-slack-community">Slack community</a> today.
            </div>
          </div>
        </section>     
        <section className={styles.tools}>
          <div className="container">
            <div className="row">
              <div className="col col--6">
                <img
                  alt="Cortex XSOAR"
                  src={useBaseUrl("img/undraw_creative_team_r90h.svg")}
                />
              </div>
              <div className="col col--6">
                <h1>Our Approach to Security Orchestration</h1>
                <h3>
                  Effective security orchestration is about making different
                  products integrate with each other and automating tasks across
                  products through workflows, while also allowing for human
                  oversight and interaction. To achieve that goal, we integrate
                  with security and non-security technologies, based on what our
                  SOC customers need to streamline and automate their incident
                  response end-to-end.
                </h3>
              </div>
            </div>
          </div>
        </section>
        <section className={styles.features}>
          <div className="integrations">
            <div className="integrations-inner">
              Check out our {" "}
              <a href="https://www.demisto.com/integrations/">
                existing integrations here!
              </a>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}

export default Home;
