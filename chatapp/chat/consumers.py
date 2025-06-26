# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
from .models import Message  # ✅ import your model here

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        username = data['username']
        message = data['message']
        timestamp = datetime.utcnow().isoformat() + 'Z'

        # ✅ save to DB here
        Message.objects.create(username=username, message=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': message,
                'timestamp': timestamp
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
