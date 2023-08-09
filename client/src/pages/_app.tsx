import 'bootstrap/dist/css/bootstrap.css';

import { buildClient } from '@lib/request';
import Header from '@components/header';

import { AppProps, AppContext } from 'next/app';
import { UserProps } from '@/app-types/user';

export default function MyApp({ Component, pageProps }: AppProps) {
  const { currentUser } = pageProps as { currentUser: UserProps };

  return (
    <main>
      <Header currentUser={currentUser} />
      <Component {...pageProps} />
    </main>
  );
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
      pageProps: {
        currentUser: null,
      },
    };
  }
};
