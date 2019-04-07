import React from 'react';
import Room from '../Room/Room';

const ListOfRooms = (props) => {
  if (props.users) {
    return (
      <div>
        {
          props.users.map(user => {
            return <Room id={user.id} title={user.title} body={user.body} />
          })
        }
      </div>
    )
  }
  return null;
}

export default ListOfRooms;
