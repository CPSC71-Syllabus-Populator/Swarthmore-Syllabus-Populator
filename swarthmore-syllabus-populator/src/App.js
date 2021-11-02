import "./App.module.scss";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import HomePage from "./Components/HomePage/HomePage";
import NavigationBar from "./Components/NavigationBar/NavigationBar";
import Events from "./Components/EventsPage/Events";

function App() {
  return (
    <div className="App">
      <NavigationBar />
      <Router>
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route exact path="/events" component={Events} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
