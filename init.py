##################################
# 本アプリの初期設定を行うプログラム
# アプリを開始する前に本プログラムを実行すること
##################################

import json
import socket

# ユーザーからの入力を取得
user_input = input("名前を英語で入力してください: ")

# ホストのIPアドレスを取得
host_ip = socket.gethostbyname(socket.gethostname())

# info.jsonファイルにデータを書き込む
data = {
    "name": user_input, 
    "HOST": host_ip,
    "mainBC": "sample",
    "CLIENT": '192.168.3.255',
    "PORT": 50000
    }

with open("info.json", "w") as json_file:
    json.dump(data, json_file, indent = 2)

print("info.jsonが作成されました。")
print("初期設定が完了しました。")
