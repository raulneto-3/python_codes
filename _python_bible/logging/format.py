import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logfile.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Our first message.")
logger.info("Our second message.")
logger.info("Our third message.")