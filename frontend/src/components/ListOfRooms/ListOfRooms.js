import React from 'react';
import Room from '../Room/Room';

const ListOfRooms = (props) => {
  if (props.users) {
    return (
      <div>
        {
          props.users.map(user => {
            return <Room key={user.id} name={user.name} title={user.company.catchPhrase} body={user.company.bs} />
          })
        }
      </div>
    )
  }
  return null;
}

export default ListOfRooms;
