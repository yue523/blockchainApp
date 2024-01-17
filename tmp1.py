'''
新しくブロックチェーンを更新するプログラム
'''
import json

# ブロックチェーンの読み込み
BCpath = './data/blockchain/blockchain.json'
with open(BCpath, 'r') as json_file:
    BCjson = json.load(json_file)

# フォルダ内のjsonファイルを取得
BLpath = "./data/block/sample.json"
# 新しいブロックのindexの作成
with open(BCpath, 'r') as file:
    BCjson = json.load(file)
lastID = BCjson[-1]['index']
nextID = lastID + 1
# 新しいブロックのjsonを作成
with open(BLpath, "r", encoding="utf-8") as file:
    newBC_json = json.load(file)
# 追加するブロックの作成と更新
newBL = {
    'index': nextID,
    'block': newBC_json
}
BCjson.append(newBL)

# JSONファイルの読み込み
with open(BCpath, 'r') as file:
    # ファイルを書き込みモードで開いてJSONデータを書き込む
    with open(BCpath, 'w') as write_file:
        json.dump(BCjson, write_file, indent=2)
