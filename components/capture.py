"""
- フロー
 - カメラ
 - 顔検出
	- もし検出できたら顔をbboxで囲み、名前を付けて保存する
	- それ以外は、カメラ作動
 - 終了
"""

from picamera2 import Picamera2
from picamera2 import Preview
from libcamera import Transform
import dlib
import face_recognition
import os
from datetime import datetime
import pytz
import time
from PIL import Image
from PIL import ImageDraw
#from PIL import ImageFont
from logging import getLogger
import sys

# logger
logger = getLogger(__name__)

# font
"""
メモに追加したけど、フォントファイルのダウンロードがんばってね
"""
#fontSize = 24
#fontFile = "Menlo-Regular.ttf"
#font = ImageFont.truetype(fontFile, fontSize)

# フォルダとファイル名
target_dir = "save_caputure"
jst = pytz.timezone("Asia/Tokyo")
now = datetime.now().astimezone(jst) # 日本時間変換
now = now.strftime("%Y-%m-%d_%H%M%S")
cap_file_name = target_dir + "/" + f"{now}.png"

# フォルダの作成
if not os.path.exists(target_dir):
  try:
	  os.makedirs(target_dir)
	  logger.info(f"{target_dir} saved")
  except OSError as e:
	  logger.error(f"do not make by error : {e}")
else:
  logger.info(f"{target_dir} already exists")

# picamera2のインスタンス化と設定
picam2 = Picamera2()
preview = Preview.NULL # プレビューに映さない
config = picam2.create_preview_configuration({"size": (400, 300), "format": "BGR888"}) # BGR:[R,G,B]
picam2.configure(config)

# 顔検出のモデルを設定
face_detector = dlib.get_frontal_face_detector()

def CaptureFace():
	try:
		# start picamera
		picam2.start()
		
		# face detected flag
		face_detected_flag = False
	
	
		# キャプチャー
		image = picam2.capture_array()
		faces = face_detector(image, 0)
	
		if len(faces) == 1:
			# 画像をpillowに変換
			pil_image = Image.fromarray(image)
			draw = ImageDraw.Draw(pil_image)
	
			# bbox情報を抽出し画像に加える
			for i, face in enumerate(faces):
				"""
				faces[0]で、 [(left, top), (right, bottom)]の情報を取得できる
				rectangleは、「四角（矩形）」という意味
				"""
	 
				# 画像に矩形の描画
				draw.rectangle(
								((face.left(), face.top()), (face.right(), face.bottom()))
								, outline=(0, 255, 0) # Green box
								, width=4
							)
				# テキスト挿入
				text_x = face.left()
				text_y = face.top()
				draw.text((text_x, text_y), text="face", textColor=(0, 255, 0))
	
			# 矩形が描かれた情報を保存
			pil_image.save(f"{cap_file_name}_with_boxes.png")
			logger.info(f"Saved image with boxes: {cap_file_name}_with_boxes.png")
			logger.info("collect capture")
			
			face_detected_flag = True
	
		else:
			# 顔を検出できなかったときを検証したいため、そのときのの画像も残す
			pil_image = Image.fromarray(image)
			pil_image.save(f"{cap_file_name}.png")
			logger.info(f"Saved image: {cap_file_name}.png")
			logger.info("not capture")
			face_detected_flag = False
	
		time.sleep(0.1)
		logger.info("continue capture")

	except KeyboardInterrupt:
		print("-"*10, "stop camera", "-"*10)
		self.logger.error("A key was interrupted during execution. ex: ctrl + c")
		sys.exit()

	return face_detected_flag


def StopCamera():
	# end camera
	picam2.stop_preview()
	picam2.stop()
	
	logger.error("A key was interrupted during execution. ex: ctrl + c")
	logger.info("stop picamera")
	
	sys.exit()
