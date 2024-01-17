'''
新しくブロックチェーンを更新するプログラム
'''
import os
import json
import shutil

# ブロックプール内から一番小さいタイムスタンプのブロックを取得
def getNewBL(Blockfolder):
    # フォルダ内のJSONファイルの一覧を取得
    json_files = [f for f in os.listdir(Blockfolder) if f.endswith('.json')]

    min_timestamp = float('inf')  # 初期値を無限大に設定
    min_timestamp_file_path = None

    for json_file in json_files:
        file_path = os.path.join(Blockfolder, json_file)

        # JSONファイルを読み込んでtimestampを取得
        with open(file_path, 'r') as f:
            data = json.load(f)
            timestamp = data.get('timestamp', float('inf'))
            if timestamp < min_timestamp:
                min_timestamp = timestamp
                min_timestamp_file_path = file_path

    return min_timestamp_file_path

# ブロックチェーンにブロックを追加する関数
def addtoBC(BCjson,BLFpath):
    # タイムスタンプが小さいブロックを取得
    BLpath = getNewBL(BLFpath)
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

    # 追加したブロックを別のフォルダに移動する
    BLmoveto = "./data/.block"
    shutil.move(BLpath, BLmoveto)

if __name__ == "__main__":
    # ブロックチェーンの読み込み
    BCpath = './data/blockchain/blockchain.json'
    with open(BCpath, 'r') as json_file:
        BCjson = json.load(json_file)
    
    # フォルダ内のファイルを取得
    BLFpath = './data/block'

    # ブロックへの追加
    while True :
        # フォルダ内にファイルが存在するかチェック
        files_in_folder = os.listdir(BLFpath)

        # ファイルが存在する場合、addtoBC関数を実行
        if files_in_folder:
            addtoBC(BCjson, BLFpath)

