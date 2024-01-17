'''
transactionを生成するファイル
実行可能(01/16 13:03)
'''

from datetime import datetime 
import json
import uuid

class transaction:
    def __init__(self,name):
        self.name = name

    def createTX(self):
        # 名前の収得
        myName = self.name
        # タイムスタンプの作成
        now = datetime.utcnow()
        timestamp = int(now.timestamp())
        # 出席記録の取得
        status = "attendance"
        # トランザクションの作成
        NewTX = {
            "name": myName,
            "timestamp": timestamp,
            "status": status
        }

        # JSONファイルへの書き込み
        json_path = './data/transaction/' + str(uuid.uuid4()) + '.json'
        # json_path = './data/transaction/' + str(timestamp) + '.json'
        with open(json_path, 'w') as json_path:
            json.dump(NewTX, json_path, indent=2)

        return NewTX

if __name__ == "__main__":

    # 名前の入力
    # name = input("名前を入力してください．->")
    name = 'Yuki Kato'

    # 出席TXの作成とブロードキャスト
    sampleTX = transaction(name)
    newTX = sampleTX.createTX()

    print(str(newTX)+"を作成しました。")
