import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import constants from "@/constants/index";

const Home: NextPage = () => {
  return (
    <div className="">
      <Head>
        <title>{constants.appName}</title>
        <meta
          name="description"
          content="Place where you can find and apply for the government jobs online"
        />
        {/* <link rel="icon" href="/favicon.ico" /> */}
      </Head>
    </div>
  );
};

export default Home;
