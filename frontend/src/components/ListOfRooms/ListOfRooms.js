import React from 'react';
import Room from '../Room/Room';

const ListOfRooms = (props) => {
  if (props.users) {
    let rooms = props.users.map(user => {
      return <Room {...props}
                   key={user.user_id}
                   name={user.username}
                   title={user.room_name}
                   body={user.description}
                   onRoomClick={props.onRoomClick}
                   user={user}
                    />
    })
    return (
      <div>
        {rooms}
      </div>
    )
  }
  return <div>Loading...</div>;
}

export default ListOfRooms;
