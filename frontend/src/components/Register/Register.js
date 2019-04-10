import React, { Component } from 'react';
import {  Link } from 'react-router-dom';

import './Register.css';

class Register extends Component {
  constructor(props) {
    super(props);
    this.state = {
      firstname: "",
      lastname: "",
      username: "",
      password: "",
    }
  }

  onFirstNameChange = (event) => {this.setState({firstname: event.target.value})};
  onLastNameChange = (event) => {this.setState({lastname: event.target.value})};
  onUserNameChange = (event) => {this.setState({username: event.target.value})};
  onPasswordChange = (event) => {this.setState({password: event.target.value})};
  onRegister = (event) => {
    event.preventDefault();
    fetch('http://localhost:5000/user/register', {
      method: 'post',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        firstname: this.state.firstname,
        lastname: this.state.lastname,
        username: this.state.username,
        password: this.state.password
      })
    }).then(resp => resp.json())
      .then(data => {
        const message = data.msg;
        if(message === 'Registration complete') {
          this.props.onRegisterChange();
          const currentUser = {
            firstname: this.state.firstname,
            lastname: this.state.lastname,
            username: this.state.username
          }
          this.props.getUserOnLogin(currentUser);
          this.props.history.push('/');
        }
        else alert(message);
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div className="container">
        <div className="form-bg">
          <form>
            <h2 className="text-center">Register Form</h2>
            <div className="form-group">
              <label>First Name</label>
              <input type="text" className="form-control" placeholder="Enter Your First Name" onChange={this.onFirstNameChange}/>
            </div>
            <div className="form-group">
              <label>Last Name</label>
              <input type="text" className="form-control" placeholder="Enter Your Last Name" onChange={this.onLastNameChange}/>
            </div>
            <div className="form-group">
              <label>Username</label>
              <input type="text" className="form-control" placeholder="Enter Username" onChange={this.onUserNameChange}/>
            </div>
            <div className="form-group">
              <label>Password</label>
              <input type="password" className="form-control" placeholder="Enter Password" onChange={this.onPasswordChange}/>
            </div>
            <div>
              <Link className="nav-link" to="/Login">Already Have an Account? Login</Link>
            </div>
            <div className="text-center mt-3">
              <button onClick={this.onRegister} type="submit" className="btn btn-primary btn-block">Register</button>
            </div>
          </form>
        </div>
      </div>
    )
  }
}

export default Register;
