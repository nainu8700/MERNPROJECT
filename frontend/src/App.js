import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import UserForm from './components/UserForm';
import './App.css';

function Home() {
  return <h1>Welcome to the Home Page</h1>;
}

function App() {
  return (
    <Router>
      <div class="topnav">
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/users">Users</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<UserForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;