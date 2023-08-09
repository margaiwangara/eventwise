import axios, { Method, AxiosRequestConfig } from 'axios';
import { NextPageContext } from 'next';

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
      .catch((error) => reject(error?.response?.data));
  });
}

type BuildClientProps = {
  clientUrl: string;
  serverUrl: string;
  method: Method;
  data?: any;
} & Pick<NextPageContext, 'req'>;

export async function buildClient({
  req,
  clientUrl,
  serverUrl,
  method,
  data: requestData,
}: BuildClientProps) {
  if (typeof window === 'undefined') {
    const data = await apiRequest(method, serverUrl, requestData, {
      headers: req.headers,
    });

    return data;
  } else {
    const data = await apiRequest(method, clientUrl, requestData);

    return data;
  }
}
