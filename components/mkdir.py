import os
from datetime import datetime
import pytz
from logging import getLogger

# logger
logger = getLogger(__name__)

def folder_and_file():
	# フォルダとファイル名
	target_dir = "save_caputure"
	jst = pytz.timezone("Asia/Tokyo")
	now = datetime.now().astimezone(jst) # 日本時間変換
	now = now.strftime("%Y-%m-%d_%H%M%S")
	cap_file_name = target_dir + "/" + f"{now}"
	
	# フォルダの作成
	if not os.path.exists(target_dir):
		try:
			os.makedirs(target_dir)
			logger.info(f"{target_dir} saved")
		except OSError as e:
			logger.error(f"do not make by error : {e}")
	else:
		logger.info(f"{target_dir} already exists")
	
	return cap_file_name
