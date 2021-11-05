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
    </div>
  );
};

export default TextInputBox;
