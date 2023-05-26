import React from "react";
import styles from "@/styles/components/background.module.scss";

const Background = (): React.JSX.Element => {
  return (
    <>
      <div className={styles.background}>
        <div className={styles.background__color}></div>
        <div className={styles.background__image}></div>
      </div>
    </>
  );
};

export default Background;
