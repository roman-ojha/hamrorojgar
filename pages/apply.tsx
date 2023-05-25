import { useRouter } from "next/router";
import React from "react";
import Error from "next/dist/pages/_error";
import NavBar from "@/components/NavBar";

const Apply = (): React.JSX.Element => {
  const router = useRouter();
  const vacancy_id = router.query.vacancy_id;
  return (
    <>
      {!vacancy_id ? (
        <Error
          statusCode={404}
          title="Please first apply for the job from '/job' page"
          withDarkMode={true}
        />
      ) : (
        <>
          <NavBar />
        </>
      )}
    </>
  );
};

export default Apply;
