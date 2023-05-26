import { useRouter } from "next/router";
import React, { useEffect, useRef } from "react";
import Error from "next/dist/pages/_error";
import NavBar from "@/components/NavBar";
import Background from "@/components/Background";
import styles from "@/styles/pages/apply.module.scss";

const Apply = (): React.JSX.Element => {
  const router = useRouter();
  const vacancy_id = router.query.vacancy_id;
  const navBarElementRef: React.MutableRefObject<HTMLElement | null> =
    useRef(null);
  useEffect(() => {
    // logic to dynamically change height of main content with respect with navbar
    function changeMainContentHeight(navbarHeight: number) {
      console.log(document.getElementById("apply-main-content"));
      const mainContentHeight = window.innerHeight - navbarHeight;
      document
        .getElementById("apply-main-content")
        ?.setAttribute("style", `min-height: ${mainContentHeight}px`);
    }
    // const navBarElement = document.getElementById("navbar");
    const navBarElement = navBarElementRef.current;
    if (navBarElement) {
      changeMainContentHeight(navBarElement?.getBoundingClientRect().height);
    }
    window.onresize = function () {
      if (navBarElement) {
        changeMainContentHeight(navBarElement?.getBoundingClientRect().height);
      }
    };
  }, []);
  return (
    <>
      {/* {!vacancy_id ? (
        <Error
          statusCode={404}
          title="Please first apply for the job from '/job' page"
          withDarkMode={true}
        />
      ) : ( */}
      <>
        <div className={styles.apply}>
          <Background />
          <span ref={navBarElementRef}>
            <NavBar />
          </span>
          <main
            id="apply-main-content"
            className={styles.apply__main_content}
          ></main>
        </div>
      </>
      {/* )} */}
    </>
  );
};

export default Apply;
