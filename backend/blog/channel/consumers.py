from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging

class BillNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logging.info(f"WebSocket connecting to channel: {self.channel_name}")
        # Join the group
        await self.channel_layer.group_add(
            "bill_notifications",  # Group name
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        logging.info(f"WebSocket disconnecting from channel: {self.channel_name}")
        # Leave the group
        await self.channel_layer.group_discard(
            "bill_notifications",  # Group name
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        logging.info(f"Received event: {event}")
        text_data_json = json.loads(text_data)
        event = text_data_json.get("event", "")
        
        # Send message to group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'bill_created',
                'event': event,
                'bill_id': text_data_json['bill_id'],
                'photo_url': text_data_json['photo_url'],
                'ocr_text': text_data_json['ocr_text'],  # Ensure ocr_text is being sent here
            }
        )
        
    async def bill_created(self, event):
        logging.info(f"send event: {event}")
        # Send message to WebSocket
        # await self.send(text_data=json.dumps({
        #     "event": event["event"],
        #     "bill_id": event["bill_id"],
        #     "photo_url": event["photo_url"],
        # }))
        await self.send(text_data=json.dumps(event))
