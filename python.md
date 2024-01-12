## main.pyの説明

本ファイルではmain.pyのコードについて説明する。

## 1. transactionクラス

```py
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
        with open('transaction.json', 'w') as json_file:
            json.dump(transaction, json_file, indent=2)

    # トランザクションをブロードキャストする関数
    def broadcast_transaction(self, transaction):
        self.pending_transactions.append(transaction)
```

| 関数                    | 内容                        |
|------------------------|----------------------------|
| create_transaction     | トランザクションを作成する       |
| broadcast_transaction  | トランザクションのブロードキャスト |

transactionクラスはtransactionに関するクラスである。

### 1.1. create_transaction

初めに構造体`transaction`を作成する。構造体`transaction`ではそれぞれ`name`、`date`、`time`、`status`を取得する。`date`と`time`は`datetime`モジュールの`now`関数を用いて変数`datetime`を作成して`datetime`変数から取得する。

```py
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
```

その後`with`ステートメントを使用してファイルのオープンとコンテキストの管理をする。`open`関数を使用してファイル`transaction.json`を書き込みモード (`w`) で開く。`json.dump`関数を使用して`transaction`をJSONフォーマットに変換し、それを`transaction.json`に書き込む。`indent=2`の引数は各レベルで2つのスペースでインデントするよう指定している。

```py
# JSONファイルへの書き込み
with open('transaction.json', 'w') as json_file:
    json.dump(transaction, json_file, indent=2)
```

### 1.2. broadcast_transaction



```py
# トランザクションをブロードキャストする関数
def broadcast_transaction(self, transaction):
    self.pending_transactions.append(transaction)
```
