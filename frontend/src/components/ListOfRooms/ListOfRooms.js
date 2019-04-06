import React from 'react';
import Room from '../Room/Room';

const ListOfRooms = (props) => {
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

export default ListOfRooms;
