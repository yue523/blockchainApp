import os
import hashlib

# 辞書の例
my_dictionary = {
    'file1.txt': 'This is content of file1',
    'file2.txt': 'This is content of file2',
    'file3.txt': 'This is content of file3'
}

# ファイルが格納されているディレクトリのパス
directory_path = '/path/to/your/files/'

# ハッシュ値を格納する配列
hash_array = []

# 辞書のキーを取得して、対応するファイルを開いて中身をハッシュ化
for key in my_dictionary.keys():
    file_path = os.path.join(directory_path, key)    
    with open(file_path, 'r') as file:
        content = file.read()
        # ハッシュ値を計算して配列に追加
        hash_value = hashlib.sha256(content.encode()).hexdigest()
        hash_array.append((key, hash_value))


# ハッシュ値を出力
for file_key, hash_value in hash_array:
    print(f"File: {file_key}, Hash: {hash_value}")
