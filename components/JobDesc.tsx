import React from "react";
import { Icon } from "@iconify/react";
import styles from "@/styles/components/jobdesc.module.scss";
import Link from "next/link";

const JobDesc = (): React.JSX.Element => {
  return (
    <div className={styles.card}>
      <div className={styles.card__title_and_button}>
        <h1>Front-End Developer Plano/Remote</h1>
        <Link className={styles.card__title_and_button__apply_button} href="/">
          Apply
        </Link>
      </div>
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
      <div className={styles.card__separator}></div>
      <div className={styles.card__description}>
        <h2>Job Description: </h2>
        <p className={styles.card__description__job_desc}>
          The position requires a junior software engineer that can learn
          various functional domain areas, such as User Interface (UI)
          development, digital mapping, messaging, and software documentation.
          This is in support of the company major software application and its
          integration with other applications and environments. The position
          reports to the President and/or Lead Software Engineer. The position
          requires the candidate to work using guidance from his supervisor.
        </p>
        <div className={styles.card__description__requirements}>
          <h2>Requirements: </h2>
          <ul>
            <li>
              Production experience with JavaScript based single page
              application and frameworks (Vue)
            </li>
            <li>
              Ability to match design direction with markup and styling
              languages (HTML, CSS, SCSS)
            </li>
            <li>
              In-depth understanding of the entire web development process
              (design, development and deployment)
            </li>
            <li>
              Experience working closely with back-end developers and an
              understanding of how to best manage interfacing with APIs
            </li>
            <li>Solid modern JavaScript experience</li>
            <li>
              Assist the SEO content team in formatting and posting content for
              our clients.
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default JobDesc;
