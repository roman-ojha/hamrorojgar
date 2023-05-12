import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import React from "react";
import styles from "@/styles/pages/signin.module.scss";
import welcomeImage from "@/assets/svg/welcome.svg";

const SingIn: NextPage = () => {
  return (
    <>
      <Head>
        <title>Sign In</title>
      </Head>
      <div className={styles.signin}>
        <div className={styles.signin__background}>
          <div className={styles.signin__background__image}></div>
          <Image
            className={styles.signin__background__welcome}
            src={welcomeImage}
            alt="welcome"
          ></Image>
        </div>
      </div>
    </>
  );
};

export default SingIn;
