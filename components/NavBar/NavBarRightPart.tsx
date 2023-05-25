import React from "react";
import styles from "@/styles/components/navbar.module.scss";
import Link from "next/link";
import { useAppState } from "@/hooks/useAppState";
import { CitizenState, citizenSelector } from "@/store/selector";
import Image from "next/image";

const NavBarRightPart = (): React.JSX.Element => {
  const [{}, [citizen]] = useAppState<[CitizenState]>([citizenSelector]);
  return (
    <div className={styles.buttons}>
      {citizen && citizen.is_authenticated ? (
        <>
          <p className={styles.buttons__button__email}>
            {citizen && citizen.is_authenticated
              ? `${citizen.f_name} ${citizen.l_name}`
              : ""}
          </p>
          <Link
            href="/signin"
            className={`${styles.buttons__button__sign_in_out} ${styles.buttons__button}`}
          >
            Log Out
          </Link>
          <Image
            className={styles.buttons__button__avatar}
            src={citizen.photo}
            width="20"
            height="20"
            alt="citizen"
          ></Image>
        </>
      ) : (
        <>
          <Link
            href="/register"
            type="button"
            className={`${styles.buttons__button__register} ${styles.buttons__button}`}
          >
            Register
          </Link>
          <Link
            href="/signin"
            className={`${styles.buttons__button__sign_in_out} ${styles.buttons__button}`}
          >
            Sign in
          </Link>
        </>
      )}
    </div>
  );
};

export default NavBarRightPart;
