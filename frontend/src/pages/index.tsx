import Head from 'next/head';
import React from 'react';

const Home = () => {
  return (
    <>
      <Head>
        <title>Home</title>
      </Head>
      <div>
        <div className="flex flex-col items-center justify-center min-h-screen py-2">
          <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
            <h1 className="text-6xl font-bold">Welcome to Next.js!</h1>
            <p className="mt-3 text-2xl">
              Get started by editing{' '}
              <code className="p-3 font-mono text-lg bg-gray-100 rounded-md">
                pages/index.tsx
              </code>
            </p>
          </main>
      </div>
      </div>
    </>
  );
};

export default Home;