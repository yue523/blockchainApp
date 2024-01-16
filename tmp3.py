import os
import json
import hashlib
from datetime import datetime

def get_timestamp_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        timestamp = data.get('timestamp', None)
        return timestamp

def calculate_file_hash(file_path):
    # ファイルの内容を読み込んでハッシュを計算
    with open(file_path, 'rb') as file:
        file_content = file.read()
        file_hash = hashlib.sha256(file_content).hexdigest()
        return file_hash

def process_folder(folder_path, num_files=8):
    result_dict = {}
    
    # フォルダ内のJSONファイルにアクセス
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            
            # JSONファイル内のtimestampを取得
            timestamp = get_timestamp_from_json(file_path)
            
            # 辞書に追加
            result_dict[filename] = timestamp

            # 最初の8つのファイルに対してハッシュを計算
            if len(result_dict) == num_files:
                break

    return result_dict

def calculate_hashes_for_files(folder_path, files_dict):
    hashes = {}
    
    for filename, timestamp in files_dict.items():
        file_path = os.path.join(folder_path, filename)
        
        # ファイルのハッシュを計算
        file_hash = calculate_file_hash(file_path)
        hashes[filename] = file_hash

    return hashes

if __name__ == "__main__":
    # フォルダのパスを指定
    folder_path = './data/transaction'

    # 最初の8つのJSONファイルから情報を取得
    data_dict = process_folder(folder_path)

    # 取得した最初の8つのJSONファイルのtimestampを表示
    print("Timestamps for the first 8 JSON files:")
    print(data_dict)

    # 最初の8つのJSONファイルのハッシュを計算
    file_hashes = calculate_hashes_for_files(folder_path, data_dict)

    # ハッシュを表示
    print("\nFile Hashes:")
    for filename, file_hash in file_hashes.items():
        print(f"{filename}: {file_hash}")
