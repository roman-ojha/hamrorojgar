import React from "react";
import Head from "next/head";
import NavBar from "@/components/NavBar";
import styles from "@/styles/pages/jobs.module.scss";
import JobDesc from "@/components/Jobs/JobDesc";
import GetJobCards from "@/components/Jobs/GetJobCards";
import Background from "@/components/Background";
import SearchJobs from "@/components/Jobs/SearchJobs";

const Jobs = (): React.JSX.Element => {
  return (
    <>
      <Head>
        <title>Search new jobs</title>
      </Head>
      <div className={styles.jobs}>
        <Background />
        <NavBar />
        <SearchJobs />
        <main id="jobs-page-main-section" className={styles.jobs__main}>
          <section className={styles.jobs__main__job_card_column}>
            <GetJobCards />
          </section>
          <section
            id="job-page-card-desc-section"
            className={styles.jobs__main__job_desc_column}
          >
            <JobDesc />
          </section>
        </main>
      </div>
    </>
  );
};

export default Jobs;
