import uvicorn
from backend.src.api.main import app

if __name__ == "__main__":
    # This file serves as the main entry point for running the FastAPI application directly.
    # In a Dockerized environment, uvicorn is often started by the Dockerfile CMD.
    uvicorn.run(app, host="0.0.0.0", port=8000)
