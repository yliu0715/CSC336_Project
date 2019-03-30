import React from 'react';

const Navbar = () => {
  return (
    <div>
      <nav className="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">
  		  <ul className="navbar-nav mr-auto">
  			<li className="nav-item">
  			  <a className="nav-link" href="#">Home</a>
  			</li>
  			<li className="nav-item">
  			  <a className="nav-link" href="#">About</a>
  			</li>
  			<li className="nav-item">
  			  <a className="nav-link" href="#">FAQ</a>
  			</li>
  		  </ul>
  		  <ul className="navbar-nav">
    			<li className="nav-item dropdown">
    			  <a className="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">My Account</a>
    			  <div className="dropdown-menu">
      				<a className="dropdown-item" href="#">My Profile</a>
      				<a className="dropdown-item" href="#">My Rooms</a>
      				<a className="dropdown-item" href="#">Logout</a>
    			  </div>
    			</li>
  		  </ul>
		  </nav>
    </div>
  )
}

export default Navbar;
