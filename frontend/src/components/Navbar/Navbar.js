import React from 'react';

const Navbar = () => {
  return (
    <div>
        <nav class="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">
		  <ul class="navbar-nav mr-auto">
			<li class="nav-item">
			  <a class="nav-link" href="#">Home</a>
			</li>
			<li class="nav-item">
			  <a class="nav-link" href="#">About</a>
			</li>
			<li class="nav-item">
			  <a class="nav-link" href="#">FAQ</a>
			</li>
		  </ul>
		  <ul class="navbar-nav">
			<li class="nav-item dropdown">
			  <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">My Account</a>
			  <div class="dropdown-menu">
				<a class="dropdown-item" href="#">My Profile</a>
				<a class="dropdown-item" href="#">My Rooms</a>
				<a class="dropdown-item" href="#">Logout</a>
			  </div>
			</li>
		  </ul>
		</nav>
    </div>
  )
}

export default Navbar;
