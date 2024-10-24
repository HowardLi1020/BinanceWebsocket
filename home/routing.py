from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/binance/', consumers.BinanceConsumer.as_asgi()),  # 這樣允許結尾的 `/` 是可選的
]
