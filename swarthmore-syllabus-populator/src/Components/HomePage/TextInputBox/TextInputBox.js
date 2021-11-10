import React from "react";
import { useState } from "react";
import Alert from "@mui/material/Alert";
import { styled } from "@mui/material/styles";
import Style from "./TextInputBox.module.scss";

const TextInputBox = () => {
  const [text, setText] = useState("");
  const [displayAlert, setDisplayAlert] = useState(false);

  const StyledAlert = styled(Alert)(({ theme }) => ({
    marginBottom: "15px",
  }));

  return (
    <div class={Style.container}>
      {displayAlert ? (
        <StyledAlert
          severity="error"
          onClose={() => {
            setDisplayAlert(false);
          }}
        >
          Unable to parse empty text
        </StyledAlert>
      ) : (
        <> </>
      )}

      <textarea
        class={Style.input}
        type="text"
        name="text"
        placeholder="Paste text here"
        rows="4"
        cols="50"
        value={text}
        onChange={(e) => {
          setText(e.target.value);
        }}
      />

      <button
        class={Style.parse_button}
        onClick={async () => {
          if (text.replace(/^\s+/, "").replace(/\s+$/, "") === "") {
            setDisplayAlert(true);
          } else {
            var reader = new FileReader();
            const data = new FormData();
            data.append("text", text);

            const response = await fetch("/parse_text", {
              method: "POST",
              body: data,
            });

            if (response.ok) {
              console.log("/parse_text post request succeeded");
            } else {
              console.error("/parse_text post request failed");
            }
          }
        }}
      >
        <span> Parse Text </span>
      </button>
    </div>
  );
};

export default TextInputBox;
