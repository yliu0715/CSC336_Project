import React from 'react';
import Room from '../Room/Room';

const ListOfRooms = (props) => {
  if (props.users) {
    let rooms = props.users.map(user => {
      return <Room {...props}
                   key={user.id}
                   name={user.name}
                   title={user.company.catchPhrase}
                   body={user.company.bs}
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
  return null;
}

export default ListOfRooms;
