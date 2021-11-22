import React, { useState } from "react";
import Checkbox from "@mui/material/Checkbox";
import TextField from "@mui/material/TextField";
import { styled } from "@mui/material/styles";
import Style from "./EventCard.module.scss";

const Event = ({ event }) => {
  const [checked, setChecked] = useState(event["checked"]);

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
    <div
      className={checked ? Style.container_checked : Style.container_unchecked}
    >
      <div className={Style.title_container}>
        <StyledTextField
          id="standard-basic"
          variant="standard"
          placeholder={event["summary"]}
          onChange={(e) => (event["summary"] = e.target.value)}
        />

        <StyledCheckbox
          defaultChecked={event["checked"]}
          size="medium"
          onChange={(e) => {
            event["checked"] = e.target.checked;
            setChecked(e.target.checked);
          }}
        />
      </div>
      <p className={Style.weekday_heading}>{event["weekday"]}</p>
      <p className={Style.time_heading}>{event["displayTime"]}</p>
    </div>
  );
};

export default Event;
