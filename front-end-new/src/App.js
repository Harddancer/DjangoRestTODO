
import React from 'react';
import './App.css';
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import TodoList from './components/Todo.js'
import LoginForm from './components/LoginForm.js'
import axios from 'axios'
import { Route, BrowserRouter, Routes, Link, useLocation } from 'react-router-dom'

const NotFound404 = () => {
  var { pathname } = useLocation()

  return (
    <div>
      Страница по адресу "{pathname}" не найдена
    </div>
  )
}

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todos': [],
      'token':''
    }
  }

  obtainAuthToken(login, password) {
    axios
        .post('http://127.0.0.1:8000/api-auth-token/', {
            'username': login,
            'password': password
        })
        .then(response => {
            const token = response.data.token
            console.log('token:', token)
            localStorage.setItem('token', token)
            this.setState({
                'token': token
            }, this.getData)
        })
        .catch(error => console.log(error))
}

isAuth() {
    return !!this.state.token
}





componentDidMount() {
  let token = localStorage.getItem('token')
  this.setState({
      'token': token
  }, this.getData)
}
getHeaders() {
  if (this.isAuth()) {
      return {
          'Authorization': 'Token ' + this.state.token
      }
  }
  return {}
}
getData() {
  let headers = this.getHeaders()

    axios.get('http://127.0.0.1:8000/api/project/',{headers})
      .then(response => {
        const projects = response.data
        this.setState(
          {
            'projects': projects
          }
        )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/todo/',)
      .then(response => {
        const todos = response.data
        this.setState(
          {
            'todos': todos
          }
        )
      }).catch(error => console.log(error))
  }
  logOut() {
    localStorage.setItem('token', '')
    this.setState({
        'token': '',
    }, this.getData)
}

  render() {
    return (
      <div className="App">
        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to='/'>Users</Link>
              </li>
              <li>
                <Link to='/project'>Project</Link>
              </li>
              <li>
                <Link to='/todo'>Todo</Link>
              </li>
              <li>
                <Link to='/login'>logi  <li>
                        {this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                        </li>n</Link>
              </li>
              <li>
                {this.isAuth() ? <button onClick={() => this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
              </li>
            </ul>
          </nav>
          <Routes>
            <Route exact path='/' element={<UserList users={this.state.users} />} />
            <Route exact path='/project' element={<ProjectList projects={this.state.projects} />} />
            <Route exact path='/todo' element={<TodoList todos={this.state.todos} />} />
            <Route exact path='/login' element={<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)} />} />
            <Route path='/users'/>
            <Route path='*' element={<NotFound404 />} />
          </Routes>
        </BrowserRouter>
      </div>
    )
  }
}


export default App;