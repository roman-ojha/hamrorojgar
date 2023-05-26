import React from "react";
import Link from "next/link";
import appIcon from "@/assets/images/appIcon.png";
import Image from "next/image";
import styles from "@/styles/components/navbar.module.scss";
import NavBarRightPart from "./NavBar/NavBarRightPart";

const NavBar = (): React.JSX.Element => {
  return (
    <nav id="navbar" className={styles.navbar}>
      <div className={styles.icon_nav_container}>
        <Link
          href="/"
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
        </Link>
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
      <NavBarRightPart />
    </nav>
  );
};

export default NavBar;
