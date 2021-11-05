import React from "react";
import { useState } from "react";
import FileInputBox from "./FileInputBox/FileInputBox";
import TextInputBox from "./TextInputBox/TextInputBox";
import LinkInputBox from "./LinkInputBox/LinkInputBox";
import Fab from "@mui/material/Fab";
import InsertDriveFileIcon from "@mui/icons-material/InsertDriveFile";
import TextFieldsIcon from "@mui/icons-material/TextFields";
import LinkIcon from "@mui/icons-material/Link";
import { styled } from "@mui/material/styles";
import Style from "./HomePage.module.scss";
import Slider from "@mui/material/Slider";
import { red } from "@mui/material/colors";

const HomePage = () => {
  const [inputMethod, setInputMethod] = useState("File");

  const StyledFab = styled(Fab)(({ theme }) => ({
    backgroundColor: "#912F40",
    "&:hover": {
      backgroundColor: "#702632",
    },
  }));

  return (
    <div class={Style.container}>
      <div class={Style.input}>
        <div class={Style.input_left}>
          <StyledFab
            size="medium"
            onClick={() => {
              setInputMethod("File");
            }}
          >
            <InsertDriveFileIcon sx={{ color: "white" }} />
          </StyledFab>
          <StyledFab
            size="medium"
            onClick={() => {
              setInputMethod("Text");
            }}
          >
            <TextFieldsIcon sx={{ color: "white" }} />
          </StyledFab>
          <StyledFab
            size="medium"
            onClick={() => {
              setInputMethod("Link");
            }}
          >
            <LinkIcon sx={{ color: "white" }} />
          </StyledFab>
        </div>
        <div class={Style.input_right}>
          {inputMethod === "File" ? <FileInputBox /> : <></>}
          {inputMethod === "Text" ? <TextInputBox /> : <></>}
          {inputMethod === "Link" ? <LinkInputBox /> : <></>}
          <button class={Style.parse_button}>
            <span> Parse {inputMethod} </span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
