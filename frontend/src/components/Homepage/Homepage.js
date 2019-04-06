import React from 'react';

import ListOfRooms from '../ListOfRooms/ListOfRooms';

const Homepage = (props) => {
  return (
    <div>
      <ListOfRooms users={props.users} />
    </div>
  )
}


export default Homepage;
