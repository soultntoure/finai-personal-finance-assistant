/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Add any specific Next.js configurations here
  // For example, if you need to configure images or internationalization
  images: {
    domains: [], // Add domains for external images if any
  },
  env: {
    NEXT_PUBLIC_API_BASE_URL: process.env.NEXT_PUBLIC_API_BASE_URL,
    // Add other public environment variables here
  },
};

module.exports = nextConfig;
