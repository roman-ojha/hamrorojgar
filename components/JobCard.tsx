import React from "react";
import styles from "@/styles/components/jobcard.module.scss";
import { Icon } from "@iconify/react";
import { JobState } from "@/store/selector";

interface JobCardProps {
  title: JobState["title"];
  salary_from: JobState["salary_from"];
  salary_to: JobState["salary_to"];
  job_type: JobState["job_type"];
  qualifications: JobState["qualifications"];
}

const JobCard: React.FC<JobCardProps> = ({
  title,
  salary_from,
  salary_to,
  job_type,
  qualifications,
}): React.JSX.Element => {
  return (
    <div className={styles.card}>
      <h1>{title}</h1>
      <h2>Kathmandu Mahanagar office</h2>
      <div className={styles.card__salary}>
        <Icon className={styles.card__salary__icon} icon="mdi:dollar" />
        <p>
          Estimated {salary_from}k - {salary_to}k per month
        </p>
      </div>
      <div className={styles.card__time}>
        <Icon
          className={styles.card__time__icon}
          icon="ic:outline-access-time"
        />
        <p>{job_type}</p>
      </div>
      <div className={styles.card__description}>
        <ul>
          {qualifications.slice(0, 2).map((qualification) => (
            <li key={qualification.id}>{qualification.description}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default JobCard;
