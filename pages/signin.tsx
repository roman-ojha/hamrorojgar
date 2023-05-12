import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import React, { useEffect } from "react";
import styles from "@/styles/pages/signin.module.scss";
import welcomeImage from "@/assets/svg/welcome.svg";
import { Icon } from "@iconify/react";
import Link from "next/link";

const SingIn: NextPage = () => {
  useEffect(() => {}, []);
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
        <main className={styles.signin__main}>
          <div className={styles.signin__main__navigate_home}>
            <span
              onMouseEnter={() => {
                const backIconStyle: CSSStyleDeclaration | undefined =
                  document.getElementById("back_icon")?.style;
                const homeNavigationStyle: CSSStyleDeclaration | undefined =
                  document.getElementById("home_navigation")?.style;
                backIconStyle!.color = "black";
                backIconStyle!.width = "25px";
                backIconStyle!.width = "25px";
                homeNavigationStyle!.color = "black";
                homeNavigationStyle!.fontWeight = "500";
              }}
              onMouseLeave={() => {
                const backIconStyle: CSSStyleDeclaration | undefined =
                  document.getElementById("back_icon")?.style;
                const homeNavigationStyle: CSSStyleDeclaration | undefined =
                  document.getElementById("home_navigation")?.style;
                backIconStyle!.color = "white";
                backIconStyle!.width = "30px";
                backIconStyle!.width = "30px";
                homeNavigationStyle!.color = "white";
                homeNavigationStyle!.fontWeight = "bold";
              }}
              className={styles.signin__main__navigate_home__button}
            >
              <Icon
                id="back_icon"
                className={styles.signin__main__navigate_home__button__icon}
                icon="material-symbols:arrow-back-ios-new-rounded"
              />
              <Link id="home_navigation" href="/">
                Home
              </Link>
            </span>
          </div>
          <h1>Sign In</h1>
          <form className={styles.signin__main__form}>
            <input type="text" placeholder="Email or mobile no." />
            <input type="password" placeholder="Password" />
            <input type="submit" value="Sign In" />
          </form>
        </main>
      </div>
    </>
  );
};

export default SingIn;
