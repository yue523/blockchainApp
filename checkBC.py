'''
ブロックチェーンをソケット通信で受け取った際、
./data/.blockchainに保存される。
その.blockchainに保存されたjsonファイルについて

    もしブロックが正当なのであれば、
    それを./data/blockchainの正当なチェーンにそのまま追加or上書き

    ブロックが対立するのであれば、それを別ファイルとしてblockchainに保存

'''

import os
import json

'''
`./data/.blockchain`フォルダ内のjsonファイルの中身を取得
(このプログラムでは1つのjsonファイルを読み込むことしか仮定していない。)
'''

BCtmpPath = './data/.blockchain'

# フォルダ内のすべてのファイル名を取得
file_names = [f for f in os.listdir(BCtmpPath) if f.endswith('.json')]

def find_matching_hash(mainBC, tmpBC):
    main_hash = mainBC[-1]["block"]["hash"]
    
    for block in tmpBC:
        if "hash" in block["block"] and block["block"]["hash"] == main_hash:
            print("一致した")
            return
    
    # 一致しない場合、mainBCの前のブロックを再帰的に検索
    if len(mainBC) > 1:
        mainBC.pop()  # 最後のブロックを削除して再帰的に検索
        find_matching_hash(mainBC, tmpBC)
    else:
        print("一致しなかった")

# 各ファイルの中身を読み取り
for file_name in file_names:
    file_path = os.path.join(BCtmpPath, file_name)
    with open(file_path, 'r') as file:
        # JSONファイルを読み取り
        data = json.load(file)
        tmpBC = json.dumps(data, indent=2)

        # 中身を表示
        print(f"{file_name}を表示します。")
        # インデントを指定してきれいに表示
        print(tmpBC)

'''
`./data/blockchain/main.json`の中身を取得
'''

mainBCPath = './data/blockchain/main.json'
confBCPath = './data/blockchain/conf.json'

with open(mainBCPath, 'r') as file:
    # JSONファイルを辞書として読み取り
    data = json.load(file)
    mainBC_last_hash = data[-1]['block']['hash']
    mainBC = json.dumps(data, indent=2)
    # 辞書を表示
    print(f"{mainBCPath}の中身を表示します。")
    # インデントを指定してきれいに表示
    print(mainBC)

'''
mainBCとtmpBCの比較
'''

# 関数を呼び出し
find_matching_hash(mainBC, tmpBC)
