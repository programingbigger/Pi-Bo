import time, datetime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.interface.serial import noop
from luma.core.render import canvas
from luma.core.virtual import viewport

CASCADED = 4
ORIENTATION = -90  # -90, 0, 90, 180
WIDTH = 32
HEIGHT = 16
# device1の設定
serial_1 = spi(port=0, device=0, gpio = noop())
device_1 = max7219(serial_1, width= WIDTH, height= HEIGHT, block_orientation=ORIENTATION,rotate=0)
virtual_1 = viewport(device_1, width=80*16, height=16)

def magao():
    # 原点の位置を設定
    virtual_1.set_position((0, 0))

    while 1:
        # 真顔
        with canvas(virtual_1) as draw:
            # 目無しの実行時間
            time.sleep(0.25)

            # 真顔
            draw.line((8,2, 8,9), fill="white")
            draw.line((23,2, 23,9), fill="white")
            draw.line((12,13, 19,13), fill="white")

        # 半目
        with canvas(virtual_1) as draw:
            # 真顔の実行時間
            time.sleep(2)

            # 半目
            draw.line((8,6, 8,9), fill="white")
            draw.line((23,6, 23,9), fill="white")
            draw.line((12,13, 19,13), fill="white")

        # 目無し
        with canvas(virtual_1) as draw:
            # 半目の実行時間
            time.sleep(0.25)

            # 目無し
            draw.line((12,13, 19,13), fill="white")
