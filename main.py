import hashlib
import json
from datetime import datetime
from time import time
from uuid import uuid4

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
        transaction = {
            "name": name,
            "date": date,
            "time": time,
            "status": status
        }
        # JSONファイルへの書き込み
        with open('./data/transaction.json', 'w') as json_file:
            json.dump(transaction, json_file, indent=2)

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
    def __init__(self, transactionX):
        self.transactionX=transactionX

    # blockを生成する関数
    def create_block(self):
        with open ('./data/transaction1.json', 'r') as file:
            transactionX = json.load(file)
        # マークルルートの作成
        hashed = hashlib.sha256(transactionX.encode()).hexdigest()
        return hashed

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


# Example usage:
# Initialize blockchain
my_blockchain = Blockchain()

# Create transactions
transaction1 = my_blockchain.create_transaction("sender1", "recipient1", 2.0)
transaction2 = my_blockchain.create_transaction("sender2", "recipient2", 3.0)

# Broadcast transactions
my_blockchain.broadcast_transaction(transaction1, "sender1_signature")
my_blockchain.broadcast_transaction(transaction2, "sender2_signature")

# Mine pending transactions
miner_address = str(uuid4())  # Generate a random miner address for simplicity
my_blockchain.mine_pending_transactions(miner_address)

# Print blockchain
for block in my_blockchain.chain:
    print(block.to_dict())
