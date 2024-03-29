"""
ASGI config for channels_practice project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from canvas1.routing import websocket_urlpatterns as canvas1_websocket_urlpatterns
from canvas2.routing import websocket_urlpatterns as canvas2_websocket_urlpatterns

websocket_urlpatterns = canvas1_websocket_urlpatterns + canvas2_websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_practice.settings')

django_asgi_app = get_asgi_application()

import canvas1.routing
import canvas2.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
    ),
})