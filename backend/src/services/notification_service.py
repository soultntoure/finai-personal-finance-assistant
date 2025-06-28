from celery import Celery

from ..core.config import settings

celery_app = Celery(
    'notification_tasks',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

@celery_app.task
def send_email_notification(
    to_email: str,
    subject: str,
    body: str
):
    # In a real application, integrate with an email sending service like SendGrid, Mailgun, or AWS SES
    print(f"Simulating email send to {to_email} with subject '{subject}':")
    print(body)
    # Example: send_email_via_ses(to_email, subject, body)
    return {"status": "success", "to": to_email, "subject": subject}

@celery_app.task
def send_push_notification(
    user_id: int,
    message: str,
    data: dict = None
):
    # In a real application, integrate with a push notification service (e.g., Firebase Cloud Messaging)
    print(f"Simulating push notification to user {user_id}: {message}")
    return {"status": "success", "user_id": user_id, "message": message}

# Example usage in other services:
# from .notification_service import send_email_notification
# send_email_notification.delay("user@example.com", "Welcome!", "Hello from FinAI!")
