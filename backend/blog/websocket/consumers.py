from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BillNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join the group
        await self.channel_layer.group_add(
            "bill_notifications",  # Group name
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            "bill_notifications",  # Group name
            self.channel_name
        )

    async def bill_created(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "event": event["event"],
            "bill_id": event["bill_id"],
            "photo_url": event["photo_url"],
        }))
