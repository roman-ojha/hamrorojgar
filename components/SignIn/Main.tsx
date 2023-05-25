import React, { useEffect } from "react";
import styles from "@/styles/pages/signin.module.scss";
import { Icon } from "@iconify/react";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { CitizenSignInFormType } from "@/store/components/citizen/types";
import { useAppState } from "@/hooks/useAppState";
import { useRouter } from "next/router";
import {
  citizenLoginStatusSelector,
  CitizenLoginStatusState,
} from "@/store/components/citizen/selector";

const Main = (): React.JSX.Element => {
  const [{ loginCitizen, resetLoginStatus }, [citizenLoginStatus]] =
    useAppState<[CitizenLoginStatusState]>([citizenLoginStatusSelector]);
  const router = useRouter();

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<CitizenSignInFormType>();

  useEffect(() => {
    resetLoginStatus();
    if (citizenLoginStatus.is_logged_in) router.push("/jobs");
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [citizenLoginStatus]);

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
          onSubmit={handleSubmit(loginCitizen)}
          className={styles.signin__main__form}
        >
          <div className={styles.signin__main__form__inputs}>
            <div className={styles.signin__main__form__inputs__fields}>
              <input
                type="text"
                placeholder="Enter your email"
                {...register("email")}
              />
              {citizenLoginStatus.email &&
              citizenLoginStatus.email?.length > 0 ? (
                <span data-type="validation-error">
                  <Icon
                    className={styles.validation_icon}
                    icon="ic:round-warning"
                  />
                  <p>{citizenLoginStatus.email[0]}</p>
                </span>
              ) : (
                ""
              )}
            </div>
            <div className={styles.signin__main__form__inputs__fields}>
              <input
                type="password"
                placeholder="Enter your password"
                id="password"
                {...register("password")}
              />
              {citizenLoginStatus.password &&
              citizenLoginStatus.password.length > 0 ? (
                <span data-type="validation-error">
                  <Icon
                    className={styles.validation_icon}
                    icon="ic:round-warning"
                  />
                  <p>{citizenLoginStatus.password[0]}</p>
                </span>
              ) : (
                ""
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
