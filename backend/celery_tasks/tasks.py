from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import logging

logger = logging.getLogger("task.py ")

@shared_task
def send_notification_task(event):
    # Get channel layer and send the event to the WebSocket group
    channel_layer = get_channel_layer()
    logger.info("This is the beginning of sending message")
    async_to_sync(channel_layer.group_send)(  # Sending the event to the group
        "bill_notifications",  # Group name
        {
            "type": "bill_created",  # Maps to the consumer method
            "event": event["event"],
            "bill_id": event["bill_id"],
            "photo_url": event["photo_url"],
            "ocr_text": event["ocr_text"],  # Include OCR text
        },
    )
    logger.info("This is the end after sending the message")