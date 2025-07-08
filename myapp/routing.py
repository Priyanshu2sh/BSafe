from django.urls import re_path
from .consumers import ChatbotConsumer, Test

websocket_urlpatterns = [
    re_path(r'^ws/chatbot/$', ChatbotConsumer.as_asgi()),
    re_path(r'^ws/test/$', Test.as_asgi()),
]
