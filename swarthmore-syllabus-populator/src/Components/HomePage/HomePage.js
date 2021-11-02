import React from "react";
import { useState } from "react";
import FileInputBox from "./FileInputBox/FileInputBox";
import TextInputBox from "./TextInputBox/TextInputBox";
import LinkInputBox from "./LinkInputBox/LinkInputBox";
import Fab from "@mui/material/Fab";
import InsertDriveFileIcon from "@mui/icons-material/InsertDriveFile";
import TextFieldsIcon from "@mui/icons-material/TextFields";
import LinkIcon from "@mui/icons-material/Link";
import Style from "./HomePage.module.scss";

const HomePage = () => {
  const [inputMethod, setInputMethod] = useState("File");
  return (
    <div class={Style.container}>
      <div class={Style.input_buttons}>
        <Fab
          class={Style.button}
          size="small"
          onClick={() => {
            setInputMethod("File");
          }}
        >
          <InsertDriveFileIcon class={Style.button} />
        </Fab>
        <Fab
          class={Style.button}
          size="small"
          onClick={() => {
            setInputMethod("Text");
          }}
        >
          <TextFieldsIcon />
        </Fab>
        <Fab
          class={Style.button}
          size="small"
          onClick={() => {
            setInputMethod("Link");
          }}
        >
          <LinkIcon class={Style.button2} />
        </Fab>
      </div>
      {inputMethod === "File" ? <FileInputBox /> : <></>}
      {inputMethod === "Text" ? <TextInputBox /> : <></>}
      {inputMethod === "Link" ? <LinkInputBox /> : <></>}
    </div>
  );
};

export default HomePage;
