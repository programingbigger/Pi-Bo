"""
- todo
  - main.py
	- clean.pyの追加

  - MY_LOGGING.py
	- LOGGINGのログを日本時間に変更する

  - capture.py
	- 画像にテキストを入れる
		- 画像にテキストを入れる時は、以下のURLを参考にして実装してね
		- https://ameblo.jp/anima-ameblo/entry-12398046009.html 
	- 保存される画像を180度回転させる
	- もう少しコードを分割する
		- フォルダを作成するコードを別コードに移行
	- コードの簡略化
		- classを定義し、見やすいような形にする
	- 顔を検出したら## 顔検出ロジックが出るように組み込む

 - faces.py⇨名前displayじゃね？
	- 顔のバリエーションをもう1つ増やし
	- 4つの顔をランダムに出力するアーキテクチャに書き換える
	- 顔検出ができた用に、「こんにちは」⇨「笑顔」になるロジックを入れる ## 顔検出ロジック
 - Readme.md
	- 生成AIに書かせる
 - requrements.txtの追加
	- ライブラリの追加
	- dev環境でライブラリをインポートしてちゃんと動く用に設定する

"""
from components import clean
from components.display import FACES
from components import capture
from LOGGING.MY_LOGGING import setup_log
import sys

# loggigの設定
main_logger = setup_log(__name__)
faces_logger = setup_log("components.display")
capture_logger = setup_log("components.capture")

'''
======================== main ========================
'''

main_logger.info("start main.py")

# clean screan
# clean.clear_screan()

faces = FACES()

while True:
	# do
	faces.magao()
	FaceDetect_FLAG = capture.CaptureFace()
	# 顔を検出したら、笑顔になるロジック
	if FaceDetect_FLAG == True:
		faces.smile()
	else:
		pass
