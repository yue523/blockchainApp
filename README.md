# ブロックチェーンの出席ファイル

## 各ファイルの説明

### 1. `main.py`

`main.py`はブロックチェーンネットワークの出席、退席を管理するプログラムである。詳しくは[こちら](./python.md)に記載しておく。

### 2. `(transaction).json`

`(transaction).json`はネットワークに参加しているノードが出席または退席したときに生成される`json`ファイルである。
ファイル名は`uuid`モジュールによってランダムに生成される。
またこのファイルは`data/transaction`ファイル内にトランザクションプールとして保存される。

```json
{
  "name": "Yuki Kato",
  "timestamp": 1705367930,
  "status": true
}
```

| キー         | 説明                   |
|-------------|-----------------------|
| `name`   | 出席者の名前    |
| `timestamp`   | トランザクションが作成された時刻    |
| `status`   | 出席者の状態    |

### 3. `block.json`

`block.json`はブロックにあたる構造体である。このファイルは`data/block`ファイル内にトランザクションプールとして保存される。

```json
{
  "prevHash": "",
  "hash": "15b23ab2c3af1bb281be6ba4fdb27d4841eaf0110631604e1b8cb07eb39cc582",
  "timestamp": 1705542341,
  "nonce": "none"
}
```

| キー         | 説明                   |
|-------------|-----------------------|
| `prevhash`  | 前ブロックでのハッシュ値    |
| `hash`      | ブロックのマークルルート    |
| `timestamp` | ブロックが作成された時刻    |
| `nonce`     | ブロックでのナンス値       |

また、`block.json`を組み合わせた連結リストとして、`blockchain.json`がある。

```json
[
  {
    "index": 1,
    "block": {
      "prevHash": "",
      "hash": "2f48bde434d358de0df398cd3c7ab1de9402d483c12fe495bd250b3b7d64e3bc",
      "timestamp": 1705457225,
      "nonce": "none"
    }
  },
  {
    "index": 2,
    "block": {
      "prevHash": "",
      "hash": "311fb33e61b11730e173976ac2a3f4640de79701b44e96c570e8fcca348d4040",
      "timestamp": 1705461947,
      "nonce": "none"
    }
  },
  {
    "index": 3,
    "block": {
      "prevHash": "",
      "hash": "1d81cfabe3b9bdbc18dd530acabdc4d495a9a0b4f925b7d8cc5d49de29721334",
      "timestamp": 1705461952,
      "nonce": "none"
    }
  }
]  
```
