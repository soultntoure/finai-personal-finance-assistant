import React from 'react';
import Head from 'next/head';
import Link from 'next/link';

const BudgetingPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <Head>
        <title>FinAI - Budgeting</title>
      </Head>

      <header className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800">Budgeting</h1>
        <Link href="/dashboard" className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Back to Dashboard
        </Link>
      </header>

      <section className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-2xl font-semibold mb-4">Your Budgets</h2>
        <p className="mb-4">View and manage your personalized budgets.</p>
        {/* Placeholder for budget list/table */}
        <div className="bg-gray-200 h-64 flex items-center justify-center text-gray-500">Budget List Placeholder</div>

        <h3 className="text-xl font-semibold mt-6 mb-3">AI Budget Recommendations</h3>
        <p className="mb-4">Get smart budget suggestions tailored to your spending habits.</p>
        {/* Placeholder for AI recommendations display */}
        <div className="bg-gray-200 h-32 flex items-center justify-center text-gray-500">Recommendation Display Placeholder</div>
      </section>
    </div>
  );
};

export default BudgetingPage;
