import React from 'react'
import { useState, useEffect} from 'react'
import Event from "./Event";

const Events = () => {
    const [events, setEvents] = useState([
        {
            id: 0,
            class: 'CS21',
            title: 'Office Hours',
            time: '5-6pm WF'
        },
        {
            id: 1,
            class: 'Math 15',
            title: 'Pi-Rate Clinic',
            time: '4-5pm TH, 7-9pm F'
        },
        {
            id: 2,
            class: 'ENVS 001',
            title: 'Office Hours',
            time: '6:30-830pm M, 2-3pm T'
        },
        {
            id: 3,
            class: 'PHIL 12B',
            title: 'Office Hours',
            time: '5-6pm WF'
        },
    ]);

    useEffect(() => {
        console.log("fetching events");
        fetch('/get_events', {
         headers : { 
         'Content-Type': 'application/json',
         'Accept': 'application/json'
           }
        })
        .then((response) => {console.log(response);})
        //  .then((messages) => {console.log("messages");})
        }, []);

    // useEffect(() => {
    //     const response = fetch("/get_events");
    //     console.log(response)
    //     if (response.ok) {
    //     console.log("request succeeded");
    //     } else {
    //     console.error("request failed");
    //     }
    //   }, []);

      const displayEvents = () => {
          return events.map((event) => {
              return (
                    <div className="Option">
                        <Event key={event.id} meeting={event.class} 
                        title={event.title} time={event.time}/>
                        <p>Add event?</p>
                        <input type="checkbox" />
                    </div>
                    )
          })
      }

    return (
        <div>
            <h2>Our parsing results:</h2>
            {displayEvents()}
        </div>
    )
}

export default Events

// console.log("Testing")
//         fetch('/get_events')
//           .then((response) => response.json())
//           .then((data) => console.log('Here'));