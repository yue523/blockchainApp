# import socket
import json

def process_data(data):
    data_dict = json.loads(data)

    if 'status' in data_dict:
        print('これはTX')
    elif 'hash' in data_dict:
        print('これはBL')
    elif 'index' in data_dict:
        print('これはBC')
    else:
        print('不明なデータ')


# 仮のソケット通信の例
# 実際の使用に合わせて変更してください
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind(('localhost', 12345))

while True:
    # data, address = server_socket.recvfrom(1024)
    data = {
        "index":3,
        "timpstamp":"hogehoge"
        }
    process_data(data.decode('utf-8'))
