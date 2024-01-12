import hashlib
import json
from time import time
from uuid import uuid4

class Block:
    def __init__(self, index, transactions, previous_hash, timestamp=None, nonce=0):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time()
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }, sort_keys=True).encode('utf-8')

        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def to_dict(self):
        return {
            "index": self.index,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "hash": self.hash
        }

    @staticmethod
    def from_dict(block_dict):
        return Block(
            block_dict["index"],
            block_dict["transactions"],
            block_dict["previous_hash"],
            block_dict["timestamp"],
            block_dict["nonce"]
        )

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, [], "0")

    def get_last_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        new_block = Block(
            len(self.chain),
            self.pending_transactions,
            self.get_last_block().hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = [{"from": None, "to": miner_address, "amount": 1.0}]

    def create_transaction(self, sender, recipient, amount):
        transaction = {
            "from": sender,
            "to": recipient,
            "amount": amount
        }
        self.pending_transactions.append(transaction)
        return transaction

    def broadcast_transaction(self, transaction, sender_signature):
        # Perform authentication logic here
        # For simplicity, let's assume the signature is valid
        self.pending_transactions.append(transaction)

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
