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
        print(f"Contents of {file_name}:")
        # インデントを指定してきれいに表示
        print(json.dumps(data, indent=2))
        print("\n" + "="*30 + "\n")


# 
