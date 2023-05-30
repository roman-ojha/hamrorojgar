import React from "react";
import styles from "@/styles/components/jobcard.module.scss";
import { Icon } from "@iconify/react";
import { useAppState } from "@/hooks/useAppState";
import { jobSelector, JobState } from "@/store/selector";
import { JobTypeChoices } from "@/models/vacancy";

interface JobCardProps {
  id: JobState["id"];
  title: JobState["title"];
  salary_from: JobState["salary_from"];
  salary_to: JobState["salary_to"];
  job_type: JobState["job_type"];
  qualifications: JobState["qualifications"];
}

const JobCard: React.FC<JobCardProps> = ({
  id,
  title,
  salary_from,
  salary_to,
  job_type,
  qualifications,
}): React.JSX.Element => {
  const [{ fetchJob }, [job]] = useAppState<[JobState]>([jobSelector]);
  return (
    <div
      className={styles.card}
      onClick={() => {
        fetchJob(id);
      }}
      data-component="job-card"
      style={
        job != null && id == job.id
          ? {
              borderColor: "rgba(244, 19, 219, 0.4)",
            }
          : {}
      }
    >
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
        <p>{new JobTypeChoices(job_type).get}</p>
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
