# ブロックチェーンの出席ファイル

## 各ファイルの説明

### 1. main.py

main.pyはブロックチェーンネットワークの出席、退席を管理するプログラムである。

### 2. block.json

block.jsonはブロックチェーンの部分を担うファイルであり以下の構造体から成り立つ。

| キー         | 説明                   |
|-------------|-----------------------|
| timestamp   | ブロックが作成された時刻    |
| previos hash| 前ブロックでのハッシュ値    |
| markle root | ブロックのマークルルート    |
| nonce       | ブロックでのナンス値       |

また、block.jsonを組み合わせた連結リストとして、blockchain.jsonがある。

```json
{
    "blockchain": [
      {
        "hash_prev_block": "00000000000000000000000000000000",
        "merkle_root": "6b86a4b58f8300bfc7b0a3f5c55c2d155be3a0eac3d81b12f2f79e834b53a8df",
        "timestamp": 1641900000,
        "nonce": 248942
      },
      {
        "hash_prev_block": "6b86a4b58f8300bfc7b0a3f5c55c2d155be3a0eac3d81b12f2f79e834b53a8df",
        "merkle_root": "b8c62d7a1f64d8f5aeb8b512be45b187f3d8f6706d1d4c3e015a3c7a1d3f672d",
        "timestamp": 1641901000,
        "nonce": 319033
      },
      {
          "hash_prev_block": "b8c62d7a1f64d8f5aeb8b512be45b187f3d8f6706d1d4c3e015a3c7a1d3f672d",
        "merkle_root": "e6a9e24e9a56c920d0e9c3b3e5b0f7f5d0e2b2e5b5f3a2e8b2a2e1a2e2b5f0",
        "timestamp": 1641902000,
        "nonce": 923918
      }
    ]
  }
  
```

blockchain.jsonはブロックは基本的に最初のブロックから記載する。

### 3. absence.csv

absence.csvは出席者の出席状況が確認できるファイルである。

```csv
名前,01/01,01/02,01/03,01/04,01/05
Kato,出席,欠席,出席,出席,出席
Murai,出席,出席,出席,出席,欠席
Harasawa,出席,欠席,出席,出席,出席
Takagi,欠席,欠席,欠席,欠席,出席
```

absence.csvはトランザクションからブロックが生成されてそれがブロックチェーンとして承認された時に、出席表が更新される。

### 4. transactionX.json

transactionX.jsonはネットワークに参加しているノードが出席または退席したときに生成されるjsonファイルである。transactionX.jsonのXの部分には数字が入っていき、transaction1.json、transaction2.json、transaction3.jsonのように増えていく。

```json
{
  "absence": [
    {
      "name": "Yuki Kato",
      "date": 0111,
      "time": 0931,
      "status": "attendance"
    },
  ]
}
```

なお、transactionX.jsonには出席状況が更新されたノードのみ記載する。また、上に記載のdateの値0111は1/11を示して、timeの値0931は9:31を示す。
