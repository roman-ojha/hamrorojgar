import React from "react";
import styles from "@/styles/pages/verify.module.scss";
import emailIcon from "@/assets/images/email.jpg";
import Image from "next/image";

const Verify = (): React.JSX.Element => {
  return (
    <>
      <div className={styles.verify}>
        <section className={styles.verify__notice_container}>
          <h1>Hamro rojgar</h1>
          <Image
            src={emailIcon}
            alt="email-icon"
            className={styles.verify__notice_container__email_icon}
          />
          <h2>Thank you for you registration</h2>
          <p>
            Please verify you email address for you account by checking your
            same email address that you use for this platform to register, where
            we have give you a way to verify you account.
          </p>
        </section>
      </div>
    </>
  );
};

export default Verify;
