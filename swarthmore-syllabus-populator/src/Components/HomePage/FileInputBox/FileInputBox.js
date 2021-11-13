import React, { useMemo, useState } from "react";
import { useDropzone } from "react-dropzone";
import { useHistory } from "react-router-dom";
import { styled } from "@mui/material/styles";
import Alert from "@mui/material/Alert";
import Style from "./FileInputBox.module.scss";

const FileInputBox = () => {
  const [displayAlert, setDisplayAlert] = useState(false);
  const [fileDropped, setFileDropped] = useState(false);

  let history = useHistory();

  const StyledAlert = styled(Alert)(({ theme }) => ({
    marginBottom: "15px",
  }));

  const baseStyle = {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    paddingRight: "20px",
    paddingLeft: "20px",
    paddingBottom: "20px",
    paddingTop: "20px",
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
    cursor: "pointer",
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

  const style = useMemo(
    () => ({
      ...baseStyle,
      ...(isDragActive ? activeStyle : {}),
      ...(isDragAccept ? acceptStyle : {}),
      ...(isDragReject ? rejectStyle : {}),
    }),
    [isDragActive, isDragReject, isDragAccept]
  );

  const FileContainer = acceptedFiles.map((file) => (
    <div key={file.path} class={Style.file_container}>
      <i class="fas fa-file-pdf fa-5x"></i>
      <p class={Style.file_path}> {file.path} </p>
    </div>
  ));

  return (
    <div class={Style.container}>
      {displayAlert ? (
        <StyledAlert
          severity="error"
          onClose={() => {
            setDisplayAlert(false);
          }}
        >
          Please upload a file
        </StyledAlert>
      ) : (
        <> </>
      )}

      <div class="container">
        <div
          {...getRootProps({
            style,
            onDrop: () => setFileDropped(true),
          })}
        >
          <input {...getInputProps()} />
          {fileDropped ? (
            FileContainer
          ) : (
            <p>Drag and drop PDF files here, or click to select files</p>
          )}
        </div>
      </div>

      <button
        class={Style.parse_button}
        onClick={async () => {
          if (!fileDropped) {
            setDisplayAlert(true);
          } else {
            const data = new FormData();
            data.append("file", acceptedFiles[0]);

            const response = await fetch("/parse_pdf", {
              method: "POST",
              body: data,
            });

            if (response.ok) {
              history.push("/events");
            } else {
              console.error("/parse_pdf post request failed");
            }
          }
        }}
      >
        <span> Parse PDF File </span>
      </button>
    </div>
  );
};

export default FileInputBox;
