import socket

# サーバーのIPアドレスとポート番号
server_ip = '192.168.3.105'
server_port = 12345

# ソケットの作成
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# バインド
server_socket.bind((server_ip, server_port))

print(f"サーバーが {server_ip}:{server_port} で待機中...")

# メッセージの受信
data, client_address = server_socket.recvfrom(1024)
print(f"クライアントから受信したメッセージ: {data.decode()}")

# ソケットのクローズ
server_socket.close()
