import React from 'react';
//import logo from './logo.svg';
import './App.css';
import axios from 'axios'
class AppMain extends React.Component {
constructor(props) {
super(props)
this.state = {
'Project': []
}

}
render () {
return (
<div>
Main App
</div>
)
}
}

componentDidMount() {
  axios.get('http://127.0.0.1:8000/api/authors')
  .then(response => {
  
    const project = response.data
  this.setState(
  {
  'Project': Project
  }
  )
  }).catch(error => console.log(error))
  }
  render () {
  return (
  <div>
  < <PROJECT name={this.state.name} />
  </div>
  )
  }
  }
 
  
export default AppMain;
