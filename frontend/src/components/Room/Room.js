import React from 'react';

import './Room.css';

const Room = (props) => {
  const click = () => {
    props.onRoomClick(props.user);
    props.history.push('/roompage');
  }
  return (
    <div className="text-center roomButton" onClick={() => {click()}}>
          <h2>{`Room Name: ${props.title}`}</h2>
          <h3>{`Creator: ${props.name}`}</h3>
          <h4>{`Description: ${props.body}`}</h4>
    </div>
  )
}

export default Room;
