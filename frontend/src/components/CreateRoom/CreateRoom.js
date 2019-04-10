import React, { Component } from 'react';
import  './CreateRoom.css';

class CreateRoom extends Component {
  constructor(props) {
    super(props);
    this.state = {
      rname: "",
	  loc: "",
      desc: "",
      skills: []
    }
  }

  onNameChange = (event) => {this.setState({rname: event.target.value})};
  onLocChange = (event) => {this.setState({loc: event.target.value})};
  onDescChange = (event) => {this.setState({desc: event.target.value})};
  onSkillsChange = (event) => {this.setState({skills: event.target.value})};
  onCreate = (event) => {
    event.preventDefault();
    fetch('http://localhost:5000/user/create', {
      method: 'post',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        name: this.state.rname,
        location: this.state.loc,
		description: this.state.desc,
		skills: (this.state.skills).split(" ")
      })
    }).then(resp => resp.json())
      .then(data => {
        const message = data.msg;
        if(message === 'Created Room') {
          this.props.onCreateRoom();
          this.props.history.push('/');
        }
        else alert(message);
      })
      .catch(err => console.log(err));
  }

  render() {
    return(
		<div className="container">
        <div className="form-bg">
          <form>
            <h2 className="text-center">Create Room</h2>
            <div className="form-group">
              <label>Room Name</label>
              <input type="text" className="form-control" placeholder="Enter RoomName" onChange={this.onNameChange}/>
            </div>
			<div className="form-group">
              <label>Location</label>
              <input type="text" className="form-control" placeholder="Enter Location" onChange={this.onLocChange}/>
            </div>
            <div className="form-group">
              <label>Description</label>
              <input type="text" className="form-control" placeholder="Enter Description" onChange={this.onDescChange}/>
            </div>
			<div className="form-group">
              <label>Skills</label>
              <input type="text" className="form-control" placeholder="Enter Skills separated by space" onChange={this.onSkillsChange}/>
            </div>
            <div className="text-center mt-3">
              <button onClick={this.onCreate} type="submit" className="btn btn-primary btn-block">Create</button>
            </div>
          </form>
        </div>
      </div>
	)
  }
}

export default CreateRoom;