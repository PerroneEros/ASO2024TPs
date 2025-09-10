import { axiosInstance } from './axiosInstance';

export const getPromociones = async () => {
  const res = await axiosInstance.get('/promociones');
  return res.data;
};
