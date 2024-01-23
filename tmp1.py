def compare_hashes(mainBC, tmpBC):
    # mainBCの一番最後のblockのhash
    mainBC_last_hash = mainBC[-1]['block']['hash']

    # tmpBCの中でmainBCの最後のhashが存在するか確認
    same_ind = None
    for index, block_data in enumerate(tmpBC):
        if 'hash' in block_data['block'] and block_data['block']['hash'] == mainBC_last_hash:
            same_ind = index + 1  # インデックスは1から始まるため+1する
            break

    if same_ind is not None:
        if same_ind == tmpBC[-1]['index']:
            # same_indがtmpBCの最後のindexと一致する場合、tmpBCをmainBCとして出力
            print("tmpBCをmainBCとして出力:")
            print(tmpBC)
        else:
            # same_indがtmpBCの最後のindexと一致しない場合、tmpBCをconfBCとして保存
            print("tmpBCをconfBCとして保存:")
            # ここでtmpBCを保存する処理を追加する

        print("same_ind:", same_ind)
    else:
        print("mainBCの最後のhashがtmpBCに見つかりませんでした。")

# サンプルデータ
mainBC = [
    {
        "index": 1,
        "block": {
            "hash": "0000000000000000000000000000000000000000000000000000000000000000",
            "nonce": 0
        }
    },
    {
        "index": 2,
        "block": {
            "id": "59f349e8-43d7-4863-961d-1ab73c63ec79",
            "hash": "5ff1080318226325ac7b4562c5b21206dd12dfc6c691ae54588170307a928ee6",
            "timestamp": 1705971000,
            "nonce": 2857,
            "prevhash": "0000000000000000000000000000000000000000000000000000000000000000"
        }
    },
    {
        "index": 3,
        "block": {
            "id": "58486a90-a935-4d67-a844-b54636434498",
            "hash": "7256fc3e21d14d96d59d02e0819246c5b8a1c27e36ed858bb66d3c637b69b848",
            "timestamp": 1705971000,
            "nonce": 2422,
            "prevhash": "5ff1080318226325ac7b4562c5b21206dd12dfc6c691ae54588170307a928ee6"
        }
    }
]

tmpBC = [
    {
        "index": 1,
        "block": {
            "hash": "0000000000000000000000000000000000000000000000000000000000000000",
            "nonce": 0
        }
    },
    {
        "index": 2,
        "block": {
            "id": "59f349e8-43d7-4863-961d-1ab73c63ec79",
            "hash": "5ff1080318226325ac7b4562c5b21206dd12dfc6c691ae54588170307a928ee6",
            "timestamp": 1705971000,
            "nonce": 2857,
            "prevhash": "0000000000000000000000000000000000000000000000000000000000000000"
        }
    },
    {
        "index": 3,
        "block": {
            "id": "58486a90-a935-4d67-a844-b54636434498",
            "hash": "7256fc3e21d14d96d59d02e0819246c5b8a1c27e36ed858bb66d3c637b69b848",
            "timestamp": 1705971000,
            "nonce": 2422,
            "prevhash": "5ff1080318226325ac7b4562c5b21206dd12dfc6c691ae54588170307a928ee6"
        }
    }
]

# プログラムの実行
compare_hashes(mainBC, tmpBC)
