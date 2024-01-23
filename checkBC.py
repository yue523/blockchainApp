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

# mainBCの一番最後のblockのhash


# tmpBCの中でmainBCの最後のhashが存在するか確認
same_index = None
for index, block_data in enumerate(tmpBC):
    if 'hash' in block_data['block'] and block_data['block']['hash'] == mainBC_last_hash:
        same_index = index + 1  # インデックスは1から始まるため+1する
        break

if same_index is not None:
    if same_index == tmpBC[-1]['index']:
        # same_indがtmpBCの最後のindexと一致する場合、tmpBCをmainBCとして出力
        with open(mainBCPath, 'w') as file:
            json.dump(tmpBC, file, indent=2) 
        print("tmpBCをmainBCとして出力:")
        print(tmpBC)
    else:
        # same_indがtmpBCの最後のindexと一致しない場合、tmpBCをconfBCとして保存
        print("tmpBCをconfBCとして保存:")
        # ここでtmpBCを保存する処理を追加する
        with open(confBCPath, 'w') as file:
            json.dump(tmpBC, file, indent=2)

    print("same_index:", same_index)
else:
    print("mainBCの最後のhashがtmpBCに見つかりませんでした。")