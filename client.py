import socket

# サーバーのIPアドレスとポート番号
server_ip = '192.168.3.105'
server_port = 12345

# クライアントのIPアドレスとポート番号
client_ip = '192.168.3.55'
client_port = 54321

# ソケットの作成
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# メッセージの送信
message = "Hello, server!"
client_socket.sendto(message.encode(), (server_ip, server_port))

# ソケットのクローズ
client_socket.close()
