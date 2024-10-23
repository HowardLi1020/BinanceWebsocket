const socket = new WebSocket('ws://127.0.0.1:8000/ws/binance/');

socket.onopen = function() {
    console.log("WebSocket 已連接");
};

socket.onmessage = function(event) {
    console.log("收到數據: ", event.data);
};

socket.onclose = function(event) {
    console.log("WebSocket 連接已關閉");
    console.log("Close event: ", event);  // 檢查關閉事件是否包含更多信息
};

socket.onerror = function(error) {
    console.error("WebSocket 錯誤: ", error);  // 捕捉錯誤信息
};
