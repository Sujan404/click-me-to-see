import os
import pytesseract
from PIL import Image
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from blog.channel.consumers import BillNotificationConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task
import logging

logger = logging.getLogger("ocr_view_log")

@csrf_exempt
@shared_task
def ocr_view(request):
    logging.info("****************************************************************")
    logging.info(request.method)
    logging.info("Inside ocr_view function")

    # Hardcoded image URL (adjust as needed)
    image_url = '/media/users/bill_images/2024/11/14/IMG_4947.png'  # Replace with the desired file path

    # Check if the file exists in the media directory
    image_path = os.path.join(settings.MEDIA_ROOT, image_url[7:])  # Remove the '/media/' prefix
    if not os.path.exists(image_path):
        return JsonResponse({'error': 'Image file not found'}, status=404)

    try:
        # Open image using PIL
        img = Image.open(image_path)
        
        # Process the image using pytesseract (OCR)
        ocr_text = pytesseract.image_to_string(img)
        
        event = {
            "event": "Bill notification",  # Ensure this key is included
            "bill_id": "1",
            "photo_url": "abcedef",
        }
        
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.send)(
            "bill_notifications",  # Group name
            {
                "type": "bill_created",  # Maps to the consumer method
                "event": event["event"],
                "bill_id": event["bill_id"],
                "photo_url": event["photo_url"],
            },
        )
        
        return JsonResponse({'text': ocr_text})

    except Exception as e:
        logging.error(f"Error processing the image: {str(e)}")
        return JsonResponse({'error': f'Error processing the image: {str(e)}'}, status=500)
