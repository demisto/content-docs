import React from 'react'
import Contributors from '../marketplace/top-contributors.md'
import Layout from '@theme/Layout';
import styles from "./styles.module.css";



function topContrib() {
  return (
    <Layout title="Contributors">
    <main className={styles.contribArticle}>
      <h1 className={styles.h1Contrib}>Top Contributors</h1>
      <table className={styles.tableContrib}><Contributors /></table>
    </main>
    </Layout>
  );
}

export default topContrib;
