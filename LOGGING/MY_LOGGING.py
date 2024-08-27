from logging import getLogger
from logging import Formatter
from logging import FileHandler
from logging import DEBUG
from logging import INFO
from logging import StreamHandler

'''
astime    : ログメッセージ生成の日付と時刻
name      : loggerの名前を表示
levelname : ログレベル
message   : メッセージ
'''

def setup_log(name):
	'''
	custom loggig
	'''

	# set log_format
	formatter = Formatter("%(asctime)s - %(name)s > -%(levelname)s- > %(message)s")

	# create get logger
	logger = getLogger(name)
	logger.setLevel(DEBUG)

	# create file handler
	file_handler = FileHandler("LOGGING/log.log")
	file_handler.setFormatter(formatter)
	file_handler.setLevel(DEBUG)

	# create console handler 
	stream_handler = StreamHandler()
	stream_handler.setFormatter(formatter)
	stream_handler.setLevel(INFO)

	# add handlers to the logger
	logger.addHandler(file_handler)
	logger.addHandler(stream_handler)

	return logger
