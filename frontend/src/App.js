import React, { Component } from 'react';
import './App.css';

import { Route, BrowserRouter as Router } from 'react-router-dom';
import HomePage from './components/Homepage/Homepage';
import Navbar from './components/Navbar/Navbar';
import Register from './components/Register/Register';
import Roompage from './components/Roompage/Roompage';
import SignIn from './components/SignIn/SignIn';
import Error from './components/Error/Error';

class App extends Component {
  constructor() {
    super();
    this.state = {
      users : [],
      authenticated : false
    }
  }

  onLogOut = () => this.setState( { authenticated : false } );

  componentDidMount() {
    //This acts as a fake backend, we will replace this with fetching from our db later
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(resp => resp.json())
      .then(users => this.setState({ users }))
  }

  render() {
    return (
      <Router>
        <div className="App">
          <Navbar authenticated={ this.state.authenticated } onLogOut={ this.onLogOut } />
          <Route exact path="/" render={(props) => <HomePage users={ this.state.users } /> } />
          <Route path="/register" component={Register} />
          <Route path="/login" component={SignIn} />
          <Route path="/roompage" component={Roompage} />
          <Route component={Error} />
        </div>
      </Router>
    );
  }
}

export default App;
