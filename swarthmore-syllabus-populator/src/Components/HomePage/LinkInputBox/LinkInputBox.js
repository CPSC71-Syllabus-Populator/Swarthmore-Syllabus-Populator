import React from 'react';
import { useState } from "react";
import { useHistory } from 'react-router-dom';

const LinkInputBox = () => {
    const [link, setLink] = useState("");
    const history = useHistory();

    return (
        <div>
            <input
                type="text"
                name="link"
                placeholder="Paste link here"
                value={link}
                onChange={(e) => {
                    setLink(e.target.value);
                }}
                // onChange={handleChange}
            />
            <button
                onClick={async () => {
                    const data = new FormData();
                    data.append("link", link);

                    const response = await fetch("/send_link", {
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
                Submit link
            </button>
            {link}
        </div>
    )
}

export default LinkInputBox

    // const handleChange = (e) => {
    //     const target = e.target;
    //     //const name = target.name;
    //     const value = target.value;

    //     setLink(value);
    // }

    // useEffect(() => {
    //     console.log(link);
    // }, [link]);

    // const resetField = () => {
    //     setLink("");
    // }
