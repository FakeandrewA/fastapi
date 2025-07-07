import React, { useState, useEffect } from 'react';
import { getPost } from '../api';
import { useParams, Link } from 'react-router-dom';
import { Card, Button } from 'react-bootstrap';

const Post = () => {
  const [post, setPost] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    const fetchPost = async () => {
      try {
        const response = await getPost(id);
        setPost(response.data);
      } catch (error) {
        console.error('Error fetching post:', error);
      }
    };
    fetchPost();
  }, [id]);

  if (!post) {
    return <div>Loading...</div>;
  }

  return (
    <>
      <Link className="btn btn-light my-3" to="/">
        Go Back
      </Link>
      <Card>
        <Card.Body>
          <Card.Title>{post.Post.title}</Card.Title>
          <Card.Text>{post.Post.content}</Card.Text>
          <Card.Text>Votes: {post.votes}</Card.Text>
        </Card.Body>
      </Card>
    </>
  );
};

export default Post;
