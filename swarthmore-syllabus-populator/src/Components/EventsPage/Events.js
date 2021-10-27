import React from 'react'
import { useState, useEffect} from 'react'

const Events = () => {
    const [todos, setTodos] = useState('Current state');

    useEffect(() => {
        fetch('/get_test')
          .then((response) => response.json())
          .then((data) => console.log(data));
      }, []);
    


    return (
        <div>
            Current state: 
            {todos}
        </div>
    )
}

export default Events
