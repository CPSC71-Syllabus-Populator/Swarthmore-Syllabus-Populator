import React, { useState, useEffect } from "react";
import Event from "./Event";

const Events = () => {
  const [events, setEvents] = useState([{}]);

  useEffect(() => {
    fetch("/get_events", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      })
      .then((data) => {
        console.log(data);
        setEvents(data["events"]);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const EventsContainer = events.map((event) => (
    <div key={event["id"]}>
      <Event title={event["title"]} time={event["time"]}></Event>
    </div>
  ));

  return (
    <div>
      <h2>Our parsing results:</h2>
      {EventsContainer}
    </div>
  );
};

export default Events;
