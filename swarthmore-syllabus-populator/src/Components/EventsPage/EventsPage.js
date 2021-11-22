import React, { useState, useEffect } from "react";
import Event from "./EventCard/EventCard";
import Box from "@mui/material/Box";
import CircularProgress from "@mui/material/CircularProgress";
import Style from "./EventsPage.module.scss";

const Events = () => {
  const [events, setEvents] = useState([{}]);
  const [loading, setLoading] = useState(true);

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
        setEvents(data["parsed_events"]);
      })
      .catch((error) => {
        console.log(error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  const EventsContainer = events.map((event) => (
    <div key={event["id"]}>
      <Event event={event}></Event>
    </div>
  ));

  return (
    <div className={Style.container}>
      {loading ? (
        <Box sx={{ display: "flex" }}>
          <CircularProgress />
        </Box>
      ) : (
        <div className={Style.events_container}>
          <div className={Style.events_grid}>{EventsContainer}</div>

          <button
            className={Style.add_events_button}
            onClick={async () => {
              const selected_events = [];
              for (let i = 0; i < events.length; i++) {
                if (events[i]["checked"] === true) {
                  selected_events.push(events[i]);
                }
              }

              const data = new FormData();
              data.append("selected_events", JSON.stringify(selected_events));

              const response = await fetch("/post_events_to_calendar", {
                method: "POST",
                body: data,
              });

              console.log(response);

              if (response.ok) {
                console.log("/post_events_to_calendar request succeeded");
              } else {
                console.error("/post_events_to_calendar request failed");
              }
            }}
          >
            Add to Calendar
          </button>
        </div>
      )}
    </div>
  );
};

export default Events;
