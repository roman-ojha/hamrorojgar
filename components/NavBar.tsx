import React from "react";
import appIcon from "@/assets/images/appIcon.png";
import Image from "next/image";
import styles from "@/styles/components/navbar.module.scss";

const NavBar = (): React.JSX.Element => {
  return (
    <nav className={styles.navbar}>
      <div className={styles.icon_nav_container}>
        <Image className={styles.app_icon} src={appIcon} alt="app-icon"></Image>
        <ul className={styles.nav_list}>
          <li>How it works</li>
          <li>About</li>
          <li>Contact</li>
        </ul>
      </div>
      <div className={styles.buttons}>
        <button
          type="button"
          className={`${styles.buttons__button__register} ${styles.buttons__button}`}
        >
          Register
        </button>
        <button
          type="button"
          id="sign_in_button"
          className={`${styles.buttons__button__sign_in} ${styles.buttons__button}`}
        >
          Sign in
        </button>
      </div>
    </nav>
  );
};

export default NavBar;
