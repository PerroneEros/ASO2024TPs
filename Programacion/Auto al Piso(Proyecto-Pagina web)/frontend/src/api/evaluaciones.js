import { axiosInstance } from './axiosInstance';

export const getEvaluaciones = async () => {
  const res = await axiosInstance.get('/evaluacion');
  return res.data;
};

export const postEvaluacion = async (formData) => {
  return axiosInstance.post('/evaluacion', formData);
};
