import axios from 'axios';

const API_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const login = async (username, password) => {
  const formData = new FormData();
  formData.append('username', username);
  formData.append('password', password);
  const response = await api.post('/login', formData);
  if (response.data.access_token) {
    localStorage.setItem('token', response.data.access_token);
  }
  return response.data;
};

export const getPosts = async () => {
  return await api.get('/posts');
};

export const getPost = async (id) => {
  return await api.get(`/posts/${id}`);
};

export const createPost = async (post) => {
  return await api.post('/posts', post);
};

export const updatePost = async (id, post) => {
  return await api.put(`/posts/${id}`, post);
};

export const deletePost = async (id) => {
  return await api.delete(`/posts/${id}`);
};
