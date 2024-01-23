import socket
import json
import os

# ソケットの作成
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

recvIP = '192.168.3.105'

# 送信先のブロードキャストIPアドレスとポート
receiver_broadcast_address = (recvIP, 12345)

# ブロードキャストの設定
sender_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 送信するデータの準備
folders_to_send = ['./data/transaction', './data/block', './data/broadcast']
data_to_send = []

# 指定ディレクトリ内のJSONファイルを読み込んでデータリストに追加
for folder in folders_to_send:
    for filename in os.listdir(folder):
        if filename.endswith('.json'):
            file_path = os.path.join(folder, filename)
            with open(file_path, 'r') as file:
                file_data = json.load(file)
                data_to_send.append(file_data)

# データの送信
for data in data_to_send:
    encoded_data = json.dumps(data).encode('utf-8')
    print(encoded_data)
    sender_socket.sendto(encoded_data, receiver_broadcast_address)

# ソケットのクローズ
sender_socket.close()
