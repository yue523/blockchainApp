from datetime import datetime
import hashlib
import json
import socket
import random
import uuid
import os
import glob

####################
# トランザクションクラス
####################
class transaction:
    # blockchainの初期化関数
    def __init__(self, name):
        self.name = name

    # トランザクションを生成する関数
    def createTX(self):
        # 名前の収得
        myName = self.name
        # タイムスタンプの作成
        now = datetime.now()
        timestamp = int(now.timestamp())
        # 出席記録の取得
        status = "attendance"
        # トランザクションの作成
        newTX = {
            "name": myName,
            "timestamp": timestamp,
            "status": status
        }
        # JSONファイルへの書き込み
        json_path = './data/transaction/' + str(uuid.uuid4()) + '.json'
        with open(json_path, 'w') as json_path:
            json.dump(newTX, json_path, indent=2)
        
        # 作成したjsonファイルを返す
        return newTX

####################
# ブロッククラス
####################
class Block:
    

    def calculate_merkle(self):

        directory_path = "./data/transaction"

        # ディレクトリ内のJSONファイルのパスを取得
        json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]

        # JSONファイルのパスとtimestampの値を格納するリスト
        files_with_timestamp = []

        # ディレクトリ内のJSONファイルからtimestampの値を取得
        for json_file in json_files:
            file_path = os.path.join(directory_path, json_file)
            
            with open(file_path, 'r') as f:
                data = json.load(f)
                timestamp_value = data.get('timestamp')
                if timestamp_value is not None:
                    files_with_timestamp.append((file_path, timestamp_value))

        # timestampの値が小さい順にソート
        sorted_files = sorted(files_with_timestamp, key=lambda x: x[1])

        # 最初の8つのファイルの中身を文字列型の配列に格納
        file_contents = []
        for file_path, _ in sorted_files[:8]:
            with open(file_path, 'r') as f:
                content = f.read()
                file_contents.append(content)

        # ファイルの内容をハッシュ化してリストに追加
        hashed_values = [hashlib.sha256(data.encode('utf-8')).hexdigest() for data in file_contents]

        # マークルルートを計算
        while len(hashed_values) > 1:
            temp = []
            for i in range(0, len(hashed_values), 2):
                # 2つのハッシュを連結してハッシュ化
                combined_hash = hashlib.sha256((hashed_values[i] + hashed_values[i + 1]).encode('utf-8')).hexdigest()
                temp.append(combined_hash)

            # 新しいハッシュリストを使用してループを続行
            hashed_values = temp
        # マークルルートが得られます
        merkle_root = hashed_values[0]
        return merkle_root

    def createBL(self): 
        # マークルルートの作成
        merkle = self.calculate_merkle()

        # タイムスタンプの作成
        now = datetime.now()
        timestamp = int(now.timestamp())

        # ブロックチェーン最後のハッシュの取得
        prevHash = ""
        # ノンス値の作成
        # nonce = random.randomint(1, 1000000)
        nonce = "none"
        # ブロックの作成
        newBL = {
            "prevHash": prevHash,
            "hash": merkle,
            "timestamp": timestamp,
            "nonce": nonce
        }
        # JSONファイルへの書き込み
        block_path = './data/block/' + str(uuid.uuid4()) + '.json'
        with open(block_path, 'w') as json_file:
            json.dump(newBL, json_file, indent=2)

####################
# ブロックチェーンクラス
####################
class Blockchain:
    def __init__(self, BC):
        self.BC = BC

    # 新しいブロックチェーンを作成する関数
    def createBC(self):
        with open("blockchain.json", "w") as file:
            file.write("")
    
    # 前のブロックチェーンのハッシュ値を取得
    def getPreBC(self):
        with open("blockchain.json", 'r') as file:
            prevHash = json.load(file)
        return prevHash
    
    # 新しいブロックチェーンを作成する関数
    def create_newBC(self):
        newBC=self.BC
        with open("blockchain.json", "w") as file:
            json.write(newBC)

####################
# main関数
####################
if __name__ == "__main__":

    # 名前の入力
    myName = input("名前を入力してください．->")

    # ホスト(本ノード)とクライアントのIPアドレス、ポートを設定
    HOST = '192.168.3.105'
    CLIENT = '192.168.3.255'
    PORT = 50000

    # ソケットの作成とバインド
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST,PORT))

    # 出席トランザクションの作成とブロードキャスト
    sampleTX = transaction(myName)
    newTX = sampleTX.createTX()
    sock.sendto(newTX, (CLIENT, PORT))

    ########
    # ブロックに関するプログラム
    ########

    ########
    # ブロックチェーンに関するプログラム
    ########

    # 常時実行プログラム
    while True:
        # データの受取
        data, address = sock.recvfrom(4096)
        print(f"{address}から{data}トランザクションを受信しました。")

        #######
        # データをトランザクション、ブロック、ブロックチェーンに仕分けする
        # 仕分けしたデータをディレクトリに書き込む
        #######

        ################################
        # 8つ以上のTXがあった場合、ブロックを作成
        ################################
        TXfiles = glob.glob(os.path.join("./data", '*.json'))
        TXcount = len(TXfiles)
        if TXcount >= 8:
            newBL = Block()
            newBL.createBL()
