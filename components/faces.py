import time
import sys
from logging import getLogger
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.interface.serial import noop
from luma.core.render import canvas
from luma.core.virtual import viewport

# logger
logger = getLogger(__name__)

CASCADED = 4
ORIENTATION = -90  # -90, 0, 90, 180
WIDTH = 32
HEIGHT = 16
# device1の設定
serial_1 = spi(port=0, device=0, gpio = noop())
device_1 = max7219(serial_1, width= WIDTH, height= HEIGHT, block_orientation=ORIENTATION,rotate=0)
virtual_1 = viewport(device_1, width=80*16, height=16)

# 原点の位置を設定
virtual_1.set_position((0, 0))

def magao():
	try :
		n = 0
		while(True):
			# 真顔
			with canvas(virtual_1) as draw:
				# 目を瞑る時間
				time.sleep(0.5)

				# 真顔
				draw.line((8,2, 8,9), fill="white")
				draw.line((23,2, 23,9), fill="white")
				draw.line((12,13, 19,13), fill="white")

			# 半目
			with canvas(virtual_1) as draw:
				# 真顔の実行時間
				time.sleep(2)

				if n == 1:
					break

				# 半目
				draw.line((8,6, 8,9), fill="white")
				draw.line((23,6, 23,9), fill="white")
				draw.line((12,13, 19,13), fill="white")

			# 目無し
			with canvas(virtual_1) as draw:
				# 目無しの実行時間
				time.sleep(0.25)
				# 目無し
				draw.line((12,13, 19,13), fill="white")
			n += 1
		logger.info("correct do winking")

	except KeyboardInterrupt:
		print("-"*10, "stop winking", "-"*10)
		logger.error("A key was interrupted during execution. ex: ctrl + c")
		sys.exit()

def eyes_LR():
	try:
		# 目左右
		for n in (0,2, 0,2):
			with canvas(virtual_1) as draw:
				draw.line((7+n,2, 7+n,9), fill="white")
				draw.line((22+n,2, 22+n,9), fill="white")
				draw.line((12,13, 19,13), fill="white")
	
			# 実行時間
			time.sleep(1)
		logger.info("correct do eyes_LR")

	except KeyboardInterrupt:
		print("-"*10, "stop eyes_LR", "-"*10)
		logger.error("A key was interrupted during execution. ex: ctrl + c")
		sys.exit()

def smile():
	try:
		for n in (0, 1, 0, 1):
			# 笑顔
			with canvas(virtual_1) as draw:
				# 左目
				draw.line((8,3+n, 5,6+n), fill="white")
				draw.line((8,3+n, 11,6+n), fill="white")
				# 右目
				draw.line((23,3+n, 20,6+n), fill="white")
				draw.line((23,3+n, 26,6+n), fill="white")
				# 口
				draw.line((12,13, 19,13), fill="white")
			# 前の時間
			time.sleep(1.0)
		logger.info("correct do smile")

	except KeyboardInterrupt:
		print("-"*10, "stop smile", "-"*10)
		logger.error("key was interrupted during execution. ex: ctrl + c")
		sys.exit()

def trouble():
	try:
		for n in (0,2, 0,2):
			# 困った顔
			with canvas(virtual_1) as draw:
				draw.line((8,3, 8,8), fill="white")
				draw.line((23,3, 23,8), fill="white")
				draw.line((12,13, 19,13), fill="white")
				# 汗の表現
				draw.line((27,4+n, 27,6+n), fill="white")
				draw.line((28,2+n, 28,7+n), fill="white")
				draw.line((29,0+n, 29,7+n), fill="white")
				draw.line((30,2+n, 30,7+n), fill="white")
				draw.line((31,4+n, 31,6+n), fill="white")
			time.sleep(1)
		logger.info("correct do trouble")

	except KeyboardInterrupt:
		print("-"*10, "stop trouble", "-"*10)
		logger.error("key was interrupted during execution. ex: ctrl + c")
		sys.exit()
