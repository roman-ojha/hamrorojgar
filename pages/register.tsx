import React from "react";
import Head from "next/head";
import styles from "@/styles/pages/register.module.scss";
import Link from "next/link";
import { Icon } from "@iconify/react";
import avatar from "@/assets/svg/avatar.svg";
import Image from "next/image";

const Register = (): React.JSX.Element => {
  return (
    <>
      <Head>
        <title>Register</title>
      </Head>
      <div className={styles.register}>
        <div className={styles.register__navigate_home}>
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
            className={styles.register__navigate_home__button}
          >
            <Icon
              id="back_icon"
              className={styles.register__navigate_home__button__icon}
              icon="material-symbols:arrow-back-ios-new-rounded"
            />
            <h3 id="home_navigation">Home</h3>
          </Link>
        </div>
        <form
          onSubmit={(e) => {
            e.preventDefault();
          }}
          className={styles.register__form}
        >
          <h1 className={styles.register__form__title}>Registration</h1>
          <div className={styles.register__form__first_row}>
            <div className={styles.register__form__first_row__upload_picture}>
              <div
                className={
                  styles.register__form__first_row__upload_picture__avatar_container
                }
              >
                <Image
                  className={
                    styles.register__form__first_row__upload_picture__avatar_container__icon
                  }
                  src={avatar}
                  alt="avatar"
                />
              </div>
              <label htmlFor="picture-file">Upload photo</label>
              <input type="file" name="picture" id="picture-file" hidden />
            </div>
            <div className={styles.register__form__first_row__field_group}>
              <label htmlFor="first-name">Name</label>
              <div
                className={
                  styles.register__form__first_row__field_group__fields
                }
              >
                <input
                  type="text"
                  placeholder="First name"
                  id="first-name"
                  data-field="input"
                />
                <input
                  type="text"
                  placeholder="Middle name(optional)"
                  data-field="input"
                />
                <input type="text" placeholder="Last name" data-field="input" />
              </div>
            </div>
            <div className={styles.register__form__first_row__field_group}>
              <label htmlFor="permanent-address-province">
                Permanent address
              </label>
              <div
                className={
                  styles.register__form__first_row__field_group__fields
                }
              >
                <input
                  type="text"
                  placeholder="Province"
                  id="permanent-address-province"
                  data-field="input"
                />
                <input type="text" placeholder="District" data-field="input" />
                <input
                  type="text"
                  placeholder="Municipality"
                  data-field="input"
                />
                <input
                  type="number"
                  placeholder="Ward no."
                  data-field="input"
                />
              </div>
            </div>
            <div className={styles.register__form__first_row__field_group}>
              <label htmlFor="temporary-address-province">
                Temporary address (optional)
              </label>
              <div
                className={
                  styles.register__form__first_row__field_group__fields
                }
              >
                <input
                  type="text"
                  placeholder="Province"
                  id="temporary-address-province"
                  data-field="input"
                />
                <input type="text" placeholder="District" data-field="input" />
                <input
                  type="text"
                  placeholder="Municipality"
                  data-field="input"
                />
                <input
                  type="number"
                  placeholder="Ward no."
                  data-field="input"
                />
              </div>
            </div>
          </div>
          <div className={styles.register__form__second_row}></div>
          <div className={styles.register__form__button_container}></div>
        </form>
      </div>
    </>
  );
};

export default Register;
