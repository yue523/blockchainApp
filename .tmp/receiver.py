import socket
import json

# ソケットの作成
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

myIP = '192.168.3.105'

# バインドするIPアドレスとポート
receiver_address = (myIP, 12345)
receiver_socket.bind(receiver_address)

# 受信と処理
while True:
    data, sender_address = receiver_socket.recvfrom(1024)
    decoded_data = json.loads(data.decode('utf-8'))
    
    # 受信したデータの処理（ここでは印刷）
    print(f"Received data from {sender_address}: {decoded_data}")

# ソケットのクローズ（通常はここに到達しない）
receiver_socket.close()
