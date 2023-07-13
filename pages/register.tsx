import React, { useEffect } from "react";
import Head from "next/head";
import styles from "@/styles/pages/register.module.scss";
import Link from "next/link";
import { Icon } from "@iconify/react";
import avatar from "@/assets/svg/avatar.svg";
import Image from "next/image";
import type { NextPage } from "next";
import { useForm } from "react-hook-form";
import { Citizen } from "@/models/citizen";
import { api } from "@/services/api";
import { useRouter } from "next/router";
import { isOkResponse } from "@/utils/checkApiStatus";
import DatePicker from "@/components/RegisterPage/DatePicker";

interface CitizenFormExtension {
  date_of_birth: {
    year: string;
    month: string;
    day: string;
  };
  user: {
    email: string;
    password: string;
    c_password: string;
  };
}

export interface CitizenForm extends Override<Citizen, CitizenFormExtension> {}

const Register: NextPage = () => {
  const router = useRouter();
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<CitizenForm>();

  const onSubmit = async (data: CitizenForm) => {
    const res = await api.citizen.register(data);
    if (res && isOkResponse(res.status)) {
      console.log(res.data);
      console.log(res.status);
      router.push("/verify");
    }
  };

  useEffect(() => {
    // showing citizen image on change
    document.getElementById("picture-file")?.addEventListener("change", (e) => {
      const target = e.target as HTMLInputElement;
      let file: File | undefined;
      if (target.files && target.files?.length > 0) {
        file = target.files?.[0];
      }
      if (file) {
        const reader = new FileReader();
        reader.onload = (event) => {
          const imageSrc = event.target?.result;
          document
            .getElementById("avatar-picture")
            ?.setAttribute("src", imageSrc as string);
          document
            .getElementById("avatar-picture")
            ?.setAttribute("style", "border-radius:50%");
          document
            .getElementById("avatar-picture-outline")
            ?.setAttribute("style", "border-width:0px");
        };
        reader.readAsDataURL(file);
      }
    });
  }, []);

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
          onSubmit={handleSubmit(onSubmit)}
          className={styles.register__form}
        >
          <h1 className={styles.register__form__title}>Registration</h1>
          <div className={styles.register__form__first_row}>
            <div className={styles.register__form__first_row__upload_picture}>
              <div
                className={
                  styles.register__form__first_row__upload_picture__avatar_container
                }
                id="avatar-picture-outline"
              >
                <Image
                  className={
                    styles.register__form__first_row__upload_picture__avatar_container__icon
                  }
                  src={avatar}
                  alt="avatar"
                  id="avatar-picture"
                />
              </div>
              <label htmlFor="picture-file">Upload photo</label>
              <input
                type="file"
                id="picture-file"
                hidden
                {...register("photo")}
                // ref={fileInput}
                accept=".jpg, .png, .jpeg, .gif, .bmp, .tif, .tiff|image/*"
              />
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
                  {...register("f_name")}
                />
                <input
                  type="text"
                  placeholder="Middle name(optional)"
                  data-field="input"
                  {...register("m_name")}
                />
                <input
                  type="text"
                  placeholder="Last name"
                  data-field="input"
                  {...register("l_name")}
                />
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
                {/* <input
                  type="text"
                  placeholder="Province"
                  id="permanent-address-province"
                  data-field="input"
                /> */}
                <input
                  type="text"
                  placeholder="District"
                  data-field="input"
                  {...register("p_address.district")}
                />
                <input
                  type="text"
                  placeholder="Municipality"
                  data-field="input"
                  {...register("p_address.municipality")}
                />
                <input
                  type="number"
                  placeholder="Ward no."
                  data-field="input"
                  {...register("p_address.ward_no")}
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
                {/* <input
                  type="text"
                  placeholder="Province"
                  id="temporary-address-province"
                  data-field="input"
                /> */}
                <input
                  type="text"
                  placeholder="District"
                  data-field="input"
                  {...register("t_address.district")}
                />
                <input
                  type="text"
                  placeholder="Municipality"
                  data-field="input"
                  {...register("t_address.municipality")}
                />
                <input
                  type="number"
                  placeholder="Ward no."
                  data-field="input"
                  {...register("t_address.ward_no")}
                />
              </div>
            </div>
          </div>
          <div className={styles.register__form__second_row}>
            <div className={styles.register__form__second_row__column}></div>
            <div className={styles.register__form__second_row__column}>
              <div className={styles.register__form__second_row__column__field}>
                <input
                  type="email"
                  id="email"
                  placeholder="Email"
                  data-field="input"
                  value={undefined}
                  {...register("user.email")}
                />
              </div>
              <div className={styles.register__form__second_row__column__field}>
                <input
                  type="number"
                  id="mobile_no"
                  placeholder="Mobile no."
                  data-field="input"
                  value={undefined}
                  {...register("mobile")}
                />
              </div>
              <div className={styles.register__form__second_row__column__field}>
                <input
                  type="text"
                  id="nationality"
                  placeholder="Nationality"
                  data-field="input"
                  value={undefined}
                  {...register("nationality")}
                />
              </div>
            </div>
            <div className={styles.register__form__second_row__column}>
              <div className={styles.register__form__second_row__column__field}>
                <input
                  type="text"
                  id="citizenship_no"
                  placeholder="Citizenship no."
                  data-field="input"
                  {...register("citizenship_no")}
                />
              </div>
              <div className={styles.register__form__second_row__column__field}>
                <input
                  type="password"
                  id="password"
                  placeholder="Password"
                  data-field="input"
                  {...register("user.password")}
                />
              </div>
              <div className={styles.register__form__second_row__column__field}>
                <input
                  type="password"
                  id="c_password"
                  placeholder="Confirm password"
                  data-field="input"
                  {...register("user.c_password")}
                />
              </div>
            </div>
            <div className={styles.register__form__second_row__column}>
              <div
                className={
                  styles.register__form__second_row__column__gender_dob
                }
              >
                <div
                  className={styles.register__form__second_row__column__gender}
                >
                  <label htmlFor="gender" data-field="gender">
                    Gender
                  </label>
                  <div
                    className={
                      styles.register__form__second_row__column__gender__fields
                    }
                  >
                    <div
                      className={
                        styles.register__form__second_row__column__gender__fields__radio
                      }
                    >
                      <input
                        type="radio"
                        id="gender-male"
                        value="M"
                        {...register("gender")}
                      />
                      <label htmlFor="gender-male">Male</label>
                    </div>
                    <div
                      className={
                        styles.register__form__second_row__column__gender__fields__radio
                      }
                    >
                      <input
                        type="radio"
                        id="gender-female"
                        value="F"
                        {...register("gender")}
                      />
                      <label htmlFor="gender-female">Female</label>
                    </div>
                    <div
                      className={
                        styles.register__form__second_row__column__gender__fields__radio
                      }
                    >
                      <input
                        type="radio"
                        id="gender-other"
                        value="O"
                        {...register("gender")}
                      />
                      <label htmlFor="gender-other">Other</label>
                    </div>
                  </div>
                </div>
                <DatePicker register={register} />
              </div>
            </div>
          </div>
          <input type="submit" value="Register" />
        </form>
      </div>
    </>
  );
};

export default Register;
