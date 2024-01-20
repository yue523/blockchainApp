import socket

def start_server():
    # ソケットの作成
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # ホストとポートの設定
    host = 'localhost'
    port = 12345
    server_address = (host, port)

    # ソケットを指定したアドレスにバインド
    server_socket.bind(server_address)

    print(f"Server listening on {host}:{port}")

    try:
        while True:
            # データを受信
            data, client_address = server_socket.recvfrom(1024)
            print(f"Received data from {client_address}: {data.decode()}")

            # 受信したデータをそのままクライアントに送信
            server_socket.sendto(data, client_address)

    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
