# AI Finance Assistant (MVP)

## Project Title: FinAI - Your Personalized Financial Brain

## Brief Description

FinAI is a revolutionary AI-powered personal finance assistant designed to automate and optimize your budgeting, savings, and investment strategies. Moving beyond static financial tools, FinAI leverages advanced machine learning to understand your unique spending habits, income patterns, and financial goals. It proactively adjusts your financial plan in real-time, provides integrated insights across all your accounts, and helps you achieve your financial aspirations with minimal manual intervention.

**Key MVP Features:**

*   **Secure Account Aggregation:** Connect to your bank accounts, credit cards, and investment portfolios via Plaid.
*   **Intelligent Transaction Categorization:** Automatically categorize spending and income with AI-driven precision.
*   **Dynamic Budgeting:** Receive personalized budget recommendations that adapt to your actual spending behavior and income fluctuations.
*   **Automated Savings Identification:** FinAI identifies optimal amounts to save based on your financial health and progress towards goals.
*   **Goal-Oriented Planning:** Set and track financial goals (e.g., down payment, debt reduction, retirement), with AI guiding your path.
*   **Basic Investment Insights:** Get AI-driven recommendations on potential investment contributions based on your current financial surplus and long-term goals.
*   **Intuitive Dashboard:** A clear, user-friendly interface to visualize your financial health, track progress, and view AI insights.

## Tech Stack

The FinAI MVP is built using a modern, scalable, and robust tech stack:

*   **Backend:**
    *   **Language:** Python 3.10+
    *   **Web Framework:** FastAPI
    *   **Database ORM:** SQLAlchemy
    *   **Authentication:** JWT
    *   **Task Queue:** Celery with Redis
    *   **External Integrations:** Plaid (Financial Data Aggregation)
*   **AI/Machine Learning Service:**
    *   **Language:** Python 3.10+
    *   **ML Frameworks:** TensorFlow, PyTorch, Scikit-learn
    *   **Serving:** FastAPI
*   **Database:**
    *   **Primary:** PostgreSQL
    *   **Caching/Broker:** Redis
*   **Frontend (Web Application):**
    *   **Framework:** Next.js (React)
    *   **Language:** TypeScript
    *   **Styling:** Tailwind CSS
*   **Deployment & CI/CD:**
    *   **Cloud Provider:** AWS (Fargate, RDS, S3, CloudWatch, etc.)
    *   **CI/CD:** GitHub Actions
*   **Containerization:** Docker, Docker Compose

## Architecture Overview

FinAI operates as a microservices-oriented application, consisting of three primary services:

1.  **Backend Service (FastAPI):** The core API layer handling user authentication, data management (CRUD for users, transactions, budgets, goals), and orchestrating interactions with external services (Plaid) and the ML Service.
2.  **ML Service (FastAPI):** A dedicated service exposing machine learning models via REST APIs. This service is responsible for dynamic budgeting calculations, transaction categorization, behavioral insights, and investment strategy recommendations.
3.  **Frontend Service (Next.js):** The user-facing web application that consumes APIs from the Backend Service to provide an interactive and responsive user experience.

All services are containerized with Docker, enabling consistent local development and scalable deployment on AWS Fargate. PostgreSQL serves as the primary data store, with Redis used for caching and asynchronous task management.

## Setup Instructions

This guide will help you set up FinAI for local development using Docker Compose.

### Prerequisites

*   Docker Desktop installed (includes Docker Engine and Docker Compose)
*   Git
*   A Plaid Developer Account (required for financial data aggregation). You'll need `PLAID_CLIENT_ID`, `PLAID_SECRET`, and `PLAID_ENV` (e.g., `sandbox`).
*   A local `.env` file for sensitive credentials.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/finai.git
cd finai
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory of the project based on `.env.example`. This file will be used by `docker-compose`.

```bash
# .env.example content (copy this to .env and fill in values)

# Database Configuration (PostgreSQL)
POSTGRES_DB=finai_db
POSTGRES_USER=finai_user
POSTGRES_PASSWORD=finai_password
DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}

# Backend Service Configuration
BACKEND_SECRET_KEY="YOUR_SUPER_SECRET_KEY_FOR_JWT_SIGNING"
# Ex: http://localhost:3000, for CORS
BACKEND_CORS_ORIGINS="http://localhost:3000"
BACKEND_PLAI_ENV=sandbox # sandbox, development, production
BACKEND_PLAID_CLIENT_ID="YOUR_PLAID_CLIENT_ID"
BACKEND_PLAID_SECRET="YOUR_PLAID_SECRET"
BACKEND_ML_SERVICE_URL=http://ml_service:8001

# ML Service Configuration (if needed)
ML_SERVICE_SECRET_KEY="ANOTHER_SECRET_KEY" # For internal ML API calls if secured

# Frontend Configuration
NEXT_PUBLIC_API_BASE_URL="http://localhost:8000/api/v1" # Or your backend service URL
# Add any other frontend specific env vars here
```

**Important:** Replace placeholder values (e.g., `YOUR_SUPER_SECRET_KEY_FOR_JWT_SIGNING`, Plaid credentials) with actual secure values. For local development, simpler values are fine, but for production, use strong, randomly generated secrets managed by a service like AWS Secrets Manager.

### 3. Build and Run Services with Docker Compose

From the root of the project, run:

```bash
docker-compose up --build -d
```

This command will:
*   Build Docker images for the `backend`, `ml_service`, and `frontend`.
*   Start all services, including `db` (PostgreSQL) and `redis` (for Celery and caching).
*   The `-d` flag runs the containers in detached mode (in the background).

Wait for all services to start. You can check their status with `docker-compose ps`.

### 4. Database Migrations

Once the `db` and `backend` services are up, run database migrations to set up the schema:

```bash
docker-compose exec backend alembic upgrade head
```

### 5. Access the Application

*   **Frontend (Web UI):** Open your browser and navigate to `http://localhost:3000`
*   **Backend API Docs:** Access the interactive API documentation at `http://localhost:8000/docs`
*   **ML Service API Docs:** Access the ML API documentation at `http://localhost:8001/docs`

### 6. Stopping the Application

To stop all running services and remove containers:

```bash
docker-compose down
```

To stop and remove volumes (e.g., to reset the database):

```bash
docker-compose down -v
```

## Running Tests

### Backend Tests

From the project root:

```bash
docker-compose exec backend pytest backend/tests/
```

### ML Service Tests

From the project root:

```bash
docker-compose exec ml_service pytest ml_service/tests/
```

### Frontend Tests

Currently, run frontend tests directly from the `frontend` directory:

```bash
cd frontend
npm install # if not already installed
npm test
```

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request. Ensure your code adheres to the project's coding standards and includes relevant tests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
