import React from "react";
import styles from "@/styles/pages/apply.module.scss";
import { Icon } from "@iconify/react";

const ApplySection = (): React.JSX.Element => {
  return (
    <section className={styles.apply__main_content__apply_section}>
      <form action="">
        <div
          className={styles.apply__main_content__apply_section__cv_container}
        >
          <h1>CV</h1>
        </div>
        <label htmlFor="picture-file">
          <Icon icon="ph:upload-light" />
          Upload CV
        </label>
        <input
          type="file"
          id="picture-file"
          hidden
          // {...register("photo")}
          // ref={fileInput}
          accept=".jpg, .png, .jpeg, .gif, .bmp, .tif, .tiff|image/*"
        />
        <textarea
          name=""
          id=""
          placeholder="Wanted to add something? explain it here..."
        ></textarea>
        <input type="submit" value="Apply" />
      </form>
    </section>
  );
};

export default ApplySection;
