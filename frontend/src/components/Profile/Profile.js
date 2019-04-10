import React from 'react';
import './Profile.css';

const Profile = () => {
	return(
		<div className="profile">
			<div className="bio">
				<img src="https://dab1nmslvvntp.cloudfront.net/wp-content/uploads/2016/09/1473921124injection-attack.jpg" />
				<p>Hello</p>
			</div>
			<div className="main">
				<h1>Profile</h1>
				<form>
				<p>Name:</p>
				<input type="text" name="fullname" />
				<p>Email Address:</p>
				<input type="email" name="email" />
				<p>Location:</p>
				<input type="text" name="Location" />
				<p>Skills:</p>
				<div className="d-inline-flex flex-nowrap">
					<div className="p-2 border align-middle">React</div>
					<div className="p-2 border">Python</div>
					<div className="p-2 border">SQL</div>
				</div>
				</form>
				<p>My Rooms</p>
			</div>
		</div>
	)
}

export default Profile;