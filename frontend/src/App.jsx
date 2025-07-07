import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Container } from 'react-bootstrap';
import Header from './components/Header.jsx';
import Login from './components/Login.jsx';
import Posts from './components/Posts.jsx';
import Post from './components/Post.jsx';
import CreatePost from './components/CreatePost.jsx';
import EditPost from './components/EditPost.jsx';

function App() {
  const token = localStorage.getItem('token');

  if (!token) {
    return <Login />;
  }

  return (
    <Router>
      <Header />
      <main className="py-3">
        <Container>
          <Routes>
            <Route path="/" element={<Posts />} />
            <Route path="/login" element={<Login />} />
            <Route path="/posts/:id" element={<Post />} />
            <Route path="/create" element={<CreatePost />} />
            <Route path="/edit/:id" element={<EditPost />} />
          </Routes>
        </Container>
      </main>
    </Router>
  );
}

export default App;