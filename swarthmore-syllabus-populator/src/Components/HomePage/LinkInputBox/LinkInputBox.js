import React from 'react';
import { useState } from "react";

const LinkInputBox = () => {
    const [link, setLink] = useState("");

    const onChange = () => {
        console.log(link);
    }
    
    const handleChange = (e) => {
        setLink(e.target.value)
        console.log(e.target.value)
        console.log(link)
    }

    const resetField = () => {
        setLink("");
    }

    return (
        <div>
            <input
                type="text"
                placeholder="Paste link here"
                onChange={handleChange}
                name="name"
            />
            <input
                type="submit"
                value="Submit"
                onClick={resetField}
            />
        </div>
    )
}

export default LinkInputBox
