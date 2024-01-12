import hashlib
import json
from datetime import datetime
from time import time
from uuid import uuid4

# トランザクションに関する関数
class transaction:
    # blockchainの初期化関数
    def __init__(self):
        self.pending_transactions = []

    # トランザクションを生成する関数
    def create_transaction(self, name, date, time, status):
        
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
        with open('./transaction/transaction.json', 'w') as json_file:
            json.dump(transaction, json_file, indent=2)

    # トランザクションをブロードキャストする関数
    def broadcast_transaction(self, transaction):
        self.pending_transactions.append(transaction)

# ブロック単体に関するオブジェクトクラス
class Block:
    # blockクラスの初期化関数
    def __init__(self, index, transactions, previous_hash, timestamp=None, nonce=0):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time()
        self.nonce = nonce
        self.hash = self.calculate_hash()

    # ハッシュ値を計算する関数
    def calculate_hash(self):
        # 各属性を構造体にする
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }, sort_keys=True).encode('utf-8')

        # 上記の構造体をハッシュ化
        return hashlib.sha256(block_string).hexdigest()

    # ブロックのマイニング
    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

    # ブロックの各属性の値を返す関数
    def to_dict(self):
        return {
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "hash": self.hash
        }

    # block_dict関数を用いて新しいBlockオブジェクトを作成して返す関数
    @staticmethod
    def from_dict(block_dict):
        return Block(
            block_dict["index"],
            block_dict["transactions"],
            block_dict["previous_hash"],
            block_dict["timestamp"],
            block_dict["nonce"]
        )

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
