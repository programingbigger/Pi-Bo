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
	- 顔を検出したら## 顔検出ロジックが出るように組み込む

 - display.py
	- 顔のバリエーションを増やして、いろんな表情を見せるようにする
	- 顔検出ができた用に、「こんにちは」⇨「笑顔」になるロジックを入れる ## 顔検出ロジック
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
	FaceDetect_FLAG = capture.CaptureFace()
	# 顔を検出したら、笑顔になるロジック
	if FaceDetect_FLAG == True:
		faces.smile()
	else:
		faces.random_face()
