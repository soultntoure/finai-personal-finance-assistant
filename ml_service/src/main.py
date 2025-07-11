import uvicorn
from ml_service.src.prediction_api import app

if __name__ == "__main__":
    # This file serves as the main entry point for running the ML Service FastAPI application directly.
    # In a Dockerized environment, uvicorn is often started by the Dockerfile CMD.
    uvicorn.run(app, host="0.0.0.0", port=8001)
