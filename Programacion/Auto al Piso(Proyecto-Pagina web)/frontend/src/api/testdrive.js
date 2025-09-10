import { axiosInstance } from './axiosInstance';

export const postTestDrive = async (data) => {
  return axiosInstance.post('/testdrive', data);
};
