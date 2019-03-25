import React, { Component } from 'react';

import './SignIn.css';

class SignIn extends Component {
  constructor(props) {
    super(props);
    this.state = {
      userName: '',
      password: ''
    }
  }

  onUsernameChange = (event) => {console.log(event.target.value)}
  onPasswordChange = (event) => {console.log(event.target.value)}

  render() {
    return (
      <div className="container">
        <div className="form-bg">
          <form>
            <h2 className="text-center">Login Form</h2>
            <div className="form-group">
              <label>Username</label>
              <input type="email" className="form-control" placeholder="Enter Username"/>
            </div>
            <div className="form-group">
              <label>Password</label>
              <input type="password" className="form-control" placeholder="Enter Password"/>
            </div>
            <div>
              <a href="#"> Don't Have An Account? Register</a>
            </div>
            <div className="text-center mt-3">
              <button type="submit" className="btn btn-primary btn-block">Login</button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default SignIn;
