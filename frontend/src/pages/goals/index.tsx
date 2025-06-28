import React from 'react';
import Head from 'next/head';
import Link from 'next/link';

const GoalsPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <Head>
        <title>FinAI - Financial Goals</title>
      </Head>

      <header className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800">Financial Goals</h1>
        <Link href="/dashboard" className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Back to Dashboard
        </Link>
      </header>

      <section className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-2xl font-semibold mb-4">Your Long-Term Goals</h2>
        <p className="mb-4">Set and track progress for all your financial aspirations (e.g., retirement, debt reduction, down payment).</p>
        {/* Placeholder for goals list */}
        <div className="bg-gray-200 h-64 flex items-center justify-center text-gray-500">Financial Goals List Placeholder</div>
      </section>
    </div>
  );
};

export default GoalsPage;
