import socket
import json

# 送信先のIPアドレスとポート番号
receiver_ip = "192.168.3.55"
port = 12345

# JSONファイル読み込み
with open('./test.json', 'r') as file:
    data = json.load(file)

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ブロードキャスト用のアドレス設定
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# データのシリアライズと送信
message = json.dumps(data).encode('utf-8')
sock.sendto(message, (receiver_ip, port))

# ソケットのクローズ
sock.close()
