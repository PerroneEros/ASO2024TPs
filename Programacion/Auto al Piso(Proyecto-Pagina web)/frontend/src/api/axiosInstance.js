import axios from 'axios';

const API = import.meta.env.VITE_API_URL;

export const axiosInstance = axios.create({
  baseURL: API,
});
