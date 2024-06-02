from components import clean
from components import faces
from LOGGING.MY_LOGGING import setup_log

# setup loggig
main_logger = setup_log(__name__)
faces_logger = setup_log("components.faces")

'''
main
'''

main_logger.info("start main.py")

# clean screan
# clean.clear_screan()

faces.magao()
faces.eyes_LR()
faces.smile()
faces.trouble()

main_logger.info("end main.py")
