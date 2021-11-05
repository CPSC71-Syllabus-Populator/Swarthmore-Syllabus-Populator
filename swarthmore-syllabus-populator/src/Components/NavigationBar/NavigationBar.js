import React from "react";
import Style from "./NavigationBar.module.scss";

export const NavigationBar = () => {
  return (
    <div class={Style.container}>
      <h1 class={Style.title}> Swarthmore Syllabus Parser </h1>
    </div>
  );
};

export default NavigationBar;
