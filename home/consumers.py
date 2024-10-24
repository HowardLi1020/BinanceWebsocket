import json
import aiohttp
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class BinanceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.keep_running = True
        self.fetch_task = asyncio.create_task(self.fetch_binance_data())

    async def disconnect(self, close_code):
        self.keep_running = False
        if self.fetch_task:
            self.fetch_task.cancel()

    async def receive(self, text_data):
        print(f"收到前端消息: {text_data}")

    async def fetch_binance_data(self):
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        while self.keep_running:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if response.status == 200:
                            data = await response.json()
                            price = data.get('price')
                            if price:
                                # 向前端發送最新價格數據
                                await self.send(text_data=json.dumps({
                                    'symbol': 'BTCUSDT',
                                    'price': price,
                                }))
            except Exception as e:
                print(f"Error fetching Binance data: {e}")

            # 每5秒獲取一次數據
            await asyncio.sleep(5)
