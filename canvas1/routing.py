from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/canvas1/(?P<room_name>\w+)/$", consumers.Canvas1Consumer.as_asgi()),
]
