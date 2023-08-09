import { useMount } from 'react-use';
import { useRouter } from 'next/router';

import { apiRequest } from '@/lib/request';

export default function LogOut() {
  const router = useRouter();

  const logOut = async () => {
    try {
      await apiRequest('get', '/api/auth/logout');
      router.replace('/auth/login');
    } catch (error) {
      console.log('Error: Failed to log out', error);
      router.replace('/');
    }
  };

  useMount(() => logOut());

  return (
    <div>
      <h6>Logging you out...</h6>
    </div>
  );
}
