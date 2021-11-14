import React from "react";
import Checkbox from "@mui/material/Checkbox";
import TextField from "@mui/material/TextField";
import { styled } from "@mui/material/styles";
import Style from "./EventCard.module.scss";

const Event = ({ event }) => {
  const StyledCheckbox = styled(Checkbox)(({ theme }) => ({
    "& .MuiSvgIcon-root": {
      color: "#702632",
    },
  }));

  const StyledTextField = styled(TextField)(({ theme }) => ({
    "& .MuiInput-root": {
      color: "white;",
      fontFamily: "AirbnbCereal",
      "&:before": {
        borderBottom: "1px solid #912f40;",
      },
      "&:hover:before": {
        borderBottom: "2px solid #912f40;",
      },
      "&:after": {
        borderBottom: "2px solid #912f40;",
      },
    },
  }));

  return (
    <div class={Style.container}>
      <div class={Style.title_container}>
        <StyledTextField
          id="standard-basic"
          variant="standard"
          placeholder={event["title"]}
          onChange={(e) => (event["title"] = e.target.value)}
        />

        <StyledCheckbox
          defaultChecked={event["checked"]}
          size="medium"
          onChange={(e) => {
            event["checked"] = e.target.checked;
          }}
        />
      </div>
      <p class={Style.weekday_heading}>{event["weekday"]}</p>
      <p class={Style.time_heading}>{event["time"]}</p>
    </div>
  );
};

export default Event;
