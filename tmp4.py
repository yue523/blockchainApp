'''
フォルダ内の全てのjsonの名前とjson内のキーのtimestampを取得して辞書にする。
また、作成した辞書についてtimestampをソートする。
そして、その辞書の最初の8つを取得するプログラム
'''
import os
import json

# フォルダのパスを指定
folder_path = './data/transaction'

# フォルダ内のJSONファイルから情報を取得
data_dict = {}

# フォルダ内の全てのJSONファイルにアクセス
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        # JSONファイル内のtimestampを取得して辞書に追加
        with open(file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        timestamp = data.get('timestamp', None)
        data_dict[filename] = timestamp

# timestampでソート
sorted_dict = dict(sorted(data_dict.items(), key=lambda x: x[1]))

# ソートした辞書の最初の8つを取得して結果を表示
first_8_items = dict(list(sorted_dict.items())[:8])
print("First 8 items of the Sorted Dictionary by Timestamp:")
print(first_8_items)
