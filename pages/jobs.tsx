import React, { useEffect } from "react";
import Head from "next/head";
import NavBar from "@/components/NavBar";
import styles from "@/styles/pages/jobs.module.scss";
import { Icon } from "@iconify/react";
import JobCard from "@/components/JobCard";
import JobDesc from "@/components/JobDesc";
import { useDispatch, useSelector } from "react-redux";
import { actionCreators } from "@/store";
import { jobSelector } from "@/store/selector";
import { bindActionCreators } from "redux";

const Jobs = (): React.JSX.Element => {
  const jobs = useSelector(jobSelector);
  const { storeVacancy } = bindActionCreators(actionCreators, useDispatch());
  useEffect(() => {
    storeVacancy();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    console.log(jobs[0]);
  }, [jobs]);
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
        <form className={styles.jobs__search}>
          <div className={styles.jobs__search__what}>
            <label htmlFor="search_what">What</label>
            <div className={styles.jobs__search__what__input_field}>
              <input
                type="search"
                name="search_what"
                id="search_what"
                placeholder="Search..."
              />
              <Icon
                className={styles.jobs__search__what__input_field__icon}
                icon="ic:outline-search"
              />
            </div>
          </div>
          <div className={styles.jobs__search__where}>
            <label htmlFor="district">Where</label>
            <select name="district" id="district">
              <option value="">District</option>
              <option value="">jhapa</option>
            </select>
            <select name="municipality" id="municipality">
              <option value="">Municipality</option>
              <option value="">kamal</option>
            </select>
            <Icon
              className={styles.jobs__search__where__icon}
              icon="ic:outline-search"
            />
          </div>
          <div className={styles.jobs__search__where}></div>
        </form>
        <main className={styles.jobs__main}>
          <section className={styles.jobs__main__job_card_column}>
            <JobCard />
            <JobCard />
            <JobCard />
          </section>
          <section className={styles.jobs__main__job_desc_column}>
            <JobDesc />
          </section>
        </main>
      </div>
    </>
  );
};

export default Jobs;
