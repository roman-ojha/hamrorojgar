import React, { useState } from "react";
import styles from "@/styles/pages/signin.module.scss";
import { Icon } from "@iconify/react";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { CitizenSignInFormType } from "@/store/components/citizen/types";

const Main = (): React.JSX.Element => {
  const [isValidated, setIsValidated] = useState({
    emailOrNo: true,
    password: true,
  });
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<CitizenSignInFormType>();

  const signIn = (data: CitizenSignInFormType) => {
    console.log(data);
  };

  return (
    <>
      <main className={styles.signin__main}>
        <div className={styles.signin__main__navigate_home}>
          <Link
            href="/"
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
            <h3 id="home_navigation">Home</h3>
          </Link>
        </div>
        <h2>Sign In</h2>
        <form
          onSubmit={handleSubmit(signIn)}
          className={styles.signin__main__form}
        >
          <div className={styles.signin__main__form__inputs}>
            <div className={styles.signin__main__form__inputs__fields}>
              <input
                type="text"
                placeholder="Enter your email"
                {...register("email")}
              />
              {isValidated.emailOrNo ? (
                ""
              ) : (
                <span data-type="validation-error">
                  <Icon
                    className={styles.validation_icon}
                    icon="ic:round-warning"
                  />
                  <p>Required field</p>
                </span>
              )}
            </div>
            <div className={styles.signin__main__form__inputs__fields}>
              <input
                type="password"
                placeholder="Enter your password"
                id="password"
                {...register("password")}
              />
              {isValidated.password ? (
                ""
              ) : (
                <span data-type="validation-error">
                  <Icon
                    className={styles.validation_icon}
                    icon="ic:round-warning"
                  />
                  <p>Required field</p>
                </span>
              )}
            </div>
          </div>
          <input type="submit" value="Sign In" />
        </form>
      </main>
    </>
  );
};

export default Main;
