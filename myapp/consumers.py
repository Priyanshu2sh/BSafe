from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .chatbot import get_safety_response
from .utils import *
from asgiref.sync import sync_to_async


class Test(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        message = "aa gye meri maut ka tamasha dekhne"
        # Optional: send a message on connect
        await self.send(text_data=message)

    async def disconnect(self, close_code):
        # Optional cleanup
        pass

    async def receive(self, text_data=None, bytes_data=None):
        # No matter what message comes in, always reply "hello"
        response = 'abee yaarrrr'
        await self.send(text_data=response)


class ChatbotConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Use user session or unique channel for each user (not a group)
        self.user_id = self.scope['session'].session_key or self.channel_name
        await self.accept()

        # Initialize session history if not present
        if 'chat_history' not in self.scope['session']:
            self.scope['session']['chat_history'] = []

    async def disconnect(self, close_code):
        # Nothing special on disconnect
        pass

    async def receive(self, text_data):

        if not text_data:
            await self.send(text_data=json.dumps({'error': 'User input is required.'}))
            return

        # Get chatbot response
        bot_response = get_safety_response(text_data)

        print(f"Formatted Response: {bot_response}")
        # Update session history
        await sync_to_async(self.scope['session'].save)()

        # Send response to client
        await self.send(text_data=bot_response)
