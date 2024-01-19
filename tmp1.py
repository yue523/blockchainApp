import keyboard

def main():
    print("プログラムを開始します。q キーを押すと終了します。")

    while True:
        if keyboard.is_pressed('q'):
            print("q キーが押されたのでプログラムを終了します。")
            break

        # ここに継続的な処理を追加する

if __name__ == "__main__":
    main()
