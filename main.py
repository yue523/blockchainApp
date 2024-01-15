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
        with open('./block.json', 'w') as json_file:
            json.dump(newBL, json_file, indent=2)

    # トランザクションをブロードキャストする関数
    def broadcastBL(self, client, port):
        print(f"{client}をブロードキャストします。")
        sock.sendto("jsonファイル", (client, port))

####################
# ブロックチェーンクラス
####################
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

