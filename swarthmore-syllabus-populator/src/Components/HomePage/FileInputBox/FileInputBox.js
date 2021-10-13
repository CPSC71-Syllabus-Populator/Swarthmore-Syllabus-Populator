import React, { useState } from "react";

const FileInputBox = () => {
  const [file, setFile] = useState(null);

  return (
    <div>
      <form>
        <input
          type="file"
          name="file"
          onChange={(e) => {
            setFile(e.target.files[0]);
          }}
        />
        <button
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
          }}
        >
          Parse Syllabus
        </button>
      </form>
    </div>
  );
};

export default FileInputBox;
