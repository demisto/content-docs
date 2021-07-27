import React from 'react'
import Contributors from '../marketplace/top-contributors.md'
import Layout from '@theme/Layout';
import styles from "./styles.module.css";


function topContrib() {
  return (
    <Layout title="Contributors">
        <h1 className={styles.h1Contrib}>Top Contributors</h1>
        <table className={styles.tableContrib}>
          <Contributors />
        </table>
    </Layout>
  );
}

export default topContrib;
