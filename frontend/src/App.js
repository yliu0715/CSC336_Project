import React, { Component } from 'react';
import './App.css';

import { Route, BrowserRouter as Router } from 'react-router-dom';
import HomePage from './components/Homepage/Homepage';
import Navbar from './components/Navbar/Navbar';
import Register from './components/Register/Register';
import Roompage from './components/Roompage/Roompage';
import SignIn from './components/SignIn/SignIn';
import Error from './components/Error/Error';
import Profile from './components/Profile/Profile';

class App extends Component {
  constructor() {
    super();
    this.state = {
      users : [],
      room: {},
      authenticated : false
    }
  }

  onLogOut = () => this.setState( { authenticated : false } );
  onRegisterOrLoginChange = () => this.setState( { authenticated : true });
  onRoomClick = (room) => {
    console.log(room);
    this.setState ( { room } );
  }
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
          <Route exact path="/" render={(props) => <HomePage {...props} users={ this.state.users } onRoomClick={ this.onRoomClick } /> } />
          <Route path="/register" render={(props) => <Register {...props} onRegisterChange={ this.onRegisterOrLoginChange } /> } />
          <Route path="/login" render={(props) => <SignIn {...props} onLoginChange={ this.onRegisterOrLoginChange } /> } />
          <Route path="/roompage" render={(props) => <Roompage room={ this.state.room } /> } />
          <Route component={Error} />
        </div>
      </Router>
    );
  }
}

export default App;
