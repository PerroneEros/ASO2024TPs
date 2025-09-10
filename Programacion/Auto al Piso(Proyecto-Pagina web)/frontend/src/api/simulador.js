import { axiosInstance } from './axiosInstance';

export const simularFinanciacion = async (data) => {
  const res = await axiosInstance.post('/financiamiento/simular', data);
  return res.data;
};
