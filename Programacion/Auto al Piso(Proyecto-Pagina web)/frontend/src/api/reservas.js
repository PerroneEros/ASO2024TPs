import { axiosInstance } from './axiosInstance';

export const getReservas = async () => {
  const res = await axiosInstance.get('/reservas');
  return res.data;
};

export const postReserva = async (data) => {
  return axiosInstance.post('/reservas', data);
};
