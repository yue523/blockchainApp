import hashlib
from datetime import datetime

# 簡単なProof of Workアルゴリズムの実装
def proof_of_work(last_proof, difficulty):
    proof = 0
    while not valid_proof(last_proof, proof, difficulty):
        proof += 1
    return proof

# Proofが条件を満たしているか確認する関数
def valid_proof(last_proof, proof, difficulty):
    # f文字列を使用して文字列を構築してバイト列にエンコード
    guess = f'{last_proof}{proof}'.encode()
    # バイト列`guess`のハッシュ値を計算して16進数の文字列に変換している。
    guess_hash = hashlib.sha256(guess).hexdigest()
    # 計算されたハッシュ値が指定された難易度に合致しているかを確認する。
    return guess_hash[:difficulty] == '0' * difficulty

# テスト用例
last_proof = 4738
difficulty_level = 4

start_time = datetime.now()
new_proof = proof_of_work(last_proof, difficulty_level)
end_time = datetime.now()

print(f'新しいProof: {new_proof}')
print(f'検証にかかった時間: {end_time - start_time}秒')