from pynput import keyboard

# キーが押されたときの処理
def on_press(key):
    try:
        # キーが 'q' だった場合、プログラムを終了
        if key.char == 'q':
            print("キー 'q' が押されたため、プログラムを終了します。")
            return False
    except AttributeError:
        # 特殊キーが押された場合は無視
        pass

# キーボードの監視を開始
with keyboard.Listener(on_press=on_press) as listener:
    # ここに処理を書く
    while True:
        # 何か処理を行う
        pass

    # プログラムが終了したら監視を停止
    listener.join()
