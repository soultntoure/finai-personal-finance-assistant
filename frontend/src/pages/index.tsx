import React from 'react';
import Head from 'next/head';
import Link from 'next/link';

const HomePage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <Head>
        <title>FinAI - Your Personalized Financial Brain</title>
        <meta name="description" content="AI-powered personal finance assistant" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
        <h1 className="text-6xl font-bold text-gray-800 mb-4">
          Welcome to <span className="text-blue-600">FinAI</span>
        </h1>

        <p className="mt-3 text-2xl text-gray-600">
          Your revolutionary AI-powered personal finance assistant.
        </p>

        <div className="flex flex-wrap items-center justify-around mt-6 sm:w-full">
          <Link href="/auth/login" className="p-6 mt-6 text-left border rounded-xl hover:text-blue-600 focus:text-blue-600 bg-white shadow-md">
              <h3 className="text-2xl font-bold">Login &rarr;</h3>
              <p className="mt-4 text-xl">Access your personalized financial dashboard.</p>
          </Link>

          <Link href="/auth/signup" className="p-6 mt-6 text-left border rounded-xl hover:text-blue-600 focus:text-blue-600 bg-white shadow-md">
              <h3 className="text-2xl font-bold">Sign Up &rarr;</h3>
              <p className="mt-4 text-xl">Start your journey to financial freedom.</p>
          </Link>
        </div>
      </main>

      <footer className="w-full h-24 flex items-center justify-center border-t">
        <a
          className="flex items-center justify-center gap-2"
          href="https://finai.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by FinAI
        </a>
      </footer>
    </div>
  );
};

export default HomePage;
