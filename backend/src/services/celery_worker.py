from .notification_service import celery_app # Import celery_app instance

# This file typically defines and imports tasks from other services to be available to Celery.
# The `celery_app` instance itself is already configured in notification_service.py.
# To run the worker, you would execute: celery -A backend.src.services.celery_worker worker --loglevel=info

# You might add additional task imports here if tasks are defined in other files
# For example, if you had tasks in data_processing_tasks.py:
# from .data_processing_tasks import process_transactions

print("Celery worker initialized with tasks from notification_service.")
