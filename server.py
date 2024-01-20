import socket

# サーバーのIPアドレスとポート番号
myIP = '192.168.3.105'
myPort = 12345

# ソケットの作成
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# バインド
server_socket.bind((myIP, myPort))

print(f"サーバーが {myIP}:{myPort} で待機中...")

# メッセージの受信
data, client_address = server_socket.recvfrom(1024)
print(f"クライアントから受信したメッセージ: {data.decode()}")

# ソケットのクローズ
server_socket.close()
