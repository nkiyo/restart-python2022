# https://stackoverflow.com/a/40088591
# https://qiita.com/shotakaha/items/0fa2db1dc8253c83e2bb
# https://teratail.com/questions/116651
# https://docs.python.org/ja/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler("my_log.log", maxBytes=1000, backupCount=10, encoding="utf-8")
handler.setFormatter(logging.Formatter('%(asctime)s %(filename)s:%(lineno)4d [%(levelname)8s] %(message)s'))
logger.addHandler(handler)

#for i in range(10000):
for i in range(100):
    logger.debug("Hello, World あいうえお")
    logger.info("info あいうえお")

