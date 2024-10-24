const socket = new WebSocket('ws://127.0.0.1:8000/ws/binance/');

socket.onopen = function() {
    console.log("WebSocket 已連接");
};

socket.onmessage = function(event) {
    console.log("收到數據: ", event.data);
    const data = JSON.parse(event.data);
    document.getElementById('price').innerText = data.price; // 更新前端顯示
};

socket.onclose = function(event) {
    console.log("WebSocket 連接已關閉，代碼: ", event.code);
};

socket.onerror = function(error) {
    console.error("WebSocket 錯誤: ", error);
};
