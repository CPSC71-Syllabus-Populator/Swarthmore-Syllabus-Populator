import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import Style from "./FileInputBox.module.scss";

const FileInputBox = () => {
  const [file, setFile] = useState(null);
  const history = useHistory();

  return (
    <div>
      <form class={Style.form}>
        <input
          class={Style.input}
          type="file"
          name="file"
          onChange={(e) => {
            setFile(e.target.files[0]);
          }}
        />
        <button
          class={Style.button}
          onClick={async () => {
            const data = new FormData();
            data.append("file", file);

            const response = await fetch("/parse_pdf", {
              method: "POST",
              body: data,
            });
            if (response.ok) {
              console.log("request succeeded");
            } else {
              console.error("request failed");
            }
            history.push("/events");
          }}
        >
          Parse Syllabus
        </button>
      </form>
    </div>
  );
};

export default FileInputBox;
