from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/canvas1/", consumers.Canvas1Consumer.as_asgi()),
]
