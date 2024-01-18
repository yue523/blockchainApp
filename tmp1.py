import socket
import json

# ソケットの作成
IPaddress = "127.0.0.1"
port = 50000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IPaddress, port))

print(f"Listening on port {port}...")

while True:
    # データを受信
    recv_data, address = sock.recvfrom(1024)
    recvJson = recv_data.decode('utf-8')

    # 受信した文字列をJSONとしてパース
    json_data = json.loads(recvJson)
    # JSON形式の文字列を保存
    with open('received_data.json', 'w') as file:
        json.dump(json_data, file, indent=2)
    print("Received and saved JSON data.")
