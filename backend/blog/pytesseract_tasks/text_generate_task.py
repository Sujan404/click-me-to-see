import os
import pytesseract
from PIL import Image
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from celery_tasks.tasks import send_notification_task
from blog.models import BillImage
import logging

logger = logging.getLogger("celery task")

@csrf_exempt
def text_generate_task(user_id, imageName):
    logging.info("Inside text_generate_task function")
    
    billImage = BillImage.objects.filter(name=imageName, user_id=user_id)[0]
    logger.info("//////////////////")
    image_url = billImage.photo.path[24:]
    # logger.info(billImage.photo.path)
    # logger.info(billImage.photo.path[24:])
    # Hardcoded image URL (adjust as needed)
    # image_url =   # Replace with the desired file path
#/usr/src/app/mediafiles/users/bill_images/2024/11/30/gunicorn.png
    # Check if the file exists in the media directory
    image_path = os.path.join(settings.MEDIA_ROOT, image_url) 
    logger.info(image_path)
    logger.info(settings.MEDIA_URL)
    if not os.path.exists(image_path):
        return JsonResponse({'error': 'Image file not found'}, status=404)

    try:
        # Open image using PIL
        img = Image.open(image_path)
        
        # Process the image using pytesseract (OCR)
        ocr_text = pytesseract.image_to_string(img)
        
        # Example of generating event data, including OCR text and photo URL
        event = {
            "event": "Bill notification",  # Event name
            "bill_id": billImage.id,  # You could dynamically generate this ID
            "photo_url": settings.MEDIA_URL + image_url,  # Use the image URL for frontend
            "ocr_text": ocr_text,  # Send the extracted OCR text
        }
        
        send_notification_task.delay(event)
        
        logger.info("Message sent to group: %s", event)
        return JsonResponse({'text': ocr_text})

    except Exception as e:
        logging.error(f"Error processing the image: {str(e)}")
        return JsonResponse({'error': f'Error processing the image: {str(e)}'}, status=500)
