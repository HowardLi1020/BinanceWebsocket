# home/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/binance/', consumers.BinanceConsumer.as_asgi()),  # 確保路徑與前端匹配
]