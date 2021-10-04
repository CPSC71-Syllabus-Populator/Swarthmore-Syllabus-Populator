import React from 'react';
import { useState } from "react";
import FileInputBox from "./FileInputBox/FileInputBox";
import TextInputBox from "./TextInputBox/TextInputBox";
import LinkInputBox from "./LinkInputBox/LinkInputBox";

const HomePage = () => {
    const [inputMethod, setInputMethod] = useState("");
    return (
        <div>
            <div>
                <button onClick={() => {setInputMethod("File")}}> File </button>
                <button onClick={() => {setInputMethod("Text")}}> Text </button>
                <button onClick={() => {setInputMethod("Link")}}> Link </button>
            </div>
            {inputMethod === "File" ? <FileInputBox/> : <></>}
            {inputMethod === "Text" ? <TextInputBox/> : <></>}
            {inputMethod === "Link" ? <LinkInputBox/> : <></>}
        </div>
    )
}

export default HomePage;
