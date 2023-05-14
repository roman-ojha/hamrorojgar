import React from "react";
import styles from "@/styles/components/jobcard.module.scss";
import { Icon } from "@iconify/react";

const JobCard = (): React.JSX.Element => {
  return (
    <>
      <div className={styles.card}>
        <h1>Front-End Developer Plano/Remote</h1>
        <h2>Kathmandu Mahanagar office</h2>
        <div className={styles.card__salary}>
          <Icon className={styles.card__salary__icon} icon="mdi:dollar" />
          <p>Estimated 40.5k - 70.5k per month</p>
        </div>
        <div className={styles.card__time}>
          <Icon
            className={styles.card__time__icon}
            icon="ic:outline-access-time"
          />
          <p>Full-Time</p>
        </div>
        <div className={styles.card__description}>
          <ul>
            <li>
              Production experience with JavaScript based single page
              application and frameworks (Vue)
            </li>
            <li>
              Ability to match design direction with markup and styling
              languages (HTML, CSS, SCSS)
            </li>
          </ul>
        </div>
      </div>
    </>
  );
};

export default JobCard;
