import hashlib
import json
from datetime import datetime
from time import time
from uuid import uuid4
import socket

# トランザクションに関する関数
class transaction:
    # blockchainの初期化関数
    def __init__(self, name, date, time, status):
        self.pending_transactions = []
        self.name= name
        self.date=date
        self.time=time
        self.status=status

    # トランザクションを生成する関数
    def create_transaction(self):
        # データの収得
        name = "Yuki Kato"
        # 時間の取得
        datetime = datetime.now()
        date = int(f"{datetime.year:04d}{datetime.month:02d}{datetime.day:02d}")
        time = int(f"{datetime.hour:04d}{datetime.minute:02d}{datetime.second:02d}")
        # 出席記録の取得
        if True:
            status = "attendance"
        # トランザクションの作成
        NewTX = {
            "name": name,
            "date": date,
            "time": time,
            "status": status
        }
        # JSONファイルへの書き込み
        with open('./data/transaction.json', 'w') as json_file:
            json.dump(NewTX, json_file, indent=2)

    # トランザクションをブロードキャストする関数
    def broadcast_transaction(self, transaction):
        #########################
        # ソケット通信でのブロードキャスト
        # コードはまだ書いていない
        #########################
        self.pending_transactions.append(transaction)

# ブロック単体に関するオブジェクトクラス
class Block:
    # blockクラスの初期化関数
    def __init__(self, transactionX, hashed):
        self.transactionX=transactionX
        self.hashed=hashed

    # blockを生成する関数
    def create_block(self):
        with open ('./data/transaction1.json', 'r') as file:
            transactionX = json.load(file)
        # マークルルートの作成
        hashed = hashlib.sha256(transactionX.encode()).hexdigest()
        return hashed

    def bloadcast_block(self):
        ############################
        #ソケット通信によってブロードキャスト
        ############################
        print("tmp")

# ブロックの連結リストに関するオブジェクトクラス
class Blockchain:
    # blockchainの初期化関数
    def __init__(self, difficulty=2):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = []

    # 連結リストの最初のブロックを作成する関数
    def create_genesis_block(self):
        return Block(0, [], "0")

    # 連結リストの最後のブロックを取得する関数
    def get_last_block(self):
        return self.chain[-1]
    
    # 新しいブロックを連結リストに追加する関数
    def mine_pending_transactions(self, miner_address):
        # "Block"クラスから新しいインスタンスオブジェクトを作成する
        new_block = Block(
            len(self.chain),
            self.pending_transactions,
            self.get_last_block().hash
        )
        # 新しいブロックを生成
        new_block.mine_block(self.difficulty)
        # マイニングをしたブロックを連結リストに食い込む
        self.chain.append(new_block)
        # 次の採掘報酬のための更新
        self.pending_transactions = [{"from": None, "to": miner_address, "amount": 1.0}]

    # 連結リストの妥当性を検証する関数
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash() or current_block.previous_hash != previous_block.hash:
                return False
        return True

# jsonファイルを送信する関数
def send_json():
    # このノードのホストとポートを指定
    HOST = '192.168.3.105'
    PORT = 50000

    # サーバーソケットを作成
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    # クライアントからの接続を待機
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # 送信するJSONファイルのパス
    json_file_path = 'path/to/your/file.json'

    # JSONファイルを読み込み
    with open(json_file_path, 'r') as file:
        json_data = file.read()

    # JSONデータをクライアントに送信
    client_socket.sendall(json_data.encode('utf-8'))
    print("JSON data sent successfully")

    # ソケットを閉じる
    client_socket.close()
    server_socket.close()

# jsonファイルを受信する関数
def recive_json():
    # サーバーのホストとポートを指定
    HOST = '192.168.3.105'
    PORT = 50000

    # クライアントソケットを作成
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # 受信したJSONデータを保存するファイルのパス
    received_json_path = 'path/to/save/received_data.json'

    # サーバーからJSONデータを受信
    received_data = client_socket.recv(4096).decode('utf-8')

    # 受信したJSONデータを保存
    with open(received_json_path, 'w') as file:
        file.write(received_data)

    print(f"JSON data received and saved to {received_json_path}")

    # ソケットを閉じる
    client_socket.close()

# main関数
if __name__ == "__main__":
    # サーバーとクライアントを同時に起動
    server_thread = threading.Thread(target=start_server)
    client_thread = threading.Thread(target=start_client)

    server_thread.start()
    client_thread.start()
