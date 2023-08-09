import 'bootstrap/dist/css/bootstrap.css';

import { buildClient } from '@lib/request';

import { AppProps, AppContext } from 'next/app';

export default function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}

MyApp.getInitialProps = async ({ ctx, Component }: AppContext) => {
  const { req } = ctx;
  let pageProps;

  try {
    const data = await buildClient({
      req,
      serverUrl: `${process.env.INGRESS_NGINX_BASE_PATH}/api/auth/current-user`,
      clientUrl: '/api/auth/current-user',
      method: 'get',
    });

    if (Component.getInitialProps) {
      pageProps = await Component.getInitialProps(ctx);
    }

    return {
      pageProps: {
        ...pageProps,
        currentUser: data,
      },
    };
  } catch (error) {
    return {
      currentUser: null,
    };
  }
};
