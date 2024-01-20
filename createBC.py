'''
新しくブロックチェーンを更新するプログラム
'''
import hashlib
import os
import json
import shutil

# ブロックプール内から一番小さいタイムスタンプのブロックを取得
def getNewBL(Blockfolder):
    # フォルダ内のJSONファイルの一覧を取得
    json_files = [f for f in os.listdir(Blockfolder) if f.endswith('.json')]

    min_timestamp = float('inf')  # 初期値を無限大に設定
    min_timestamp_file_path = None

    for json_file in json_files:
        file_path = os.path.join(Blockfolder, json_file)

        # JSONファイルを読み込んでtimestampを取得
        with open(file_path, 'r') as f:
            data = json.load(f)
            timestamp = data.get('timestamp', float('inf'))
            if timestamp < min_timestamp:
                min_timestamp = timestamp
                min_timestamp_file_path = file_path

    return min_timestamp_file_path

def proof_of_work(prevNonce, hash, difficulty):
    proof = 0
    while True:
        guess = f'{prevNonce}{hash}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        if guess_hash[:difficulty] == '0' * difficulty:
            return proof
        print(f"計測終了: {proof}")
        proof += 1

# ブロックチェーンにブロックを追加する関数
def addtoBC(BCjson,BLFpath):
    # タイムスタンプが小さいブロックを取得
    BLpath = getNewBL(BLFpath)
    # 新しいブロックのindexの作成
    with open(BCpath, 'r') as file:
        BCjson = json.load(file)
    lastID = BCjson[-1]['index']
    nextID = lastID + 1
    # 新しいブロックのjsonを作成
    with open(BLpath, "r", encoding="utf-8") as file:
        newBC_json = json.load(file)
    # 追加するブロックの作成と更新
    newBL = {
        'index': nextID,
        'block': newBC_json
    }

    prevNonce = BCjson[-1]['block']['nonce']
    hash = newBL['block']['hash']
    difficulty = 4
    nonce = proof_of_work(prevNonce, hash, difficulty)
    print(f"コンセンサスアルゴリズムから{nonce}を取得しました。")
    # 追加するブロックにノンス値と一つ前のハッシュ値を追加
    newBL['block']['nonce'] = nonce
    newBL['block']['prevhash'] = BCjson[-1]['block']['hash']
    BCjson.append(newBL)

    # JSONファイルの読み込み
    with open(BCpath, 'r') as file:
        # ファイルを書き込みモードで開いてJSONデータを書き込む
        with open(BCpath, 'w') as write_file:
            json.dump(BCjson, write_file, indent=2)

    # 追加したブロックを別のフォルダに移動する
    BLmoveto = "./data/.block"
    shutil.move(BLpath, BLmoveto)
    
if __name__ == "__main__":
    # ブロックチェーンの読み込み
    BCpath = './data/blockchain/sample.json'
    with open(BCpath, 'r') as json_file:
        BCjson = json.load(json_file)
    
    # フォルダ内のファイルを取得
    BLFpath = './data/block'

    # ブロックへの追加
    while True :
        # フォルダ内にファイルが存在するかチェック
        files_in_folder = os.listdir(BLFpath)

        # ファイルが存在する場合、addtoBC関数を実行
        if files_in_folder:
            addtoBC(BCjson, BLFpath)
        else:
            break
