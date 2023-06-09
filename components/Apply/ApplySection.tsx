import React, { useEffect, useRef } from "react";
import styles from "@/styles/pages/apply.module.scss";
import { Icon } from "@iconify/react";
import { useForm } from "react-hook-form";
import { JobApplication } from "@/models/job_application";
import { api } from "@/services/api";
import { useRouter } from "next/router";
import { isOkResponse } from "@/utils/checkApiStatus";

const ApplySection = (): React.JSX.Element => {
  const router = useRouter();
  const cvImageElm: React.MutableRefObject<
    null | HTMLDivElement | HTMLImageElement
  > = useRef(null);

  const vacancy_id = router.query.vacancy_id;

  useEffect(() => {
    // showing citizen image on change
    document.getElementById("cv-file")?.addEventListener("change", (e) => {
      const target = e.target as HTMLInputElement;
      let file: File | undefined;
      if (target.files && target.files?.length > 0) {
        file = target.files?.[0];
      }
      if (file) {
        const reader = new FileReader();
        reader.onload = (event) => {
          const imageSrc = event.target?.result;
          const newImgElement = document.createElement("img");
          newImgElement.setAttribute("src", imageSrc as string);
          newImgElement.setAttribute(
            "style",
            "height: 40vh; object-fit: contain; border-radius: 0.8vw;"
          );
          cvImageElm.current?.replaceWith(newImgElement);
        };
        reader.readAsDataURL(file);
      }
    });
  }, []);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<JobApplication>();

  const applyForJob = async (data: JobApplication) => {
    const res_applied_job = await api.jobs.apply(data, vacancy_id as string);
    if (res_applied_job && isOkResponse(res_applied_job.status)) {
      console.log(res_applied_job.data);
      const res_payment = await api.payment.index(
        "khalti",
        res_applied_job.data.data.job_application_id
      );
      if (res_payment && isOkResponse(res_payment.status)) {
        console.log(res_payment);
        window.location.href = res_payment.data.data.payment_url;
      }
    }
  };

  return (
    <section className={styles.apply__main_content__apply_section}>
      <form action="" onSubmit={handleSubmit(applyForJob)}>
        <div
          className={styles.apply__main_content__apply_section__cv_container}
          ref={cvImageElm}
        >
          <h1>CV</h1>
        </div>
        <label htmlFor="cv-file">
          <Icon icon="ph:upload-light" />
          Upload CV
        </label>
        <input
          type="file"
          id="cv-file"
          hidden
          {...register("cv")}
          accept=".jpg, .png, .jpeg, .gif, .bmp, .tif, .tiff|image/*"
        />
        <textarea
          placeholder="Wanted to add something? explain it here..."
          {...register("description")}
        ></textarea>
        <input type="submit" value="Apply" />
      </form>
    </section>
  );
};

export default ApplySection;
