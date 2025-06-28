import React from 'react';
import Head from 'next/head';
import Link from 'next/link';

const SavingsPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <Head>
        <title>FinAI - Savings Goals</title>
      </Head>

      <header className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800">Savings Goals</h1>
        <Link href="/dashboard" className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Back to Dashboard
        </Link>
      </header>

      <section className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-2xl font-semibold mb-4">Your Savings Goals</h2>
        <p className="mb-4">Track your progress towards your financial savings goals.</p>
        {/* Placeholder for savings goals list */}
        <div className="bg-gray-200 h-64 flex items-center justify-center text-gray-500">Savings Goals List Placeholder</div>

        <h3 className="text-xl font-semibold mt-6 mb-3">Automated Savings Suggestions</h3>
        <p className="mb-4">FinAI helps you identify optimal amounts to save.</p>
        {/* Placeholder for AI savings suggestions */}
        <div className="bg-gray-200 h-32 flex items-center justify-center text-gray-500">Savings Suggestions Placeholder</div>
      </section>
    </div>
  );
};

export default SavingsPage;
