import React from 'react';
import { useState } from "react";
import { useHistory } from 'react-router-dom'

const TextInputBox = () => {
    const [text, setText] = useState("");    
    const history = useHistory();

    return (
        <div>
            <textarea
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

            <button
            onClick={async () => {
                const data = new FormData();
                data.append("text", text);

                const response = await fetch("/send_text", {
                method: "POST",
                body: data,
                });
                if (response.ok) {
                console.log("request succeeded");
                } else {
                console.error("request failed");
                }
                history.push('/events')
            }}
            >
            Parse Syllabus
            </button>
        </div>
    )
}

export default TextInputBox
