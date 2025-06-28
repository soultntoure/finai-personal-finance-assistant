import type { AppProps } from 'next/app';
import '../styles/globals.css'; // Global styles for Tailwind CSS

function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}

export default MyApp;
