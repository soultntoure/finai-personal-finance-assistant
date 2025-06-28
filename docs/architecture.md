# FinAI Architecture Overview

This document provides a high-level overview of the FinAI system architecture, detailing the interaction between its core components.

## 1. System Components

*   **Frontend Service (Next.js/React):** The user-facing web application.
*   **Backend Service (FastAPI/Python):** The primary API and business logic layer.
*   **ML Service (FastAPI/Python):** Dedicated service for AI/ML model inference.
*   **PostgreSQL Database:** Primary relational data store.
*   **Redis:** Cache and Celery message broker.
*   **Plaid:** Third-party financial data aggregation.

## 2. Data Flow

1.  **User Interaction:** Users interact with the Frontend.
2.  **API Requests:** Frontend makes requests to the Backend Service.
3.  **Backend Processing:**
    *   Authenticates users (JWT).
    *   Interacts with PostgreSQL for CRUD operations.
    *   Communicates with Plaid for financial data (e.g., account linking, transaction fetching).
    *   Sends asynchronous tasks to Celery (e.g., data aggregation, notifications).
    *   Queries the ML Service for predictions (e.g., categorization, budgeting suggestions).
4.  **ML Service Inference:** Receives requests from Backend, performs model inference, and returns results.
5.  **Data Persistence:** Financial data, user profiles, goals, and budgets are stored in PostgreSQL.
6.  **Caching/Queuing:** Redis is used for API response caching, session management, and Celery task queuing.

## 3. Deployment Strategy (AWS Fargate)

Each service (Backend, ML Service, Frontend) will be containerized and deployed as separate tasks on AWS Fargate within a VPC. Load Balancers will distribute traffic to the Frontend and Backend services. PostgreSQL and Redis will be managed services (RDS, ElastiCache).

```mermaid
graph TD
    User --> Frontend[Frontend (Next.js)]
    Frontend --> ALB_Backend[AWS ALB (Backend)]
    ALB_Backend --> Backend[Backend Service (FastAPI)]
    Backend --> PostgreSQL[PostgreSQL (RDS)]
    Backend --> Redis[Redis (ElastiCache)]
    Backend --> Plaid[Plaid API]
    Backend --> MLService[ML Service (FastAPI)]
    Backend -- Async Tasks --> Celery[Celery Worker (Fargate)]
    Celery -- Stores Data --> PostgreSQL
    Celery -- Uses --> Redis

    subgraph AWS VPC
        direction LR
        Frontend
        Backend
        MLService
        PostgreSQL
        Redis
        Celery
    end
```

## 4. Key Design Decisions

*   **Microservices:** Decoupling services enables independent scaling and development.
*   **Asynchronous Processing:** Celery handles long-running tasks to maintain API responsiveness.
*   **Containerization:** Docker ensures consistent environments across development and production.
*   **Managed AWS Services:** Reduces operational overhead and provides high availability.
