'''
transactionを生成するファイル
実行可能(01/16 13:03)
'''

from datetime import datetime 
import json
import uuid

class Transaction:

    # 出席状況を示す変数`status`を引数としてトランザクションを生成する
    def createTX(self, status):
        # 出席者の名前の作成
        with open('info.json', 'r') as json_file:
            info_json = json.load(json_file)
        myName = info_json["name"]
        TXid = str(uuid.uuid4())
        # タイムスタンプの作成
        now = datetime.now()
        timestamp = int(now.timestamp())
        # トランザクションの作成
        newTX = {
            "id": TXid,
            "name": myName,
            "timestamp": timestamp,
            "status": status
        }
        # JSONファイルへの書き込み
        json_path = './data/transaction/' + TXid + '.json'
        with open(json_path, 'w') as json_path:
            json.dump(newTX, json_path, indent=2)
        
        # 作成したjsonファイルを返す
        return newTX 

if __name__ == "__main__":

    # 名前の入力
    # name = input("名前を入力してください．->")
    name = 'Yuki Kato'

    # 出席TXの作成とブロードキャスト
    sampleTX = Transaction()
    newTX = sampleTX.createTX(True)

    print(str(newTX)+"を作成しました。")
