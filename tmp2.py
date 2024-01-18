import socket
import json

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ホストとポートの設定
host = 'localhost'
port = 12345
server_address = (host, port)

# ソケットを指定したホスト・ポートにバインド
sock.bind(server_address)

while True:
    recieved, CLIaddress = sock.recvfrom(4096)

    # 受け取ったデータを辞書にデシリアライズ
    recieved_json = json.loads(recieved)

    # 辞書を出力
    print("Received dictionary:", recieved_json)
