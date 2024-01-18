# ダミーの辞書を作成
recv_json = {
    'hash': True,
    'timestamp': "hogehoge",
    'hogehoge': "hogehoge"
}

# 'status'キーが存在する場合
if 'status' in recv_json:
    print('これはTX')

# 'hash'キーが存在する場合
if 'hash' in recv_json:
    print('これはBL')

# 'index'キーが存在する場合
if 'index' in recv_json:
    print('これはBC')
