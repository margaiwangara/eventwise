import axios, { Method, AxiosRequestConfig } from 'axios';

export function apiRequest(
  method: Method,
  url: string,
  data?: any,
  config?: AxiosRequestConfig,
) {
  return new Promise((resolve, reject) => {
    return axios({
      method,
      url,
      data,
      withCredentials: true,
      ...config,
    })
      .then((res) => resolve(res.data))
      .catch((error) => reject(error.response.data));
  });
}
