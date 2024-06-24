"""
- todo
  - main.py
	- faces.pyとcapture.pyを同時に処理させる並列処理の実装
	- 一応、ThreadPoolExcuterで実装できたけど、いかがなものか・・・
	- add clean.py

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
  - faces.py
	- tryとexceptをなくした状態にし、main.pyに移行させる
	- 顔をランダムに出力するアーキテクチャに書き換える

"""
from components import clean
from components import faces
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

# ~ while True:
	# ~ faces.magao()
	# ~ faces.eyes_LR()
	# ~ faces.smile()
	# ~ faces.trouble()

# 電光掲示板の実行関数
def emojishow():
	# ~ faces.magao()
	# ~ faces.eyes_LR()
	faces.smile()
	# ~ faces.trouble()

# カメラの実行関数
def face2marquee():
	capture.CaptureFace()

# 
def signal_handler(signum, frame):
  print("stop")
  executor.shutdown(wait=False)
  sys.exit(0)
  
# set signal handler
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


# ~ # capture
# ~ while True:
	# ~ try:
		# ~ capture.CaptureFace()
	# ~ except KeyboardInterrupt:
		# ~ # Ctrl+C でループ終了
		# ~ capture.StopCamera()

main_logger.info("end main.py")
