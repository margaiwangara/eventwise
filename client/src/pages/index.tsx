import { buildClient } from '@/lib/request';
import { NextPageContext } from 'next';

export default function Homepage(props) {
  return <div>{props?.currentUser ? 'signed in' : 'signed out'}</div>;
}

Homepage.getInitialProps = async ({ req }: NextPageContext) => {
  try {
    const data = await buildClient({
      req,
      serverUrl: `${process.env.INGRESS_NGINX_BASE_PATH}/api/auth/current-user`,
      clientUrl: '/api/auth/current-user',
      method: 'get',
    });

    return {
      currentUser: data,
    };
  } catch (error) {
    return {
      currentUser: null,
    };
  }
};
