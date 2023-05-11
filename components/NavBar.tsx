import React from "react";
import appIcon from "@/assets/images/appIcon.png";
import Image from "next/image";

const NavBar = (): React.JSX.Element => {
  return (
    <nav>
      <div>
        <Image src={appIcon} alt="appIcon"></Image>
      </div>
      <li>
        <ul>How it works</ul>
        <ul>About</ul>
        <ul>Contact</ul>
      </li>
      <div>
        <button>Register</button>
        <button>Sign in</button>
      </div>
    </nav>
  );
};

export default NavBar;
