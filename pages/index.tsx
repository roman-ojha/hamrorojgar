import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import constants from "@/constants/index";
import NavBar from "@/components/NavBar";
import styles from "@/styles/pages/index.module.scss";
import interviewImg from "@/assets/svg/interview.svg";

const Home: NextPage = () => {
  return (
    <div className={styles.home}>
      <Head>
        <title>{constants.appName}</title>
        <meta
          name="description"
          content="Place where you can find and apply for the government jobs online"
        />
        {/* <link rel="icon" href="/favicon.ico" /> */}
      </Head>
      <NavBar />
      <div className={styles.home__background}>
        <div className={styles.home__background__image}></div>
        <Image
          className={styles.home__background__interview}
          src={interviewImg}
          alt="interview"
        ></Image>
      </div>
      <main className={styles.main}>
        <div className={styles.main__content}>
          <div>
            <h1 className={styles.main__content__heading}>Online</h1>
            <h1 className={styles.main__content__heading}>Government</h1>
            <h1 className={styles.main__content__heading}>Job Portal</h1>
          </div>
          <div>
            <h3 className={styles.main__content__description}>
              Where you can find, apply for
            </h3>
            <h3 className={styles.main__content__description}>
              the Government Job
            </h3>
          </div>
          <button className={styles.main__content__button}>
            Search new job
          </button>
        </div>
      </main>
    </div>
  );
};

export default Home;
