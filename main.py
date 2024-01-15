from datetime import datetime
import hashlib
import json
import socket

####################
# トランザクションクラス
####################
class transaction:
    # blockchainの初期化関数
    def __init__(self, name, client,port):
        self.name= name
        self.client=client
        self.port=port

    # トランザクションを生成する関数
    def createTX(self):
        # 名前の収得
        myname=self.name
        # タイムスタンプの作成
        now = datetime.now()
        timestamp =int(now.timestamp())
        # 出席記録の取得
        status = "attendance"
        # トランザクションの作成
        NewTX = {
            "name": myname,
            "timestamp": timestamp,
            "status": status
        }
        # JSONファイルへの書き込み
        with open('./data/transaction.json', 'w') as json_file:
            json.dump(NewTX, json_file, indent=2)

    # トランザクションをブロードキャストする関数
    def broadcastTX(self, client, port):
        print(f"{client}をブロードキャストします。")
        sock.sendto("jsonファイル", (client, port))

####################
# ブロッククラス
####################
class Block:
    
    # blockを生成する関数
    def createBL(self):
        # trasactionのjsonファイルの読み込みマークルルートを作成
        with open ('./data/transaction1.json', 'r') as file:
            transactionX = json.load(file)
        markle = hashlib.sha256(transactionX.encode()).hexdigest()        
        # タイムスタンプの作成
        now = datetime.now()
        timestamp = int(now.timestamp())
        # ブロックチェーン最後のハッシュの取得
        prevHash = ""
        # ブロックの作成
        newBL = {
            "prevHash": prevHash,
            "hash": markle,
            "timestamp": timestamp,
            "nonce": ""
        }
        # JSONファイルへの書き込み
        with open('block.json', 'w') as json_file:
            json.dump(newBL, json_file, indent=2)

    # トランザクションをブロードキャストする関数
    def broadcastBL(self, client, port):
        print(f"{client}をブロードキャストします。")
        sock.sendto("jsonファイル", (client, port))

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
    # ホスト(本ノード)とクライアントのIPアドレス、ポートを設定
    HOST = '192.168.3.105'
    CLIENT = '192.168.3.255'
    PORT = 50000

    # ソケットの作成とバインド
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST,PORT))

    sampleTX = transaction("name",CLIENT,PORT)
    sampleTX.createTX()
    sampleTX.broadcastTX(CLIENT,PORT)

    ########
    # ブロックに関するプログラム
    ########

    ########
    # ブロックチェーンに関するプログラム
    ########

    # 常時実行プログラム
    while True:
        # データの受取
        data, cli_addr=sock.recvfrom("jsonファイル",)
        print(f"{cli_addr}から{data}トランザクションを受信しました。")

        #######
        # データをトランザクション、ブロック、ブロックチェーンに仕分けする
        #######

        #######
        # 仕分けしたデータをディレクトリに書き込む
        #######

