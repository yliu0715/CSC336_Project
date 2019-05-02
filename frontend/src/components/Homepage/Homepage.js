import React from 'react';
import { Link } from 'react-router-dom';

import ListOfRooms from '../ListOfRooms/ListOfRooms';

const Homepage = (props) => {
  return (
	props.authenticated ?
		<div>
        <Link to="/CreateRoom">+ Create Room</Link>
			  <ListOfRooms {...props} users={props.users} onRoomClick={ props.onRoomClick } />
		</div>
	:
    <div>
      <ListOfRooms {...props} users={props.users} onRoomClick={ props.onRoomClick } />
    </div>
  )
}


export default Homepage;
