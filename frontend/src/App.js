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
import CreateRoom from './components/CreateRoom/CreateRoom';

class App extends Component {
  constructor() {
    super();
    this.state = {
      users : [],
      currentUser : {
        firstname: '',
        lastname: '',
        username: ''
      },
      room: {},
      authenticated : false
    }
  }

  onLogOut = () => this.setState( { authenticated : false } );
  onRegisterOrLoginChange = () => this.setState( { authenticated : true });
  getUserOnLogin = (currentUser) => {this.setState( { currentUser } )};
  onRoomClick = (room) => {this.setState ( { room } )};

  componentDidMount() {
    //This acts as a fake backend, we will replace this with fetching from our db later

    fetch('http://localhost:5000/rooms')
      .then(resp => resp.json())
      .then(data => this.setState({ users: data.msg }));
  }

  render() {
    return (
      <Router>
        <div className="App">
          <Navbar authenticated={ this.state.authenticated } onLogOut={ this.onLogOut } />
          <Route exact path="/" render={(props) => <HomePage {...props} users={ this.state.users } onRoomClick={ this.onRoomClick } /> } />
          <Route path="/register" render={(props) => <Register {...props}
                                                               getUserOnLogin={ this.getUserOnLogin }
                                                               onRegisterChange={ this.onRegisterOrLoginChange } /> } />
          <Route path="/login" render={(props) => <SignIn {...props}
                                                          getUserOnLogin={ this.getUserOnLogin }
                                                          onLoginChange={ this.onRegisterOrLoginChange } /> } />
          <Route path="/roompage" render={(props) => <Roompage room={ this.state.room } /> } />
          <Route path="/profile" render={(props) => <Profile currentUser={ this.state.currentUser } /> } />
          <Route path="/createroom" render={(props) => <CreateRoom /> } />
          <Route component={Error} />
        </div>
      </Router>
    );
  }
}

export default App;
