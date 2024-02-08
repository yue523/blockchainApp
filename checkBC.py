'''
従来のブロックチェーンとと受け取ったブロックチェーンの比較するプログラム
'''

import os
import json

BCtmpPath = './data/.blockchain'

file_names = [f for f in os.listdir(BCtmpPath) if f.endswith('.json')]

def find_matching_hash(mainBC, tmpBC):
    main_hash = mainBC[-1]["block"]["hash"]
    for block in tmpBC:
        if "hash" in block["block"] and block["block"]["hash"] == main_hash:
            print(f"index {block['index']} で一致しました。")
            return
    
    if len(mainBC) > 1:
        # 最後のブロックを削除して再帰的に検索
        mainBC.pop()
        find_matching_hash(mainBC, tmpBC)
    else:
        print("新しいブロックチェーンは一致しませんでした。")

for file_name in file_names:
    file_path = os.path.join(BCtmpPath, file_name)
    with open(file_path, 'r') as file:
        # JSONファイルを読み取り
        data = json.load(file)
        # 修正: json.dumpsを使わずにデータそのものを代入
        tmpBC = data

mainBCPath = './data/blockchain/main.json'
confBCPath = './data/blockchain/conf.json'

with open(mainBCPath, 'r') as file:
    data = json.load(file)
    mainBC_last_hash = data[-1]['block']['hash']
    
    mainBC = data

find_matching_hash(mainBC, tmpBC)

'''
indexの値がmain.jsonの一番最後のブロックである場合
対立がないため、そのままmainBC.jsonとして更新
'''

'''
indexの値がmain.jsonの一番最後のブロックではない場合
対立がそんざいするためためとりあえずそのことを出力する。

対立するブロックチェーンは別名でconf1.json(仮)ちう名前で./data/blockchainへと保存される。

ブロックチェーンへブロックが一定数追加された後、もう一度その2つのブロックチェーンの長さを比較する。
ブロックチェーンの長さが6以上であった場合長さが短いブロックチェーンは消える。
'''
