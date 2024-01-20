import socket
import json

# 受信用のIPアドレスとポート番号
receiver_ip = "192.168.3.55"
port = 12345

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# バインド
sock.bind((receiver_ip, port))

# データの受信
data, addr = sock.recvfrom(1024)

# 受信したデータのデシリアライズ
received_data = json.loads(data.decode('utf-8'))

# 受信したデータの表示
print("Received Data:", received_data)

# ソケットのクローズ
sock.close()
