import React, { useMemo } from "react";
import { useDropzone } from "react-dropzone";
import Style from "./FileInputBox.module.scss";

const FileInputBox = () => {
  const baseStyle = {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    padding: "20px",
    borderWidth: 2,
    borderRadius: 2,
    borderColor: "#702632",
    borderStyle: "dashed",
    backgroundColor: "#fafafa",
    color: "#bdbdbd",
    outline: "none",
    transition: "border .24s ease-in-out",
    height: "300px",
    width: "500px",
  };

  const activeStyle = {
    borderColor: "#2196f3",
  };

  const acceptStyle = {
    borderColor: "#00e676",
  };

  const rejectStyle = {
    borderColor: "#ff1744",
  };

  const {
    acceptedFiles,
    getRootProps,
    getInputProps,
    isDragActive,
    isDragAccept,
    isDragReject,
    maxFiles = 1,
  } = useDropzone({ accept: ".pdf" });

  const acceptedFileItems = acceptedFiles.map((file) => (
    <li key={file.path}>
      {file.path} - {file.size} bytes
    </li>
  ));

  const style = useMemo(
    () => ({
      ...baseStyle,
      ...(isDragActive ? activeStyle : {}),
      ...(isDragAccept ? acceptStyle : {}),
      ...(isDragReject ? rejectStyle : {}),
    }),
    [isDragActive, isDragReject, isDragAccept]
  );

  return (
    <div class="container">
      <div {...getRootProps({ style })}>
        <input {...getInputProps()} />
        <p>Drag and drop PDF files here, or click to select files</p>
      </div>

      <button
        class={Style.parse_button}
        onClick={async () => {
          const data = new FormData();
          console.log(acceptedFiles[0]);
          data.append("file", acceptedFiles[0]);

          const response = await fetch("/parse_pdf", {
            method: "POST",
            body: data,
          });

          if (response.ok) {
            console.log("/parse_pdf post request succeeded");
          } else {
            console.error("/parse_pdf post request failed");
          }
        }}
      >
        <span> Parse PDF File </span>
      </button>
    </div>
  );
};

export default FileInputBox;
