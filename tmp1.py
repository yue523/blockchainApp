'''
作成されたトランザクションからブロックを生成するプログラム
※ブロックがdataファイル内に8個ある必要がある.
'''

from datetime import datetime 
import json
import random
import os
import glob
    
class Block:

    def createBL(self, TXcount):
        
        # トランザクションのjsonファイルの個数分
        for i in TXcount:
            # TXのjsonファイルのタイムスタンプの読み込み
            with open("TXjsonファイル") as f:
                data = json.load(f)
            i = i + 1

        desired_key = 'timestamp'

        if desired_key in data:
            value = data[desired_key]
            print(f"{desired_key}:{value}")    

        # タイムスタンプの作成
        now = datetime.now()
        timestamp = int(now.timestamp())

        # ブロックチェーン最後のハッシュの取得
        prevHash = ""
        # ノンス値の作成
        nonce = random.randomint(1, 1000000)
        # ブロックの作成
        newBL = {
            "prevHash": prevHash,
            "hash": markle,
            "timestamp": timestamp,
            "nonce": nonce
        }
        # JSONファイルへの書き込み
        with open('block.json', 'w') as json_file:
            json.dump(newBL, json_file, indent=2)

if __name__ == "__main__":

    while True:
        # 指定されたディレクトリ内のJSONファイルを検索
        TXfiles = glob.glob(os.path.join("./data", '*.json'))
        TXcount = len(TXfiles)
        print(f"ファイル数は{TXcount}個")

        # dataファイル内に8つ以上のファイルがあった場合、
        # blockクラスを呼び出してcreateBLを行う.
        if TXcount >= 8:
            newBL = Block()
            newBL.createBL(TXcount)