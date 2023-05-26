import React, { useEffect } from "react";
import { Icon } from "@iconify/react";
import styles from "@/styles/components/jobdesc.module.scss";
import { useAppState } from "@/hooks/useAppState";
import {
  jobSelector,
  JobState,
  citizenSelector,
  CitizenState,
} from "@/store/selector";
import { useRouter } from "next/router";

const JobDesc = (): React.JSX.Element => {
  const router = useRouter();
  const [{}, [job, citizen]] = useAppState<[JobState, CitizenState]>([
    jobSelector,
    citizenSelector,
  ]);

  const apply = () => {
    if (citizen && citizen.is_authenticated) {
      router.push(`/apply/?vacancy_id=${job.id}`);
    } else {
      router.push("/signin");
    }
  };

  return (
    <>
      {job == null ? (
        ""
      ) : (
        <div className={styles.card}>
          <div className={styles.card__title_and_button}>
            <h1>{job.title}</h1>
            <button
              onClick={apply}
              className={styles.card__title_and_button__apply_button}
            >
              Apply
            </button>
          </div>
          <h2>Kathmandu Mahanagar office</h2>
          <div className={styles.card__salary}>
            <Icon className={styles.card__salary__icon} icon="mdi:dollar" />
            <p>
              Estimated {job.salary_from}k - {job.salary_to}k per month
            </p>
          </div>
          <div className={styles.card__time}>
            <Icon
              className={styles.card__time__icon}
              icon="ic:outline-access-time"
            />
            <p>{job.job_type}</p>
          </div>
          <div className={styles.card__separator}></div>
          <div className={styles.card__description}>
            <h2>Job Description: </h2>
            <p className={styles.card__description__job_desc}>
              {job.description}
            </p>
            <div className={styles.card__description__requirements}>
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

export default JobDesc;
