import React from 'react';
import Navbar from '../Navbar/Navbar';
import './Homepage.css'


const Homepage = () => {

  return (
    <div className="text-center">
      <Navbar/>
      <br/>
      <br/>
      <br/>
      <button className="roomButton">Room 1</button>
      <br/>
      <br/>
      <button className="roomButton">Room 2</button>
      <br/>
      <br/>
      <button className="roomButton">Room 3</button>
      <br/>
      <br/>
      <button className="roomButton">Room 4</button>

    </div>
    
  )
}


export default Homepage;
