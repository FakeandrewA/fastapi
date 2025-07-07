import React, { useState, useEffect } from 'react';
import { getPosts, deletePost } from '../api';
import { Link } from 'react-router-dom';
import { Card, Button, Row, Col } from 'react-bootstrap';

const Posts = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await getPosts();
        setPosts(response.data);
      } catch (error) {
        console.error('Error fetching posts:', error);
      }
    };
    fetchPosts();
  }, []);

  const handleDelete = async (id) => {
    if (window.confirm('Are you sure you want to delete this post?')) {
      try {
        await deletePost(id);
        setPosts(posts.filter((post) => post.Post.id !== id));
      } catch (error) {
        console.error('Error deleting post:', error);
      }
    }
  };

  return (
    <>
      <Row className="align-items-center">
        <Col>
          <h1>Latest Posts</h1>
        </Col>
        <Col className="text-end">
          <Link to="/create" className="btn btn-primary my-3">
            <i className="fas fa-plus"></i> Create Post
          </Link>
        </Col>
      </Row>
      <Row>
        {posts.map((post) => (
          <Col key={post.Post.id} sm={12} md={6} lg={4} xl={3}>
            <Card className="my-3 p-3 rounded">
              <Link to={`/posts/${post.Post.id}`}>
                <Card.Title as="div">
                  <strong>{post.Post.title}</strong>
                </Card.Title>
              </Link>
              <Card.Text as="p">{post.Post.content}</Card.Text>
              <Card.Text as="p">Votes: {post.votes}</Card.Text>
              <Row>
                <Col>
                  <Link
                    to={`/edit/${post.Post.id}`}
                    className="btn btn-sm btn-light"
                  >
                    <i className="fas fa-edit"></i> Edit
                  </Link>
                </Col>
                <Col>
                  <Button
                    variant="danger"
                    className="btn-sm"
                    onClick={() => handleDelete(post.Post.id)}
                  >
                    <i className="fas fa-trash"></i> Delete
                  </Button>
                </Col>
              </Row>
            </Card>
          </Col>
        ))}
      </Row>
    </>
  );
};

export default Posts;
