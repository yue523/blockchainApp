import socket
import json

# ソケットの作成
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

recvIP ='192.168.3.105'

# 送信先のブロードキャストIPアドレスとポート
receiver_broadcast_address = (recvIP, 12345)

# 送信するデータの読み込み
with open('./test.json', 'r') as file:
    data_to_send = json.load(file)

# ブロードキャストの設定
sender_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# データの送信
encoded_data = json.dumps(data_to_send).encode('utf-8')
print(encoded_data)
sender_socket.sendto(encoded_data, receiver_broadcast_address)

# ソケットのクローズ
sender_socket.close()
