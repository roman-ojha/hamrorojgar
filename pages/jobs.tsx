import React from "react";
import Head from "next/head";
import Image from "next/image";
import NavBar from "@/components/NavBar";
import styles from "@/styles/pages/jobs.module.scss";

const Jobs = (): React.JSX.Element => {
  return (
    <>
      <Head>
        <title>Search new jobs</title>
      </Head>
      <div className={styles.jobs}>
        <NavBar />
        <div className={styles.jobs__background}>
          <div className={styles.jobs__background__image}></div>
        </div>
      </div>
    </>
  );
};

export default Jobs;
