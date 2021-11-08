import React from "react";
import { useState } from "react";
import Style from "./TextInputBox.module.scss";

const TextInputBox = () => {
  const [text, setText] = useState("");

  return (
    <div class={Style.container}>
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
        }}
      >
        <span> Parse Text </span>
      </button>
    </div>
  );
};

export default TextInputBox;
