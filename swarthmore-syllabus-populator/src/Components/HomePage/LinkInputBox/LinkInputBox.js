import React from 'react';
import { useState, useEffect } from "react";

const LinkInputBox = () => {
    const [link, setLink] = useState("");

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

                    fetch(`/link_test`,{
                        'method':'POST',
                        headers : {
                            'Content-Type':'application/json'
                        },
                        body:JSON.stringify(link)
                    })
                        .then(response => response.json())
                        .catch(error => console.log(error))
                    }
                // const data = new FormData();
                // data.append("link", link);

                // const response = await fetch("/link_test", {
                //     method: "POST",
                //     body: data,
                // });
                // if (response.ok) {
                //     console.log("request succeeded");
                // } else {
                //     console.error("request failed");
                // }
                }
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
