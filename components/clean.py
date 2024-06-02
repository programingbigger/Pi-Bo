#!/usr/bin/env python

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi

serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1)
device.hide()
