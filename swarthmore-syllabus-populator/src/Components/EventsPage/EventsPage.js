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
        const parsed_events = data["events"];
        console.log(typeof parsed_events);
        setEvents(data["events"]);
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
    <div class={Style.container}>
      {loading ? (
        <Box sx={{ display: "flex" }}>
          <CircularProgress />
        </Box>
      ) : (
        <div class={Style.events_container}>
          <div class={Style.events_grid}>{EventsContainer}</div>

          <button
            class={Style.add_events_button}
            onClick={() => {
              const data = new FormData();
              data.append("json_events", JSON.stringify(events));

              const response = fetch("/post_events_to_calendar", {
                method: "POST",
                body: data,
              });

              if (response.ok == true) {
                console.log("/post_events_to_calendar request succeeded");
              } else {
                console.error("/post_events_to_calendar request failed");
              }
              // events.map((event) => {
              //   if (event["checked"] == true) {
              //   }
              // });
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
