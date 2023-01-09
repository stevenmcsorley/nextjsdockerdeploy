import os

def create_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def create_file(file_name, content=''):
    with open(file_name, 'w') as f:
        f.write(content)

# Create frontend directory
create_dir('frontend/src/components')
create_dir('frontend/src/pages')
create_dir('frontend/src/styles')

# Create .env file in the root directory
create_file('.env', 'APP_ENV=development\nAPP_DEBUG=0\n')

# Create frontend files with setup code
create_file('frontend/.env', 'NEXT_PUBLIC_API_URL=http://localhost:3001')
# Create frontend package.json file with TypeScript dependencies

create_file('frontend/package.json', '{\n  "dependencies": {\n    "next": "latest",\n    "react": "latest",\n    "react-dom": "latest"\n  },\n  "devDependencies": {\n    "@types/react": "latest",\n    "@types/node": "latest",\n    "typescript": "latest",\n    "@testing-library/jest-dom": "latest",\n    "@testing-library/react": "latest",\n    "@testing-library/user-event": "latest"\n  },\n  "scripts": {\n    "test": "jest",\n    "dev": "next",\n    "build": "next build",\n    "start": "next start"\n  }\n}')
# Create frontend tsconfig.json file
create_file('frontend/tsconfig.json', '{\n  "compilerOptions": {\n    "target": "esnext",\n    "module": "commonjs",\n    "jsx": "preserve",\n    "strict": true,\n    "esModuleInterop": true,\n    "forceConsistentCasingInFileNames": true\n  },\n  "include": ["src"]\n}')
# Create frontend next.config.js file
next_config = """
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  output: 'standalone',
  webpack: (config, _) => ({
    ...config,
    watchOptions: {
      ...config.watchOptions,
      poll: 800,
      aggregateTimeout: 300,
    },
  }),
}

module.exports = nextConfig
"""
create_file('frontend/next.config.js', next_config)
# Create frontend Dockerfile.development
create_file('frontend/Dockerfile.development',
            'FROM node:lts\n\nENV APP_ENV=development\n\nWORKDIR /app\n\nCOPY package*.json .\n\nRUN npm install\n\nCOPY . .\n\nEXPOSE 3000\n\nCMD ["npm", "run", "dev"]')
# Create frontend Dockerfile.production
create_file('frontend/Dockerfile.production',
            'FROM node:lts\n\nENV APP_ENV=production\n\nWORKDIR /app\n\nCOPY package*.json .\n\nRUN npm install\n\nCOPY . .\n\nRUN npm run build\n\nEXPOSE 3000\n\nCMD ["npm", "run", "start"]')
# Create frontend src/pages/index.tsx file
create_file('frontend/src/pages/index.tsx', 'import { NextPage } from \'next\';\nimport Head from \'next/head\';\nimport React from \'react\';\n\nconst Home: NextPage = () => {\n  return (\n    <div>\n      <Head>\n        <title>My App</title>\n      </Head>\n      <p>Hello, world!</p>\n    </div>\n  );\n};\n\nexport default Home;')
# Create docker-compose.yml file
docker_compose = """
version: '3'
services:
  nextjs:
    build:
      context: ./frontend
      dockerfile: Dockerfile.${APP_ENV}
    environment:
      - APP_ENV=${APP_ENV}
    volumes:
      - ./frontend:/app
    ports:
      - "3000:3000"
    command: npm run dev
"""
create_file('docker-compose.yml', docker_compose)
create_file('README.md', '# My App\n\nThis is my app.')

# Run npm install in the frontend directory
os.chdir('frontend')
os.system('npm install')

# Start the frontend application using docker-compose
os.chdir('..')
os.system('docker-compose up')