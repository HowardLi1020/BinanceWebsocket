# consumers.py
import json
import asyncio
import websockets  # 使用 websockets 庫
from channels.generic.websocket import AsyncWebsocketConsumer

class BinanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            await self.accept()
        except Exception as e:
            print(f"Error during connection: {e}")
            await self.close()

    async def disconnect(self, close_code):
        print(f"WebSocket 斷開連接，代碼：{close_code}")

    async def receive(self, text_data):
        try:
            # 處理接收到的消息
            print(f"收到消息: {text_data}")
        except Exception as e:
            print(f"接收數據時發生錯誤: {e}")
            await self.close()

    async def binance_websocket(self):
        uri = "wss://stream.binance.com:9443/ws/btcusdt@trade"
        try:
            async with websockets.connect(uri) as websocket:
                while True:
                    message = await websocket.recv()
                    await self.on_message(message)
        except Exception as e:
            print(f"Error connecting to Binance WebSocket: {e}")
            await self.close()


    async def on_message(self, message):
        data = json.loads(message)
        price = data['p']  # 交易價格
        qty = data['q']    # 交易數量

        # 將數據發送到 WebSocket 客戶端
        await self.send(text_data=json.dumps({
            'price': price,
            'quantity': qty,
        }))
