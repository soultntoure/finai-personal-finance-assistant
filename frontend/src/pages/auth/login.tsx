import React, { useState } from 'react';
import Head from 'next/head';
import Link from 'next/link';
import { useRouter } from 'next/router';
import axios from 'axios';

const LoginPage: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      const response = await axios.post(`${process.env.NEXT_PUBLIC_API_BASE_URL}/auth/token`, 
        new URLSearchParams({
          username: email,
          password: password,
        }).toString(),
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        }
      );
      localStorage.setItem('accessToken', response.data.access_token);
      router.push('/dashboard');
    } catch (err) {
      if (axios.isAxiosError(err) && err.response) {
        setError(err.response.data.detail || 'Login failed. Please check your credentials.');
      } else {
        setError('An unexpected error occurred.');
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <Head>
        <title>FinAI - Login</title>
      </Head>

      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h2 className="text-3xl font-bold text-center text-gray-800 mb-6">Login to FinAI</h2>
        {error && <p className="text-red-500 text-center mb-4">{error}</p>}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="email" className="block text-gray-700 text-sm font-bold mb-2">Email:</label>
            <input
              type="email"
              id="email"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="mb-6">
            <label htmlFor="password" className="block text-gray-700 text-sm font-bold mb-2">Password:</label>
            <input
              type="password"
              id="password"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <div className="flex items-center justify-between">
            <button
              type="submit"
              className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
              Sign In
            </button>
            <Link href="/auth/signup" className="inline-block align-baseline font-bold text-sm text-blue-600 hover:text-blue-800">
                Don't have an account? Sign Up
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
