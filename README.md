# Pi-Bo: 顔認識で表情が変わる！ Pi-Bo ver0

## 概要

「Pi-Bo」は、Raspberry Pi とカメラモジュール、LED マトリックスを使って、あなたとコミュニケーションをとるインタラクティブなロボットです。  Pi-Bo はあなたの顔を認識し、笑顔を見せたり、時には困った顔を見せたり、様々な表情であなたを楽しませてくれます。

## Description

Pi-Bo は、搭載されたカメラモジュールを使ってあなたの顔を認識します。そして、その認識結果に応じて、LED マトリックスに表示する表情を変えます。

* あなたの顔を認識した場合: Pi-Bo は嬉しそうに笑顔を見せます。
* あなたの顔を認識できなかった場合: Pi-Bo は少し困ったような顔を見せます。

Pi-Bo は、Pythonで開発されており、顔認識には `dlib` ライブラリ、LED マトリックスの制御には `luma.led_matrix` ライブラリを使用しています。

***DEMO:***

https://github.com/programingbigger/Pi-Bo/assets/125252034/b89f9d80-1ebd-4b82-908b-feb740e55ac2


https://github.com/programingbigger/Pi-Bo/assets/125252034/90f5909e-fb79-4857-8b8a-e0f5dd32b790

## 特徴

- 顔認識機能: あなたの顔を認識して、様々な表情を見せてくれます。
- 複数の表情パターン: 笑顔や困った顔など、複数の表情パターンを搭載しています。
- カスタマイズ可能な設定 (TODO: カスタマイズ可能な項目があれば追記): あなたの好みに合わせて、Pi-Bo の設定を変更できます。

## 必要環境

### ハードウェア

- **Raspberry Pi:** 
    - Raspberry Pi 4 Model B (UD-RP4Bシリーズ)
- **カメラモジュール:** 
    - ラズベリーパイ用 カメラモジュール Camera Module for RasberryPi 500万画素 5MP
        - RasberryPi専用のCSIインターフェイス動作確認済み。
        - 【商品仕様】
            - 画像数：5MP
            - 光学系サイズ：1/4型センサー
            - F値：2.8
            - 焦点距離：3.4mm
            - 対角FoV:69.1度
            - カメラ静止画：2592 x 1944
            - フルHD 1080p/30fps動画撮影対応
            - モジュールサイズ：20 x 25 x 10mm
            - パッケージ内容
                - Camera Module for RasberryPi 500万画素 5MP x1
                - 15センチのフレックスケーブル x1 
- **MAX7219 を使った LED マトリックス:** 
    - 8x8ドットマトリクスLED（MAX7219駆動） x 8
    - 接続方法については、[https://store.shopping.yahoo.co.jp/solinnovay/rpimat1664.html](https://store.shopping.yahoo.co.jp/solinnovay/rpimat1664.html) を参考にして、購入してください。

### ソフトウェア

- **Python:** Python 3.11.2
- **必要なPythonパッケージ:** requirements.txt を参照

## インストール

1. ターミナルを開き、Desktopに移動します。
   ```bash
   cd Desktop
   ```
2. `git clone` でこのリポジトリをクローンします。
    ```bash
    git clone https://github.com/hogehoge/hogehoge  ※適切なgitリポジトリURLに置き換えてください
    ```
3. リポジトリのディレクトリに移動します。
   ```bash
   cd Pi-Bo
   ```
4. 仮想環境を構築します。
    ```bash
    python3 -m venv --system-site-packages core 
    ```
5. 仮想環境をアクティベートします。
    ```bash
    source core/bin/activate
    ```
6. 依存関係をインストールします。
    1. Raspberry Pi のターミナルで、以下のコマンドを実行し、`libopenblas-dev` をインストールします。(これは `dlib` や `face_recognition` に必要です)
        ```bash
        sudo apt-get install libopenblas-dev
        ```
    2. 以下のコマンドを実行し、`requirements.txt` に記載されているPythonパッケージをインストールします。
        ```bash
        pip install -r requirements.txt
        ```

## 使用方法

1. 以下のコマンドを実行し、電光掲示板に表示されているものを消去します。
    ```bash
    python3 clean.py 
    ```
2. 以下のコマンドを実行し、Pi-Bo を起動します。
    ```bash
    python3 main.py
    ```

## テスト

### カメラモジュールのテスト

1. ターミナルで以下のコマンドを実行します。
   ```bash
   libcamera-hello
   ```
2. エラーなく実行できれば、カメラは正常に動作しています。

### 8x8ドットマトリクスLED のテスト

1. 仮想環境をアクティベートします。
    ```bash
    source core/bin/activate
    ```
2. 以下のコマンドを実行します。
   ```bash
   python3 demo.py
   ```
3. LED マトリックスに何か表示されれば、正常に動作しています。

## その他

### 今後の展望

- **version 1: 顔識別機能の追加**
    - 特定の顔が認識されたら、「こんにちは！{名前}さん」と電光掲示板に表示し、笑顔を表示する。
- **version 2: 会話機能の追加**
    - Google API を使用して、Pi-Bo と会話できるようにする。

## 作者

[nami_fumi](https://qiita.com/nami_fumi/following_users)  
mail to: shidiannaigong@gmail.com
