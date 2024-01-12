## main.pyの説明

本ファイルではmain.pyのコードについて説明する。

### 1. transactionクラス

```py
# トランザクションに関する関数
class transaction:
    # blockchainの初期化関数
    def __init__(self):
        self.pending_transactions = []

    # トランザクションを生成する関数
    def create_transaction(self, sender, recipient, amount):
        # トランザクションの作成
        transaction = {
            "name": "Yuki Kato",
            "date": "0111",
            "time": "0931",
            "status": "attendance"
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

