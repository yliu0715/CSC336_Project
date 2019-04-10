import React from 'react';

import ListOfRooms from '../ListOfRooms/ListOfRooms';

const Homepage = (props) => {
  return (
    <div>
      <ListOfRooms {...props} users={props.users} onRoomClick={ props.onRoomClick } />
    </div>
  )
}


export default Homepage;
