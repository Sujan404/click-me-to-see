# views.py
import requests
import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import logging

logger = logging.getLogger("testing ocr")

@csrf_exempt
def ocr_view(request):
    logging.info("****************************************************************")
    logging.info(request.method)
    logging.info("I am inside ocr_view function")

    # Define the path of the image within the media directory
    media_image_path = os.path.join(settings.MEDIA_ROOT, 'users/avatars/2024/08/28/Sujan_Ale_CV.pdf')  # Remove the leading slash

    # Check if the file exists within the media directory
    if default_storage.exists(media_image_path):
        try:
            # Send the image to Tesseract API for OCR
            with open(media_image_path, 'rb') as img_file:
                tesseract_url = 'http://tesseract:5000/ocr'  # Adjust this endpoint if necessary
                response = requests.post(tesseract_url, files={'file': img_file})

            # Check if Tesseract processed the image successfully
            if response.status_code == 200:
                ocr_text = response.json().get('text', '')
                return JsonResponse({'text': ocr_text})
            else:
                return JsonResponse({'error': 'Tesseract OCR failed'}, status=500)

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return JsonResponse({'error': 'An error occurred while processing the OCR request'}, status=500)

    return JsonResponse({'error': 'Image not found in media files'}, status=400)
