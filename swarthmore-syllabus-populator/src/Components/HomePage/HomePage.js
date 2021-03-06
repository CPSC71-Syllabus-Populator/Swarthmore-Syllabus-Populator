import React from "react";
import { useState } from "react";
import FileInputBox from "./FileInputBox/FileInputBox";
import TextInputBox from "./TextInputBox/TextInputBox";
import Fab from "@mui/material/Fab";
import InsertDriveFileIcon from "@mui/icons-material/InsertDriveFile";
import TextFieldsIcon from "@mui/icons-material/TextFields";
import { styled } from "@mui/material/styles";
import Style from "./HomePage.module.scss";

const HomePage = () => {
  const [inputMethod, setInputMethod] = useState("File");

  const StyledFab = styled(Fab)(({ theme }) => ({
    backgroundColor: "#912F40",
    "&:hover": {
      backgroundColor: "#702632",
    },
  }));

  return (
    <div className={Style.container}>
      <div className={Style.input}>
        <div className={Style.input_left}>
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
        </div>
        <div className={Style.input_right}>
          {inputMethod === "File" ? <FileInputBox /> : <></>}
          {inputMethod === "Text" ? <TextInputBox /> : <></>}
        </div>
      </div>
    </div>
  );
};

export default HomePage;
