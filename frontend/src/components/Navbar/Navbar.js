import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = (props) => {
  return (
    props.authenticated ?
      <div>
        <nav className="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home</Link>
            </li>
          </ul>
          <ul className="navbar-nav">
            <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">My Account</a>
              <div className="dropdown-menu">
                <Link className="dropdown-item" to="#">My Profile</Link>
                <Link className="dropdown-item" to="#">My Rooms</Link>
                <button className="dropdown-item" onClick={props.onLogOut}>Logout</button>
              </div>
            </li>
          </ul>
        </nav>
      </div>
    :
      <div>
        <nav className="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home</Link>
            </li>
          </ul>
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link" to="/Login">Login</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/Register">Register</Link>
            </li>
          </ul>
        </nav>
      </div>
  )
}

export default Navbar;
