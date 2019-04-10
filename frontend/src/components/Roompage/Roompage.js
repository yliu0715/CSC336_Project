import React, { Component } from 'react';
import './Roompage.css'

class Roompage extends Component {
  render() {
    return (
      <div className="room-detail">
  		<h1 className="heading">{this.props.room.company.catchPhrase}</h1>
  		<div className="room-info">
  			<div className="row align-top">
  				<div className="col-sm-6">
  					<h3>Owner</h3>
  					<p>{this.props.room.name}</p>
  					<h3>Location</h3>
  					<p>{this.props.room.address.city}</p>
  				</div>
  				<div className="col-sm-6">
  					<table className="table table-hover table-dark">
  						<thead>
  							<tr>
  								<th>Username</th>
  							</tr>
  						</thead>
  						<tbody>
  							<tr>
  								<td>A User</td>
  							</tr>
  							<tr>
  								<td>Another User</td>
  							</tr>
  							<tr>
  								<td>One More</td>
  							</tr>
  						</tbody>
  					</table>
  				</div>
  			</div>
  			<h3>Description</h3>
  			<p>{this.props.room.company.bs}</p>
  			<h3>Required Skills</h3>
  			<div className="d-inline-flex flex-nowrap">
  				<div className="p-2 border align-middle">React</div>
  				<div className="p-2 border">Python</div>
  				<div className="p-2 border">SQL</div>
  			</div>
  			<br/>
  			<button className="join btn-light btn-lg">Request Join</button>
  		</div>
      </div>
    )
  }
}

export default Roompage;
