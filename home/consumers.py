import json
import aiohttp  # 使用 aiohttp 來處理 WebSocket
from channels.generic.websocket import AsyncWebsocketConsumer

class BinanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            await self.accept()
            # 在連接後啟動 Binance WebSocket 連接
            await self.start_binance_websocket()
        except Exception as e:
            print(f"Error during connection: {e}")
            await self.close()

    async def disconnect(self, close_code):
        print(f"WebSocket 斷開連接，代碼：{close_code}")

    async def receive(self, text_data):
        try:
            # 處理從前端接收到的消息
            print(f"收到消息: {text_data}")
        except Exception as e:
            print(f"接收數據時發生錯誤: {e}")
            await self.close()

    async def start_binance_websocket(self):
        uri = "wss://stream.binance.com:9443/ws/btcusdt@trade"
        try:
            # 使用 aiohttp 來進行 WebSocket 連接
            async with aiohttp.ClientSession() as session:
                async with session.ws_connect(uri) as websocket:
                    async for message in websocket:
                        # 處理 Binance WebSocket 消息
                        await self.on_message(message.data)
        except Exception as e:
            print(f"Error connecting to Binance WebSocket: {e}")
            await self.close()

    async def on_message(self, message):
        try:
            data = json.loads(message)
            price = data.get('p')  # 交易價格
            qty = data.get('q')    # 交易數量

            if price and qty:
                # 將數據發送到 WebSocket 客戶端
                await self.send(text_data=json.dumps({
                    'price': price,
                    'quantity': qty,
                }))
        except json.JSONDecodeError:
            print("無法解析 Binance WebSocket 消息")
        except Exception as e:
            print(f"處理 Binance 消息時發生錯誤: {e}")