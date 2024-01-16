# `main.py`の説明

本ファイルでは`main.py`のコードについて説明する。リンクは[こちら](./main.py)から確認できる。

## 1. `transaction`クラス

```py
class transaction:
    # blockchainの初期化関数
    def __init__(self, name):
        self.name = name

    # トランザクションを生成する関数
    def createTX(self):
        # 名前の収得
        myName = self.name
        # タイムスタンプの作成
        now = datetime.now()
        timestamp = int(now.timestamp())
        # 出席記録の取得
        status = "attendance"
        # トランザクションの作成
        newTX = {
            "name": myName,
            "timestamp": timestamp,
            "status": status
        }
        # JSONファイルへの書き込み
        json_path = './data/' + str(uuid.uuid4()) + '.json'
        with open(json_path, 'w') as json_path:
            json.dump(newTX, json_path, indent=2)
        
        # 作成したjsonファイルを返す
        return newTX
```

| 関数                    | 内容                        |
|------------------------|----------------------------|
| `createTX`             | トランザクションを作成する       |

`createTX`関数は辞書`newTX`を作成する。
辞書`newTX`ではそれぞれ`name`、`timestamp`、`status`を取得する。
`timestamp`は`datetime`モジュールの`timestamp`関数から取得する。
辞書`newTX`はその後`json`ファイルとして`dump`関数を用いて書き込まれる。
その際、作成するファイルの名前は`uuid`モジュールを用いて自動的かつランダムに生成される。
最終的に、関数`createTX`は辞書`newTX`を文字型の変数として返す。
