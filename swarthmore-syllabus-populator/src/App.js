import './App.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import HomePage from "./Components/HomePage/HomePage"
import NavigationBar from "./Components/NavigationBar/NavigationBar"

function App() {
  return (
    <div className="App">
      <NavigationBar/>
      <Router>
        <Switch>
          <Route exact path="/" component={HomePage}/> 
        </Switch>
      </Router>
    </div>
  );
}

export default App;
