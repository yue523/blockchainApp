import socket

def start_client():
    # ソケットの作成
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # サーバーのホストとポート
    server_host = '192.168.3.105'
    server_port = 12345
    server_address = (server_host, server_port)

    try:
        while True:
            # ユーザーからの入力を取得
            message = input("Enter a message to send to the server (or 'exit' to quit): ")

            if message.lower() == 'exit':
                break

            # メッセージをサーバーに送信
            client_socket.sendto(message.encode(), server_address)

            # サーバーからのレスポンスを受信
            data, server_address = client_socket.recvfrom(1024)
            print(f"Received response from server: {data.decode()}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
