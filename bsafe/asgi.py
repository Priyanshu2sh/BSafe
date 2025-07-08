import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.sessions import SessionMiddlewareStack
from myapp import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsafe.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": SessionMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
