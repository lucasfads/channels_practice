from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/canvas2/", consumers.Canvas2Consumer.as_asgi()),
]
