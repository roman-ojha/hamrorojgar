import React, { useEffect, useRef } from "react";
import styles from "@/styles/pages/apply.module.scss";
import { Icon } from "@iconify/react";

const ApplySection = (): React.JSX.Element => {
  const cvImageElm: React.MutableRefObject<
    null | HTMLDivElement | HTMLImageElement
  > = useRef(null);
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
  return (
    <section className={styles.apply__main_content__apply_section}>
      <form action="">
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
