"""
- フロー
 - カメラ
 - 顔検出
	- もし検出できたら顔をbboxで囲み、名前を付けて保存する
	- それ以外は、カメラ作動
 - 終了

- todo
 - 画像にテキストを入れる
  - 画像にテキストを入れる時は、以下のURLを参考にして実装してね
  - https://ameblo.jp/anima-ameblo/entry-12398046009.html 
 - 保存される画像を、180度回転させる
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

# 日本時間変換
jst = pytz.timezone("Asia/Tokyo")

# font
"""
メモに追加したけど、フォントファイルのダウンロードがんばってね
"""
#fontSize = 24
#fontFile = "Menlo-Regular.ttf"
#font = ImageFont.truetype(fontFile, fontSize)

# フォルダとファイル名
target_dir = "save_caputure"
now = datetime.now()
now = now.astimezone(jst)
now = now.strftime("%Y-%m-%d_%H%M%S") # collent time
cap_file_name = target_dir + "/" + f"{now}.png"

# フォルダの作成
if not os.path.exists(target_dir):
  try:
    os.makedirs(target_dir)
    print(f"{target_dir} saved")
  except OSError as e:
    print(f"do not make by error : {e}")
else:
  print(f"{target_dir} already exists")

# picamera2のインスタンス化と設定
picam2 = Picamera2()
preview = Preview.NULL # プレビューに映さない
config = picam2.create_preview_configuration({"size": (400, 300), "format": "BGR888"}) # BGR:[R,G,B]
picam2.configure(config)

# 顔検出のモデルを設定
face_detector = dlib.get_frontal_face_detector()

# start picamera
picam2.start()

try:
	while True:
		# キャプチャー
		image = picam2.capture_array()
		faces = face_detector(image, 0)
		print(image.shape)
		print(type(image))
		print(f"faces array: {faces}")
		print(len(faces))

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
			print(f"Saved image with boxes: {cap_file_name}_with_boxes.png")
			print("collect capture")
		else:
			print("not capture")
			pass

		time.sleep(0.5)
		print("continue camera")
except KeyboardInterrupt:
    # Ctrl+C でループ終了
    print("stop picamera")
    pass

# end camera
picam2.stop_preview()
picam2.stop()


# detect face
#load_image = face_recognition.load_image_file(cap_file_name)
#face_locations = face_recognition.face_locations(load_image)
#print(face_locations)

# draw box by pillow
#pil_image = Image.fromarray(load_image)
#draw = ImageDraw.Draw(pil_image)
#for (top, right, bottom, left) in face_locations:
#    draw.rectangle(((left, top), (right, bottom)),
#                   outline=(255, 0, 0), width=4)

# show result
# pil_image.show()

#try:
#	while True:
		# arrayを持って来る
		#  outputとして、(480, 640, 4)
		#image = picam2.capture_image()
#		image = picam2.capture_array()
		# image = image[:, : ,0:3]
		# image = picam2.capture_metadata()
		#print(image["Bcm2835StatsOutput"])
#		print(image.shape)
#		print(type(image))
		
		# detect face
#		faces = face_detector(image, 0)
#		print(faces)
		
		#image = image.release()
		
#		time.sleep(0.5)
#		print("collect picamera")
#except KeyboardInterrupt:
#    # end loop if Ctrl+C
#    print("stop picamera")
#    pass
