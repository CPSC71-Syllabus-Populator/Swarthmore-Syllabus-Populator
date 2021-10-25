import React from 'react';
import { useState, useEffect } from "react";

const LinkInputBox = () => {
    const [link, setLink] = useState("");
    
    const handleChange = (e) => {
        const target = e.target;
        //const name = target.name;
        const value = target.value;

        setLink(value);
    }

    useEffect(() => {
        console.log(link);
    }, [link]);

    const resetField = () => {
        setLink("");
    }

    return (
        <div>
            <input
                type="text"
                name="link"
                placeholder="Paste link here"
                value={link}
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

export default LinkInputBox
