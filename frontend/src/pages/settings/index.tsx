import React from 'react';
import Head from 'next/head';
import Link from 'next/link';

const SettingsPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <Head>
        <title>FinAI - Settings</title>
      </Head>

      <header className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold text-gray-800">Settings</h1>
        <Link href="/dashboard" className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Back to Dashboard
        </Link>
      </header>

      <section className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-2xl font-semibold mb-4">Account Settings</h2>
        <p className="mb-4">Manage your profile, preferences, and connected accounts.</p>
        {/* Placeholder for various settings sections */}
        <ul className="list-disc list-inside text-gray-700">
          <li>Profile Information (Email, Name)</li>
          <li>Change Password</li>
          <li>Connected Bank Accounts (Plaid Integration)</li>
          <li>Notification Preferences</li>
          <li>Data Privacy</li>
        </ul>
      </section>
    </div>
  );
};

export default SettingsPage;
