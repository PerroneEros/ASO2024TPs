import { axiosInstance } from './axiosInstance';

export const getVehiculos = async () => {
  const res = await axiosInstance.get('/vehiculos');
  return res.data;
};
