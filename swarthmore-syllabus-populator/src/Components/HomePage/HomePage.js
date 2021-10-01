import React from 'react'
import { useState } from "react";
import FileInputBox from "./FileInputBox/FileInputBox"

const HomePage = () => {
    const [inputMethod, setInputMethod] = useState("File");
    return (
        <div>
            <div>
                <button> File </button>
                <button onClick={() => {setInputMethod("Text")}}> Text </button>
                <button> Link </button>
            </div>
            {inputMethod == "File" ? <FileInputBox/> : <></>}
        </div>
    )
}

export default HomePage;
