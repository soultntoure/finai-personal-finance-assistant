#!/bin/bash

# This script helps set up local development environment variables.
# It's a placeholder for more sophisticated setup or for guidance.

echo "Copying .env.example files to .env..."

cp .env.example .env
cp backend/.env.example backend/.env
cp ml_service/.env.example ml_service/.env
cp frontend/.env.example frontend/.env

echo "Please edit the newly created .env files with your actual credentials and secrets."
