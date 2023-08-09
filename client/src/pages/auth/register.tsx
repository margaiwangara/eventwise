import { useState } from 'react';
import { apiRequest } from '@lib/request';
import CustomAlert from '@components/CustomAlert';
import { useRouter } from 'next/router';

export default function Register() {
  const [values, setValues] = useState({
    name: '',
    email: '',
    password: '',
  });
  const [errors, setErrors] = useState<string | string[]>('');

  const router = useRouter();

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) =>
    setValues((prev) => ({ ...prev, [e.target.name]: e.target.value }));

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      await apiRequest('post', '/api/auth/register', values);
      setErrors('');
      router.push('/');
    } catch (error) {
      setErrors(
        Array.isArray(error.detail)
          ? error?.detail?.map((err) => err.msg)
          : error?.detail,
      );
    }
  };

  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-md-6 offset-md-3">
          <div className="card">
            <div className="card-body">
              <form onSubmit={onSubmit}>
                <h3>Register</h3>
                {errors && <CustomAlert type="danger" data={errors} />}
                <div className="form-group">
                  <label htmlFor="name">Name</label>
                  <input
                    type="text"
                    className="form-control"
                    id="name"
                    name="name"
                    value={values.name}
                    onChange={onChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="email">Email address</label>
                  <input
                    type="email"
                    className="form-control"
                    id="email"
                    name="email"
                    value={values.email}
                    onChange={onChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="password">Password</label>
                  <input
                    type="password"
                    className="form-control"
                    id="password"
                    name="password"
                    value={values.password}
                    onChange={onChange}
                  />
                </div>
                <button className="btn btn-primary mt-2">Submit</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
