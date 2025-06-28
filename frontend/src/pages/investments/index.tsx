import React from 'react';
import Head from 'next/head';
import Link from 'next/link';

const InvestmentsPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <Head>
        <title>FinAI - Investments</title>
      </Head>

      <header className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800">Investment Insights</h1>
        <Link href="/dashboard" className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Back to Dashboard
        </Link>
      </header>

      <section className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-2xl font-semibold mb-4">Your Investment Portfolio</h2>
        <p className="mb-4">View linked investment accounts and performance.</p>
        {/* Placeholder for investment portfolio overview */}
        <div className="bg-gray-200 h-64 flex items-center justify-center text-gray-500">Investment Portfolio Placeholder</div>

        <h3 className="text-xl font-semibold mt-6 mb-3">AI-Driven Investment Recommendations</h3>
        <p className="mb-4">Receive personalized insights for optimizing your investment strategy.</p>
        {/* Placeholder for AI investment tips */}
        <div className="bg-gray-200 h-32 flex items-center justify-center text-gray-500">Investment Recommendations Placeholder</div>
      </section>
    </div>
  );
};

export default InvestmentsPage;
