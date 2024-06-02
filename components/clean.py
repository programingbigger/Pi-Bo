#!/usr/bin/env python

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi

def clear_screan():
	CASCADED = 4
	ORIENTATION = -90  # -90, 0, 90, 180
	WIDTH = 32
	HEIGHT = 16
	# device1の設定
	serial = spi(port=0, device=0)
	device = max7219(serial, width= WIDTH, height= HEIGHT, block_orientation=ORIENTATION,rotate=0)
	device.hide()
