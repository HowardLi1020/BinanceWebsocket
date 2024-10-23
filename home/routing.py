# home/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/binance/$', consumers.Binance.as_asgi()),
]
