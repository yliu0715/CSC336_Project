import React from 'react';

import './Room.css';

const Room = (props) => {
  return (
    <div className="text-center roomButton">
          <h2>{`Room Name: ${props.title}`}</h2>
          <h3>{`Creator: ${props.name}`}</h3>
          <h4>{`Description: ${props.body}`}</h4>
    </div>
  )
}

export default Room;
