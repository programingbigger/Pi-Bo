"""
- todo
  - main.py
	- faces.pyとcapture.pyを同時に処理させる並列処理の実装
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
"""
from components import clean
from components import faces
from components import capture
from LOGGING.MY_LOGGING import setup_log

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

# capture
capture.CaptureFace()

main_logger.info("end main.py")
