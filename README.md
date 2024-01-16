# ブロックチェーンの出席ファイル

## 各ファイルの説明

### 1. `main.py`

`main.py`はブロックチェーンネットワークの出席、退席を管理するプログラムである。詳しくは[こちら](./python.md)に記載しておく。

### 2. `(transaction).json`

`(transaction).json`はネットワークに参加しているノードが出席または退席したときに生成される`json`ファイルである。
ファイル名は`python`ファイルの`uuid`モジュールによってランダムに生成される。
`(transaction).json`は`data`ファイル内に保管される。
すなわち`data`ファイルはトランザクションプールとして利用される。
トランザクションファイルのサンプルを示す。

```json
{
  "name": "Yuki Kato",
  "timestamp": 1705367930,
  "status": "attendance"
}
```

| キー         | 説明                   |
|-------------|-----------------------|
| `name`   | 出席者の名前    |
| `timestamp`   | トランザクションが作成された時刻    |
| `status`   | 出席者の状態    |

### 3. block.json

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

### 4. absence.csv

absence.csvは出席者の出席状況が確認できるファイルである。

```csv
名前,01/01,01/02,01/03,01/04,01/05
Kato,出席,欠席,出席,出席,出席
Murai,出席,出席,出席,出席,欠席
Harasawa,出席,欠席,出席,出席,出席
Takagi,欠席,欠席,欠席,欠席,出席
```

absence.csvはトランザクションからブロックが生成されてそれがブロックチェーンとして承認された時に、出席表が更新される。
