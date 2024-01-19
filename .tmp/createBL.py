'''
作成されたトランザクションからブロックを生成するプログラム
※ブロックがdataファイル内に8個ある必要がある.
'''

from datetime import datetime 
import json
import hashlib
import uuid
import os
import shutil
import glob
    
class Block:

    def calculate_merkle(self):
        # ディレクトリ内のJSONファイルのパスを取得
        directory_path = "./data/transaction"
        json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]

        # JSONファイルのパスとtimestampの値を格納するリスト
        files_with_timestamp = []
        # ディレクトリ内のJSONファイルからtimestampの値を取得して小さい順にソート
        for json_file in json_files:
            file_path = os.path.join(directory_path, json_file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                timestamp_value = data.get('timestamp')
                files_with_timestamp.append((file_path, timestamp_value))
        sorted_files = sorted(files_with_timestamp, key=lambda x: x[1])

        # 最初の8つのファイルの中身を文字列型の配列に格納
        file_contents = []
        for file_path, _ in sorted_files[:8]:
            with open(file_path, 'r') as f:
                content = f.read()
                file_contents.append(content)

        # マークルルートを計算
        hashed_values = [hashlib.sha256(data.encode('utf-8')).hexdigest() for data in file_contents]
        while len(hashed_values) > 1:
            temp = []
            for i in range(0, len(hashed_values), 2):
                # 2つのハッシュを連結してハッシュ化
                combined_hash = hashlib.sha256((hashed_values[i] + hashed_values[i + 1]).encode('utf-8')).hexdigest()
                temp.append(combined_hash)
            # 新しいハッシュリストを使用してループを続行
            hashed_values = temp
        merkle_root = hashed_values[0]

        # 移動先のディレクトリ
        destination_directory = "./data/.transaction"

        # 最初の8つのファイルを移動
        for file_path, _ in sorted_files[:8]:
            # ファイルを移動
            shutil.move(file_path, os.path.join(destination_directory, os.path.basename(file_path)))

        return merkle_root

    def createBL(self): 
        # マークルルートの作成
        merkle = self.calculate_merkle()

        # タイムスタンプの作成
        now = datetime.now()
        timestamp = int(now.timestamp())

        BLid = str(uuid.uuid4())
        # ブロックチェーン最後のハッシュの取得
        prevHash = ""
        # ノンス値の作成
        # nonce = random.randomint(1, 1000000)
        nonce = "none"
        # ブロックの作成
        newBL = {
            "id": BLid,
            "prevHash": prevHash,
            "hash": merkle,
            "timestamp": timestamp,
            "nonce": nonce
        }
        # JSONファイルへの書き込み
        block_path = './data/block/' + BLid + '.json'
        with open(block_path, 'w') as json_file:
            json.dump(newBL, json_file, indent=2)
        
        return newBL

if __name__ == "__main__":

    ################
    # ブロックの処理
    ################
    while True:
        # 指定されたディレクトリ内のJSONファイルを検索
        TXfiles = glob.glob(os.path.join("./data/transaction", '*.json'))
        TXcount = len(TXfiles)

        # dataファイル内に8つ以上のファイルがあった場合、
        # blockクラスを呼び出してcreateBLを行う.
        if TXcount >= 8:
            sampleBL = Block()
            newBL = sampleBL.createBL()
            print(f"{newBL}を作成しました。")
        # main.pyはelse分はいらない
        else :
            break
