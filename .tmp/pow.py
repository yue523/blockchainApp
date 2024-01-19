import hashlib
from datetime import datetime
import random

def proof_of_work(last_proof, difficulty):
    proof = 0
    while True:
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        if guess_hash[:difficulty] == '0' * difficulty:
            return proof
        print(f"計測終了: {proof}")
        proof += 1

# テスト用例
last_proof = random.randint(1, 99999)
print(f"前のproof: {last_proof}")
difficulty_level = 3

start_time = datetime.now()
new_proof = proof_of_work(last_proof, difficulty_level)
end_time = datetime.now()

print(f'新しいProof: {new_proof}')
print(f'検証にかかった時間: {end_time - start_time}秒')