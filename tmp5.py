import os
import json

def get_min_timestamp_file_path(folder_path):
    # フォルダ内のJSONファイルの一覧を取得
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

    min_timestamp = float('inf')  # 初期値を無限大に設定
    min_timestamp_file_path = None

    for json_file in json_files:
        file_path = os.path.join(folder_path, json_file)

        # JSONファイルを読み込んでtimestampを取得
        with open(file_path, 'r') as f:
            data = json.load(f)
            timestamp = data.get('timestamp', float('inf'))
            if timestamp < min_timestamp:
                min_timestamp = timestamp
                min_timestamp_file_path = file_path

    return min_timestamp_file_path

if __name__ == "__main__":
    folder_path = "./data/block"

    min_timestamp_file_path = get_min_timestamp_file_path(folder_path)

    print(f"The file with the lowest timestamp is: {min_timestamp_file_path}")
