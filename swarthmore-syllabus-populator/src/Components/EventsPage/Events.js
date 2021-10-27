import React from 'react'
import { useState, useEffect} from 'react'

const Events = () => {
    const [todos, setTodos] = useState('Current state');

    useEffect(() => {
        console.log("Testing")
        fetch('/get_events')
          .then((response) => response.json())
          .then((data) => console.log('Here'));
      }, []);
    


    return (
        <div>
            Current state: 
            {todos}
        </div>
    )
}

export default Events
