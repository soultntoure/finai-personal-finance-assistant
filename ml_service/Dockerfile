# Multi-stage build for a lean production image

# Stage 1: Build dependencies
FROM python:3.10-slim-buster AS builder

WORKDIR /app/ml_service

# Install build dependencies if needed (e.g., for specific ML libraries)
# RUN apt-get update && apt-get install -y --no-install-recommends ...

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.10-slim-buster

WORKDIR /app/ml_service

# Copy only the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy application code and trained models
COPY ./src ./src

# Expose port 8001 for ML Service FastAPI
EXPOSE 8001

# Command to run the FastAPI application with Uvicorn
CMD ["uvicorn", "src.prediction_api:app", "--host", "0.0.0.0", "--port", "8001"]
