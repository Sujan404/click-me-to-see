import os
import pytesseract
from PIL import Image
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger("ocr_view_log")

@csrf_exempt
def ocr_view(request):
    logging.info("****************************************************************")
    logging.info(request.method)
    logging.info("Inside ocr_view function")

    # Hardcoded image URL (adjust as needed)
    image_url = '/media/users/avatars/2024/08/29/Mediaco-logo-white-yellow.png'  # Replace with the desired file path

    # Check if the file exists in the media directory
    image_path = os.path.join(settings.MEDIA_ROOT, image_url[7:])  # Remove the '/media/' prefix
    if not os.path.exists(image_path):
        return JsonResponse({'error': 'Image file not found'}, status=404)

    try:
        # Open image using PIL
        img = Image.open(image_path)
        
        # Process the image using pytesseract (OCR)
        ocr_text = pytesseract.image_to_string(img)

        return JsonResponse({'text': ocr_text})

    except Exception as e:
        logging.error(f"Error processing the image: {str(e)}")
        return JsonResponse({'error': f'Error processing the image: {str(e)}'}, status=500)
