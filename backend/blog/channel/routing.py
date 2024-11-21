# routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/bill_notifications/', consumers.BillNotificationConsumer.as_asgi()),
]
