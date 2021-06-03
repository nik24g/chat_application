import os
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import aroom.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pchat.settings")
django.setup()
application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            aroom.routing.websocket_urlpatterns
        )
    ),
})
