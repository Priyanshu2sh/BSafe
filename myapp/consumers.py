from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .chatbot import query_mistral, format_response_as_points
from .utils import get_chunks_from_pdf
from asgiref.sync import sync_to_async


# Replace these with your actual functions and data
# from .utils import query_mistral, format_response_as_points
# chunks = [...]  # Your predefined list of chunks
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

        general_keywords = [
            "hello", "hi", "hey", "good morning", "good afternoon", "good evening",
            "how are you", "what's up", "goodbye", "bye", "see you", "thank you", "thanks"
        ]

        # Determine context
        if any(greet in text_data.lower() for greet in general_keywords):
            context = ""
        else:
            relevant_chunks = []
            user_words = set(text_data.lower().split())
            chunks = get_chunks_from_pdf()
            for chunk in chunks:
                chunk_words = set(chunk.lower().split())
                if user_words & chunk_words:
                    relevant_chunks.append(chunk)
            context = " ".join(relevant_chunks[:2]) if relevant_chunks else (chunks[0] if chunks else "")

        # Maintain history
        history = self.scope['session'].get('chat_history', [])[-5:]

        # Get chatbot response
        bot_response = query_mistral(text_data, context, history)
        formatted_response = format_response_as_points(bot_response)
        print(f"Formatted Response: {formatted_response}")
        # Update session history
        history.append({'user': text_data, 'bot': bot_response})
        self.scope['session']['chat_history'] = history
        await sync_to_async(self.scope['session'].save)()

        # Send response to client
        for msg in formatted_response:
            await self.send(text_data=msg)
