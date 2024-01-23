import uuid
import socket
import json
import os

def recvTX(recv_json):
    # ./data/.transaction フォルダ内のファイルを調べる
    file_path = f'./data/.transaction/{recv_json["id"]}.json'

    # 同じjsonファイルが存在する場合は処理を終了
    if os.path.exists(file_path):
        return

    # ./data/transaction フォルダに保存する
    destination_path = f'./data/transaction/{recv_json["id"]}.json'
    with open(destination_path, 'w') as destination_file:
        json.dump(recv_json, destination_file, indent=2)

    print(f"id {recv_json['id']}のトランザクションが保存されました。")

def recvBL(recv_json):
        # ./data/.block フォルダ内のファイルを調べる
    file_path = f'./data/.block/{recv_json["id"]}.json'

    # 同じjsonファイルが存在する場合は処理を終了
    if os.path.exists(file_path):
        print(f"block with id {recv_json['id']} already exists.")
        return

    # ./data/block フォルダに保存する
    destination_path = f'./data/block/{recv_json["id"]}.json'
    with open(destination_path, 'w') as destination_file:
        json.dump(recv_json, destination_file, indent=2)

    print(f"ID:{recv_json['id']}のブロックが生成されました。")

def recvBC(recv_json):
    # UUIDを生成
    unique_id = str(uuid.uuid4())

    # 保存先ディレクトリが存在しない場合は作成
    save_directory = "./data/.blockchain"
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # JSONファイルのパスを構築
    save_path = os.path.join(save_directory, f"{unique_id}.json")

    # 辞書をJSONファイルとして保存
    with open(save_path, 'w') as json_file:
        json.dump(recv_json, json_file, indent=2)

    print(f"{recv_json}が保存されました。")


# ソケットの作成
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

myIP = '192.168.3.105'

# バインドするIPアドレスとポート
receiver_address = (myIP, 12345)
receiver_socket.bind(receiver_address)

# 受信と処理
while True:
    data, sender_address = receiver_socket.recvfrom(1024)
    recv_json = json.loads(data.decode('utf-8'))
    
    # 受信したデータの処理（ここでは印刷）
    print(f"Received data from {sender_address}: {recv_json}")

    if 'status' in recv_json:
        recvTX(recv_json)
    elif 'hash' in recv_json:
        recvBL(recv_json)
    elif 'index' in recv_json:
        recvBC(recv_json)

# ソケットのクローズ（通常はここに到達しない）
receiver_socket.close()
