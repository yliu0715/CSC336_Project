import React, {Component} from 'react';
import { Link } from 'react-router-dom';

class Navbar extends Component {

constructor(props){
  super (props);
  this.state = {
    room: ''
  }
}

  onSeachBar = (event) => {
    this.setState({room: event.target.value});
  };

  onSearch = (event) => {
    const { room } = this.state;
    event.preventDefault();
    console.log(room);

    fetch(`http://localhost:5000/rooms/${this.state.room}`, {
      method: 'post',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        room: this.state.room,
      })
    }).then(resp => resp.json())
      .then(data => {
        const message = data.msg;
        if(message === 'Search complete') {
          this.props.onRegisterChange();
          this.props.history.push('/');
        }
        else alert(message);
      })
      .catch(err => console.log(err));
  }

  render(){
  return (
    this.props.authenticated ?
      <div>
        <nav className="navbar navbar-expand-sm bg-dark navbar-dark">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home</Link>
            </li>
            </ul>
            <ul className="navbar-nav mr-auto">
            <li className="nav-item">
            <form>
              <input type="text" className="form-control" placeholder="Search Rooms" onChange={this.onSearchBar}/>
              <button onClick={this.onSearch} type="submit" className="btn btn-primary">Go</button>
              </form>
            </li>
          </ul>
          <ul className="navbar-nav">
            <li className="nav-item dropdown">
              <div className="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown" style={{cursor: 'pointer'}}>My Account</div>
              <div className="dropdown-menu">
                <Link className="dropdown-item" to="/profile">My Profile</Link>
                <Link className="dropdown-item" to="#">My Rooms</Link>
                <a href="/" className="dropdown-item" onClick={this.props.onLogOut}>Logout</a>
              </div>
            </li>
          </ul>
        </nav>
      </div>
    :
      <div>
        <nav className="navbar navbar-expand-sm bg-dark navbar-dark">
          <ul className="navbar-nav mr-auto">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home</Link>
            </li>
          </ul>
          <ul className="navbar-nav">
            <li className="nav-item">
              <Link className="nav-link" to="/Login">Login</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/Register">Register</Link>
            </li>
          </ul>
        </nav>
      </div>
  )
}
}
export default Navbar;
