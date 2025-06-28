import React, { useEffect, useState } from 'react';
import Head from 'next/head';
import { useRouter } from 'next/router';
import axios from 'axios';

interface UserProfile {
  id: number;
  email: string;
  created_at: string;
}

const DashboardPage: React.FC = () => {
  const router = useRouter();
  const [user, setUser] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchUser = async () => {
      const token = localStorage.getItem('accessToken');
      if (!token) {
        router.replace('/auth/login');
        return;
      }
      try {
        const response = await axios.get<UserProfile>(
          `${process.env.NEXT_PUBLIC_API_BASE_URL}/users/me`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );
        setUser(response.data);
      } catch (err) {
        console.error('Failed to fetch user:', err);
        setError('Failed to load user data. Please log in again.');
        localStorage.removeItem('accessToken'); // Invalidate token
        router.replace('/auth/login');
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, [router]);

  const handleLogout = () => {
    localStorage.removeItem('accessToken');
    router.push('/auth/login');
  };

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center">Loading dashboard...</div>;
  }

  if (error) {
    return <div className="min-h-screen flex items-center justify-center text-red-500">Error: {error}</div>;
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <Head>
        <title>FinAI - Dashboard</title>
      </Head>

      <header className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800">Welcome, {user?.email}!</h1>
        <button
          onClick={handleLogout}
          className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded"
        >
          Logout
        </button>
      </header>

      <nav className="mb-8">
        <ul className="flex space-x-4">
          <li><Link href="/dashboard" className="text-blue-600 hover:underline">Dashboard</Link></li>
          <li><Link href="/budgeting" className="text-blue-600 hover:underline">Budgeting</Link></li>
          <li><Link href="/savings" className="text-blue-600 hover:underline">Savings</Link></li>
          <li><Link href="/investments" className="text-blue-600 hover:underline">Investments</Link></li>
          <li><Link href="/goals" className="text-blue-600 hover:underline">Goals</Link></li>
          <li><Link href="/settings" className="text-blue-600 hover:underline">Settings</Link></li>
        </ul>
      </nav>

      <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-2xl font-semibold mb-4">Financial Overview</h2>
          <p>Display aggregated account balances, net worth trends.</p>
          {/* Placeholder for a chart component */}
          <div className="bg-gray-200 h-40 flex items-center justify-center text-gray-500">Chart Placeholder</div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-2xl font-semibold mb-4">Recent Transactions</h2>
          <p>List of latest categorized transactions.</p>
          {/* Placeholder for a table component */}
          <div className="bg-gray-200 h-40 flex items-center justify-center text-gray-500">Transactions Table Placeholder</div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-2xl font-semibold mb-4">AI Insights</h2>
          <p>Budget recommendations, savings suggestions, investment tips.</p>
          {/* Placeholder for AI insights/recommendations */}
          <div className="bg-gray-200 h-40 flex items-center justify-center text-gray-500">AI Insights Placeholder</div>
        </div>
      </section>
    </div>
  );
};

export default DashboardPage;
