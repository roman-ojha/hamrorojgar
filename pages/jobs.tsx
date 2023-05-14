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
        <div className={styles.jobs__background}>
          <div className={styles.jobs__background__color}></div>
          <div className={styles.jobs__background__image}></div>
        </div>
        <NavBar />
        {/* <div className={styles.jobs__search}>
          <div className={styles.jobs__search__what}>
            <label htmlFor="search_what">What</label>
            <input type="search" name="search_what" id="search_what" />
          </div>
          <div className={styles.jobs__search__where}>
            <label htmlFor="district">What</label>
            <select name="district" id="district">
              <option value="">jhapa</option>
            </select>
            <select name="municipality" id="municipality">
              <option value="">kamal</option>
            </select>
          </div>
          <div className={styles.jobs__search__where}></div>
        </div> */}
      </div>
    </>
  );
};

export default Jobs;
