"""
- todo
  - main.py
	- clean.pyの追加
	- 顔を検出し笑顔が出るが、以前の真顔の処理を同時に処理している
		- これを同時に処理させないようにする。

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

"""
from components import clean
from components.faces import LEDMatrixDisplay
from components import capture
from LOGGING.MY_LOGGING import setup_log
from concurrent.futures import ThreadPoolExecutor
import signal
import sys

# setup loggig
main_logger = setup_log(__name__)
faces_logger = setup_log("components.faces")
capture_logger = setup_log("components.capture")

'''
main
'''

main_logger.info("start main.py")

# clean screan
# clean.clear_screan()

display = LEDMatrixDisplay()

# 電光掲示板の実行関数
def emojishow():
	display.magao()
	# ~ display.eyes_LR()
	# ~ display.smile()
	# ~ display.trouble()

# カメラの実行関数
def face2marquee():
	FaceDetect_FLAG = capture.CaptureFace()

	# 顔を検出したら、笑顔になるロジック
	if FaceDetect_FLAG == True:
		display.smile()
	else:
		pass

# signal handlerの設定
def signal_handler(signum, frame):
  print("stop")
  executor.shutdown(wait=False)
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# 並列処理の実装
with ThreadPoolExecutor(max_workers=2) as executor:
	try:
		while True:
			emoji = executor.submit(emojishow)
			face = executor.submit(face2marquee)

			emoji = emoji.result()
			face = face.result()

			print("do ThreadPoolExecutor")
	except KeyboardInterrupt:
		pass

main_logger.info("end main.py")
