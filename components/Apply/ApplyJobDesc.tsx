import React from "react";
import styles from "@/styles/pages/apply.module.scss";
import { Icon } from "@iconify/react";
import { useRouter } from "next/router";

const ApplyPageJobDesc = (): React.JSX.Element => {
  const router = useRouter();
  const vacancy_id = router.query.vacancy_id;
  return (
    <>
      <div className={styles.apply__main_content__job_desc_section__card}>
        <div
          className={
            styles.apply__main_content__job_desc_section__card__title_and_button
          }
        >
          {/* <h1>{job.title}</h1> */}
          <button
            // onClick={apply}
            className={
              styles.apply__main_content__job_desc_section__card__title_and_button__apply_button
            }
          >
            Apply
          </button>
        </div>
        <h2>Kathmandu Mahanagar office</h2>
        <div
          className={styles.apply__main_content__job_desc_section__card__salary}
        >
          <Icon
            className={
              styles.apply__main_content__job_desc_section__card__salary__icon
            }
            icon="mdi:dollar"
          />
          <p>
            {/* Estimated {job.salary_from}k - {job.salary_to}k per month */}
          </p>
        </div>
        <div
          className={styles.apply__main_content__job_desc_section__card__time}
        >
          <Icon
            className={
              styles.apply__main_content__job_desc_section__card__time__icon
            }
            icon="ic:outline-access-time"
          />
          {/* <p>{job.job_type}</p> */}
        </div>
        <div
          className={
            styles.apply__main_content__job_desc_section__card__separator
          }
        ></div>
        <div
          className={
            styles.apply__main_content__job_desc_section__card__description
          }
        >
          <h2>Job Description: </h2>
          <p
            className={
              styles.apply__main_content__job_desc_section__card__description__job_desc
            }
          >
            {/* {job.description} */}
          </p>
          <div
            className={
              styles.apply__main_content__job_desc_section__card__description__requirements
            }
          >
            <h2>Qualification: </h2>
            <ul>
              {/* {job.qualifications.map((qualification) => (
                  <li key={qualification.id}>{qualification.description}</li>
                ))} */}
            </ul>
          </div>
        </div>
      </div>
    </>
  );
};

export default ApplyPageJobDesc;
