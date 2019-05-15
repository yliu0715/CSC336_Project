import React, { Component } from 'react';
import './Roompage.css'

class Roompage extends Component {
	constructor(props) {
		super(props);
		this.state = {
			users: [],
			owner: ""
		}
	}

	componentDidMount() {
		console.log(this.props.room.room_name)
		fetch(`http://localhost:5000/rooms/${this.props.room.room_name}`)
		.then(res => res.json())
		.then(data => {
			var uniqueUsers = new Set()
			data.msg.map(item => {
				if (item.is_owner) this.setState({ owner: item.username })
				uniqueUsers.add(item.username)
			})
			this.setState({ users: [...uniqueUsers] })
		}).then(users => {console.log(this.state.users); console.log(this.state.owner)})
	}
  render() {
		const {users, owner} =  this.state;
    return (
      <div className="room-detail">
  		<h1 className="heading">{this.props.room.room_name}</h1>
  		<div className="room-info">
  			<div className="row align-top">
  				<div className="col-sm-6">
  					<h3>Owner</h3>
  					<p>{owner}</p>
  					<h3>Location</h3>
  					<p>{this.props.room.location}</p>
  				</div>
  				<div className="col-sm-6">
  					<table className="table table-hover table-dark">
  						<thead>
  							<tr>
  								<th>Username</th>
  							</tr>
  						</thead>
  						<tbody>
								{users && users.map(user => {
									if (user === owner) {
										return (<div >
											<th>{user}⭐</th>
											</div>)
									}
									return (<div >
										<th>{user}</th>
										</div>)
								})}
  						</tbody>
  					</table>
  				</div>
  			</div>
  			<h3>Description</h3>
  			<p>{this.props.room.description}</p>
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
