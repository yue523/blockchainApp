import socket

# サーバーのIPアドレスとポート番号
recvIP = '192.168.3.255'
recvPort = 12345

# クライアントのIPアドレスとポート番号
sendIP = '192.168.3.55'
sendPort = 54321

# ソケットの作成
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# メッセージの送信
message = "Hello, server!"
client_socket.sendto(message.encode(), (recvIP, recvPort))

# ソケットのクローズ
client_socket.close()
