import React, { useEffect, useState } from "react";
import styles from "@/styles/pages/apply.module.scss";
import { Icon } from "@iconify/react";
import { useRouter } from "next/router";
import { api } from "@/services/api";
import { JobState } from "@/store/selector";

const ApplyPageJobDesc = (): React.JSX.Element => {
  const router = useRouter();
  const vacancy_id = router.query.vacancy_id;
  const [job, setJob] = useState<null | JobState>(null);
  const fetchJobDesc = async (vacancy_id: string) => {
    if (vacancy_id != undefined) {
      const res = await api.jobs.get(parseInt(vacancy_id));
      setJob(res?.data);
    }
  };
  useEffect(() => {
    fetchJobDesc(vacancy_id as string);
  }, [vacancy_id]);
  return (
    <>
      {!job ? (
        ""
      ) : (
        <div className={styles.apply__main_content__card}>
          <h1>{job.title}</h1>
          <h2>Kathmandu Mahanagar office</h2>
          <div className={styles.apply__main_content__card__salary}>
            <Icon
              className={styles.apply__main_content__card__salary__icon}
              icon="mdi:dollar"
            />
            <p>
              Estimated {job.salary_from}k - {job.salary_to}k per month
            </p>
          </div>
          <div className={styles.apply__main_content__card__time}>
            <Icon
              className={styles.apply__main_content__card__time__icon}
              icon="ic:outline-access-time"
            />
            <p>{job.job_type}</p>
          </div>
          <div className={styles.apply__main_content__card__separator}></div>
          <div className={styles.apply__main_content__card__description}>
            <h2>Job Description: </h2>
            <p
              className={
                styles.apply__main_content__card__description__job_desc
              }
            >
              {job.description}
            </p>
            <div
              className={
                styles.apply__main_content__card__description__requirements
              }
            >
              <h2>Qualification: </h2>
              <ul>
                {job.qualifications.map((qualification) => (
                  <li key={qualification.id}>{qualification.description}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default ApplyPageJobDesc;
