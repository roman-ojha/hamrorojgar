import React from "react";
import Link from "next/link";
import appIcon from "@/assets/images/appIcon.png";
import Image from "next/image";
import styles from "@/styles/components/navbar.module.scss";
import type { SetStateAction, Dispatch } from "react";

const NavBar = (): React.JSX.Element => {
  return (
    <nav className={styles.navbar}>
      <div className={styles.icon_nav_container}>
        <button
          style={{
            backgroundColor: "transparent",
            borderWidth: "0px",
            padding: "0px",
          }}
        >
          <Image
            className={styles.app_icon}
            src={appIcon}
            alt="app-icon"
          ></Image>
        </button>
        <ul className={styles.nav_list}>
          <li>
            <button>How it works</button>
          </li>
          <li>
            <button>About</button>
          </li>
          <li>
            <button>Contact</button>
          </li>
        </ul>
      </div>
      <div className={styles.buttons}>
        <Link
          href="/register"
          type="button"
          className={`${styles.buttons__button__register} ${styles.buttons__button}`}
        >
          Register
        </Link>
        <Link
          href="/signin"
          className={`${styles.buttons__button__sign_in} ${styles.buttons__button}`}
        >
          Sign in
        </Link>
      </div>
    </nav>
  );
};

export default NavBar;
