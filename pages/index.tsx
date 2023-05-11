import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import constants from "@/constants/index";
import NavBar from "@/components/NavBar";
import backgroundImg from "@/assets/images/background.png";

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
      <Image src={backgroundImg} alt="background-image"></Image>
    </div>
  );
};

export default Home;
