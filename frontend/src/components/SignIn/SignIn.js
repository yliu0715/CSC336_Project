import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import './SignIn.css';

class SignIn extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: ''
    }
  }

  onUsernameChange = (event) => {this.setState({ username: event.target.value })}
  onPasswordChange = (event) => {this.setState({ password: event.target.value })}
  onLogin = (event) => {
    event.preventDefault();
    fetch('http://localhost:5000/user/login', {
      method: 'post',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        username: this.state.username,
        password: this.state.password
      })
    }).then(resp => resp.json())
      .then(data => {
        const message = data.msg;
        if(message === 'Logged in.') {
          this.props.onLoginChange();
          this.props.history.push('/');
        }
        else alert(message);
      })
      .then(err => console.log(err));
  }

  render() {
    return (
      <div className="container">
        <div className="form-bg">
          <form>
            <h2 className="text-center">Login Form</h2>
            <div className="form-group">
              <label>Username</label>
              <input type="text" className="form-control" placeholder="Enter Username" onChange={this.onUsernameChange}/>
            </div>
            <div className="form-group">
              <label>Password</label>
              <input type="password" className="form-control" placeholder="Enter Password" onChange={this.onPasswordChange}/>
            </div>
            <div>
              <Link className="nav-link" to="/Register">{`Don't Have an Account? Register`}</Link>
            </div>
            <div className="text-center mt-3">
              <button onClick={this.onLogin} type="submit" className="btn btn-primary btn-block">Login</button>
            </div>
          </form>
        </div>
      </div>
    );
  }
}

export default SignIn;
