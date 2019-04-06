import React, { Component } from 'react';
import './App.css';

import Navbar from './components/Navbar/Navbar';
import Homepage from './components/Homepage/Homepage';

class App extends Component {
  constructor() {
    super();
    this.state = { users : [] }
  }

  componentDidMount() {
    //This acts as a fake backend, we will replace this with fetching from our db later
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(resp => resp.json())
      .then(users => this.setState({ users }));
  }

  render() {
    return (
      <div className="App">
        <Navbar />
        <Homepage users={this.state.users} />
      </div>
    );
  }
}

export default App;
