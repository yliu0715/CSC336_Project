import React from 'react';

import './Room.css';

const Room = (props) => {
  return (
    <div className="text-center">
      <button className="roomButton">
        <div>
          <h2>{`Room Name: ${props.title}`}</h2>
          <h3>{`Creator: ${props.id}`}</h3>
          <h4>{`Description: ${props.body}`}</h4>
        </div>
      </button>
    </div>
  )
}

export default Room;
