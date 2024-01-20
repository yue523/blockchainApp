import socket
import json

# ソケットの作成
server_ip = "192.168.3.105"
server_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((server_ip, server_port))

# ./test.jsonの読み込み
with open('./test.json', 'r') as file:
    data_to_send = json.load(file)

# クライアントのIPアドレスとポート番号
client_ip = "192.168.3.55"
client_port = 12346

# ソケット通信でデータを送信
sock.sendto(json.dumps(data_to_send).encode(), (client_ip, client_port))

# ソケット通信でデータを受信
received_data, addr = sock.recvfrom(1024)
print("Received data from {}: {}".format(addr, received_data.decode()))

# ソケットを閉じる
sock.close()
