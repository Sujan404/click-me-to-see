
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task
def test_task():
    return "Hello, Celery!"

app.autodiscover_tasks(['celery_tasks'])
