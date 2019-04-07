import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { Route, Link, BrowserRouter as Router } from 'react-router-dom';
import HomePage from './components/Homepage/Homepage';
import ListOfRooms from './components/ListOfRooms/ListOfRooms';
import Navbar from './components/Navbar/Navbar';
import Register from './components/Register/Register';
import Room from './components/Room/Room';
import Roompage from './components/Roompage/Roompage';
import SignIn from './components/SignIn/SignIn';

const routing = (
    <Router>
      <div>
        <Route exact path="/" component={HomePage} />
        <Route path="/register" component={Register} />
        <Route path="/login" component={SignIn} />
        <Route path="/room" component={Room} />
        <Route path="/roompage" component={Roompage} />
      </div>
    </Router>
  )

ReactDOM.render(routing, document.getElementById('root'));
