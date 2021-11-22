import React from "react";
import Style from "./NavigationBar.module.scss";

export const NavigationBar = () => {
  return (
    <div className={Style.container}>
      <h1 className={Style.title}> Swarthmore Syllabus Parser </h1>
    </div>
  );
};

export default NavigationBar;
