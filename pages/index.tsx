import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import constants from "@/constants/index";
import NavBar from "@/components/NavBar";

const Home: NextPage = () => {
  return (
    <div>
      <Head>
        <title>{constants.appName}</title>
        <meta
          name="description"
          content="Place where you can find and apply for the government jobs online"
        />
        {/* <link rel="icon" href="/favicon.ico" /> */}
      </Head>
      <NavBar />
    </div>
  );
};

export default Home;
