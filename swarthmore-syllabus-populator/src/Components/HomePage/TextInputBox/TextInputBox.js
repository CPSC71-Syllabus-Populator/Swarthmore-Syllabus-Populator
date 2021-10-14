import React from 'react';
import { useState, useEffect } from "react";

const TextInputBox = () => {
    const [text, setText] = useState("");
    
    const handleChange = (e) => {
        const target = e.target;
        //const name = target.name;
        const value = target.value;

        setText(value);
    }

    useEffect(() => {
        console.log(text);
    }, [text]);

    const resetField = () => {
        setText("");
    }
    

    return (
        <div>
            <textarea
                type="text"
                name="text"
                placeholder="Paste text here"
                rows="4"
                cols="50"
                value={text}
                onChange={handleChange}
            />
            <input
                type="submit"
                value="Submit"
                onClick={resetField}
            />

        </div>
    )
}

export default TextInputBox
