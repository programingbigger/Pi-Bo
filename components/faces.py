import time
import sys
from logging import getLogger
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport

class LEDMatrixDisplay:
    def __init__(self):
        self.logger = getLogger(__name__)
        self.CASCADED = 4
        self.ORIENTATION = -90  # -90, 0, 90, 180
        self.WIDTH = 32
        self.HEIGHT = 16

        serial_1 = spi(port=0, device=0, gpio=noop())
        device_1 = max7219(serial_1, width=self.WIDTH, height=self.HEIGHT, block_orientation=self.ORIENTATION, rotate=0)
        self.virtual_1 = viewport(device_1, width=80*16, height=16)
        self.virtual_1.set_position((0, 0))

    def magao(self):
        try:
            n = 0
            while True:
                with canvas(self.virtual_1) as draw:
                    time.sleep(0.5)
                    draw.line((8,2, 8,9), fill="white")
                    draw.line((23,2, 23,9), fill="white")
                    draw.line((12,13, 19,13), fill="white")
                
                with canvas(self.virtual_1) as draw:
                    time.sleep(2)
                    if n == 1:
                        break
                    draw.line((8,6, 8,9), fill="white")
                    draw.line((23,6, 23,9), fill="white")
                    draw.line((12,13, 19,13), fill="white")
                
                with canvas(self.virtual_1) as draw:
                    time.sleep(0.25)
                    draw.line((12,13, 19,13), fill="white")
                n += 1
            self.logger.info("correct do winking")
        except KeyboardInterrupt:
            print("-"*10, "stop winking", "-"*10)
            self.logger.error("A key was interrupted during execution. ex: ctrl + c")
            sys.exit()

    def eyes_LR(self):
        try:
            for n in (0,2, 0,2):
                with canvas(self.virtual_1) as draw:
                    draw.line((7+n,2, 7+n,9), fill="white")
                    draw.line((22+n,2, 22+n,9), fill="white")
                    draw.line((12,13, 19,13), fill="white")
                time.sleep(1)
            self.logger.info("correct do eyes_LR")
        except KeyboardInterrupt:
            print("-"*10, "stop eyes_LR", "-"*10)
            self.logger.error("A key was interrupted during execution. ex: ctrl + c")
            sys.exit()

    def smile(self):
        try:
            for n in (0, 1, 0, 1):
                with canvas(self.virtual_1) as draw:
                    draw.line((8,3+n, 5,6+n), fill="white")
                    draw.line((8,3+n, 11,6+n), fill="white")
                    draw.line((23,3+n, 20,6+n), fill="white")
                    draw.line((23,3+n, 26,6+n), fill="white")
                    draw.line((12,13, 19,13), fill="white")
                time.sleep(1.0)
            self.logger.info("correct do smile")
        except KeyboardInterrupt:
            print("-"*10, "stop smile", "-"*10)
            self.logger.error("key was interrupted during execution. ex: ctrl + c")
            sys.exit()

    def trouble(self):
        try:
            for n in (0,2, 0,2):
                with canvas(self.virtual_1) as draw:
                    draw.line((8,3, 8,8), fill="white")
                    draw.line((23,3, 23,8), fill="white")
                    draw.line((12,13, 19,13), fill="white")
                    draw.line((27,4+n, 27,6+n), fill="white")
                    draw.line((28,2+n, 28,7+n), fill="white")
                    draw.line((29,0+n, 29,7+n), fill="white")
                    draw.line((30,2+n, 30,7+n), fill="white")
                    draw.line((31,4+n, 31,6+n), fill="white")
                time.sleep(1)
            self.logger.info("correct do trouble")
        except KeyboardInterrupt:
            print("-"*10, "stop trouble", "-"*10)
            self.logger.error("key was interrupted during execution. ex: ctrl + c")
            sys.exit()
