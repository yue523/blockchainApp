import hashlib
import os
import json
from datetime import datetime

def get_timestamp_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        timestamp = data.get('timestamp', None)
        return timestamp

def process_folder(folder_path):
    result_dict = {}
    
    # フォルダ内の全てのJSONファイルにアクセス
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            
            # JSONファイル内のtimestampを取得
            timestamp = get_timestamp_from_json(file_path)
            
            # 辞書に追加
            result_dict[filename] = timestamp

    return result_dict

def sort_dict_by_timestamp(input_dict):
    # timestampで辞書をソート
    sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[1]))

    return sorted_dict

if __name__ == "__main__":
    # フォルダのパスを指定
    folder_path = './data/transaction'

    # フォルダ内のJSONファイルから情報を取得
    data_dict = process_folder(folder_path)

    # timestampでソート
    sorted_dict = sort_dict_by_timestamp(data_dict)

    # ソートした辞書の最初の8つを取得
    first_8_items = dict(list(sorted_dict.items())[:8])

    # ハッシュ値を格納する配列
    hash_array = []

    # 辞書のキーを取得して、対応するファイルを開いて中身をハッシュ化
    for key in first_8_items.keys():
        file_path = os.path.join(folder_path, key)    
        with open(file_path, 'r') as file:
            content = file.read()
            # ハッシュ値を計算して配列に追加
            hash_value = hashlib.sha256(content.encode()).hexdigest()
            hash_array.append((key, hash_value))


    # ハッシュ値を出力
    for file_key, hash_value in hash_array:
        print(f"File: {file_key}, Hash: {hash_value}")


    # # 結果を表示
    # print("First 8 items of the Sorted Dictionary by Timestamp:")
    # print(first_8_items)
